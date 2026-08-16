# Jump Lead Sourcing Engine — Durable Master Plan

> Planning document only. This file is not authorization to implement the
> engine, install dependencies, scrape, browse prospect websites, spend money,
> use credentials, change a dialer/CRM, contact anyone, or perform any other
> external action.

> **Historical plan, not a routine boot file.** Current authority is the
> engine's `AGENTS.md`, frozen contract/receipt, `00_STATE/WORKFLOW.json`, and
> `00_STATE/CURRENT_STATE.md`. Run `lead-sourcing-engine/scraperctl rehydrate`
> instead of reading this complete file during routine recovery.

## Execution update — 2026-08-11

Kenzo subsequently authorized execution of this plan. Phases 0–6 are complete
and verified offline. Phase 7 is complete: the six-county Jump contract is
approved, frozen, and checksum-bound. Campaign-layer implementation and Phases
8–12 remain separately gated; no external action is authorized.

**Corrective update:** a later strict audit retracted the first Phase 3–6
readiness claim, identified concrete adapter, lease, state, recovery, identity,
capture, Git-safety, and verifier gaps, and Kenzo authorized their correction.
Run `20260811-engine-hardening` rebuilt those layers and re-ran the acceptance
gates with 58 adversarial tests and a zero-network end-to-end simulation. The
generic engine is now verified within its offline boundary. No live adapter or
campaign is configured. A later cross-harness governance hardening phase owns
the active deterministic handoff before campaign-layer implementation.

## Purpose

Build a real, reusable lead sourcing engine for Jump without copying the
historical Texas workspace wholesale and without weakening the safeguards that
made the original process trustworthy.

The finished Jump engine should be substantial in code, schemas, tests, and
verification, while keeping its routine cold-start context small. Workspace
size and boot-context size are separate concerns: agents should read a compact
authority surface first and inspect implementation modules only when their
current phase requires them.

## Current verified baseline

### Jump scratchpad

- Scratchpad root:
  `/Users/kenzoquiambao/AIOS/00-universal-workspace-scratchpad/jump-scratchpad`
- This master plan lives outside the engine so it survives engine redesign and
  remains easy to name after context compaction.
- The only meeting file read so far is `first-call.txt`. Other Jump scratchpad
  files have not been read as part of this work.

### New Jump engine shell

- Path:
  `/Users/kenzoquiambao/AIOS/00-universal-workspace-scratchpad/jump-scratchpad/lead-sourcing-engine`
- State: lean shell only; not yet an operational engine.
- Local Git branch: `main`
- Baseline commit:
  `2b90a191d4bac17180e18383235f34b1bdddf112`
- Git remote: none.
- Existing shell contains compact instructions, current state, decisions,
  contract and pipeline placeholders, ignored data/runtime/output directories,
  and an append-only run log.
- It contains no acquisition runner, reconciler, classifier, schemas,
  dependency locks, fixtures, or tests yet.

### Frozen original engine

- Path:
  `/Users/kenzoquiambao/AIOS/original-lead-sourcing-engine`
- Authority: frozen, read-only provenance reference.
- Verified HEAD at Jump bootstrap:
  `ef0554a78ff4f165df8650de1718d3c5a38156a2`
- Verified tree at Jump bootstrap:
  `0e56e2a6518e4fa72ee2f5ffd0b810885c8815de`
- It must never be edited, used as a worker lane, or receive Jump outputs.
- Its Texas data, ignored evidence, run history, RMP logic, Fable recovery
  state, and CRM outputs must not be copied into the Jump engine.

## Non-negotiable operating principles

1. **Original remains untouched.** Comparison and selective read-only study
   are allowed. Writes, generated outputs, runs, or repairs there are not.
2. **Extract the spine, not the history.** Reuse proven generic patterns and,
   where justified, small reviewed utilities. Do not duplicate the original
   repository or its data corpus.
3. **Freeze before computing.** Targeting, sources, schema, limits, decision
   rules, and authorization must be written before a result is produced.
4. **Stable identity before weak evidence.** Prefer stable platform IDs, then
   corroborated published phones/domains/name-address evidence. Ambiguity is a
   hold, not a forced merge.
