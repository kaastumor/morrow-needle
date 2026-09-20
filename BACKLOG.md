# Morrow // Needle — Backlog

This is the canonical execution order for autonomous work.

The backlog is a **risk register**, not a feature wishlist. Early work is ranked by how badly a wrong assumption could poison later architecture.

## Autonomous Next Pick

Unless new official evidence creates a more severe blocker, the hourly build loop should start here:

1. **P0-F / Issue #6 — multilingual corrigenda.** Prove that language expressions require separate text-state/mutation histories using official language-scoped corrigenda.
2. Then **P0-G / Issue #7 — identifier/equivalence resolution**.
3. Then P0-H → P0-I.
4. Keep P0-C cross-cutting: feed each resolved P0 adversary into the Gold Corpus without letting corpus-format work displace the active foundation blocker.

Do **not** return to P0-B unless a new official source fixture falsifies the validated ingestion contract. Issue #2 is closed; residual Cellar work is adapter/regression hardening.

P0-C / Gold Corpus is cross-cutting infrastructure: keep feeding each P0 fixture into it, but do not let standalone corpus-format polishing displace an unresolved foundation assumption.

## Priority model

- **P0 — Foundation blocker:** resolve before significant product/application build.
- **P1 — Core capability:** required for a credible first system once P0 is stable.
- **P2 — Product intelligence:** improves usefulness, comprehension, and discovery.
- **P3 — Expansion:** valuable after the legal-change core is trustworthy.

Within a priority band, prefer the task that:
1. can falsify the largest architectural assumption;
2. affects the greatest number of downstream components;
3. can be tested against authoritative evidence;
4. produces a reusable fixture, schema, test, or code path.

## Foundation Queue

### P0-A — Provision and rule identity
**Issue #1 — Stress-test provision identity across renumbering, split/merge and replacement**

Status: **FOUNDATION CONTRACT RESOLVED; keep fixtures as regression corpus.**

Established:
- persistent provision identity is rejected;
- use immutable Provision Instances + evidence-backed Lineage Edges;
- distinguish STRUCTURAL_LINEAGE from proposition-granular RULE_LINEAGE;
- structural lineage and substantive change can coexist;
- same-act physical moves still create distinct instances across text states;
- authentic official recitals can provide DIRECT structural-lineage evidence when they explicitly identify a move, even without a correlation table;
- lineage confidence/conflict is explicit and non-numeric;
- deterministic text/structure alignment is a **candidate generator, not sufficient evidence for an asserted lineage edge**;
- act-level succession, same article number, same heading and strong textual similarity do not establish one-to-one provision ancestry;
- grouped transitional substitution must not be laundered into one-to-one provision mappings;
- deterministic-only/authentic-comparison-only/model-only fallback claims remain `CANDIDATE + UNRESOLVED + INSUFFICIENT_EVIDENCE` until promoted by stronger evidence/review.

Conceptual ancestry remains deliberately interpretive and must not be promoted from textual/structural similarity alone.

### P0-B — Cellar as ingestion backbone
**Issue #2 — Probe Cellar structured text and identifier resolution**

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Validated path: CELEX → Cellar SPARQL inventory → language expression → deterministic manifestation selection → official byte delivery → immutable Source Observation.

Key constraints: availability is expression-scoped; manifestations may be multi-stream; WEMI Item count is not internal stream count; raw artifact changes are not legal mutations.

Modern multi-asset FMX4 and early historical HTML now normalize through the frozen AST interface. Remaining source-adapter work (including deeper manifestation assembly/completeness audits) is regression/adapter hardening rather than a blocker on the canonical model.

### P0-C — Gold Corpus / regression contract
**Issue #3 — Formalize Gold Corpus case format**

Status: **CROSS-CUTTING; DO NOT PICK AHEAD OF ACTIVE P0-E/F/G/H RISK.**

Goal: every foundational claim becomes a machine-testable regression case. Keep open until real reconstruction outputs, not only fixture syntax, are matched against expectations in CI. Temporal adversaries are now executable fixtures and should later be folded into the common Gold Corpus case contract rather than redesigned separately.

### P0-D — Canonical document/provision AST
**Issue #4**

Status: **FOUNDATION CONTRACT RESOLVED — AST v0.1 INTERFACE FROZEN.**

The flat-with-links contract (structural nodes + ordered segments + references + annotations + explicit parse/completeness state) passed live modern Formex, 1958 HTML, and large consolidated Formex adversaries.

Fail-closed invariants now enforce zero unexplained source text, zero duplicate ownership and zero unknown structural kinds before `FULL_STRUCTURAL`. The consolidated fixture also exercises annexes, 197 tables, 739 footnotes, ELI references and 48 embedded mutation annotations.

Important separation retained: `FULL_STRUCTURAL` does not imply complete representation coverage; raster/opaque evidence can keep completeness unknown.

Adapters continue to evolve, but the v0.1 core schema should change only when a new official fixture demonstrates a representational impossibility. See `docs/decisions/ast-v0.1-interface-freeze.md`.

