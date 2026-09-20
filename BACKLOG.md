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

Status: ACTIVE.

Already established:
- persistent provision identity is rejected;
- use immutable Provision Instances + evidence-backed Lineage Edges;
- distinguish STRUCTURAL_LINEAGE from RULE_LINEAGE.

Remaining attacks:
- move without recodification;
- recast with substantive change;
- no-correlation-table fallback;
- proposition-level continuity;
- lineage confidence/evidence model.

### P0-B — Cellar as ingestion backbone
**Issue #2 — Probe Cellar structured text and identifier resolution**

Goal: prove CELEX → official structured source → language expression → manifestation → normalized provision tree without fragile page scraping.

### P0-C — Gold Corpus / regression contract
**Issue #3 — Formalize Gold Corpus case format**

Goal: every foundational claim becomes a machine-testable regression case.

### P0-D — Canonical document/provision AST
**Issue #4**

Define the normalized internal representation of legal texts before parsers proliferate.

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

### P0-I — Deterministic mutation engine
**Issue #9**

Specify and prototype structural matching and textual diffing after identity/AST/time assumptions stabilize.

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