5. **Raw evidence is immutable.** Corrections create new derived artifacts or
   new snapshots; they never overwrite preserved source material.
6. **Checkpoint every external unit.** A completed request is never repeated.
   Resume comes from a durable atomic ledger.
7. **Desired counts are capacity goals, not qualification rules.** A target
   such as 100 may size discovery, but it may not change whether a business
   passes.
8. **Unknown is a valid outcome.** Missing, stale, conflicting, or weak
   evidence never becomes a positive claim.
9. **Published business contact remains distinct from personal enrichment.**
   Personal or skip-traced data is outside the default engine and requires a
   separate experiment and approval.
10. **Models do not certify their own work.** Material transforms require
    deterministic validation, replay where appropriate, and an independent
    verification path.
11. **External actions are separately gated.** Planning does not authorize
    scraping; scraping does not authorize CRM import; CRM preparation does not
    authorize calling or outreach.
12. **Context stays routed.** Routine startup reads only governing state and
    the active phase/run. Historical runs and large evidence trees are opened
    only on demand.

## Compaction recovery procedure

When a new agent or compacted session resumes, read the scratchpad router and
engine `AGENTS.md`, then run `lead-sourcing-engine/scraperctl rehydrate`.
Follow its verified compact read order. This historical plan is consulted only
for archaeology; it cannot select or authorize the current phase.

Suggested recovery instruction from Kenzo:

> Rehydrate from the Jump lead sourcing engine master plan, verify the Jump
> engine and frozen original baselines, then continue only the next explicitly
> authorized phase.

## What to reuse from the original design

The read-only capability audit should evaluate these generic components:

- Workspace-root discovery and portable relative paths.
- Stable command entrypoint design.
- Read-only preflight and dependency verification.
- Machine-readable run specifications and authorization receipts.
- Atomic JSON state writes and append-only event ledgers.
- Per-checkpoint immutable inputs, logs, raw outputs, hashes, and resume rules.
- Process-group timeouts and completed-request adoption after host loss.
- Result ceilings that reserve full per-checkpoint headroom.
- Blocking, schema, checksum, no-overwrite, and ambiguity guards.
- Input provenance maps.
- Phone, domain, name, address, and stable-ID normalization.
- Conflict-safe campaign identity reconciliation.
- Lifetime registry reconciliation into net-new, historical duplicate,
  historical changed-detail, and manual-review outcomes.
- Target-blind classification with explicit reason codes.
- Disjoint output partitions and exact count balancing.
- Formula-prefix protection and CSV parse-back.
- Deterministic replay and independent verification patterns.
- Offline synthetic simulation.
- Private-repository and sensitive-data checks.
- Optional host lease and encrypted backup patterns if the Jump operating
  model later needs them.

Reuse must be selective. Every imported utility receives a source reference,
a Jump-specific review, tests, and removal of historical hard-coding.

## What must not be imported as active Jump logic

- Texas plumbing geography, grid files, counties, and query sequence.
- `plumber` or other Texas-specific query constants.
- Texas RMP datasets, roles, scoring, matching, or licenses.
- Texas Comptroller/entity-source assumptions.
- SINNTHETIC offer, company context, field naming, or operational state.
- The 1,873-row or 7,777-row Texas lifetime registries.
- Historical Class A/Class B lead files or GoHighLevel packages.
- Fable incident/recovery phases, raw evidence, corrective queues, or
  historical handoffs as live procedure.
- One-off geographic plan generators for DFW, Houston, Austin, or later Texas
  bands.
- Old run IDs, authorization tokens, hashes, counts, forecasts, or next actions.
- Platform-specific launch agents and runtime receipts.
- Browser profiles, cookies, caches, vendor trees, compiled binaries, or
  ignored lead data.
- Any rule that equates a trade license holder with an owner or decision maker.

Historical failures may be converted into small sanitized regression fixtures
without copying real lead records.

## Desired engine architecture

The target architecture is compact at the top and modular underneath:

