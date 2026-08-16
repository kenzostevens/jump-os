#!/usr/bin/env python3
"""SHIPPING: the only bridge from engine output to LEADS.

Takes one or more engine classified.json files, keeps only qualified
(Class A/B) phone-bearing leads never shipped before (by normalized phone
against the canonical registry), stages them with origin tags, formats them
to Teleblast columns, folds them into LEADS/<NICHE>/<CLASS>/<STATE>/<county>
masters and batches, renumbers county folders by size, and records every
shipped lead in the registry.

Engines never write LEADS. LEADS is never edited by hand. Re-running with
the same inputs ships nothing (the registry remembers).

Usage:
  python3 ship.py --niche car-detailers --lane engine-v2 \
      --classified /path/to/classified.json [--classified more.json] \
      [--dry-run]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import re
import sys
from collections import defaultdict
from pathlib import Path

SHIPPING = Path(__file__).resolve().parents[1]
OS_ROOT = SHIPPING.parents[1]
LEADS = OS_ROOT / "02-LEADS"
REGISTRY = SHIPPING / "registry.csv"
STAGING = SHIPPING / "staging"

REGISTRY_FIELDS = [
    "stable_id", "niche", "business_name", "published_business_phone",
    "city", "county", "state", "lead_class", "website_state",
    "candidate_website_url", "status", "first_seen",
]
TELEBLAST_FIELDS = [
    "Business Name", "Contact / First & Last Name", "Phone", "Email",
    "Address", "City", "State / Province", "Notes", "Birthday", "Industry",
]
ALLOWED_STATES = {"CA", "OR", "WA"}
BATCH_CEILING = 100
REASONS = [
    ("social", "only a Facebook/booking/directory page"),
    ("third_party", "only a Facebook/booking/directory page"),
    ("no_website", "no website found on Google"),
    ("parked", "domain parked or for sale"),
    ("broken", "website broken or unreachable"),
    ("unreachable", "website broken or unreachable"),
]


def normalized_phone(value) -> str | None:
    digits = re.sub(r"\D", "", str(value or ""))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits if len(digits) == 10 else None


def pretty_phone(digits: str) -> str:
    return f"+1-{digits[:3]}-{digits[3:6]}-{digits[6:]}"


def website_state(row: dict) -> str:
    audit = row.get("website_audit") or {}
    return str(audit.get("website_state") or row.get("website_state") or "")


def reason_for(row: dict) -> str:
    ws = website_state(row).lower()
    for key, text in REASONS:
        if key in ws:
            return text
    return "no website found on Google" if row.get("lead_class") == "A" else "website has objective flaws"


def priority_for(row: dict) -> str:
    ws = website_state(row).lower()
    if row.get("lead_class") == "A":
        if "social" in ws or "third_party" in ws:
            return "P1"
        if "parked" in ws or "broken" in ws or "unreachable" in ws:
            return "P3"
        return "P2"
    return "P4"


def county_for(row: dict) -> str:
    county = str(row.get("verified_county") or row.get("county_hint") or "").strip()
    if not county:
        raise SystemExit(f"lead has no county attribution: {row.get('business_name')!r}")
    return county


def city_for(row: dict) -> str:
    return str(row.get("verified_city") or row.get("locality_text") or "").strip()


def slug(value: str) -> str:
    return re.sub(r"[^A-Z0-9]+", "-", value.upper()).strip("-")


def load_registry() -> list[dict]:
    with REGISTRY.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


TRACKER_FIELDS = ["niche", "class", "state", "county", "batch_file", "leads",
                  "status", "date_loaded", "date_called", "booked", "notes"]


def guard_and_sync_tracker(niche_slug: str, states_touched: set[str], *, force: bool) -> None:
    """Refuse to reshuffle batches a human already loaded; then re-sync rows.

    Folding rebuilds a state's county folders, which can renumber and
    repartition batch files. That is only safe while every tracked batch in
    the state is still 'untouched'. Afterward, tracker rows are rebuilt for
    the touched states (untouched only, by construction).
    """
    niche_dir = LEADS / niche_slug
    tracker_path = niche_dir / "TRACKER.csv"
    old_rows = list(csv.DictReader(tracker_path.open(encoding="utf-8"))) if tracker_path.is_file() else []
    conflicted = [r for r in old_rows
                  if r["state"] in states_touched and r["status"] != "untouched"]
    if conflicted and not force:
        names = ", ".join(r["batch_file"] for r in conflicted[:5])
        raise SystemExit(
            f"refusing to refold {sorted(states_touched)}: {len(conflicted)} batch(es) already "
            f"loaded/called there ({names}...). Ship into a fresh state, or rerun with "
            f"--force-refold after reconciling the tracker by hand.")
    kept = [r for r in old_rows if r["state"] not in states_touched]
    for batch in sorted(niche_dir.glob("CLASS-*/*/[0-9][0-9]-*/BATCHES/*.csv")):
        county_dir = batch.parent.parent
        st = county_dir.parent.name
        if st not in states_touched:
            continue
        kept.append({
            "niche": niche_dir.name, "class": county_dir.parents[1].name,
            "state": st, "county": county_dir.name, "batch_file": batch.name,
            "leads": sum(1 for _ in batch.open()) - 1, "status": "untouched",
            "date_loaded": "", "date_called": "", "booked": "", "notes": "",
        })
    kept.sort(key=lambda r: (r["class"], r["state"], r["county"], r["batch_file"]))
    niche_dir.mkdir(parents=True, exist_ok=True)
    with tracker_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=TRACKER_FIELDS)
        writer.writeheader(); writer.writerows(kept)


def fold_niche_tree(niche_slug: str, teleblast_rows_by_key: dict) -> None:
    """Rebuild <niche>/<class>/<state> county folders from master files."""
    for cls in ("CLASS-A", "CLASS-B"):
        for st in sorted({k[1] for k in teleblast_rows_by_key if k[0] == cls}):
            groups = defaultdict(list)
            for row, county in teleblast_rows_by_key[(cls, st)]:
                groups[slug(county)].append(row)
            state_dir = LEADS / niche_slug / cls / st
            # wipe and rebuild: county folders are derived data
            if state_dir.exists():
                import shutil
                shutil.rmtree(state_dir)
            ranked = sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))
            for i, (county_slug, grp) in enumerate(ranked, 1):
                folder = state_dir / f"{i:02d}-{county_slug}"
                mdir, bdir = folder / "00-MASTER", folder / "BATCHES"
                mdir.mkdir(parents=True), bdir.mkdir()
                tag = cls.lower()
                stem = f"{county_slug.lower()}-{st.lower()}-{tag}"
                with (mdir / f"{stem}.csv").open("w", newline="", encoding="utf-8") as h:
                    w = csv.DictWriter(h, fieldnames=TELEBLAST_FIELDS)
                    w.writeheader(); w.writerows(grp)
                parts = math.ceil(len(grp) / BATCH_CEILING)
                base, extra = divmod(len(grp), parts)
                index = 0
                for b in range(parts):
                    size = base + (1 if b < extra else 0)
                    with (bdir / f"{stem}-batch-{b + 1:02d}.csv").open("w", newline="", encoding="utf-8") as h:
                        w = csv.DictWriter(h, fieldnames=TELEBLAST_FIELDS)
                        w.writeheader(); w.writerows(grp[index:index + size])
                    index += size


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--niche", required=True)
    parser.add_argument("--lane", required=True, help="origin label, e.g. engine-v1 / engine-v2")
    parser.add_argument("--classified", action="append", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--force-refold", action="store_true")
    args = parser.parse_args()

    niche_slug = slug(args.niche)
    today = dt.date.today().isoformat()

    registry = load_registry()
    shipped_phones = {
        normalized_phone(r["published_business_phone"])
        for r in registry if r["status"].startswith("exported")
    } - {None}
    known_phones = {normalized_phone(r["published_business_phone"]) for r in registry} - {None}

    new_leads: dict[str, dict] = {}
    skipped_shipped = 0
    skipped_unqualified = 0
    for path in args.classified:
        rows = json.loads(Path(path).read_text(encoding="utf-8"))
        for row in rows:
            phone = normalized_phone(row.get("published_business_phone"))
            if phone is None or row.get("lead_class") not in ("A", "B"):
                skipped_unqualified += 1
                continue
            if phone in shipped_phones:
                skipped_shipped += 1
                continue
            state = str(row.get("state") or "").upper()
            if state not in ALLOWED_STATES:
                raise SystemExit(f"lead outside allowed states ({state}): {row.get('business_name')!r}")
            previous = new_leads.get(phone)
            if previous is None or (row["lead_class"], ) < (previous["lead_class"], ):
                new_leads[phone] = row

    if not new_leads:
        print(json.dumps({"shipped": 0, "already_shipped": skipped_shipped,
                          "skipped_unqualified": skipped_unqualified}))
        return 0

    # staging record: lead-shaped, origin-tagged, pre-format
    staging_rows = []
    for phone, row in new_leads.items():
        staging_rows.append({
            "origin": args.lane,
            "niche": args.niche,
            "stable_id": str(row.get("stable_id") or ""),
            "business_name": row.get("business_name"),
            "published_business_phone": pretty_phone(phone),
            "candidate_website_url": row.get("candidate_website_url") or "",
            "lead_class": row.get("lead_class"),
            "city": city_for(row),
            "county": county_for(row),
            "state": str(row.get("state")).upper(),
            "website_state": website_state(row),
        })
    if args.dry_run:
        print(json.dumps({"would_ship": len(staging_rows), "already_shipped": skipped_shipped,
                          "skipped_unqualified": skipped_unqualified}))
        return 0

    # Guard BEFORE any state is written: if the fold would reshuffle batches a
    # human already loaded, fail here while registry and staging are untouched.
    prior_states = {
        r["state"] for r in registry
        if r["niche"] == args.niche and r["status"].startswith("exported")
    }
    states_touched = {s["state"] for s in staging_rows} | prior_states
    guard_and_sync_tracker(niche_slug, states_touched, force=args.force_refold)

    STAGING.mkdir(exist_ok=True)
    stage_path = STAGING / f"{niche_slug.lower()}-{args.lane}-{today}.csv"
    with stage_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(staging_rows[0].keys()))
        writer.writeheader(); writer.writerows(staging_rows)

    # registry: every shipped lead is remembered forever
    for s in staging_rows:
        registry.append({
            "stable_id": f"{args.lane}:{s['stable_id']}" if s["stable_id"] else f"{args.lane}:phone:{s['published_business_phone']}",
            "niche": args.niche,
            "business_name": s["business_name"],
            "published_business_phone": s["published_business_phone"],
            "city": s["city"], "county": s["county"], "state": s["state"],
            "lead_class": s["lead_class"], "website_state": s["website_state"],
            "candidate_website_url": s["candidate_website_url"],
            "status": f"exported_{today}", "first_seen": today,
        })
    tmp = REGISTRY.with_suffix(".tmp")
    with tmp.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=REGISTRY_FIELDS)
        writer.writeheader(); writer.writerows(registry)
    tmp.replace(REGISTRY)

    # rebuild the niche tree in LEADS from the full shipped population
    by_key: dict = defaultdict(list)
    for r in registry:
        if r["niche"] != args.niche or not r["status"].startswith("exported"):
            continue
        cls = f"CLASS-{r['lead_class']}"
        note_parts = []
        if not r["stable_id"].startswith("google_maps:"):
            lane = r["stable_id"].split(":", 1)[0]
            if lane not in ("", args.niche) and lane.startswith(("engine-", "v1")):
                note_parts.append("V1" if "v1" in lane else lane)
        pseudo = {"lead_class": r["lead_class"], "website_state": r["website_state"]}
        note = " | ".join(note_parts + [priority_for(pseudo), f"Class {r['lead_class']}",
                                        reason_for(pseudo)])
        if r.get("candidate_website_url"):
            note = f"{note} | {r['candidate_website_url']}"
        by_key[(cls, r["state"])].append(({
            "Business Name": r["business_name"],
            "Contact / First & Last Name": "",
            "Phone": r["published_business_phone"],
            "Email": "", "Address": "",
            "City": r["city"], "State / Province": r["state"],
            "Notes": note, "Birthday": "",
            "Industry": args.niche.replace("-", " ").title(),
        }, r["county"]))
    fold_niche_tree(niche_slug, {k: v for k, v in by_key.items()})
    guard_and_sync_tracker(niche_slug, {st for (_, st) in by_key}, force=True)  # sync AFTER fold

    print(json.dumps({
        "shipped": len(staging_rows),
        "already_shipped_suppressed": skipped_shipped,
        "skipped_unqualified": skipped_unqualified,
        "staging_file": str(stage_path),
        "registry_total": len(registry),
    }, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
