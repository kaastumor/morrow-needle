# Morrow // Needle — Backlog

This is the canonical execution order for autonomous work.

The backlog is a **risk register**, not a feature wishlist. Early work is ranked by how badly a wrong assumption could poison later architecture.

## Autonomous Next Pick

Unless new official evidence creates a more severe blocker, the hourly build loop should start here:

1. **P1-A / Issue #11 — Change Atom v0.3 + Adversary.** Repair the stale semantic contract so it references frozen temporal/procedural/mutation truth instead of collapsing it.
2. Use the VERIFIED Regulation 794/2004 Article 3 replacement as the first end-to-end semantic adversary.
3. Require exact authentic source-span support for high-risk legal semantics and add at least one plausible-but-unsupported negative case.
4. Feed every durable semantic invariant into the Gold Corpus.
5. After P1-A has a stable semantic contract, reassess P1-C provenance ledger vs P1-B source update detection as the next system risk.

All P0 foundation contracts are now resolved. Do not reopen P0 interfaces for convenience; require a new official adversarial case that demonstrates representational failure.

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

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

The v0.2 schema, semantic validator, PRESENT/ABSENT matcher and CI workflow are frozen. The corpus itself remains an ongoing asset and must continue growing across P1/P2.

Current verified cases include official provision-lineage reconstruction and the fully live VERIFIED Regulation 794/2004 Article 3 textual mutation.

See `docs/decisions/gold-corpus-v0.2-interface-freeze.md`.

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

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Frozen language-expression mutation contract:
- `schemas/language-scoped-mutation-v0.1.schema.json`
- `src/needle/multilingual/mutations.py`

Established:
1. mutation histories are expression-scoped;
2. non-listed corrigendum languages mean `NO_ASSERTION`, never a global negative;
3. different language groups may receive materially different correction sets;
4. corrigenda may correct prior corrigenda and the chain remains explicit;
5. source-publication time and corrected text-state time are different dimensions;
6. current consolidations may back-project later corrigenda into earlier labelled text states;
7. language-scoped corrections may alter operative monetary rules, so scope must survive into downstream Change Atoms.

See `docs/decisions/multilingual-corrigenda-v0.1-interface-freeze.md`.

### P0-G — Identifier/equivalence resolution
**Issue #7**

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Frozen typed identity contract:
- `schemas/identifier-graph-v0.1.schema.json`
- `schemas/identifier-resolution-query-v0.1.schema.json`
- `src/needle/identity/resolver.py`

Established:
1. there is no generic `same_document` equivalence;
2. CELEX, ELI and Cellar may identify the same Work/legal resource while Expressions, Manifestations and Items remain distinct;
3. consolidated states are related to but not equivalent to the authentic base act;
4. corrigenda are their own legal resources;
5. proposal, procedure and adopted act are distinct identities;
6. OJ citations and ELI subdivisions are typed relations, not aliases;
7. authoritative historical quirks such as the 1958 ELI `1(1)` must be resolved rather than normalized away;
8. unknown identifiers produce abstention rather than synthesis.

See `docs/decisions/identifier-graph-v0.1-interface-freeze.md`.

### P0-H — Legal/procedural state machine
**Issue #8**

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Frozen model:
- `schemas/procedure-state-event-v0.1.schema.json`
- `src/needle/procedure/resolver.py`

Procedure state is an orthogonal vector, not one status. Proposal state, institutional positions, political agreement, formal adoption, publication and delegated scrutiny remain separate. Withdrawn proposals terminate without an adopted act. Legal force/application remain in P0-E's temporal model.

See `docs/decisions/procedure-state-v0.1-interface-freeze.md`.

### P0-I — Source-assisted deterministic mutation engine
**Issue #9**

Status: **FOUNDATION CONTRACT RESOLVED; ISSUE CLOSED.**

Frozen canonical interface:
- `schemas/mutation-candidate-v0.2.schema.json`
- `src/needle/mutation/diff.py`
- `src/needle/mutation/reconcile.py`
- `src/needle/mutation/structural.py`
- `src/needle/mutation/instructions.py`

Validated:
- INSERT / DELETE / REPLACE;
- MOVE / RENUMBER / SPLIT / MERGE through evidence-backed structural lineage;
- annex/table cell changes;
- numeric/date/reference deltas;
- conflict quarantine;
- representation-noise suppression;
- exact authentic source-span verification;
- fully live Article 3 verification using real Cellar before/after checkpoints plus Regulation 271/2008.

Semantic legal effect remains downstream.

See `docs/decisions/mutation-engine-v0.2-interface-freeze.md`.

## P1 — Core system

### P1-A — Change Atom extraction + Adversary
**Issue #11**

Status: **ACTIVE CORE CAPABILITY.**

First task: replace stale Change Atom v0.2 with v0.3. The semantic layer must reference frozen mutation, temporal and procedure truth rather than recreate a collapsed lifecycle.

First adversary: VERIFIED Regulation 794/2004 Article 3 replacement.

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