```text
lead-sourcing-engine/
├── AGENTS.md
├── README.md
├── scraperctl
├── 00_STATE/
│   ├── CURRENT_STATE.md
│   └── DECISIONS.md
├── 01_CONTRACT/
│   ├── PROJECT.md
│   └── schemas/
├── 02_PIPELINE/
│   ├── README.md
│   ├── config/
│   ├── src/
│   │   ├── workspace/
│   │   ├── acquisition/
│   │   ├── identity/
│   │   ├── websites/
│   │   ├── qualification/
│   │   ├── registry/
│   │   ├── packaging/
│   │   └── verification/
│   ├── fixtures/
│   └── tests/
├── 03_DATA/
│   ├── raw/
│   ├── interim/
│   └── final/
├── 04_RUNS/
│   ├── RUN_LOG.md
│   └── _TEMPLATES/
├── 05_RUNTIME/
└── outputs/
```

The exact programming-language/module layout should be chosen during design,
not assumed from this sketch.

## Implementation phases

Each phase requires a documented start boundary, verification, state update,
and clean checkpoint. Later phases are not authorized merely because an
earlier one finishes.

### Phase 0 — Audit the existing Jump shell

**Goal:** establish whether the current shell is the correct durable base.

Actions:

- Verify the baseline commit and clean status.
- Review the shell's instruction and state files for omissions, duplication,
  stale claims, and context bloat.
- Confirm ignored operational directories behave as intended.
- Confirm no other Jump scratchpad file was accidentally incorporated.
- Decide whether the engine stays an independent Git repository inside the
  scratchpad.
- Produce a concise audit receipt and amend the shell only if authorized.

Exit gate:

- The shell is accepted as the build base or replaced through an explicit,
  non-destructive correction.

Status: **complete** (2026-08-11).

### Phase 1 — Read-only original capability audit

**Goal:** map the proven generic machinery without hydrating irrelevant
history or copying anything.

Actions:

- Inspect the original's active command surface, acquisition runner, identity
  reconciler, lifetime reconciler, workspace utilities, preflight, lease,
  offline simulation, tests, and schemas.
- Map dependencies between those components.
- Identify hardcoded Texas/SINNTHETIC assumptions line by line where they
  affect reusable code.
- Record candidate utilities as `reuse`, `rewrite`, `reference only`, or
  `exclude`.
- Record licensing and provenance for imported third-party code.
- Do not run original campaigns or generate outputs there.

Deliverable:

- A machine-readable and human-readable capability matrix stored in the Jump
  engine.

Exit gate:

- Every proposed import has a reason, dependency map, and contamination check.

Status: **complete** (2026-08-11).

### Phase 2 — Freeze the extraction and build contract

**Goal:** prevent an ad hoc partial copy or a second bloated historical clone.

Actions:

- Freeze the exact original source commit/tree used as reference.
- List every source file or algorithm to port and every prohibited path.
- Define whether each selected component is copied, generalized, or rewritten.
- Define the target module interfaces and minimal supported command surface.
- Define code provenance and expected tests.
- Define no-network and no-data-copy assertions.

Exit gate:

- Kenzo can see exactly what will be brought over and what will remain behind.

Status: **complete** (2026-08-11).

### Phase 3 — Build the generic operational foundation

**Goal:** make the Jump folder a real engine without selecting or acquiring a
campaign.

Expected components:

- Workspace/root discovery.
- Stable CLI entrypoint.
- Atomic file and state utilities.
- Run ID and manifest handling.
- Machine-readable authorization receipt.
- Generic plan validation.
- Checkpoint initialization, execution, status, verification, and resume.
- No-overwrite artifact finalization.
- Request/result caps and fail-closed stop reasons.
- Process timeout/termination handling.
- Provenance-map export.
- Zero-network preflight.
- Sensitive-data and repository audit.

No active source query, geography, target niche, or live scraper request is
part of this phase.

Exit gate:

- The generic command surface operates entirely on sanitized offline fixtures.

Status: **complete** (2026-08-11).

### Phase 4 — Build generic identity and registry layers

**Goal:** reproduce the original engine's strongest reusable data guarantees.

Expected components:

- Canonical normalization for stable platform IDs, published phones, domains,
  names, and structured addresses.
