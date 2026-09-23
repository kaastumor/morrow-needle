# Morrow // Needle — Backlog

This is the canonical execution order for autonomous work.

The backlog is a **risk register**, not a feature wishlist. Early work is ranked by how badly a wrong assumption could poison later architecture.

## Autonomous Next Pick

Issue #49 compared Needle against the strong simpler baseline on four real
cases. The result did **not** satisfy the charter's requirement for repeated
material public-product advantage.

> **REDIRECT. Keep the evidence engine, stop presuming the operational feed is
> the product, and test the remaining Thread / legal-change-audit proposition
> before building anything else.**

Comparative evidence:

- Regulation (EU) 2026/2104 initially exposed a Needle completeness LOSS:
  EUR-Lex surfaced entry into force that Needle omitted. The gap was repaired
  using explicit Cellar metadata and the existing temporal model, yielding
  parity/semantic clarity rather than a product win.
- the English-only ECU 225 → 255 corrigendum was PARITY for a careful
  official-source + capable-LLM reader; Needle mainly adds machine-safe
  `NO_ASSERTION` discipline;
- the REACH Article 67 / Annex XVII case produced a PLAUSIBLE ADVANTAGE in
  automatic discovery of an indirect dependency effect without manufacturing a
  local textual mutation;
- the DSA context-dependent application case was PARITY on user understanding,
  though Needle's `CONTEXT_REQUIRED` representation remains valuable machine
  safety.

Unless new official/executable evidence reopens a foundation risk:

1. **Issue #59 — Thread / legal-change audit comparative value gate. ACTIVE NEXT
   HORIZON.** Test the existing Article 3 Thread against EUR-Lex, emendrix,
   direct official sources, ordinary search and a capable LLM. Do not add Thread
   architecture.
2. **Gate after #59:** CONTINUE the audit/Thread direction, SIMPLIFY further, or
   STOP public-product expansion. A negative result is a successful gate.
3. **Parked:** general public change-feed expansion, affected-entity modelling,
   ranking, subscriptions, Half-Life v0.2, new analytics, scale infrastructure
   and wider jurisdictions.

Operational Needle remains an evidence generator, regression surface and source
monitor. It is no longer presumed to be the public product.

All P0/P1 ownership boundaries remain explicitly tested. A freeze is reopened
only when official or executable adversarial evidence demonstrates failure.

Comparative audit: `docs/audits/comparative-value-2026-09-23.md`  
Post-#49 health decision: `docs/audits/project-health-2026-09-23-post-value.md`  
Canonical charter: `docs/project-charter.md`  
Active assumptions: `docs/assumptions.md`  
Autonomous worker contract: `docs/automation/hourly-worker.md`

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
8. new and legacy regimes may overlap during transition and end on different dates;
9. inclusive/exclusive boundaries are executable semantics, not documentation: an integration adversary exposed and fixed a resolver bug where `inclusive: false` was previously ignored.

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

Status: **CORE INTERFACE RESOLVED; ISSUE CLOSED.**

Change Atom v0.3 is frozen. VERIFIED semantic claims reference VERIFIED textual mutations, temporal/procedure truth, explicit language scope and exact immutable authentic source spans. The first Article 3 graph decomposes one replacement into DUTY, exceptional PERMISSION and LEGAL_STATUS atoms, with a permanent negative regression against false SANI globalization.

See `docs/decisions/change-atom-v0.3-interface-freeze.md`.

### P1-B — Source update detection
**Issue #13**

Status: **CORE INTERFACE RESOLVED; ISSUE CLOSED.**

Cellar update detection v0.1 is frozen: live RSS/Atom feed normalization, cross-format event identity, overlap-safe polling, fail-closed pagination, WEMI-targeted refresh planning and auditable Source Change classification.

See `docs/decisions/cellar-update-detection-v0.1-interface-freeze.md`.

### P1-C — Provenance ledger
**Issue #12**

Status: **CORE INTERFACE RESOLVED; ISSUE CLOSED.**

Append-only provenance ledger v0.1 is frozen: immutable Source Observations, derivation runs, claim-support edges and correction/supersession/retraction records with deterministic hashes and a derived current view.

See `docs/decisions/provenance-ledger-v0.1-interface-freeze.md`.

### P1-D — Search/retrieval
**Issue #15**

Status: **CORE INTERFACE RESOLVED; ISSUE CLOSED.**

Structured retrieval v0.1 is frozen as a deterministic, rebuildable projection over canonical Needle objects. It supports typed exact/entity/identifier filtering, explainable lexical discovery, explicit bitemporal perspective, provenance-current Source Mode, searchable unknown/non-impact records and fail-closed temporal abstention.

