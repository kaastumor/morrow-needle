# Technical system and historical asset inventory

Status: **HISTORICAL + CURRENT REPOSITORY INVENTORY**

This document records what Needle actually built. Many of these components are not part of the
current default identity, but they remain real technical capital in `main`.

At the time of this review, current `main` still contains roughly:

- 54 JSON schema files;
- 81 test-file entries;
- 31 explicit interface/decision records;
- the `src/needle` package with analytics, AST, identity, mutation, operations, provenance,
  retrieval, semantic, temporal, Thread and update modules;
- the frozen Corpus Explorer;
- Reference Pack v0.1 and v0.2;
- the new Maintenance Delta v0.1 contract.

Counts are descriptive only, never project targets.

## 1. Official-source ingestion and observation

### Problem

Needle could not treat 'download the current EUR-Lex page' as a trustworthy historical substrate.
It needed explicit source identity, representation selection, language, bytes and observation time.

### Built

- Cellar SPARQL discovery: CELEX -> Work -> language Expression -> Manifestation -> Item.
- deterministic representation selection;
- immutable Source Observation contract;
- modern FMX4 and historical HTML ingestion paths;
- separation of legal text state from representation/rendering bytes;
- Cellar update-feed parser, overlap-safe cursor/deduplication, targeted re-observation and
  change classification.

### Important findings

- Cellar expression suffixes are work-local IDs, not language codes;
- a Manifestation can expose many internal streams;
- WEMI Item count is not internal stream count;
- publication bytes can be regenerated without legal mutation;
- representation availability is expression-scoped and historically uneven;
- feed UPDATE is a hint, not proof of legal change.

### Current repository

- `src/needle/updates/`
- `schemas/source-observation-v0.1.schema.json`
- `schemas/manifestation-selection-v0.1.schema.json`
- `schemas/cellar-ingestion-event-v0.1.schema.json`
- source/ingestion fixtures and decisions.

### Status

**HISTORICALLY VALID / PARKED AS PRODUCT INFRASTRUCTURE.**

The scheduled monitor was later frozen because the public-product loop was no longer justified
and Git-backed operational state generated unnecessary churn. The source contracts themselves were
not invalidated.

## 2. Canonical Legal AST and source-text accounting

### Problem

Source-specific XML/HTML quirks could not become the ontology. Needle needed one normalized legal
structure without silently dropping text or inventing hierarchy.

### Built

- Legal AST v0.1, flat-with-links;
- adapters for modern Formex/FMX4 and historical HTML;
- structural nodes, ordered text segments, references and source annotations;
- embedded consolidation modification annotations;
- exact source-text accounting.

### Strong technical gate

The foundation reached zero unexplained source-text characters and zero duplicate ownership on
key live cases, including:

- 1958 Regulation No 1 HTML;
- original Regulation 794/2004 FMX4;
- consolidated Regulation 794/2004 FMX4 with annexes, tables, footnotes and modification metadata.

The parser interface was frozen while adapters remained evolvable.

### Current repository

- `src/needle/ast/`
- `src/needle/formex/`
- `schemas/legal-ast-v0.1.schema.json`
- `schemas/consolidation-modification-annotation-v0.1.schema.json`.

### Status

**HISTORICALLY VALID / FOUNDATION TOOLKIT.**

Not part of the current small reference product, but not disproven.

## 3. Identity, identifiers and lineage

### Problem

Naive article-number identity fails under recast, split/merge, move and repeal/replacement.

### Built / learned

- immutable Provision Instances instead of persistent provision identity;
- evidence-backed Lineage Edges;
- `STRUCTURAL_LINEAGE` separated from proposition-granular `RULE_LINEAGE`;
- official correlation tables as DIRECT structural evidence;
- candidate versus asserted lineage;
- ordinal confidence/rationale/conflict state without fake model probability;
- Identifier Graph and explicit resolution/equivalence;
- Regime Lineage capable of genealogical continuity across a real legal applicability gap.

### Key invariant

> Structural correspondence never automatically proves semantic rule continuity.

### Current repository

- `src/needle/identity/`
- `schemas/provision-lineage-v0.1` through `v0.5`;
- `schemas/identifier-graph-v0.1.schema.json`;
- `schemas/regime-lineage-v0.1/v0.2.schema.json`.

### Status

**HISTORICALLY VALID / CASE-EARNED.**

These models mattered in difficult historical reconstruction but did not prove a general product advantage.

## 4. Temporal and procedural state

### Problem

EU legal time is not one date.

### Built

- Temporal Assertion v0.1 and later v0.2;
- explicit perspectives such as historical source state versus ex-post legal effect;
- application separate from entry into force;
- context-dependent application (for example entity/designation-triggered timing);
- sub-day precision when real law required it;
- regime gaps and reenactment;
- Procedure State Events;
- retrieval that refuses to synthesize end dates from later events.

### Key discoveries

