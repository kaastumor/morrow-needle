# Durable asset and reactivation register

Status: **HISTORICAL CAPABILITY MEMORY — NOT AN IMPLEMENTATION QUEUE**

This register exists to prevent the mistaken inference:

> not current = disproven = delete/forget.

Nothing here is automatically authorised for new work.

## Status vocabulary

- **CURRENT** — part of supported current identity or active MVP candidate.
- **CASE-EARNED** — use only if a concrete task demonstrates need.
- **PARKED** — technically real but no current investment case.
- **HISTORICAL VALID** — accepted subsystem/contract remains useful evidence/tooling but does not
  define current scope.
- **REJECTED CLAIM** — the associated value/superiority claim failed; code may still be valid.

## Register

| Asset / concept | Main repository location(s) | Historical value | Current status | What would earn reactivation / use |
| --- | --- | --- | --- | --- |
| Morrow Constitution / epistemic invariants | `docs/foundation-v0.1.md` | source/evidence/time/uncertainty discipline | **CURRENT principles; architecture conditional** | always apply binding principles; old architecture only when task needs it |
| Cellar ingestion / WEMI resolver | `src/needle/updates`, source schemas | authentic source identity + immutable observations | **HISTORICAL VALID / PARKED ops** | recurring source-ingestion job or EU-state product that needs live observation |
| Canonical Legal AST | `src/needle/ast`, `schemas/legal-ast-v0.1` | representation-neutral source structure, zero-loss accounting | **HISTORICAL VALID** | task needs machine reconstruction from official source bytes |
| Formex adapters/modification parsing | `src/needle/formex`, AST/mutation fixtures | authentic amendment/consolidation evidence | **HISTORICAL VALID** | live EU legal text reconstruction |
| Provision / Rule Lineage | `schemas/provision-lineage-*`, identity code | safe ancestry without fake persistent article identity | **CASE-EARNED** | repeated historical/renumber/recast queries where persistence reduces reopening/error |
| Identifier Graph | `schemas/identifier-*`, identity resolver | literal-vs-canonical ID resolution | **CASE-EARNED** | ambiguous/cross-system identifiers materially affect result |
| Temporal model v0.1/v0.2 | `src/needle/temporal`, temporal schemas | multidimensional legal time, context/subday support | **HISTORICAL VALID / case-earned** | any task with time-sensitive score-bearing/legal state |
| Procedure State | `src/needle/procedure`, schema | proposal/adoption/procedure state separate from law | **CASE-EARNED** | procedural state is decision-relevant |
| Deterministic mutation engine | `src/needle/mutation` | authentic before/after + source-assisted mutation | **HISTORICAL VALID** | legal-change reconstruction job |
| Language-scoped mutation | multilingual code/schema | corrigenda/authentic expression divergence | **CASE-EARNED** | language expression materially changes legal answer/history |
| Change Atom v0.3 | schema + semantic adversary | semantic claim only after verified textual mutation | **PARKED default / case-earned** | concrete legal-change job needs durable semantic mutation object |
| Provenance ledger | `src/needle/provenance`, provenance schemas | append-only support graph, correction without rewrite | **HISTORICAL VALID / conceptually current** | any durable artifact where future audit/reconstruction matters |
| Authoritative Dynamic Set | schema/fixtures | legal effect from authoritative membership/status | **HISTORICAL VALID** | task needs dynamic set state beyond text |
| Authoritative Metric + Rule Evaluation | metric schemas/fixtures | dynamic official numeric input to unchanged rule | **HISTORICAL VALID** | thresholds/formulas depend on versioned official observations |
| Authoritative Finding | finding schema/fixtures | categorical official determination distinct from text | **HISTORICAL VALID** | regulatory finding/inspection/disease state matters |
| Legal Spatial State | spatial schemas/fixtures | horizontal + vertical legal extent | **HISTORICAL VALID** | territorial/volumetric applicability job |
| Judicial Holding | schema/fixtures | court effect separate from text mutation | **CASE-EARNED** | evaluator/research task needs explicit holding state |
| Recognized External Determination | schema/fixtures | private-origin decision + separate public-law recognition | **HISTORICAL VALID** | legally recognized ratings/certifications/etc. |
| Thread | `src/needle/thread`, thread schema | executable longitudinal audit object | **PARKED product; valid audit tool** | repeated real job where manual chronology/reopening is costly |
| Structured Retrieval | `src/needle/retrieval`, retrieval schemas | typed retrieval with temporal/evidence boundaries | **PARKED** | product/job requires searching canonical state at scale |
| Dependency Ripple / X-Ray | `src/needle/analytics/dependency_ripple.py` | changed meaning/effect without local text mutation | **PARKED analytic** | real job benefits from systematic dependency discovery beyond ordinary diff |
| Half-Life | `src/needle/analytics/half_life.py` | temporary regime extension/gap/reenactment history | **PARKED analytic** | repeated temporary-regime analysis demand |
| Source Anomaly | `src/needle/analytics/source_anomaly.py` | source availability/conflict/fallback without legal overclaim | **PARKED analytic** | source fragility itself becomes a recurring job |
| Evidence / Why this is shown | presentation/provenance code | human-readable support/limits | **HISTORICAL VALID discipline** | any external artifact needing inspectable claims |
| Operational update pipeline | `src/needle/operations`, `updates` | live official event -> maintained source state / verified-or-abstained projection | **PARKED operations — #407 lightweight baseline sufficient** | concrete job that needs more than root grouping + source snapshots + hash comparison + ordinary legal review; do not revive generic monitoring by default |
| Frozen operational snapshot | `data/` historical state | unique Source Observations / provenance | **PRESERVE** | migrate unique observations before deleting snapshot |
| Gold/adversarial corpus | `corpus`, fixtures, evaluation protocol | known failure mechanisms + negative controls | **CURRENT** | default reference/regression role |
| Needle Method | protocol/charter/evaluation docs | structured source/authority/time/uncertainty handoff | **OPTIONAL convention** | concrete workflow demonstrates handoff/review benefit |
| Needle Core | old canonical state contracts | persistence can aid repeated/historical state | **CASE-EARNED ONLY** | real error/reopening cost prevented beyond Method |
| Full Needle | combined historical system | integrated engine existed; no 5-case gain over Core | **REJECTED AS DEFAULT IDENTITY** | only concrete external job needing multiple parked subsystems could reopen subset; not by nostalgia |
| Thin feed/product checkpoint v0.1 | `product/checkpoint-v0.1/` | early public-facing delivery prototype from the live-change/feed phase | **HISTORICAL PRODUCT PROTOTYPE / PARKED** | external recurring public change-intelligence job that first survives the stronger incumbent/value gates |
| Corpus Explorer v0.1 | `mvp/` | complete thin static corpus browser | **PARKED technical MVP** | real human browsing/distribution job or observed repeated use |
| Reference Pack v0.1/v0.2 | `release/` | current external navigation/reference surface | **CURRENT** | maintain only for accepted reference role / concrete user need |
| Evaluation integrity protocol | `docs/evaluations/adversarial-corpus-protocol-v0.1.md` | task/representation/evidence/execution/version/uncertainty discipline | **CURRENT when evaluations are run** | any consequential comparative evaluation |
| Failure-analysis packet discipline | v0.2 docs/uses | conditional reusable value after strong postmortem | **CURRENT conditional rule** | use when non-trivial state/boundary/reuse structure remains |
| Candidate A Maintenance Delta | `docs/mvp`, schema/validator/fixtures | smallest surviving eval-maintenance intervention | **CURRENT lead MVP candidate core** | external evaluator-owned value test |
| Candidate B EU operative state / harmonised-standard status | `docs/mvp/candidate-b-harmonised-standard-status-core-v0.1.md`, `mvp/candidate-b/`, dynamic-set fixtures | cross-owner operative-state research narrowed into a five-case standards-status usability wedge for lean product teams | **ACTIVE DISPOSABLE MVP CANDIDATE — VALUE UNPROVEN** | target-user usability vs free official sources, then direct incumbent-product comparison per #411 |
| Candidate C failure -> regression/oracle | failure-analysis + Candidate-A trigger | close fit to surviving corpus asset | **SECONDARY CANDIDATE / possible wedge** | real incident owner + current postmortem/regression process |

## Critical interpretation notes

### Thread, X-Ray, Half-Life, Source Anomaly and Retrieval were not 'bad code'

They lost **default/product priority**, not necessarily technical validity.

### Full Needle's claim failed, not every subsystem

#86 showed 0/5 material Full-over-Core gains. This means the integrated architecture was not
required for the tested research value. It does not imply every component is useless.

### Core lost default status, not all value

#87 showed no Core-over-Method handoff win across the sealed confirmation. Yet #86 had already
shown concrete cases where persistence improved deterministic historical/repeated-query handling.
Hence today's rule: **case-earned only**.

### Corpus-assisted research superiority failed more strongly

#214 is binding negative allocation evidence for the tested latent corpus-assisted workflow.
Do not revive that claim merely because the corpus remains useful for debugging/regression/reference.

## Reactivation protocol

Before reactivating a parked historical asset, require all four:

1. **Concrete job** — who needs it and for what decision/output?
2. **Strong incumbent** — what do they do today without this asset?
3. **Specific residual** — what consequential distinction/work does the asset add?
4. **Smallest re-entry** — use the narrowest historical component; never resurrect Full Needle by default.

Historical existence lowers implementation uncertainty. It does **not** lower the evidence threshold
for user value.