- Platform/directory-domain exclusions.
- Stable-before-weak campaign deduplication.
- Conflict quarantine that prevents transitive weak chains from bridging
  incompatible stable identities.
- Complete input-to-canonical provenance.
- Lifetime registry schema.
- Net-new, historical duplicate, changed-detail, and manual-review partitions.
- Exact union/disjointness accounting.
- Deterministic permanent ID allocation rules appropriate to Jump.

Exit gate:

- Sanitized positive and adversarial fixtures pass with exact balanced counts.

Status: **complete** (2026-08-11).

### Phase 5 — Build bounded website and qualification infrastructure

**Goal:** support Jump's likely website-opportunity research without freezing
the actual campaign rules prematurely.

Expected components:

- Public-URL safety and redirect controls.
- Immutable response capture with byte/time/request limits.
- Website-state observations kept separate from business identity.
- Evidence categories capable of representing no site, social-only,
  unreachable/dead, parked/hijacked, broken, functional, and unresolved.
- Classification contracts with allowed reason codes and an explicit hold.
- Target-blind decision queues that do not expose desired output totals.
- Published business-phone callability handling.
- Clear separation between observed facts and final qualification decisions.

The exact meaning of Class A, Class B, hold, and exclusion belongs in the
later Jump project contract.

Exit gate:

- Offline fixtures prove that missing or failed website evidence cannot be
  promoted into a positive sales opportunity.

Status: **complete** (2026-08-11).

### Phase 6 — Verification and portability closure

**Goal:** prove the generic engine is safe before real campaign design.

Required verification:

- Complete unit suite.
- Adversarial identity suite.
- Intentional interrupted-checkpoint preservation and resume.
- No duplicate request after completed checkpoint.
- Schema and checksum mismatch failure.
- No-overwrite behavior.
- Row-union and disjointness checks.
- Independent verifier that does not import the primary transform.
- Offline end-to-end simulation with zero network.
- Root discovery from nested paths.
- Private repository audit.
- Original-engine clean/unchanged comparison.
- Boot-context review confirming routine startup remains concise.

Exit gate:

- A terminal engine-readiness receipt identifies all passes, limitations, and
  any separately deferred operational features.

Status: **complete** (2026-08-11).

### Phase 7 — Freeze the Jump project contract

**Goal:** translate approved business requirements into a campaign contract.

Possible inputs include the already read first-call transcript and any other
specific Jump materials Kenzo later authorizes for reading. Do not scan the
scratchpad broadly.

The contract must explicitly define:

- Company and offer.
- Target niche and exclusions.
- Geography and order of expansion.
- Business-size and independence signals.
- Website-opportunity evidence and decision precedence.
- Published phone requirements.
- Owner/decision-maker expectations, if any.
- Lead classes, holds, exclusions, and unresolved outcomes.
- Required fields and evidence provenance.
- Initial operating objective and quality gates.
- Output/dialer schema and import boundary.
- Compliance, cost, network, and credential limits.

Exit gate:

- Kenzo approves the written contract before plan generation.

Status: **complete — approved and checksum-frozen** (2026-08-11).

### Phase 8 — Design and validate the pilot plan

**Goal:** create a bounded, non-authorized plan sized to produce useful
evidence about yield and quality.

Actions:

- Select geography and query strategy from the frozen contract.
- Calibrate overlap and likely raw-to-qualified yield with a small plan.
- Freeze checkpoint inputs, order, caps, source configuration, expected
  maximum cost, and stop conditions.
- Bind the plan to the current lifetime registry, even if the initial registry
  is empty.
- Validate the plan offline.
- Keep every row and run state explicitly `not_authorized`.

Exit gate:

- Kenzo reviews the exact plan before any external request.

Status: **pending**.

### Phase 9 — Execute separately authorized acquisition

**Goal:** acquire only the frozen pilot evidence.

Rules:

- Record Kenzo's exact approval in the run manifest.
- Use the exact verified runner and plan.
- Run conservatively with checkpointing and hard ceilings.
- Preserve logs, raw artifacts, failures, and hashes.
- Never repeat a completed checkpoint.
- Stop on blocking, schema drift, integrity failure, unexpected output depth,
  or ambiguous recovery state.
