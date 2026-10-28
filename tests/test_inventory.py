"""Unit tests for the read-only inventory browser."""

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.inventory import COLUMNS, filter_inventory, load_inventory, main


class InventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.path = Path(self.tmp.name) / "inventory.csv"
        self.path.write_text(
            ",".join(COLUMNS) + "\n"
            "Alpha,causal LM,50M,completed,test_nll=5,not mirrored,GitHub\n"
            "Beta,tokenizer,128k,pending,no benchmark,local,GitHub\n",
            encoding="utf-8",
        )

    def test_load_and_preserve_values(self):
        rows = load_inventory(self.path)
        self.assertEqual([row["model"] for row in rows], ["Alpha", "Beta"])
        self.assertEqual(rows[0]["primary_metric"], "test_nll=5")

    def test_case_insensitive_filters(self):
        rows = load_inventory(self.path)
        self.assertEqual([r["model"] for r in filter_inventory(rows, status="COMPLETED")], ["Alpha"])
        self.assertEqual([r["model"] for r in filter_inventory(rows, family="TOKEN")], ["Beta"])
        self.assertEqual([r["model"] for r in filter_inventory(rows, search="128K")], ["Beta"])

    def test_no_matches(self):
        self.assertEqual(filter_inventory(load_inventory(self.path), search="absent"), [])

    def test_duplicate_model_rejected(self):
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("alpha,causal LM,60M,completed,test_nll=4,local,GitHub\n")
        with self.assertRaisesRegex(ValueError, "Duplicate model"):
            load_inventory(self.path)

    def test_missing_column_rejected(self):
        self.path.write_text("model,status\nAlpha,completed\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "columns"):
            load_inventory(self.path)

    def test_malformed_row_rejected(self):
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("broken,only two\n")
        with self.assertRaisesRegex(ValueError, "Incomplete"):
            load_inventory(self.path)

    def test_json_cli(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = main(["--file", str(self.path), "--status", "pending", "--json"])
        self.assertEqual(code, 0)
        payload = json.loads(output.getvalue())
        self.assertEqual(payload["matched"], 1)
        self.assertEqual(payload["total"], 2)
        self.assertEqual(payload["statuses"], {"pending": 1})

    def test_sort_by_model_preserves_default_and_supports_descending(self):
        original = self.path.read_text(encoding="utf-8")
        self.path.write_text(original.replace("Alpha,", "zulu,").replace("Beta,", "alpha,"), encoding="utf-8")
        for options, expected in (
            ([], ["zulu", "alpha"]),
            (["--sort-by", "model"], ["alpha", "zulu"]),
            (["--sort-by", "model", "--descending"], ["zulu", "alpha"]),
        ):
            with self.subTest(options=options):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    self.assertEqual(main(["--file", str(self.path), "--json", *options]), 0)
                self.assertEqual([row["model"] for row in json.loads(output.getvalue())["models"]], expected)

    def test_sort_by_status_keeps_original_order_for_ties(self):
        with self.path.open("a", encoding="utf-8") as handle:
            handle.write("Gamma,causal LM,80M,completed,test_nll=4,local,GitHub\n")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--file", str(self.path), "--sort-by", "status", "--json"]), 0)
        self.assertEqual([row["model"] for row in json.loads(output.getvalue())["models"]],
                         ["Alpha", "Gamma", "Beta"])

    def test_descending_requires_sort_by(self):
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as error:
                main(["--file", str(self.path), "--descending"])
        self.assertEqual(error.exception.code, 2)

    def test_missing_file_error_code(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["--file", str(self.path) + ".missing"]), 2)


if __name__ == "__main__":
    unittest.main()
