"""Read-only, dependency-free search of the model inventory CSV."""

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

COLUMNS = (
    "model", "family", "scale", "status", "primary_metric",
    "artifact_status", "source_type",
)
DEFAULT_INVENTORY = Path(__file__).with_name("model_inventory.csv")


def load_inventory(path):
    """Load inventory rows, rejecting ambiguous or incomplete records."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != list(COLUMNS):
            raise ValueError("Inventory CSV columns do not match the expected schema")
        rows = []
        seen = set()
        for line_number, raw in enumerate(reader, start=2):
            if None in raw or any(raw[column] is None or not raw[column].strip() for column in COLUMNS):
                raise ValueError(f"Incomplete or malformed inventory row at line {line_number}")
            row = {column: raw[column].strip() for column in COLUMNS}
            key = row["model"].casefold()
            if key in seen:
                raise ValueError(f"Duplicate model at line {line_number}: {row['model']}")
            seen.add(key)
            rows.append(row)
    return rows


def filter_inventory(rows, *, status=None, family=None, search=None):
    """Case-insensitive substring filters; never infer model quality."""
    def matches(row):
        return (
            (not status or status.casefold() in row["status"].casefold())
            and (not family or family.casefold() in row["family"].casefold())
            and (not search or search.casefold() in " ".join(row.values()).casefold())
        )
    return [row for row in rows if matches(row)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file", type=Path, default=DEFAULT_INVENTORY, help="Inventory CSV path")
    parser.add_argument("--status", help="Filter by status (substring)")
    parser.add_argument("--family", help="Filter by family (substring)")
    parser.add_argument("--search", help="Search all columns (substring)")
    parser.add_argument("--json", action="store_true", help="Machine-readable report")
    args = parser.parse_args(argv)
    try:
        rows = load_inventory(args.file)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Inventory error: {exc}", file=sys.stderr)
        return 2
    selected = filter_inventory(rows, status=args.status, family=args.family, search=args.search)
    counts = dict(sorted(Counter(row["status"] for row in selected).items()))
    if args.json:
        print(json.dumps({"total": len(rows), "matched": len(selected), "statuses": counts,
                          "models": selected}, ensure_ascii=False, indent=2))
    else:
        print(f"Models: {len(selected)} matched / {len(rows)} total")
        for row in selected:
            print(f"- {row['model']} | {row['status']} | {row['primary_metric']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
