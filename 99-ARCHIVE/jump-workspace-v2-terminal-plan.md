# Jump Workspace V2 — Terminal Lead-Sourcing Rebuild

## Summary

- No files are changed during this planning turn.
- Before any duplication or implementation, save this complete plan verbatim to:
  `/Users/kenzoquiambao/AIOS/00-universal-workspace-scratchpad/jump-workspace-v2-terminal-plan.md`
- Build `/Users/kenzoquiambao/AIOS/jump-workspace-v2/` from the verified pre-scrape snapshot, not from the actively changing V1 workspace.
- V1 may continue operating independently. Do not interrupt, modify, import from, or share mutable state with it.
- V2 remains a candidate until its terminal scraper passes offline verification, a bounded live benchmark, committed review, and Kenzo’s explicit approval.
- “Jump V1” and “Jump V2” remain explicit names. The generic “Jump workspace” becomes intentionally ambiguous and must trigger a clarification.
- V2 will not use agent-operated browser scraping. The terminal binary may internally use automated headless Chromium, but no agent will manually open, scroll, extract, or save Google pages.

## Founding the V2 Workspace

1. Verify the source snapshot before copying:

   - Source: `/Users/kenzoquiambao/AIOS/00-universal-workspace-scratchpad/jump-workspace-pre-scrape-snapshot-20260815`
   - Nested repository commit: `22cbc3d20c21ab6dda73916224d779dd85ffa231`
   - Expected branch: `pre-scrape-snapshot`
   - Expected state: clean, no Git remote, and no car-detailer browser captures.
   - Preserve the source snapshot unchanged.

2. Duplicate the snapshot contents—not an extra nesting level—into:

   - `/Users/kenzoquiambao/AIOS/jump-workspace-v2/`
   - Keep the top-level shell outside Git.
   - Keep `/Users/kenzoquiambao/AIOS/jump-workspace-v2/jump-leads/` as the independent Git repository.
   - Confirm the destination initially matches the source commit and contains no active-process files or V1 scrape output.
   - Create branch `v2-terminal-candidate` and make a founding commit only after the V2 identity and instructions are updated.

3. Update routing and operating instructions:

   - Add explicit “Jump V1” and “Jump V2” aliases to the AIOS root router.
   - Remove deterministic routing for the generic “Jump workspace”; require clarification when no version is named.
   - Mark V2 as a terminal-scraper candidate.
   - Prohibit manual-browser acquisition and silent browser fallback in V2.
   - Preserve the one-pen, commit-boundary review, and explicit-authorization rules.
   - V1 remains independently writable by Claude Fable and is not converted to read-only.

4. Data boundary:

   - V2 starts with zero car-detailer acquisition data.
   - Do not copy or import any current V1 browser captures, normalized car-detailer rows, ledgers, or exports.
   - The older dog-groomer registry already present in the pre-scrape snapshot remains intact.
   - V2 performs no CRM export or outreach during candidate development.

## Terminal Acquisition Engine

### Toolchain

- Reuse the proven toolchain from the frozen original lead-sourcing engine by copying only generic assets into V2; never modify the original workspace.
- Seed the verified executable:

  - Source: `/Users/kenzoquiambao/AIOS/original-lead-sourcing-engine/tools/bin/google_maps_scraper`
  - Expected SHA-256: `26af4aa3e19c1446867d209925c4fc68eed30dae090cd02810781278835343a6`
  - Upstream: `gosom/google-maps-scraper`
  - Pinned commit: `0ef302ecc72a8872d5dac68cbbeab78800f80fdd`
  - Preserve the telemetry-disabled and compatibility patches, build receipt, and toolchain lock.
  - Keep the large binary and runtime/browser artifacts out of Git; track their hashes, versions, patches, and reproducible bootstrap instructions.

- Preflight must fail closed on a missing executable, hash mismatch, incompatible runtime, missing Chromium dependency, dirty run configuration, or unavailable output directory.

### Coordinates and campaign plan

