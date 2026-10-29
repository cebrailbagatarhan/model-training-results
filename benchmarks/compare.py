"""Compare only completed benchmark runs with matching experimental budgets."""

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

METRICS = {"test_nll": False, "test_perplexity": False, "tokens_per_second": True}
GROUP_KEYS = ("experiment", "budget_type", "budget_value_s", "seed")


def comparable_groups(path, metric="test_nll", experiment=None, min_runs=2):
    if isinstance(min_runs, bool) or not isinstance(min_runs, int) or min_runs < 2:
        raise ValueError("Minimum cohort size must be at least 2")
    if metric not in METRICS:
        raise ValueError(f"Unsupported metric: {metric}")
    groups = defaultdict(list)
    with open(path, newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        required = set(GROUP_KEYS) | {"model", "variant", "status", metric}
        if not required.issubset(reader.fieldnames or []):
            raise ValueError("Benchmark CSV is missing required columns")
        for row in reader:
            if row["status"].strip().lower() != "completed":
                continue
            if experiment and row["experiment"] != experiment:
                continue
            try:
                value = float(row[metric])
            except (ValueError, TypeError):
                continue
            if not math.isfinite(value):
                continue
            key = tuple(row[name] for name in GROUP_KEYS)
            groups[key].append({"model": row["model"], "variant": row["variant"], "value": value})
    return [
        {"cohort": dict(zip(GROUP_KEYS, key)), "metric": metric,
         "ranked": sorted(rows, key=lambda item: item["value"], reverse=METRICS[metric])}
        for key, rows in sorted(groups.items()) if len(rows) >= min_runs
    ]


def main(argv=None):
    parser = argparse.ArgumentParser(description="Rank comparable, completed benchmark runs")
    parser.add_argument("--csv", default=str(Path(__file__).with_name("summary.csv")))
    parser.add_argument("--experiment", help="Restrict to one experiment")
    parser.add_argument("--metric", choices=sorted(METRICS), default="test_nll")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output")
    parser.add_argument("--min-runs", type=int, default=2, help="Minimum completed runs per comparable cohort (at least 2)")
    args = parser.parse_args(argv)
    try:
        groups = comparable_groups(args.csv, args.metric, args.experiment, min_runs=args.min_runs)
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Cannot read benchmarks: {exc}\\n")
    if args.json:
        print(json.dumps(groups, ensure_ascii=False, indent=2))
    elif not groups:
        print("No comparable completed runs (same experiment, budget and seed).")
    else:
        for group in groups:
            cohort = group["cohort"]
            print(f"{cohort['experiment']} | {cohort['budget_type']}={cohort['budget_value_s']} | seed={cohort['seed']}")
            for rank, row in enumerate(group["ranked"], 1):
                print(f"  {rank}. {row['model']} / {row['variant']}: {row['value']:.6f} ({args.metric})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
