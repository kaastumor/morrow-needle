# Issue #402 — Candidate A consolidation and incumbent subtraction

Date: 2026-09-26  
Mode: **CONSOLIDATE / MAINTAIN — CANDIDATE A MVP CORE**

## Phase 1 result — one job model

### User

Primary:

> legal-AI evaluation / benchmark maintainer who owns the legal validity of tasks, answer
> keys / criteria and the comparability of results across revisions.

Possible environments:

- independent benchmark operator;
- legal-tech vendor QA/evaluation team;
- legal department maintaining a private evaluation estate.

### Trigger

A maintained evaluation item needs attention because one of these happened:

- governing law/source state changed;
- a score-bearing legal proposition was found wrong or stale;
- a criterion was ambiguous, inconsistent or under-covering;
- a task/rubric revision changed the score-bearing contract;
- a real failure/postmortem needs to become a regression;
- an adjudication changes what the task should accept/reject.

### Input

The incumbent evaluation estate already owns most static material:

- task/instructions;
- source documents / authorities;
- answer/reference contract or rubric;
- deliverables;
- historical results;
- task/dataset version.

Candidate A does **not** need to re-model all of that.

### Decision/output

The maintainer needs to decide:

1. what actually changed;
2. why the change is authoritative / justified;
3. what score-bearing part of the evaluation contract is affected;
4. what must be repaired;
5. whether earlier results can still be compared;
6. whether existing outputs can be re-judged or subjects must be rerun;
7. what remains unresolved.

### Strongest incumbent

Public incumbent practice is already sophisticated.

#### DELTA / Legal Benchmarks

Current public contracts already include:

- fixed lawyer-authored binary criteria;
- explicit legal cut-off (law_as_of);
- cited authority for citation criteria;
- accommodation of professionally defensible approaches;
- qualified-human review of novel defensible approaches;
- criterion disputes;
- legal review of task changes;
- semantic dataset versioning / changelog;
- task pass only when all required criteria pass.

#### Harvey LAB

Current public LAB already includes:

- task instructions and source documents;
- deliverable-scoped criteria;
- semantic match_criteria;
- all-pass scoring;
- dual judges;
- per-criterion reasoning artifacts;
- repository versioning / task history;
- a maintained, evolving task estate.

Therefore the baseline is **not** a loose spreadsheet or naive answer key.

### Burden hypothesis

The residual burden worth testing is the **maintenance propagation step**:

> after a legally or evaluatively meaningful change is discovered, a qualified maintainer
> must determine its authoritative basis, scope its effect across criteria/results, repair
> the contract, and decide comparability / re-judging / rerun consequences.

Public evidence shows this work exists.

Public evidence does **not** establish its typical expert-hours cost or that Needle reduces it.

### Candidate A value hypothesis

> A compact maintenance-delta contract can reduce qualified reopening/reasoning/rework by
> making the change owner, affected evaluation surface and retest/comparability consequence
> explicit.

This is a **DELIVERY / maintenance-efficiency** hypothesis only.

### Strong counterevidence

- DELTA already has explicit legal-change/version/dispute discipline.
- Legal Benchmarks already uses legal review, alternative-aware criteria and human adjudication.
- Harvey LAB already has rich Git history and per-task rubric contracts.
- #362 warns that excellent ordinary evaluator practice may absorb most residual value.
- no public evidence proves maintainers currently lose substantial time because a delta contract is missing.

### External unknowns

Still externally owned:

- actual maintainer burden;
- private incumbent maintenance tooling;
- which fields maintainers already track internally;
- acceptable process overhead;
- willingness to reuse;
- whether delta records reduce future reopening.

---

## Phase 2 — incumbent-overlap subtraction

| Proposed #400 element | Disposition | Reason |
| --- | --- | --- |
| Task / intended decision | **JOB_REQUIRED_BUT_NOT_DIFFERENTIATING** | Every mature evaluation system already has a task/instruction contract. |
| Full authoritative source set | **JOB_REQUIRED_BUT_NOT_DIFFERENTIATING** | Sources are essential, but benchmark/task estates already preserve supplied files/authorities. |
| Accepted legal proposition / answer key | **INCUMBENT_STANDARD** | Core benchmark/oracle material. |
| Observable criteria | **INCUMBENT_STANDARD** | DELTA, Legal Benchmarks and Harvey all expose criterion-based contracts. |
| Valid alternatives | **INCUMBENT_STANDARD** | DELTA / Legal Benchmarks explicitly design for defensible alternatives and human review. |
| Fatal / non-compensatory failures | **INCUMBENT_STANDARD** | All-pass evaluation and mandatory criteria already implement non-compensation. |
| Whole-task / dataset version | **INCUMBENT_STANDARD** | DELTA versions/changelogs; Harvey uses repository revisions/tags. |
| Generic adjudication notes | **INCUMBENT_STANDARD** | Mature systems escalate disagreement and preserve review artifacts. |
| Generic evidence map | **JOB_REQUIRED_BUT_NOT_DIFFERENTIATING** | Source/criterion association exists in modern task contracts; a generic graph is not earned. |
| Per-change authoritative evidence owner | **NEEDLE_RESIDUAL_CANDIDATE** | Maintenance needs to show why this specific delta is justified; not enough evidence to call it absent elsewhere. |
| Per-change governing time/effective boundary | **NEEDLE_RESIDUAL_CANDIDATE** | #375 shows mutable score-bearing values can fail when event/effective time is wrong. |
| Semantic delta -> affected criteria mapping | **NEEDLE_RESIDUAL_CANDIDATE** | Git/versioning records bytes/revisions; maintainers still need to reason about scoring consequence. |
| Explicit prior-result comparability / rejudge / rerun disposition | **NEEDLE_RESIDUAL_CANDIDATE** | This is the clearest potential maintenance artifact after subtraction. |
| Needle failure-class / taxonomy label | **REMOVE** | No user value evidence; unnecessary for the maintenance job. |
| Full legal-state ontology | **REMOVE** | #395 strongly rejects assuming this is required. |
| Generic trajectory record | **REMOVE** | #390 narrows trajectories to diagnostic unless a workflow contract makes them constitutive. |

## Subtraction conclusion

The #400 maintenance packet is too large as an MVP core.

The smallest plausible residual is:

# **MAINTENANCE DELTA CONTRACT**

It does **not** recreate the evaluation estate.

It sits beside an existing estate and records only:

> **change -> evidence/time owner -> affected score-bearing contract -> repair ->
> comparability/retest consequence -> adjudication state**

Candidate C can enter through the same core when the change trigger is a production failure
or postmortem.

Candidate B remains separate; EU-specific state details appear only if an actual delta needs
them.

## Sources used for incumbent subtraction

- DELTA judge contract:
  https://github.com/legalbenchmarks/delta/blob/main/docs/judge.md
- DELTA contribution/version contract:
  https://github.com/legalbenchmarks/delta/blob/main/CONTRIBUTING.md
- Legal Benchmarks methodology:
  https://www.legalbenchmarks.ai/methodology
- Harvey LAB evaluation methodology:
  https://github.com/harveyai/harvey-labs/blob/main/docs/eval-strategies.md
- Harvey LAB architecture:
  https://github.com/harveyai/harvey-labs/blob/main/docs/architecture.md

## Phase disposition

# **STATIC_PACKET_REJECTED — DELTA_CORE_EARNED_FOR_REPLAY**

Delta core earned means only that the smaller contract is worth hardening/replaying.

It is not evidence of external value or uniqueness.