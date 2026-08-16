#!/usr/bin/env python3
"""Regenerate LEADS/REPORT.md from the trackers and the canonical registry.

Four layers of zoom: totals -> status rollup -> every county -> every batch.
REPORT.md is a generated view. Never hand-edit it; edit reality (the
tracker, the registry) and rerun this.
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

SHIPPING = Path(__file__).resolve().parents[1]
OS_ROOT = SHIPPING.parents[1]
LEADS = OS_ROOT / "02-LEADS"
REGISTRY = SHIPPING / "registry.csv"
STATUS_ORDER = ("untouched", "loaded", "called", "done")


def county_progress(batches: list[dict]) -> str:
    total = len(batches)
    done_like = sum(1 for b in batches if b["status"] in ("called", "done"))
    loaded = sum(1 for b in batches if b["status"] == "loaded")
    if done_like == total:
        return "complete"
    if done_like == 0 and loaded == 0:
        return "untouched"
    parts = []
    if done_like:
        parts.append(f"{done_like}/{total} called")
    if loaded:
        parts.append(f"{loaded} loaded")
    return ", ".join(parts)


def main() -> int:
    lines = [
        "# LEADS Report",
        "",
        f"Generated {dt.datetime.now().strftime('%Y-%m-%d %H:%M')} by report.py — do not hand-edit.",
        "",
    ]
    registry = list(csv.DictReader(REGISTRY.open(encoding="utf-8")))

    for niche_dir in sorted(p for p in LEADS.iterdir() if p.is_dir()):
        tracker_path = niche_dir / "TRACKER.csv"
        if not tracker_path.is_file():
            continue
        rows = list(csv.DictReader(tracker_path.open(encoding="utf-8")))
        total = sum(int(r["leads"]) for r in rows)
        booked = sum(int(r["booked"] or 0) for r in rows)
        niche_name = niche_dir.name.replace("-", " ").title()
        lines += [f"## {niche_name}", "",
                  f"**{total} leads in {len(rows)} batches.**"
                  + (f" **Booked so far: {booked}.**" if booked else ""), ""]

        by_status = defaultdict(lambda: [0, 0])
        for r in rows:
            by_status[r["status"]][0] += 1
            by_status[r["status"]][1] += int(r["leads"])
        lines += ["| Status | Batches | Leads |", "|---|---:|---:|"]
        for status in STATUS_ORDER:
            if status in by_status:
                b, l = by_status[status]
                lines.append(f"| {status} | {b} | {l} |")
        for status, (b, l) in sorted(by_status.items()):
            if status not in STATUS_ORDER:
                lines.append(f"| {status} | {b} | {l} |")
        lines.append("")

        loaded_now = [r for r in rows if r["status"] == "loaded"]
        if loaded_now:
            lines.append("**Currently loaded in Teleblast:** "
                         + ", ".join(f"{r['batch_file']} ({r['leads']})" for r in loaded_now))
            lines.append("")

        review_rows = [r for r in rows if r["class"] == "REVIEW-UNVERIFIED"]
        if review_rows:
            lines.append(
                f"**Unverified pile (not Class A/B — websites unreachable by machine; "
                f"ask about the site on the call):** "
                f"{sum(int(r['leads']) for r in review_rows)} leads in "
                f"{len(review_rows)} batches under `REVIEW-UNVERIFIED/`.")
            lines.append("")

        for cls in ("CLASS-A", "CLASS-B"):
            for st in sorted({r["state"] for r in rows if r["class"] == cls}):
                subset = [r for r in rows if r["class"] == cls and r["state"] == st]
                counties: dict[str, list[dict]] = defaultdict(list)
                for r in subset:
                    counties[r["county"]].append(r)
                state_leads = sum(int(r["leads"]) for r in subset)
                lines += [f"### {cls} / {st} — {state_leads} leads, "
                          f"{len(counties)} counties, {len(subset)} batches", ""]

                lines += ["| # | County | Leads | Batches | Progress |",
                          "|---|---|---:|---:|---|"]
                for county in sorted(counties, key=lambda c: int(c.split("-", 1)[0])):
                    batches = counties[county]
                    number, name = county.split("-", 1)
                    lines.append(
                        f"| {number} | {name} | {sum(int(b['leads']) for b in batches)} "
                        f"| {len(batches)} | {county_progress(batches)} |")
                lines.append("")

                lines += ["| Batch file | Leads | Status | Loaded | Called | Booked | Notes |",
                          "|---|---:|---|---|---|---:|---|"]
                for r in sorted(subset, key=lambda r: (int(r["county"].split("-", 1)[0]),
                                                       r["batch_file"])):
                    lines.append(
                        f"| {r['batch_file']} | {r['leads']} | {r['status']} "
                        f"| {r['date_loaded']} | {r['date_called']} | {r['booked']} "
                        f"| {r['notes']} |")
                lines.append("")

    exported = sum(1 for r in registry if r["status"].startswith("exported"))
    lines += ["---", "",
              f"Registry: {len(registry)} rows, {exported} shipped. "
              "Suppression authority: `LEAD-SOURCING-ENGINE/SHIPPING/registry.csv`.", ""]
    (LEADS / "REPORT.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {LEADS/'REPORT.md'} ({len(lines)} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
