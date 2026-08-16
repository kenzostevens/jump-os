#!/usr/bin/env python3
"""Integrity check for the LEADS tree against the canonical registry.

Verifies, per niche:
  - every county's BATCHES sum exactly to its 00-MASTER
  - no phone appears twice anywhere in the niche tree
  - every phone in LEADS is registered as exported in the registry
  - every exported registry row for the niche appears in LEADS
  - county folder numbering is contiguous and ranked by size
Exit 0 with a summary on success; exit 1 naming every failure otherwise.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

SHIPPING = Path(__file__).resolve().parents[1]
OS_ROOT = SHIPPING.parents[1]
LEADS = OS_ROOT / "02-LEADS"
REGISTRY = SHIPPING / "registry.csv"


def normalized_phone(value) -> str | None:
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if len(digits) == 10 else None


def main() -> int:
    failures: list[str] = []
    registry = list(csv.DictReader(REGISTRY.open(encoding="utf-8")))
    summary = {}

    for niche_dir in sorted(p for p in LEADS.iterdir() if p.is_dir()):
        niche_phones: Counter = Counter()
        tree_count = 0
        masters = list(niche_dir.glob("CLASS-*/*/[0-9][0-9]-*/00-MASTER/*.csv"))
        masters += list(niche_dir.glob("REVIEW-UNVERIFIED/00-MASTER/*.csv"))
        for master in masters:
            county_dir = master.parent.parent
            master_rows = list(csv.DictReader(master.open(encoding="utf-8")))
            batch_rows = []
            for batch in sorted((county_dir / "BATCHES").glob("*.csv")):
                batch_rows.extend(csv.DictReader(batch.open(encoding="utf-8")))
            if len(master_rows) != len(batch_rows):
                failures.append(f"batch/master mismatch: {county_dir} "
                                f"({len(master_rows)} vs {len(batch_rows)})")
            for row in master_rows:
                phone = normalized_phone(row["Phone"])
                if phone is None:
                    failures.append(f"undialable phone in {master}: {row['Business Name']!r}")
                else:
                    niche_phones[phone] += 1
            tree_count += len(master_rows)
        for phone, count in niche_phones.items():
            if count > 1:
                failures.append(f"{niche_dir.name}: phone repeated {count}x: ...{phone[-4:]}")

        # numbering: contiguous, ranked by size
        for state_dir in niche_dir.glob("CLASS-*/*"):
            if not state_dir.is_dir():
                continue
            folders = sorted(d for d in state_dir.iterdir() if d.is_dir())
            sizes = []
            for i, folder in enumerate(folders, 1):
                prefix = folder.name.split("-", 1)[0]
                if prefix != f"{i:02d}":
                    failures.append(f"numbering gap at {folder}")
                master = next((folder / "00-MASTER").glob("*.csv"), None)
                sizes.append(sum(1 for _ in master.open()) - 1 if master else 0)
            if sizes != sorted(sizes, reverse=True):
                failures.append(f"{state_dir}: folders not ranked by size")

        niche_name = niche_dir.name.lower()
        reg_exported = {
            normalized_phone(r["published_business_phone"])
            for r in registry
            if r["status"].startswith("exported")
            and re.sub(r"[^a-z0-9]+", "-", r["niche"].lower()) == niche_name
        } - {None}
        tree_set = set(niche_phones)
        for phone in sorted(tree_set - reg_exported):
            failures.append(f"{niche_dir.name}: in LEADS but not registered exported: ...{phone[-4:]}")
        for phone in sorted(reg_exported - tree_set):
            failures.append(f"{niche_dir.name}: registered exported but missing from LEADS: ...{phone[-4:]}")
        summary[niche_dir.name] = {"leads": tree_count, "registry_exported": len(reg_exported)}

    if failures:
        for failure in failures:
            print("FAIL:", failure)
        print(f"{len(failures)} failures")
        return 1
    print(json.dumps({"status": "PASS", **summary}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
