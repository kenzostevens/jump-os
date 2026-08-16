# Lead Sourcing Engine

The machinery of Jump OS. Two independent acquisition engines and one
shipping dock. Read this before operating anything here.

## Layout

- `ENGINE-V1/` — the browser-capture engine. An operating agent drives
  Google results pages and saves captures; slower, supervised, sees a
  slightly different slice of Google than V2. Its own world: own repo,
  own pipeline, own data, own run log.
- `ENGINE-V2/` — the terminal engine. A pinned headless scraper binary
  runs complete campaigns unattended (plan → run/resume → reconcile →
  classify → verify), with immutable per-checkpoint receipts. The
  production workhorse. Its own world, same as V1.
- `SHIPPING/` — the only bridge between engine output and `../../02-LEADS/`.
  - `registry.csv` — the canonical shipping registry: every lead ever
    shipped, any lane, any niche. THE suppression authority.
  - `staging/` — origin-tagged, pre-format records of each ship.
  - `tools/ship.py` — the shipping step (see below).
  - `tools/verify_leads.py` — integrity check: LEADS vs registry.

## The one law

**Engines scrape and classify. Only SHIPPING ships.**

No engine's own export command is ever used to produce calling files. An
engine's job ends at its `classified.json`. Everything callable enters
`02-LEADS/` exclusively through `ship.py`, which diffs against the canonical
registry (by normalized phone), stages what is genuinely new, formats it
for Teleblast, folds it into the LEADS county structure, and records it
in the registry. Re-shipping the same input ships nothing. This is what
makes double-dialing structurally impossible with two live engines.

Corollaries:
- The registry only grows. A DNC mark is forever and is never downgraded.
- `02-LEADS/` is derived data: never hand-edited, always regenerable.
- Both engines may run the same territory; SHIPPING merges their outputs
  and keeps whichever qualified listing arrives first per phone number.

## Running a campaign (the one-button flow)

1. **Choose the engine.** V2 unless there is a specific reason; V1 costs
   an agent session supervising browser loads for hours.
2. **Engine phase (V2):** inside `ENGINE-V2/`, on a clean committed tree:
   `preflight → plan → run` (background, resumable), then
   `reconcile → classify → verify`. Stop on any block/CAPTCHA evidence —
   never auto-recover from a block. Commit with an honest runs.md line.
3. **Ship:** `python3 SHIPPING/tools/ship.py --niche <niche> --lane
   engine-v2 --classified <path/to/classified.json>`.
4. **Verify:** `python3 SHIPPING/tools/verify_leads.py` must PASS.
5. The new territory now exists in `02-LEADS/<NICHE>/` as numbered county
   folders with `00-MASTER` + `BATCHES` (≤100 leads per batch,
   best-first order). Update `../STATE.md`.

## Authorization

Kenzo's standing delegation covers the full pipeline through shipping.
Still his alone, always: anything that leaves the machine (sending
files or counts to anyone, CRM/dialer writes, outreach), any spend or
credentials, and opening a NEW territory or niche (a scrape begins on
his word, e.g. "ship Washington"; readiness is not authorization).