- Enrich the existing 236-city CA/OR grid using the official [2025 U.S. Census Gazetteer Places file](https://www.census.gov/geographies/reference-files/2025/geo/gazetter-file.html).
- Record the source URL, download timestamp, and SHA-256.
- Match by normalized place name and state, then validate the representative latitude/longitude against the configured state and county geometry.
- Any unmatched, ambiguous, or county-mismatched city blocks the live run. Do not guess or browser-geocode it; coordinate overrides require separate approval and source documentation.
- Preserve the existing query policy:

  - Tier 1–2: `car detailing`, `auto detailing`, and `mobile car detailing`.
  - Tier 3: `car detailing` only.
  - Expected total: 450 deterministic city/query checkpoints.

### Runner interface and behavior

Provide one terminal entrypoint, exposed through `scraperctl`, with these commands:

- `preflight`: verify repository, toolchain, coordinates, configuration hashes, ceilings, and disk/runtime availability.
- `plan`: generate an immutable campaign manifest without making network requests.
- `run`: execute pending checkpoints for a new run.
- `resume`: continue only checkpoints that have no verified successful output.
- `status`: report completed, pending, failed, blocked, row counts, and elapsed time.
- `reconcile`: normalize immutable raw outputs and deduplicate them.
- `verify`: independently reconstruct counts and lineage from raw output.

Each run manifest records:

- Run ID and creation time.
- Git commit and dirty-state assertion.
- Grid, niche, coordinate-source, and toolchain digests.
- Selected scraper profile and exact arguments.
- Ordered checkpoint IDs and queries.
- Per-checkpoint and total result ceilings.
- Concurrency, timeout, radius, zoom, and stop policy.

Checkpoint behavior:

- One city/query pair per checkpoint.
- Deterministic ID based on state, city, and query variant.
- Immutable query input and raw terminal CSV.
- Separate stdout, stderr, exit code, duration, command metadata, and SHA-256 receipt.
- Atomic ledger replacement and crash-safe resumption.
- Never overwrite a successful checkpoint.
- Never mark partial or malformed output successful.
- Configuration or code changes require a new run ID.

### Scraper profiles

1. Primary profile: fast terminal mode.

   - Geo-centered on the verified Census coordinate.
   - Radius: 10,000 metres.
   - Zoom: 13.
   - Concurrency: 1.
   - Inactivity timeout: 3 minutes.
   - Maximum: 21 raw results per checkpoint and 9,450 for the complete campaign.

2. Coverage fallback: standard automated terminal mode.

   - Used only if the benchmark proves fast mode materially incomplete.
   - Depth: 3.
   - Concurrency: 1.
   - Inactivity timeout: 3 minutes.
   - Maximum: 75 raw results per checkpoint and 33,750 for the complete campaign.
   - This remains unattended terminal automation; it is not the V1 manual-browser workflow.

3. There is no browser-operated fallback. If both terminal profiles fail acceptance, V2 stays a candidate and the full run does not start.

### Normalization and safety

- Preserve the binary’s CSV as the acquisition source of truth.
- Normalize into the existing Jump lead schema through a dedicated terminal adapter rather than disguising terminal output as a browser capture.
- Add provenance fields for source kind, input ID, checkpoint ID, toolchain hash, raw-file hash, and acquisition timestamp.
- Prefer stable Google identifiers in this order: `data_id`, `cid`, then `place_id`; retain the existing safe fallback identity policy where none exists.
- Reuse the existing scope filter, deduplication, website audit, registry, export preparation, and independent verifier.
- Website auditing remains concurrent Python HTTP work, not interactive browsing.
- Stop the run on CAPTCHA/block evidence, binary hash drift, schema drift, ceiling violations, unexplained empty output, or two consecutive zero-result checkpoints.
- Do not use proxies, logins, personal Google sessions, paid APIs, or automatic block recovery.

## Verification, Benchmark, and Promotion

### Offline verification

Before any Google request:

- Confirm source/destination snapshot equivalence and clean Git state.
- Confirm V2 contains no V1 car-detailer captures.
- Test Census coordinate matching and county validation for all 236 cities.
- Confirm exactly 450 unique checkpoint IDs.
- Exercise runner planning, atomic ledger writes, idempotent resume, corrupted output handling, failure preservation, and ceiling enforcement using fixtures.
- Test terminal CSV parsing with normal businesses, missing fields, service-area businesses, duplicate stable IDs, malformed rows, and unexpected categories.
- Run the full downstream pipeline and independent verifier against fixture data.
- Commit the implementation and review that exact commit before the live benchmark.

### Bounded live benchmark

- Use Modesto, Anaheim, and Fresno with all three query variants: nine terminal checkpoints.
- Freeze the comparison to a specific committed V1 revision containing complete browser captures for those cities. Read it only; do not import it.
- Run fast mode first, with a maximum of 189 raw terminal results.
- Measure:

  - Total and per-checkpoint runtime.
  - Gross and unique businesses.
  - In-scope phone-bearing businesses.
  - Website and phone completeness.
  - Stable-ID overlap with V1.
  - Category exclusions, service-area handling, and out-of-scope rows.
  - Errors, blocking signals, retries, and malformed output.

- Fast mode passes when:

  - It has no blocks, schema failures, or ceiling violations.
  - It finishes in no more than 50% of the V1 elapsed acquisition time for the equivalent queries.
  - It recovers at least 75% of V1’s unique in-scope phone-bearing businesses.
  - Its phone and website completeness rates are each no more than five percentage points below V1.

- If fast mode misses those coverage thresholds, run the same nine checkpoints once using standard automated mode, capped at 675 raw rows.
- Standard mode passes when:

  - It has no blocks, schema failures, or ceiling violations.
  - It finishes in no more than 75% of the equivalent V1 acquisition time.
  - It recovers at least 90% of V1’s unique in-scope phone-bearing businesses.
  - Its phone and website completeness rates are each no more than five percentage points below V1.

- If simultaneous V1 traffic produces blocking or makes timing unreliable, record the benchmark as failed/inconclusive. Do not interrupt V1 or promote V2 based on contaminated measurements.

### Promotion

- Commit benchmark evidence and the independently generated verification report.
- Review the exact committed candidate snapshot.
- Require Kenzo’s explicit approval before the full 450-checkpoint run.
- Use the fastest terminal profile that passed every acceptance threshold.
- Keep concurrency at 1 for the initial production campaign.
- After the full run, require raw-to-export reconciliation, zero unexplained count differences, and a final committed review before any V2 export is authorized.
- Even after V2 is approved, both workspaces retain explicit names. Generic “Jump workspace” requests must still be clarified.

## Assumptions and Locked Decisions

- V1 may continue scraping and processing while V2 is constructed; V2 will not touch or interrupt it.
- Current V1 browser-acquired data remains in V1 only.
- V2 is founded from the verified pre-scrape snapshot, not the current V1 head.
- No manual or agent-operated browser acquisition is allowed in V2.
- The original lead-sourcing engine remains frozen and read-only.
- No V2 CRM export, outreach, paid service, proxy, or personal-account use is included.
- The plan MD file is the first artifact created when execution is authorized, before the V2 directory or any other tracked state is changed.
