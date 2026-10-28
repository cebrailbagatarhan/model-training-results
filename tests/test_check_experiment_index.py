"""Fixture-based regression tests for the experiment index checker."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest

from scripts.check_experiment_index import audit, main


class ExperimentIndexTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "experiments" / "first").mkdir(parents=True)
        (self.root / "experiments" / "first" / "README.md").write_text("# First\n")
        self.write_index("| [`first`](experiments/first/) | Model | completed |\n")

    def write_index(self, row):
        (self.root / "EXPERIMENT_INDEX.md").write_text(
            "# Experiment Index\n\n| Deney | Model | Durum |\n|---|---|---|\n" + row,
            encoding="utf-8",
        )

    def test_valid_index(self):
        self.assertTrue(audit(self.root)["ok"])

    def test_missing_folder(self):
        self.write_index("| [`missing`](experiments/missing/) | Model | completed |\n")
        self.assertEqual(audit(self.root)["missing_folders"], ["missing"])

    def test_unindexed_folder(self):
        (self.root / "experiments" / "extra").mkdir()
        self.assertEqual(audit(self.root)["unindexed_folders"], ["extra"])

    def test_duplicate_entry(self):
        self.write_index("| [`first`](experiments/first/) | M | completed |\n" * 2)
        self.assertEqual(audit(self.root)["duplicate_entries"], ["first"])

    def test_missing_readme(self):
        (self.root / "experiments" / "first" / "README.md").unlink()
        self.assertEqual(audit(self.root)["missing_readmes"], ["first"])

    def test_malformed_link(self):
        self.write_index("| [bad](experiments/../secret/) | M | completed |\n")
        self.assertEqual(len(audit(self.root)["malformed_rows"]), 1)

    def test_json_cli_exit_code(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--root", str(self.root), "--json"]), 0)
        self.assertTrue(json.loads(output.getvalue())["ok"])

    def test_status_counts_from_index_column(self):
        (self.root / "experiments" / "second").mkdir()
        (self.root / "experiments" / "second" / "README.md").write_text("# Second\n")
        self.write_index(
            "| [`first`](experiments/first/) | M | completed |\n"
            "| [`second`](experiments/second/) | M | partial |\n"
        )
        report = audit(self.root)
        self.assertTrue(report["ok"])
        self.assertEqual(report["status_counts"], {"completed": 1, "partial": 1})

    def test_status_counts_ignore_malformed_rows(self):
        self.write_index(
            "| [`first`](experiments/first/) | M | completed |\n"
            "| [bad](experiments/../secret/) | M | partial |\n"
        )
        report = audit(self.root)
        self.assertEqual(report["status_counts"], {"completed": 1})
        self.assertEqual(report["malformed_rows"], [6])


if __name__ == "__main__":
    unittest.main()
