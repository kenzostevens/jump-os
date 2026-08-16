# STATE — Jump OS

Updated: 2026-08-17 (early morning — niche expansion shipped; full OS
audit passed)

## Current campaigns

Scraping is COMPLETE for California + Oregon (San Joaquin and Amador
counties reserved, untouched by design). Calling begins Monday
2026-08-17 via Teleblast; the owner plans ~60 dials/day against a
40/day expectation.

## Counts (see `02-LEADS/REPORT.md` for the full breakdown)

| Niche | Class A | Class B | Callable | Batches |
|---|---:|---:|---:|---:|
| CAR-DETAILERS | 4,980 | 1,771 | 6,751 | 187 |
| CAR-WASHES | 870 | 369 | 1,239 | 125 |
| WINDOW-TINT | 173 | 143 | 316 | 86 |
| CAR-DETAILERS unverified pile | — | — | 296 | 3 |

New-niche counts are after registry suppression of phones already
shipped under another niche. Totals: **8,602 registry-protected
callable leads.** All batches `untouched`; every niche has its own
TRACKER.csv.

- Canonical registry: 10,307 rows; 8,602 exported, remainder
  discovered-and-suppressed. `verify_leads.py`: PASS, all niches.
- The unverified pile (`CAR-DETAILERS/REVIEW-UNVERIFIED/`) is honestly
  labeled: websites unreachable by machine, ask about the site on the
  call. Never mixed with Class A/B.
- Still preserved unbuilt in ENGINE-V2: wrap shops, auto glass, auto
  repair/body, and other excluded categories (~5,600 rows) — future
  niches on the owner's word.

## Standing decisions

- Disposition tool: declined; call outcomes are recorded by an operator
  session by hand when reported.
- Joel share window: declined; nothing is shared or uploaded.
- Washington: engine-ready, not scraped, awaits the owner's explicit
  order.
- Off-machine backup: LIVE as of 2026-08-17. Private GitHub remotes
  under kenzostevens: JUMP-OS, JUMP-OS-ENGINE-V1, JUMP-OS-ENGINE-V2.
  Backing up = `git push` in each repo after committing. Note: the
  engine repos' gitignores exclude the scraper toolchain and raw
  campaign data — full recovery of those needs a whole-folder copy
  (see 03-LEAD-SOURCING-ENGINE/SETUP.md).

## Next

1. Calling starts from any niche's `BATCHES` files (batch-01 of a
   county is its best leads). Report outcomes to an operator session to
   keep tracker + registry true.
2. Future niches ship from the preserved pile on the owner's word.
