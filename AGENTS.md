# AGENTS.md — Jump OS

Kenzo's lead operation for Jump Web Design (Joel, designedbyjump.com,
$48/mo websites for small service businesses). This OS discovers small
service businesses, verifies them, classifies their web presence, and
produces Teleblast-ready calling files. Kenzo calls; the OS does
everything before the call.

## Boot

1. Read `STATE.md` — current niche, coverage, counts, next action.
2. Read `03-LEAD-SOURCING-ENGINE/README.md` before operating any machinery.
3. Everything else on demand. Do not hydrate engine internals for
   questions a master CSV or STATE.md can answer.

## Layout — the organs

Jump OS is an evolving operating system for Kenzo's whole Jump job, not
a leads folder. Top-level ALL-CAPS folders are its organs; each owns its
world. **Organs are earned, never pre-built**: a new one appears only
when real, recurring work needs a permanent home. Inside every organ,
living documents (edited, versioned) are kept distinct from archives
(add-only, never edited).

- `02-LEADS/<NICHE>/<CLASS>/<STATE>/<NN-COUNTY>/` — the product. Teleblast-
  ready CSVs only. `00-MASTER` holds the full cut; `BATCHES` holds the
  ≤100-lead files Kenzo actually loads, best leads first. Folder numbers
  rank counties by lead count. Per-niche `TRACKER.csv` is the logbook;
  `REPORT.md` is its generated view. Derived data: never hand-edited.
- `01-PLAYBOOK/` — the craft. `SCRIPTS/` (living call scripts),
  `CALLS/` (add-only call transcripts and recordings),
  `TRAINING/` (sales training material).
- `03-LEAD-SOURCING-ENGINE/` — the machinery: `ENGINE-V1` (browser lane),
  `ENGINE-V2` (terminal lane), `SHIPPING` (the only path from engine
  output to LEADS; owns `registry.csv`, the suppression authority).
- `04-SKILLS/` — trigger-phrase instruction documents (see Skills below).
- `99-ARCHIVE/` — add-only shelf for material that mattered once and has no
  living home. Never a junk drawer: if something has a real home, it
  goes there.
- `STATE.md` — the single answer to "where are we."

## Skills

Trigger phrases map to instruction documents in `04-SKILLS/`. When the
user says the phrase, read the document and follow it.

- "give me a tour" / "show me around" / "how does this work"
    → read and follow `04-SKILLS/TOUR.md`

Adding a skill = drop a CAPS-DASH-NAMED.md in `04-SKILLS/` and add one
trigger line here.

## Laws

1. **Engines scrape and classify. Only SHIPPING ships.** Nothing enters
   LEADS except through `SHIPPING/tools/ship.py`; the canonical registry
   makes re-shipping and double-dialing structurally impossible.
2. **The registry only grows.** Exported is permanent history; DNC is
   forever and never downgraded.
3. **Classes are earned, not asserted.** Class A = no site / social-only /
   broken. Class B = site with objective flaws. Bot-blocked or
   inconclusive websites are REVIEW, never Class A. Missing evidence is
   never a positive claim.
4. **Stop on blocks.** CAPTCHA or block evidence halts acquisition for
   diagnosis. No automatic block recovery, no browser fallback, ever.
5. **Honest funnels.** Every campaign reports gross → unique → in-scope →
   eligible → phone-bearing → A/B/NQ/REVIEW, and failures are reported as
   failures.
6. **Reserved territory** (currently San Joaquin and Amador counties, CA)
   never ships regardless of which search surfaced it.
7. **LEADS is derived; engines are sovereign.** Rebuild LEADS from the
   registry and engine data any time; never reorganize an engine's
   internals from outside it.

## Authorization

Kenzo's standing delegation: once he orders a campaign (e.g. "ship
Washington on V2"), the full arc runs without per-step approvals —
plan, scrape, resume through transient failures, reconcile, classify,
verify, ship, verify again, update STATE. Report at completion or on a
genuine stop (a block, or evidence something is structurally wrong).

Always his alone, no matter what: anything leaving the machine (sending
counts or files to Joel or anyone, CRM/dialer writes, outreach), spend or
credentials, and STARTING a new territory or niche. Readiness is never
authorization.

## Working with Kenzo

He frequently uses speech-to-text: resolve garbled names against this
workspace before treating them as new things, and confirm before acting
when a transcription would change the destination. When he corrects you,
skip stock acknowledgments and respond with substance. Talk before
building: when he says "let's brainstorm" or "don't act yet," the
deliverable is the conversation.