### P0-E — Temporal semantics
**Issue #5**

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Frozen interfaces:
- `schemas/temporal-assertion-v0.1.schema.json`
- `schemas/temporal-query-v0.1.schema.json`
- `src/needle/temporal/resolver.py`

Established:
1. publication, force, application, text-state, transition, derogation and deadlines are separate dimensions;
2. explicit provision/regime overrides may differ from act-wide defaults;
3. applicability may depend on entity-specific events and require `CONTEXT_REQUIRED`;
4. text-state change may precede application;
5. genealogical continuity may cross a real applicability gap;
6. retroactive application may predate entry into force;
7. historical queries must distinguish `EX_POST_LEGAL_EFFECT` from `OFFICIAL_SOURCE_STATE_AS_OF`;
8. new and legacy regimes may overlap during transition and end on different dates.

See `docs/decisions/temporal-v0.1-interface-freeze.md`.

### P0-F — Corrigenda + multilingual state
**Issue #6**

Status: **ACTIVE FOUNDATION BLOCKER.**

First adversary: Regulation 794/2004 corrigenda of 28 January 2005. Official Journal metadata splits the corrections across different language groups, and the correction sets themselves differ. A language-neutral mutation history would therefore create false text states.

Next: model language-expression mutation scope, build cross-language fixtures, and prove that an unaffected expression is not silently mutated.

### P0-G — Identifier/equivalence resolution
**Issue #7**

Formalize CELEX ↔ ELI ↔ Cellar ↔ OJ ↔ procedure/interinstitutional identifiers and never synthesize identifiers when authoritative mapping exists.

### P0-H — Legal/procedural state machine
**Issue #8**

Validate the distinction between proposal/draft/position/agreement/adoption/publication/force/application/repeal against real procedures.

### P0-I — Source-assisted deterministic mutation engine
**Issue #9**

Architecture revised after live consolidated Formex testing.

Reconcile five evidence channels: authentic modifying/correcting acts, embedded official consolidation provenance, official relationship metadata, consolidated checkpoints, and deterministic canonical-AST diff.

A parser/schema/test fixture now exists for Formex CLG.MDF* provenance, including nested corrigenda. Full mutation engine implementation remains downstream of the now-frozen AST and still-active temporal contract. P0-I becomes the next major implementation target only after P0-E/F/G/H foundation decisions are stable enough.

## P1 — Core system

### P1-A — Change Atom extraction + Adversary
Turn verified textual mutations into legal-semantic changes while preserving evidence state and uncertainty.

### P1-B — Source update detection
Detect new/changed official source objects without repeatedly crawling everything.

### P1-C — Provenance ledger
Immutable source hashes, observation times, transformation versions, and claim-support edges.

### P1-D — Search/retrieval
Structured-first retrieval over acts, provisions, atoms, entities, dates and lineage; embeddings remain secondary discovery.

### P1-E — First end-to-end Thread
One historically messy act/domain reconstructed from original source to public explanation.

## P2 — Public intelligence

- Needle daily/weekly change feed.
- Legislative X-Ray.
- impact/affected-entity model with strict direct-vs-inferred separation.
- public ranking dimensions and transparent ranking rationale.
- plain-language explanation evaluation.
- domain subscriptions and saved monitors.
- Dark Matter: known-but-unavailable document representation.
- **Half-Life (Issue #10):** factual history of temporary regimes — original planned duration, extensions, gaps, re-enactments, final expiry or transition into successor/permanent rules.

## P3 — Expansion

- national transposition of directives;
- CURIA interpretation layer;
- agency/regulator guidance;
- national ELI/N-Lex integration;
- cross-jurisdiction comparison;
- academic/journalist bulk API.

---

# Discovery Lane

Morrow is explicitly allowed to pursue high-upside questions that are not next in the strict queue.

A Discovery task is justified when it is:
- unusually informative;
- capable of invalidating a foundation assumption;
- likely to reveal a novel public-interest capability;
- or exposes a historical/legal pattern that Needle could uniquely make visible.

A discovery run must leave behind at least one of:
- official evidence;
- a fixture;
- a documented hypothesis;
- a schema/architecture change;
- a new backlog issue;
- or a clear negative result.

Interesting-but-unproductive wandering should stop.

A useful default is roughly **one discovery-oriented cycle for every three foundation cycles**, unless a discovery finding becomes a P0 blocker.

Examples worth pursuing:
- temporary exceptions that quietly became permanent;
- rule ancestry surviving across repeal/recast;
- numerical thresholds unchanged for decades despite inflation;
- language-specific corrections with materially different history;
- provisions whose descendants proliferate into delegated/implementing acts;
- regulatory concepts that migrate between legal instruments.

---

# Autonomy rule

Morrow may reorder tasks when new evidence changes risk.

When it does, the reason must be recorded here or in the relevant issue. The backlog must reflect actual project priorities rather than preserving stale plans.
