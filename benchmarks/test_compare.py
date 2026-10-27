import contextlib
import csv
import io
import json
import tempfile
import unittest
from pathlib import Path

from benchmarks.compare import comparable_groups, main


class CompareTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "summary.csv"
        with self.path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["model", "variant", "experiment", "status", "seed", "budget_type", "budget_value_s", "test_nll", "test_perplexity", "tokens_per_second"])
            writer.writeheader()
            for variant, seed, status, nll, speed in [
                ("A", "42", "completed", "5", "10"),
                ("B", "42", "completed", "4", "20"),
                ("pending", "42", "pending", "1", "99"),
                ("other-seed", "43", "completed", "3", "30"),
                ("invalid", "42", "completed", "nan", "30"),
            ]:
                writer.writerow(dict(model="M", variant=variant, experiment="exp", status=status, seed=seed, budget_type="wall_clock", budget_value_s="600", test_nll=nll, test_perplexity="100", tokens_per_second=speed))

    def test_lower_is_better_and_incomparable_excluded(self):
        groups = comparable_groups(self.path)
        self.assertEqual(len(groups), 1)
        self.assertEqual([r["variant"] for r in groups[0]["ranked"]], ["B", "A"])

    def test_throughput_descending(self):
        groups = comparable_groups(self.path, "tokens_per_second")
        self.assertEqual([r["variant"] for r in groups[0]["ranked"][:2]], ["invalid", "B"])

    def test_filter_no_cohorts(self):
        self.assertEqual(comparable_groups(self.path, experiment="unknown"), [])

    def test_json_cli(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(main(["--csv", str(self.path), "--json"]), 0)
        self.assertEqual(json.loads(output.getvalue())[0]["ranked"][0]["variant"], "B")

    def test_invalid_schema(self):
        self.path.write_text("model,variant\\nM,A\\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "missing required columns"):
            comparable_groups(self.path)


if __name__ == "__main__":
    unittest.main()