- genealogy may continue across an actual legal void;
- an act may be in force before a provision applies;
- applicability can depend on entity/event context;
- later consolidation can contain a correction published after the consolidation's nominal date;
- day-granular modeling can be insufficient.

### Current repository

- `src/needle/temporal/`
- `src/needle/procedure/`
- `schemas/temporal-*`
- `schemas/procedure-state-event-v0.1.schema.json`.

### Status

**LOAD-BEARING HISTORICAL SCIENTIFIC CAPITAL.**

Even the current Maintenance Delta core inherits its governing-time discipline from this work.

## 5. Deterministic mutation and semantic Change Atoms

### Problem

A textual diff is not automatically a legal-semantic claim.

### Built

- deterministic structural diff / mutation engine;
- authentic amendment-instruction parsing and reconciliation;
- mutation candidates with fail-closed promotion;
- language-scoped mutation;
- Change Atom v0.3;
- semantic adversary that rejects unsupported atoms;
- exact source span and authentic-byte hashes for verified claims.

### Important design correction

Change Atom originally risked becoming a collapsed legal-status object. v0.3 deliberately reduced
it to a semantic claim about a verified textual mutation and references temporal/procedural truth
instead of copying it.

### Current repository

- `src/needle/mutation/`
- `src/needle/multilingual/`
- `src/needle/semantic/adversary.py`
- `schemas/change-atom-v0.2/v0.3.schema.json`
- mutation candidate schemas.

### Status

**HISTORICALLY VALID / PARKED AS DEFAULT PRODUCT PRIMITIVE.**

## 6. Append-only provenance ledger

### Problem

Needle required an audit path from a public claim back to immutable official bytes without rewriting history.

### Built

- Source Observation, Derivation Run, Claim Support, correction/supersession records;
- deterministic record hashing;
- backward-only references;
- tamper detection;
- correction without historical rewrite;
- current-view projection;
- source-origin distinction later expanded to preserve private-primary determinations separately
  from their public-law recognition.

### Current repository

- `src/needle/provenance/ledger.py`
- `schemas/provenance-record-v0.1/v0.2.schema.json`.

### Status

**CORE HISTORICAL CAPABILITY / STILL CONCEPTUALLY LOAD-BEARING.**

## 7. Specialized legal-state owners discovered by adversarial research

Needle repeatedly found legal state that could not honestly be represented as text mutation.
Rather than force everything into Change Atom, narrow owners were added only when real cases demanded them.

### Preserved owners

- **Authoritative Dynamic Set** — legal consequence depends on membership/status in an authoritative set.
- **Authoritative Metric Observation** + **Metric Rule Evaluation** — an official numeric observation feeds a binding formula/predicate.
- **Authoritative Finding** — direct categorical determinations such as official disease/inspection findings.
- **Legal Spatial State v0.1/v0.2** — horizontal and later vertical legal extent.
- **Judicial Holding v0.1** — judicial legal-state effects distinct from textual mutation.
- **Recognized External Determination** — private-origin determination that matters because public law recognizes it.

### Current repository

Corresponding schemas and decision records remain in `schemas/` and `docs/decisions/`.

### Status

**HISTORICAL SCIENTIFIC ASSETS.**

These are examples of the project's strongest modeling habit: singular canonical ownership and narrow admission after adversarial proof.

## 8. Thread

### Purpose

Thread was the flagship longitudinal projection: reconstruct how a rule became what it is today.

### First complete Thread

Regulation 794/2004 Article 3 combined:

- original state;
- provision-specific application;
- 2008 whole-Article replacement;
- later 2025 paragraph replacement;
- unchanged paragraph dependency ripple;
- corrigendum/non-impact evidence;
- semantic atoms;
- provenance;
- unresolved technical-system identity.

### Current repository

- `src/needle/thread/`
- `schemas/thread-v0.1.schema.json`.

### Status

**TECHNICALLY VALID, PRODUCT VALUE PARKED.**

#59 found Thread a useful audit object, but a careful official-source baseline recovered almost all positive legal facts.
Thread retained machine-safety, audit closure and derived-dependency advantages, not enough repeated public-product advantage.

## 9. Retrieval

### Purpose

Structured-first search over canonical Needle objects, always resolving back to source-backed owners.

### Design

- deterministic identity/filter retrieval;
- explicit temporal perspective;
- direct versus derived match reasons;
- unknown/non-impact records remain searchable;
- embeddings only secondary discovery, never legal truth.

### Current repository

- `src/needle/retrieval/`
- retrieval schemas and temporal-boundary docs.

### Status

**TECHNICALLY VALID / PARKED.**

## 10. Legislative X-Ray / Dependency Ripple

### Purpose

Expose legal effect that changes because an unchanged local provision depends on another state that changed.

### Canonical shape

- local text hash unchanged;
- upstream referenced rule/annex/definition changes;
- local meaning/effect may shift;
- result is DERIVED, never falsely labeled a local textual mutation.

### Current repository

- `src/needle/analytics/dependency_ripple.py`
- dependency-ripple schemas/fixtures.

