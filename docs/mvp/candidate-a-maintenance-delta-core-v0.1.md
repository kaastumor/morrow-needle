# Candidate A — Maintenance Delta Contract v0.1

Status: **PROVISIONAL INTERNAL MVP CORE — NOT YET EXTERNALLY VALIDATED**

Purpose:

> record the smallest evidence needed to maintain a legal evaluation contract after a
> legally or evaluatively meaningful change, without duplicating the underlying task,
> rubric, answer key, source pack or benchmark infrastructure.

This contract is the current Candidate-A core extracted in Issue #402.

It is not a claim of Needle-specific value.

---

## 1. Core principle

A maintenance record exists to answer six questions:

1. **What changed?**
2. **Why is that change justified?**
3. **What legal/evaluation time owns it, if time matters?**
4. **Which score-bearing contract elements are affected?**
5. **What repair is required?**
6. **What happens to prior outputs/results/comparisons?**

If a field does not help answer one of those questions, it does not belong in the core.

---

## 2. What this contract deliberately does not own

Do not duplicate:

- full task instructions;
- complete source bundles;
- full answer keys;
- full rubrics;
- generic valid-alternative policy;
- generic all-pass / fatal semantics;
- full benchmark version history;
- generic judge traces;
- Needle failure-class labels;
- a legal ontology;
- a product-specific execution harness.

Those belong to the incumbent evaluation estate.

The delta contract links to them by stable identifiers.

---

## 3. Minimal record

### 3.1 Identity

Required:

- `record_id` — stable maintenance-delta identifier;
- `core_version` — this contract version;
- `subject.task_id` — incumbent task/evaluation item identifier;
- `subject.baseline_contract_ref` — immutable version/commit/release of the contract being changed.

Optional until a repair is accepted:

- `subject.candidate_contract_ref` — immutable revised version/commit/release.

### 3.2 Trigger

Required:

- `trigger.kind` — one of:
  - `LAW_OR_SOURCE_CHANGE`
  - `WRONG_OR_STALE_LEGAL_PROPOSITION`
  - `CRITERION_ACTIVATION_AMBIGUITY`
  - `CRITERION_COVERAGE_GAP`
  - `CROSS_CRITERION_INCONSISTENCY`
  - `ACCEPTANCE_BOUNDARY_CHANGE`
  - `TASK_OR_RUBRIC_REVISION`
  - `FAILURE_POSTMORTEM`
  - `OTHER`;
- `trigger.summary` — concise description;
- `trigger.reference` — issue, source, incident, adjudication or change artifact that caused review.

Optional:

- `trigger.observed_at` — timestamp/date when operationally useful.

### 3.3 Delta units

At least one delta unit is required.

Each unit contains:

- `id` — local identifier;
- `kind` — one of:
  - `LEGAL_PROPOSITION`
  - `CRITERION_ACTIVATION`
  - `CRITERION_COVERAGE`
  - `CRITERION_CONSISTENCY`
  - `TASK_INSTRUCTION`
  - `ACCEPTANCE_BOUNDARY`
  - `RESULT_INTERPRETATION`
  - `OTHER`;
- `before` — exact or concise prior score-bearing state;
- `after` — proposed/revised state, or `UNRESOLVED`;
- `affected_contract_refs` — criterion IDs / answer-key fields / deliverable IDs / task fields actually affected;
- `risk` — zero or more of:
  - `FALSE_REJECT`
  - `FALSE_ACCEPT`
  - `AMBIGUOUS_GRADING`
  - `NON_COMPARABLE_RESULTS`
  - `NO_KNOWN_SCORE_IMPACT`
  - `UNKNOWN`.

### 3.4 Evidence owner

Required for a delta that asserts a factual/legal correction:

- `evidence.owner_ref` — authoritative source or evidence artifact;
- `evidence.proposition` — what that source supports;
- `evidence.status` — `SUPPORTED`, `CONTESTED`, or `UNRESOLVED`.

For purely evaluative contract changes, the evidence owner may be the task instructions,
rubric contract, adjudication decision or reproducible internal inconsistency rather than
external law.

### 3.5 Governing time

Required only when the corrected proposition can vary over time.

Use:

- `governing_time.kind`:
  - `LAW_AS_OF`
  - `CONTROLLING_EVENT_DATE`
  - `EFFECTIVE_PERIOD`
  - `NOT_APPLICABLE`
  - `UNRESOLVED`;
