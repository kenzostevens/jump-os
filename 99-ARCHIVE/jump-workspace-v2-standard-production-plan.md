# Jump V2 — Standard Terminal Production Hardening

## Summary

- First execution action: save this plan verbatim to `/Users/kenzoquiambao/AIOS/00-universal-workspace-scratchpad/jump-workspace-v2-standard-production-plan.md`.
- After any compaction, rehydrate from that plan, V2’s `AGENTS.md`, `STATE.md`, and Git—not chat memory.
- Baseline: clean V2 commit `d459a2dccc74dbc0b866d8bd5913d31c7d8b666d`.
- V2 becomes the production engine only after its standard-profile benchmark passes.
- No agent or LLM will operate Google searches individually. One terminal command owns the complete checkpoint loop.
- V1 stays paused and untouched. The original engine remains frozen and read-only.
- Offline implementation does not authorize scraping, website requests, export, CRM changes, or outreach.

## Implementation Changes

### Category gate

- Partition reconciled in-scope rows before website auditing:
  - `expected` → eligible.
  - `unknown` → eligible.
  - `unexpected` → excluded as `wrong_niche_category`.
- Produce immutable/reproducible `category-eligible.json` and `category-excluded.json`.
- Preserve each excluded row’s business, observed category, checkpoint, and provenance.
- Add funnel fields for expected, unknown, unexpected-excluded, eligible, and eligible-phone-bearing counts.
- Website auditing and export may consume only category-eligible rows.
- The independent verifier must reconstruct the partition and fail if an unexpected row reaches classification or export.
- Never silently widen the expected-category allowlist.

### Standard terminal profile

- Standard depth-3 becomes the approved benchmark and production profile: concurrency 1, 75-result checkpoint ceiling.
- Fast mode remains available for diagnostics but is not used for promotion or production.
- Update operating instructions and benchmark reporting accordingly.
- Preserve both existing fast manifests as zero-progress historical artifacts; they become stale after the new commit and must never run.
- Generate the fresh standard benchmark only after the repository is clean and committed:
  - Run ID: `jump-v2-standard-benchmark-20260815`
  - Cities: Anaheim, Fresno, Modesto
  - Nine checkpoints
  - Maximum 675 raw rows
  - V1 comparison commit: `25f6da79f525e10e00ba15483b06b1268869ab1b`

### No-LLM-labor guarantee

- Audit the complete V2 path: plan, run/resume, raw saving, ledger advancement, reconciliation, category filtering, website classification, verification, and export preparation.
- Confirm no terminal entrypoint invokes `capture_snippet.js`, `save_capture.py`, an interactive browser, or an agent-controlled page loop.
- A single `scraperctl run` or `resume` invocation must automatically process every pending checkpoint.
- Normal execution may require human/LLM involvement only to start an authorized stage, review results, or diagnose a fail-closed safety stop.
- CAPTCHA, blocking, schema drift, corruption, ceilings, and suspicious zero-result sequences remain exceptional stops, not routine labor.

## Offline Verification and Commit

- Add tests proving:
  - Expected and unknown categories continue.
  - Unexpected categories are excluded and never website-fetched.
  - Exclusions remain visible in artifacts and funnel counts.
  - Independent verification detects partition tampering.
  - One runner invocation automatically completes multiple synthetic checkpoints.
  - Crash/resume never repeats verified successes or verified zeros.
  - No browser-capture dependency exists in the terminal entrypoint.
  - Terminal fixture reaches category partition, classification, export selection, and independent verification without network access.
- Run the complete offline suite, compilation checks, diff checks, and compatibility checks against the original engine’s historical CSV artifacts.
- Update `AGENTS.md`, `STATE.md`, and `runs.md`; commit the exact offline candidate.
- Generate the standard benchmark manifest after that commit, then require:
  - Clean Git state.
  - Preflight PASS.
  - Nine pending checkpoints.
  - Zero completed checkpoints.
  - Zero network requests during planning.
- Stop and wait for Kenzo’s explicit scraping signal.

## Benchmark, Promotion, and Production Gates

- On Kenzo’s benchmark go, execute the nine checkpoints with one unattended terminal command, then reconcile and verify locally.
- Do not perform website-audit requests or exports during the benchmark.
- Standard benchmark passes only when:
  - No block, schema failure, ceiling violation, or unexplained output occurs.
  - Runtime is at most 1,488 seconds, 75% of V1’s 1,984-second baseline.
  - It recovers at least 162 of V1’s 180 unique phone-bearing businesses.
  - Phone completeness is at least 92.83%.
  - Website-field completeness is at least 74.35%.
  - At least 80% of in-scope rows have an observed category; unknown-category rate is at most 20%.
  - Zero `unexpected` rows reach the eligible population.
  - The report lists excluded categories, counts, unknown rate, overlap, malformed rows, and obvious remaining junk.
- If an excluded category plausibly represents real detailers, mark the benchmark inconclusive and report it; do not automatically modify the allowlist.
- If the benchmark fails, V2 remains a candidate. Do not fall back to V1 or automatically run fast mode.
- If it passes, commit the evidence and stop for Kenzo’s separate full-campaign approval.
- After that approval, enable the production gate, commit it, generate a fresh standard 450-checkpoint manifest, and run the complete CA/OR acquisition with one unattended command.
- Website classification remains a separately authorized unattended stage after production reconciliation.

## Registry and Export Safety

- Current V1 and V2 registries are identical: 283 rows at SHA-256 `c8e22dd3acc1418b4a6678d99615f507570f072f21053ad5ed94e304b5ba7ae0`.
- Before the first V2 export, recompare them at explicit committed boundaries.
- If V1 is unchanged, no merge is necessary.
- If V1 gained calling history, import only `exported`, `called`, `booked`, and `dnc` suppression history—never its unexported browser discoveries.
- Match stable ID first and normalized phone second; status precedence is `dnc > booked > called > exported > discovered`.
- Preserve DNC permanently and preserve the earliest `first_seen` date.
- Commit and independently verify the synchronized V2 registry before export.
- V2 becomes the sole export lane; V1 must never export independently after cutover.
- Export, CRM/dialer mutation, and outreach each remain separately unauthorized until Kenzo explicitly approves them.

## Locked Assumptions

- `unexpected` means wrong niche and is excluded; `unknown` is not evidence of a violation and continues.
- Standard depth-3 is preferred over a fast sweep plus selective re-touch because it keeps one unattended acquisition and provenance path.
- Browser automation internal to the terminal binary is allowed; agent-operated browser work is prohibited.
- V1 car-detailer captures and rows are never imported into V2.
- Every code/config change requires a new run ID and fresh manifest.
- No scraper, website auditor, benchmark, production campaign, or export starts while implementing this offline plan.
