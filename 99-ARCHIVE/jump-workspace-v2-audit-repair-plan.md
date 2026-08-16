# Jump Workspace V2 — Audit Repair Plan

## Authorization boundary

- Kenzo authorized this offline repair on 2026-08-15.
- This repair may change V2 code, tests, operating documentation, and Git history.
- It does not authorize Google Maps scraping, the prepared live benchmark,
  website-audit network requests, export, CRM/dialer changes, outreach, spend,
  credentials, proxies, or changes to Jump V1 or the frozen original engine.

## Repair 1: terminal zero-result correctness

1. Recognize the pinned scraper's legitimate zero-byte output as a possible
   successful zero-row checkpoint.
2. Accept zero rows only when the scraper exits successfully, creates the
   output file, emits no block/error evidence, and supplies the expected clean
   terminal-completion evidence.
3. Preserve the raw output exactly, finalize it immutably, and create the same
   hash-bound receipt used for nonempty checkpoints with `row_count: 0`.
4. Mark a verified zero-row checkpoint `done`, so resume never repeats it.
5. Apply the two-consecutive-zero diagnostic only after both successful
   checkpoint artifacts are finalized. Stop when work remains; do not turn two
   terminal zeros at the natural end of a campaign into a false failure.
6. Make reconciliation and the independent verifier understand verified
   zero-byte and header-only zero-row terminal outputs.
7. Add regression tests for legitimate and malformed empty results, blocking
   evidence, isolated zeros, consecutive zeros, terminal zeros, immutable
   resume, and zero-row reconciliation.

## Repair 2: terminal-to-Jump downstream handoff

1. Add `scraperctl classify --run-id <id>` as the explicit step between
   terminal reconciliation and export preparation.
2. Read the reconciled `in-scope.json`, run the existing concurrent Python
   website classifier, and write `classified.json` plus a classification
   summary without coupling website requests to Maps acquisition.
3. Preserve resumability by reusing compatible prior website audits and never
   requiring a Maps checkpoint to repeat.
4. Extend verification so terminal lineage is always reconstructed and, when
   classified output exists, classification membership, counts, and lead-class
   decisions are independently checked.
5. Keep export and registry mutation separately authorized; offline tests use
   fixtures and fake website responses only.
6. Add a complete offline fixture path from terminal CSV through normalization,
   dedupe, scope, classification, independent verification, and export
   preparation.
7. Correct V2 operating documentation so every required command is visible.

## Acceptance gates

1. No Google Maps or website network request occurs during implementation or
   verification.
2. Jump V1 and the frozen original engine remain unchanged.
3. All offline tests pass, including the new regression and end-to-end cases.
4. The prepared nine-checkpoint benchmark remains planned with all checkpoints
   pending.
5. The exact candidate diff receives a read-only audit before commit.
6. State and run records honestly describe the repair and the continuing live
   authorization boundary.
7. Commit the repaired candidate, then stop. Any live benchmark still requires
   Kenzo's separate explicit scraping signal.