- `governing_time.value_or_ref` — the date/period/event/source that actually owns the proposition.

Do not require a standalone law-as-of field when a transaction, filing, closing or other
event unambiguously owns legal time.

### 3.6 Repair

Required:

- `repair.actions` — the minimal changes needed to restore a coherent evaluation contract;
- `repair.status` — `PROPOSED`, `ACCEPTED`, `REJECTED`, or `PARTIAL`.

An accepted repair must point to `subject.candidate_contract_ref`.

### 3.7 Prior-result consequence

Required:

- `result_impact.comparability` — one of:
  - `COMPARABLE`
  - `NOT_COMPARABLE`
  - `UNKNOWN`;
- `result_impact.existing_outputs_action` — one of:
  - `NONE`
  - `REJUDGE_EXISTING_OUTPUTS`
  - `RERUN_SUBJECTS`
  - `REVIEW_SAMPLE`
  - `HUMAN_DECISION_REQUIRED`;
- `result_impact.scope` — which historical/current results are potentially affected;
- `result_impact.reason` — why.

This is the central Candidate-A residual after incumbent subtraction.

Version change alone is not a defect.

The contract must distinguish:

- semantic revision with no evidence of error;
- repair of a defective contract;
- change that invalidates historical comparison;
- change where existing raw outputs can be re-judged without rerunning the subject;
- change that requires a fresh subject run.

### 3.8 Open questions / adjudication

Optional but explicit when needed:

- `open_questions[]`;
- `adjudication.status` — `NOT_REQUIRED`, `PENDING`, `ACCEPTED`, `REJECTED`, `SPLIT`;
- `adjudication.note`;
- `adjudication.owner_ref` when available.

Do not convert unresolved legal disagreement into a confident repaired oracle.

---

## 4. Invariants

A delta record is structurally invalid if any of these fail:

1. at least one delta unit exists;
2. every delta unit either identifies affected score-bearing contract refs or explicitly records `NO_KNOWN_SCORE_IMPACT`;
3. a legal/factual correction has an evidence owner or is marked `UNRESOLVED`;
4. a time-varying legal proposition has a governing-time owner or is marked `UNRESOLVED`;
5. an accepted repair has an immutable candidate-contract reference;
6. any potential historical-score effect has an explicit comparability decision;
7. `NOT_COMPARABLE` or `UNKNOWN` may not silently pair with `existing_outputs_action: NONE`;
8. unresolved evidence may not support `repair.status: ACCEPTED` without explicit qualified adjudication;
9. the delta record may not silently add unrelated rubric requirements;
10. taxonomy/class labels are never required.

---

## 5. Compact human rendering

Every machine/human record should be renderable as one **Maintenance Delta Card**:

### Subject
`task-id @ baseline-version -> candidate-version/pending`

### Trigger
`why this contract was reopened`

### Changed score-bearing state
`before -> after`, with evidence owner and governing time when applicable.

### Evaluation impact
`affected criteria / risk direction`

### Repair
`minimal contract edit`

### Existing results
`comparable / rejudge / rerun / human decision required`

### Open questions
`none` or explicit unresolved items.

The card should remain understandable without Needle taxonomy knowledge.

---

## 6. Why there is no JSON Schema yet

Phase #402 deliberately freezes semantics before implementation.

A schema/validator is earned only if the three bounded replays show that:

- the same fields recur;
- deterministic checks catch real mistakes;
- the contract does not need immediate restructuring;
- validation does not create more maintenance burden than it removes.

Until then, schema work would be premature hardening.

---

## 7. Candidate C entry path

`FAILURE_POSTMORTEM` is an explicit trigger kind.

This allows Candidate C to use the same core when a real legal-AI failure becomes a
maintenance/regression event.

Candidate C remains a live secondary candidate; this contract does not collapse its
commercial/value hypothesis into Candidate A.

---

## 8. Candidate B boundary

EU-specific state is not built into the core.

If an evaluation delta depends on:

- a national option;
- certificate/registry state;
- standard citation status;
- dynamic authoritative value;
- other cross-owner EU state;

the delta unit references the required evidence owner.

No generic EU state model is created.

---

## 9. Current claim

Supported:

> this is the smallest internally coherent Candidate-A intervention currently worth replaying.

Not supported:

- that evaluators lack an equivalent internal artifact;
- that it reduces expert time;
- that it improves legal correctness;
- that it has commercial value;
- that it should become software.

Those remain future evidence gates.