### Status

**USEFUL ANALYTIC / PARKED AS PRODUCT PILLAR.**

This was one of the few recurring areas where Needle showed plausible proactive discovery advantage.

## 11. Half-Life

### Purpose

Show the real legal history of 'temporary' regimes:

- original duration;
- extensions;
- legal gaps;
- reenactment;
- eventual replacement/expiry/permanent transition where evidenced.

### Current repository

- `src/needle/analytics/half_life.py`
- Half-Life schemas.

### Status

**TECHNICALLY BUILT / PARKED.**

Later work explicitly refused to add terminal/rule-survival claims without stronger evidence.

## 12. Source Anomaly

### Purpose

Expose surprising official-source infrastructure facts without laundering them into legal truth:

- preferred-route unavailable but authoritative fallback exists;
- literal source identifier conflicts;
- duplicate representations;
- language/format availability gaps.

### Current repository

- `src/needle/analytics/source_anomaly.py`
- source-anomaly schemas.

### Status

**TECHNICALLY BUILT / PARKED.**

## 13. Evidence / Why this is shown

Source Mode evolved into a human-readable evidence resolver:

- official source;
- what it supports;
- DIRECT/DERIVED/unresolved status;
- what does **not** follow;
- timing known versus unknown.

### Current repository

- `src/needle/presentation/evidence.py` and related provenance/presentation work.

### Status

**PRESENTATION DISCIPLINE RETAINED; GENERAL PUBLIC PRODUCT VALUE NOT PROVEN.**

## 14. Operational update -> feed-card pipeline

### Built loop

Official Cellar update -> re-observe source -> classify source/representation change -> parse/normalize ->
diff/reconcile authentic cause -> verified mutation or abstention -> semantic/temporal/provenance -> retrieval ->
public projection/feed card.

The real 2026/2104 path was processed through this loop and rerun idempotently.

### Operational monitor

A scheduled Git-backed monitor later accumulated dozens of state-promotion commits and multi-megabyte snapshots.
#84 froze the schedule, removed write-to-main behavior and kept the snapshot only because it still contains unique provenance observations.

### Status

**END-TO-END CAPABILITY PROVEN; LIVE PRODUCT LOOP FROZEN.**

This is a critical historical distinction: the loop was not retired because it could not work.
It was retired because repeated value gates did not justify the product/operations cost.

## 15. Gold Corpus -> adversarial corpus -> frozen 81/26 corpus

### Gold Corpus origin

Machine-readable regression fixtures with:

- expected positive assertions;
- `FORBIDDEN_INFERENCE` negatives;
- evidence refs;
- DRAFT -> EVIDENCED -> VERIFIED;
- CI validation;
- source-accounting and semantic regressions.

### Evolution

The corpus later became a broader adversarial known-failure estate, eventually frozen at:

> **81 cases / 26 classes**

All exposed cases are `REGRESSION_ONLY`; blind re-use is false.

### Current repository

- `corpus/index-v0.1.json`
- fixtures across many historical components;
- Reference Pack exports.

### Status

**CURRENT CORE ASSET.**

## 16. Corpus Explorer v0.1

### Built

A deliberately thin static browser:

- HTML/CSS/vanilla JavaScript;
- direct read of canonical corpus JSON;
- search/filter;
- case detail;
- evidence/provenance references;
- deep links;
- responsive/accessibility work;
- browser regression tests.

### Current repository

- `mvp/`.

### Status

**TECHNICAL MVP COMPLETE; HUMAN/BEHAVIORAL VALUE PARKED.**

Cycle-1 synthetic use showed a mechanical discovery/provenance advantage but did not establish adoption or important human value.

## 17. Reference Pack v0.1/v0.2

### Purpose

Make the frozen corpus usable without repository archaeology.

### Built

- deterministic manifest/export;
- machine-readable case/class data;
- evidence navigation map;
- human catalog;
- quickstart/safe-use guidance;
- validator/checksums;
- cold-start audit;
- later v0.2 failure-analysis/navigation surface.

### Current repository

- `release/needle-reference-pack-v0.1/`
- `release/needle-reference-pack-v0.2/`.

### Status

**CURRENT RELEASED REFERENCE SURFACE.**

## 18. Maintenance Delta Contract v0.1

### Origin

Candidate-A hardening in #402 started with a much larger legal-evaluation maintenance packet.
Incumbent subtraction showed most static elements were already mature evaluation hygiene.

### Surviving core

> change -> evidence/time owner -> affected score-bearing contract -> revised state -> prior-result consequence -> adjudication state

### Current repository

- `docs/mvp/candidate-a-maintenance-delta-core-v0.1.md`
- `docs/mvp/candidate-a-maintenance-delta-card-template.md`
- `schemas/maintenance-delta-v0.1.schema.json`
- validator/tests/fixtures.

### Status

**CURRENT FIRST MVP CANDIDATE CORE; EXTERNAL VALUE UNPROVEN.**