# Morrow // Needle — Backlog

This is the canonical execution order for autonomous work.

The backlog is a **risk register**, not a feature wishlist. Early work is ranked by how badly a wrong assumption could poison later architecture.

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

Status: **SOURCE CONTRACT VALIDATED; AST INTEGRATION PENDING #4.**

Validated path: CELEX → Cellar SPARQL inventory → language expression → deterministic manifestation selection → official byte delivery → immutable Source Observation.

Key constraints: availability is expression-scoped; manifestations may be multi-stream; WEMI Item count is not internal stream count; raw artifact changes are not legal mutations.

Remaining P0-B work is downstream of the canonical AST: normalize one modern FMX4 multi-stream act and one early HTML act.

### P0-C — Gold Corpus / regression contract
**Issue #3 — Formalize Gold Corpus case format**

Goal: every foundational claim becomes a machine-testable regression case.

### P0-D — Canonical document/provision AST
**Issue #4**

Status: **DRAFT CONTRACT COMMITTED; LIVE FIXTURES/PARSERS IN PROGRESS.**

Adopted flat-with-links model: structural nodes + ordered text segments + references + source annotations, all source-anchored. Live consolidated FMX4 validated the need for first-class nested mutation provenance annotations.

Next: normalize modern FMX4, 1958 HTML, and consolidated FMX4 into the same AST before freezing v0.1.

### P0-E — Temporal semantics
**Issue #5**

Stress-test entry into force, application, expiry, delayed provisions, transition periods, partial applicability, retroactivity, time-scoped derogations, and **gapped regime continuity**.

Discovery finding now adopted into the foundation: genealogical continuity and applicability continuity are separate dimensions. A successor regime may descend directly from an expired predecessor while a real legal gap exists between them.

### P0-F — Corrigenda + multilingual state
**Issue #6**

Determine how language-specific corrigenda alter text states and whether a single language-neutral mutation graph is ever safe.

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

A parser/schema/test fixture now exists for Formex CLG.MDF* provenance, including nested corrigenda. Full mutation engine implementation remains downstream of the AST and temporal contracts.

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