- Stop after acquisition; qualification and external delivery remain separate
  phases unless the authorization explicitly includes them.

Status: **pending**.

### Phase 10 — Reconcile and qualify the pilot

**Goal:** create defensible Jump lead partitions from immutable evidence.

Actions:

- Reconcile the campaign internally.
- Apply lifetime suppression.
- Acquire only separately approved missing detail or website evidence.
- Freeze any judgment queue before decisions.
- Apply the target-blind contract to every candidate.
- Produce accepted classes, holds, exclusions, and unresolved outputs.
- Reconcile every input identity exactly once.
- Replay and independently verify the terminal result.

Status: **pending**.

### Phase 11 — Package and hand off

**Goal:** create a verified calling package without silently mutating an
external system.

Actions:

- Preserve canonical research outputs unchanged.
- Transform only checksum-bound snapshots.
- Map fields to the chosen dialer/CRM schema.
- Use only published business contact information unless another data class is
  explicitly approved.
- Protect CSV fields and parse exports back.
- Prove unique identities/phones and zero cross-class overlap.
- Produce field mapping, counts, checksums, and an import handoff.
- Treat actual import, calling, and outreach as separate external actions.

Status: **pending**.

### Phase 12 — Close the pilot and prepare repeatability

**Goal:** turn the pilot into a reusable operating baseline without inventing
success from volume alone.

Actions:

- Record observed raw, unique, qualified, held, and excluded yield.
- Promote every confirmed discovered business into the Jump lifetime registry,
  not only callable leads.
- Record source and decision limitations.
- Record calling outcomes later only as a separate CRM overlay keyed by stable
  registry ID.
- Decide whether the next action is more geography, another niche, rule
  refinement, or no further acquisition.
- Consider promoting the project from scratchpad status to a permanent Jump
  workspace only after Kenzo explicitly chooses that lifecycle.

Status: **pending**.

## Generic engine acceptance gates

Before a real Jump acquisition plan is considered executable, all applicable
gates must pass:

1. Jump Git worktree is clean and intentional.
2. Frozen original engine is unchanged.
3. No original lead data or Texas operational state exists in Jump.
4. No active Texas, plumbing, RMP, SINNTHETIC, Fable, or old-run hard-coding.
5. Workspace paths are portable and root-discovered.
6. Operational data, secrets, browser state, and outputs are ignored.
7. Plan schema and authorization receipt are machine-validated.
8. Preflight makes zero prospect/source requests.
9. Initialization makes zero prospect/source requests.
10. Live execution requires the exact authorized run identity and plan hashes.
11. Atomic checkpoint state survives forced interruption.
12. Completed requests cannot repeat on resume.
13. No-overwrite and checksum guards fail closed.
14. Blocking/schema/integrity anomalies stop the run.
15. Raw evidence and source provenance are immutable.
16. Stable identifiers precede weak identity evidence.
17. Weak transitive conflicts route to review.
18. All output partitions are disjoint and balance to the full input.
19. Desired counts cannot alter classification.
20. Offline simulation passes with zero network.
21. Primary and independent verification agree.
22. Routine boot context remains compact and contains one unambiguous next
    action.
23. Kenzo explicitly approves the exact campaign before the first request.

## Documentation discipline

- `CURRENT_STATE.md` is the only live state stamp inside the engine.
- Decisions with reasons go into the append-only decision log.
- Runs and their later completions are appended rather than rewritten.
- Historical receipts describe what was true at their time; later corrections
  supersede them explicitly.
- Do not paste the same long status into multiple boot files.
- Do not put raw lead rows, personal information, credentials, or large output
  artifacts in tracked documentation.
- Prefer concise machine-readable contracts plus focused human explanations.

## Live-status disclaimer

This is a historical build plan and never names current authorization or a
legal next action. Run `lead-sourcing-engine/scraperctl rehydrate` and use the
validated engine workflow and generated current-state file. Do not infer live
authority from any completed or pending phase recorded above.
