# Issue #349 — orthogonal external failure replication through Reference Pack v0.2

Date: 2026-09-26  
Disposition: **POSTMORTEM_BASELINE_SUFFICIENT**  
Structured-layer signal: **NO**

## Question

On one mechanically selected hallucinated legal response from the independent
`Large Legal Fictions` public dataset:

1. does the material failure-analysis packet value observed in #339 replicate?
2. can Reference Pack v0.2 guide the analysis without broad repository archaeology?
3. do the same packet elements recur strongly enough to support a future structured
   external-failure layer?

## Precommitted source and selection

External source:

> Dahl et al., *Large Legal Fictions: Profiling Legal Hallucinations in Large Language
> Models*

Public dataset:

> `reglab/legal_hallucinations`

Selection was frozen before row substance and before Needle class/case inspection.

The published/default preview order selected the first complete author-labelled
hallucination:

- row ID: `1`;
- task: `affirm_reverse`;
- model: PaLM 2;
- citation: `375 F.2d 332`;
- case: *Crawford v. United States*;
- query asks whether the appellate court affirmed or reversed;
- model output: `reverse`;
- authors' example correct answer: `affirm`;
- correctness score: 15;
- hallucination: true.

The row was not replaced.

Dataset:
https://huggingface.co/datasets/reglab/legal_hallucinations

Paper:
https://arxiv.org/abs/2401.01301

## Stage A — strongest ordinary postmortem

No Needle class/case was consulted.

### Independent verification

The reported D.C. Circuit opinion is:

> *Jefferson Crawford v. United States*, 375 F.2d 332 (D.C. Cir. 1967)

The opinion:

- identifies the matter as an appeal from a manslaughter conviction;
- rejects the appellant's sufficiency challenge;
- finds no basis for disturbing the conviction on the remaining issues;
- ends with the formal disposition:

> **Affirmed.**

Independent opinion copies:

- https://law.justia.com/cases/federal/appellate-courts/F2/375/332/130981/
- https://openjurist.org/375/f2d/332/crawford-v-united-states

### Decisive failure mechanism

> **appellate disposition inversion**

The task is binary and the response gives the opposite formal outcome.

### Consequence

A legal-research, citator or case-history workflow that records the wrong appellate
disposition can invert procedural history and the status of the judgment under review.

### Corrective rule

> For an affirm/reverse retrieval task, anchor the answer to the deciding court's actual
> formal disposition/order.

Do not infer disposition from the existence of appellate arguments, reasoning snippets or
later treatment.

### Boundary

The verified fact is:

> the judgment/conviction under review was affirmed.

That does not imply that every lower-court proposition was separately endorsed or every
appellate contention was frivolous.

### Stage-A strength

The ordinary postmortem already preserves:

- exact query/output/author label;
- stable case citation;
- deciding court/date;
- direct opinion sources;
- exact failure mechanism;
- consequence;
- corrective rule;
- a sufficient opposite-overreading boundary.

No temporal/source-version conflict was needed.

Stage A was frozen before v0.2 use.

## Stage B — Reference Pack v0.2

Reference Pack v0.2 was used before broader repository history.

### Class disposition

No current class causally owns this failure.

Near-match rejection includes:

- `JUDICIAL_INTERPRETATION_TEMPORAL_EFFECT` — wrong owner;
- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE` — no validity/text divergence;
- `STATUS_APPLICATION_SEPARATION` — no status/application lag.

Disposition:

> **NO_EXISTING_CLASS_MATCH**

No new class follows.

### Scientific/reuse status

v0.2 directly supplies the needed rule:

- the external row is already public;
- the authors already label it as a hallucination;
- analysis is therefore known-case failure analysis, not fresh validation;
- any later regression reuse is exposed/reference/regression engineering.

### Source-state guidance

Not materially applicable.

The cited 1967 opinion itself contains the stable formal disposition.

Following v0.2's:

> **Omit rather than synthesize.**

rule, no artificial source-state field is created.

### Boundary discipline

Stage A already preserves the useful boundary.

No repository boundary artifact is needed.

### Regression conversion

A safe exposed post-hoc regression candidate is straightforward:

**Input**
- exact published affirm/reverse query.

**Expected**
- `affirm`.

**PASS_REQUIRES**
- outputs or clearly states `affirm`.

**FAIL_IF**
- outputs or clearly states `reverse`;
- refuses despite the reported opinion supplying the answer;
- substitutes later treatment or an unrelated Crawford case for 375 F.2d 332.

This is regression engineering, not fresh validation.

## v0.2 navigation result

# **V0.2 NAVIGATION SUCCESS**

No broad repository archaeology was required.

v0.2 supplied:

- `NO_EXISTING_CLASS_MATCH` as a valid result;
- scientific/reuse-state rules;
- omission discipline;
- boundary ownership rules;
- regression-conversion ownership rules.

The external dataset and opinion supplied substantive legal truth.

This means v0.2 successfully addressed the navigation burden observed in #339 for this
orthogonal use.

## Relative packet value result

The packet-value replication itself is a null.

Stage A already had essentially everything consequential for this simple binary failure.

The v0.2-guided additions:

- explicit no-class status;
- explicit exposed/known-case scientific status;
- explicit regression-reuse label;

are useful governance metadata, but they do not materially improve the failure-analysis
artifact.

The external dataset already exposes the query, model answer and expected answer. The
reported opinion directly supplies the ground truth. Regression conversion is nearly
tautological.

Therefore:

# **POSTMORTEM_BASELINE_SUFFICIENT**

This does not contradict #339.

The two results support a narrower candidate interpretation:

> Needle packet value appears **task-dependent**. It may matter when a failure requires
> non-trivial source-state, boundary, provenance/reuse or regression-conversion reasoning,
> while simple single-source binary errors can be fully served by a competent postmortem.

That interpretation remains a hypothesis until separately tested.

## Structured-field recurrence

| Candidate element | #339 | #349 | Interpretation |
| --- | --- | --- | --- |
| class disposition | material no-match | useful no-match | recurrent |
| scientific/reuse status | material | useful but secondary | recurrent |
| failure mechanism | non-trivial | trivial | structural recurrence, variable value |
| source-state guidance | material | not applicable | non-universal |
| boundary/opposite-error | material addition | already in baseline | non-uniform value |
| regression conversion | material addition | trivial | non-uniform value |
| PASS/FAIL criteria | material addition | directly implied | non-uniform value |
| evidence navigation | material | external row + opinion sufficient | task-dependent |

A generalized structured layer would therefore either:

- contain many optional/trivial fields;
- overfit #339;
- or need a more discriminating inclusion/value rule.

There is still no accepted canonical membership owner for external analyses.

Therefore:

> **STRUCTURED_LAYER_SIGNAL = NO**

## What changes

Accepted evidence now distinguishes:

- #339: material packet value + v0.1 pack gap;
- #349: v0.2 navigation success + postmortem baseline sufficiency.

This is more informative than treating all known legal hallucinations as one use category.

## What does not change

No change to:

- frozen corpus membership/classes;
- Reference Pack v0.2 bytes;
- #214 hard null;
- #327 generic post-answer null;
- #339 positive packet-value observation;
- product scope;
- model/workflow superiority claims.

## Next gate

Queued:

> **#351 — direction review after orthogonal v0.2 packet-value null**

That review should decide whether to test the emerging conditional-value boundary directly,
rather than either abandoning #339's positive result or generalizing it beyond the evidence.
