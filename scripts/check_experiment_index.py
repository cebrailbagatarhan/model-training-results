"""Validate that the experiment index and on-disk experiment folders agree.

Read-only, standard-library utility; no network or model dependencies.
"""

import argparse
import json
from pathlib import Path
import re

LINK_RE = re.compile(r"\]\(experiments/([A-Za-z0-9][A-Za-z0-9._-]*)/?\)")


def audit(root: Path) -> dict:
    root = Path(root)
    index = (root / "EXPERIMENT_INDEX.md").read_text(encoding="utf-8")
    experiments = root / "experiments"
    names = []
    malformed_rows = []
    for number, line in enumerate(index.splitlines(), start=1):
        if not line.startswith("|") or not line.lstrip("| ").startswith("["):
            continue
        match = LINK_RE.search(line.split("|", 2)[1])
        if match:
            names.append(match.group(1))
        else:
            malformed_rows.append(number)

    found = {p.name for p in experiments.iterdir() if p.is_dir() and not p.is_symlink()}
    listed = set(names)
    duplicates = sorted({name for name in names if names.count(name) > 1})
    missing = sorted(listed - found)
    unindexed = sorted(found - listed)
    missing_readmes = sorted(name for name in found & listed if not (experiments / name / "README.md").is_file())
    return {
        "ok": not (duplicates or missing or unindexed or missing_readmes or malformed_rows),
        "indexed_count": len(names),
        "folder_count": len(found),
        "duplicate_entries": duplicates,
        "missing_folders": missing,
        "unindexed_folders": unindexed,
        "missing_readmes": missing_readmes,
        "malformed_rows": malformed_rows,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Check EXPERIMENT_INDEX.md against experiments/.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = audit(args.root)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Unable to read experiment index: {exc}\n")
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Indexed: {report['indexed_count']}, folders: {report['folder_count']}")
        for key in ("duplicate_entries", "missing_folders", "unindexed_folders", "missing_readmes", "malformed_rows"):
            if report[key]:
                print(f"{key}: {report[key]}")
        print("OK" if report["ok"] else "FAILED")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
