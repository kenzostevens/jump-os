# STATE — Jump OS

Updated: 2026-08-16 (night — OS founded; LEADS and SHIPPING live)

## Current campaign

**Car detailers, California + Oregon** (San Joaquin and Amador counties
reserved, untouched by design). Scraping COMPLETE for both states.
Calling begins Monday 2026-08-17 via Teleblast; Joel expects 40 dials/day,
Kenzo plans ~60.

## Counts

- 6,751 shipped callable leads: 4,980 Class A + 1,771 Class B, in 187
  batches, all `untouched` in `02-LEADS/CAR-DETAILERS/TRACKER.csv` (the
  logbook; `02-LEADS/REPORT.md` is its generated view — rerun
  `SHIPPING/tools/report.py` after any tracker change).
- 02-LEADS/CAR-DETAILERS: CA 51 + OR 28 county folders (Class A),
  CA 48 + OR 27 (Class B); every county has 00-MASTER + BATCHES (≤100).
- Canonical registry: 8,752 rows (6,751 exported + 2,001 discovered,
  suppressed-if-ever-reshipped). `verify_leads.py`: PASS.
- Inventory awaiting decisions: 322 REVIEW businesses (unreachable/
  bot-walled sites), ~9,800 wrong-niche rows (car washes, tint) preserved
  in ENGINE-V2 if Joel ever widens the niche.

## Migration status

FOUNDING COMPLETE 2026-08-17. Both engine repos live at
`03-LEAD-SOURCING-ENGINE/` (V1 53/53 and V2 88/88 tests green at their
new homes; clean trees). The retired pre-OS workspaces are archived
whole in `99-ARCHIVE/` with FROZEN markers. The AIOS root router
resolves "Jump OS" here. Remaining hardening: git remotes for backup
(JUMP-OS itself is not yet a git repo; the SHIPPING registry and
trackers are currently version-controlled nowhere), and the disposition
tool for Monday evenings.

## Next

1. Kenzo starts calling Monday from 02-LEADS/CAR-DETAILERS batches
   (grab a batch, dial top-down; batch-01 of any county is its best).
2. Evening disposition rhythm: Kenzo reports called/booked/DNC; the
   operator records them in the registry and tracker.
3. Finish the founding: move engines + reference in, update the AIOS
   root router, add git remotes for backup.
4. Washington: engine-ready, ships only on Kenzo's explicit order after
   Joel triggers it.
