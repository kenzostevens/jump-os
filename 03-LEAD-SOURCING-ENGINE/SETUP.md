# SETUP — running the engines on a new machine

For any operator (human or AI) bootstrapping this OS somewhere other
than the machine that grew it. Read before assuming anything works.

## Requirements

- **macOS on Apple Silicon (arm64).** ENGINE-V2's pinned scraper binary
  and its bundled Chromium build are darwin-arm64 only. On any other
  platform the offline pipeline (reconcile, classify, ship, verify)
  still works, but live Google Maps acquisition does not, without
  obtaining and pinning an equivalent scraper build for that platform.
- **Python 3.9+**, standard library only. No pip installs, no
  virtualenvs, nothing else.
- ENGINE-V1 needs no toolchain: its acquisition is agent-driven browser
  capture, so it requires an AI harness with browser access and nothing
  more.

## Copy vs clone — the trap

ENGINE-V2's `.gitignore` deliberately excludes the heavy toolchain:
`tools/bin/` (the pinned scraper binary), `tools/browser-data/`
(Chromium and driver), caches and vendor trees, plus all campaign data
under `data/campaigns/`, `data/raw/*/terminal/`, `data/interim/`.

Consequences:

- A **git clone gives you code, not a working scraper** and not the
  raw campaign evidence. After cloning, copy `tools/` (and any needed
  `data/` history) from a working machine or backup by ordinary file
  transfer.
- A **whole-folder copy of the OS** (Finder copy, rsync, external
  drive) carries everything and is the recommended way to move to
  another Mac.

After placing the toolchain, verify the binary is intact: its expected
SHA-256 lives in `ops/toolchain.lock.json` and preflight checks it.

## Absolute-path caveat

Campaign manifests record absolute paths from the machine that planned
them. Completed campaigns remain fully readable and verifiable
anywhere. **Resuming an unfinished campaign or starting a new one on a
new machine requires planning a fresh run there** (`scraperctl plan`);
never hand-edit an existing manifest to fix paths.

## Verifying an install

From `ENGINE-V2/`:

1. `python3 -m unittest discover -s tests` — the offline suite must
   pass completely. Zero network involved.
2. `./scraperctl preflight --run-id <any existing run>` — exercises the
   binary hash, config digests, and git binding checks.

From `ENGINE-V1/`: `python3 -m unittest discover -s tests`.

From `SHIPPING/`: `python3 tools/verify_leads.py` must PASS — proves
the LEADS tree and canonical registry agree on this machine.

## What never travels

Credentials (none exist — the engines use no logins, proxies, or paid
APIs), and authorization: a new machine inherits the code and data,
not permission. Scraping, shipping, and anything beyond reading still
follow the laws in `../AGENTS.md`.