Integration discoveries retained as regressions:
- exact legal retrieval must remain distinct from broad lexical discovery;
- date-aware retrieval may not synthesize validity from event order, mutation dates or lineage;
- retrieval pressure exposed missing canonical PKI/SANI lifecycle boundaries, which were repaired in P0-E data rather than patched in search;
- official-source-as-of queries require evidence-backed publication time;
- duplicate identical Formex metadata across streams is representation duplication, not evidence conflict;
- superseded provenance support must disappear from the active retrieval projection even when support cardinality is unchanged;
- typed CELEX/ELI/Cellar equivalence must not absorb Expressions, Manifestations, consolidated states or corrigenda.

See `docs/decisions/retrieval-v0.1-interface-freeze.md`.

### P1-E — First end-to-end Thread
**Issue #14**

Status: **CORE INTERFACE RESOLVED; ISSUE CLOSED.**

Thread v0.1 is frozen as a reference-only chronological composition over canonical domain entities. The Article 3 Thread reconstructs 2004 → 2008 → 2025/2026, has zero Source Mode gaps, canonical Gold chronology/negative regressions, and generated evidence-linked 3-second / 30-second / 3-minute public views.

Important integration discoveries retained as regressions:
- baseline state must not be manufactured as a mutation;
- exclusive temporal boundaries must be executed correctly;
- unchanged paragraph text can have a derived cross-reference ripple without a textual mutation;
- related corrigenda can be retained as reviewed non-impact evidence;
- live endpoint availability is separate from pinned legal truth;
- Thread persistence must not duplicate semantic/temporal truth.

See `docs/decisions/thread-v0.1-interface-freeze.md`.

### P1-F — Post-P1 foundation audit
**Issue #16**

Status: **COMPLETED; ALL P0/P1 FREEZES RETAINED; P2 UNBLOCKED.**

The composed red-team found one real enforcement defect and several useful negative/source-anomaly cases without requiring a canonical interface redesign.

Key durable findings:
- VERIFIED Change Atoms now require source-span evidence for every claimed language;
- preferred source-route failure is not legal/source absence;
- authentic source text may conflict internally and must be preserved literally while canonical identity is resolved separately;
- structural lineage does not inherit temporal application;
- a transposition deadline is not an application start;
- genealogical succession may cross a real applicability gap;
- the Gold Corpus now includes a non-Article-3 multilingual semantic adversary.

See docs/audits/post-p1-foundation-audit-v0.1.md.

## P2 — Public intelligence / audit value

Current horizon after Issue #49:

1. **Thread / legal-change audit comparative gate / Issue #59.** Test the
   already-frozen Article 3 Thread against the strong simpler baseline. No new
   schema or feature work is authorized.
2. **Project Health gate.** If Thread does not produce recurring material
   improvement, stop public-product expansion and retain Needle as a
   research/audit engine plus regression corpus.
3. Only a positive gate may authorize a new product experiment.

Completed P2/value slices:

- **Comparative value proof / Issue #49: COMPLETE, direction REDIRECT.** Four
  real comparisons produced no repeated clear product advantage: one initial
  loss repaired to parity/semantic clarity, two parity cases, and one plausible
  advantage in proactive dependency discovery. Evidence presentation survived;
  the broad general-interest change-feed thesis did not.
- **Evidence / Why this is shown:** implemented as a disposable read-side
  projection over existing provenance and canonical temporal references. The
  real 2026/2104 view closes without a new truth store.
- **Pre-analysis adversarial audit / Issue #29: COMPLETE, direction SIMPLIFY.**
  The audit found and repaired source-availability, baseline contamination,
  DELETE semantics, authentic-context/locality, evidence cross-binding,
  operational promotion and CI-semantics defects. Broad novelty claims were
  rejected.
- **Product checkpoint v0.1 / Issue #27: COMPLETE.** Three real operational
  classes established evidence presentation as a comprehension gap, while raw
  audit/abstention output was rejected as default general-interest news.
- **Operational Needle v0.1 / Issue #21: CLOSED.** Retained as evidence/source
  infrastructure rather than presumed product destination.
- **Legislative X-Ray v0.1 / Issue #20: CLOSED/FROZEN.** Retained primarily as
  dependency-audit capability; its REACH case is the strongest #49 comparative
  result but not sufficient to rescue a broad feed thesis.
- **Half-Life v0.1 / Issue #10: CLOSED/FROZEN.** Retained as a valid
  demonstration; v0.2 remains parked.
- **Source Anomaly v0.1 / Issue #17: CLOSED/FROZEN.** Retained as trust/audit
  diagnostics.

Strategic constraints:

- Do not use machine formalisation itself as evidence of product value.
- Do not add another analytic primitive to rescue a failed comparative gate.
- Do not create infrastructure for hypothetical scale.
- Do not promote source/audit activity into legal news.
- Do not assume Thread wins because it is richer; #59 must falsify it.
- Keep `docs/project-charter.md`, `docs/assumptions.md`, the latest Project
  Health decision and this backlog aligned with #59 evidence.

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
