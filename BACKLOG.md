# Morrow // Needle — Backlog

This is the canonical execution order for autonomous work.

The backlog is a **risk register**, not a feature wishlist. Early work is ranked by how badly a wrong assumption could poison later architecture.

## Autonomous Next Pick

Issues #49 and #59 have now falsified the assumption that the current Needle
architecture should automatically become a general public legal-change product.

> **STOP PUBLIC-PRODUCT EXPANSION. CONTINUE RESEARCH/AUDIT MODE.**

This is not project abandonment. The evidence engine has repeatedly found real
source, timing, identity, dependency and provenance traps. What stops is the
obligation to turn every useful legal-information distinction into a feature or
marketing claim.

Research/audit mode rules:

1. start from a concrete legal-information question capable of being wrong;
2. prefer official-source evidence and the smallest existing contract that can
   answer it;
3. produce a fixture, finding, regression, or bounded negative result;
4. do not add schema, infrastructure or product surface unless the question
   proves the existing baseline cannot represent the finding;
5. a well-supported “nothing new / baseline already handles this” result is
   successful work.

**No preselected research task is currently eligible. The hourly worker should
idle rather than manufacture work.**

The first explicit research/audit runway is complete:

- **#61:** independently confirmed consolidation back-projection: a current
  consolidation labelled 13 August 2025 can contain wording sourced from a
  corrigendum published in July 2026;
- **#64:** confirmed expression-scoped corrigendum semantics with a useful
  asymmetry: English required the 2026 correction while independent authentic
  Dutch 2025 text already contained the “bestaande steunregeling” concept;
- **#67:** proved EUR-Lex `C#` correction markers are expression-local
  presentation ordinals, not cross-language corrigendum identities;
- **#69:** narrowed the Article 3 system-identity gap: current Commission
  documentation supports SANI/SANI2 as the notification application, while
  SANI technical continuity and post-2025 PKI correspondence identity remain
  unresolved.

These results reinforce research/audit mode without reopening a frozen
contract or creating new architecture.

The next task should be selected only when a concrete falsifiable legal-
information question is identified from fresh source evidence, an operational
monitor anomaly, an unresolved canonical claim, or an explicit sponsor research
question. Until then, **no AUTO READY issue is intentional**.


Operational Needle remains an evidence generator, regression surface and source
monitor. Thread, X-Ray, Source Anomaly, Half-Life and public cards remain useful
audit projections; none implies an active product roadmap.

Public-product work may reopen only from external/user evidence of a recurring
concrete problem that the strong baseline cannot reliably solve. Architecture
itself is not such evidence.

Thread comparative audit:
`docs/audits/thread-comparative-value-2026-09-23.md`  
Research-mode health decision:
`docs/audits/project-health-2026-09-23-post-thread.md`  
Canonical charter: `docs/project-charter.md`  
Active assumptions: `docs/assumptions.md`  
Autonomous worker contract: `docs/automation/hourly-worker.md`

## Priority model

- **P0 — Foundation blocker:** resolve before significant product/application build.
- **P1 — Core capability:** required for a credible first system once P0 is stable.
- **P2 — Research / audit intelligence:** derived analyses used to falsify, inspect, and reconstruct legal-change claims.
- **P3 — Expansion:** parked unless a concrete research need or externally evidenced user problem earns it.

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

## P2 — Research / audit intelligence

Current mode after Issues #49 and #59:

1. **Issue #61 — consolidation back-projection audit.** First bounded
   research-mode task. Test a current official-source trap and leave a fixture
   and regression; no product feature.
2. Future work enters the queue only through a concrete audit/research question
   with authoritative evidence and a falsifiable outcome.
3. Public-product expansion is stopped. It may reopen only from external/user
   evidence, not from unused architectural capability.

Completed value gates:

- **Thread comparative gate / Issue #59: COMPLETE — STOP PUBLIC-PRODUCT
  EXPANSION.** The Article 3 Thread is materially better as an audit package
  than raw browsing, especially for negative checks and provenance closure, but
  a careful official-source + capable-LLM baseline can reconstruct the same
  legal history. One polished Thread does not establish recurring public-product
  advantage.
- **Comparative value proof / Issue #49: COMPLETE — REDIRECT.** Four real
  comparisons produced no repeated clear product advantage.
- **Pre-analysis adversarial audit / Issue #29: COMPLETE — SIMPLIFY.** The
  foundation survived after multiple real enforcement repairs and broad novelty
  claims were rejected.

Retained audit tools:

- **Evidence / Why this is shown** — disposable read-side provenance projection.
- **Operational Needle** — source monitor and adversarial evidence generator.
- **Thread** — evidence-linked historical reconstruction when a research
  question justifies the cost.
- **Legislative X-Ray** — dependency-ripple detector.
- **Source Anomaly** — source/audit diagnostics.
- **Half-Life v0.1** — bounded temporal/genealogical demonstration.

Strategic constraints:

- Do not manufacture product demand from architecture.
- Do not count formalisation alone as user value.
- Do not add another analytic primitive to rescue a failed product thesis.
- Do not create infrastructure for hypothetical scale.
- Keep negative findings, source anomalies, non-impact and abstention as valid
  research outputs.
- Keep the charter, assumptions, latest Project Health record and this backlog
  aligned with evidence.

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
