# Issue #385 — legal rubric acceptance-boundary audit

Date: 2026-09-26  
Mode: **DISCOVER — LEGAL RUBRIC ACCEPTANCE-BOUNDARY AUDIT**

## Result

# **PUBLIC_EVIDENCE_INSUFFICIENT**

The audit finds a credible **mechanism** for false rejection of professionally valid legal
answers, but it does not find enough public legal-domain evidence to claim that the mechanism
is materially present in current expert-authored legal benchmarks.

The strongest legal benchmark evidence cuts both ways:

- some published legal evaluators use strict item-by-item / literal matching against finite
  expert rubrics, creating a structural omission risk;
- strong practitioner-authored benchmarks explicitly design around professionally defensible
  alternatives and provide human-review / criterion-revision escape hatches;
- the public defects located in DELTA and Harvey LAB mostly concern **wrong law, activation,
  internal inconsistency, stale values or false acceptance**, not a demonstrated
  independently-valid answer being rejected solely because the accepted path was omitted.

The correct conclusion is therefore not:

> legal rubrics have a demonstrated false-rejection problem.

It is:

> **legal false-rejection by incomplete acceptable-set authoring is a plausible risk with a
> clear probe design, but current public evidence does not establish its prevalence or even a
> clean observed legal case under the strict #385 definition.**

No new protocol repair is required beyond the protections already added by #375/#381.

---

## 1. What counts as evidence for #385

A qualifying positive needs all of the following:

1. the criterion/rubric representation is otherwise appropriate for the task;
2. an answer/strategy is independently supportable as legally and professionally acceptable;
3. the evaluation contract rejects it;
4. the rejection is caused by an **incomplete acceptance boundary** rather than:
   - wrong legal authority;
   - stale law;
   - judge execution error;
   - ambiguous instructions;
   - a genuinely mandatory requirement;
   - representation mismatch;
   - an internally inconsistent rubric;
5. widening the accepted set can be done without admitting a paired materially wrong answer.

This high bar prevents ordinary benchmark defects from being relabelled as false rejection.

---

## 2. Strong negative control — DELTA

DELTA is currently the strongest inspectable counterexample to a naive
"expert legal rubrics enumerate one path" thesis.

### Explicit contract safeguards

DELTA's public judge contract states that:

- criteria must accommodate professionally defensible approaches;
- judges must grade the written criterion rather than personal taste;
- if an answer takes a potentially defensible approach not clearly covered by the criterion,
  the issue goes to qualified human review rather than failing novelty alone;
- if the approach is accepted, the criterion is revised in the next dataset version;
- pass-changing judge disagreement is escalated to a qualified lawyer.

Its contribution rules similarly require criterion authors to:

- state the common minimum requirements where multiple approaches are defensible;
- include accepted alternatives;
- keep substance and form separate;
- make each criterion observable from the answer;
- version substantive criterion changes.

This is not proof that DELTA never falsely rejects an alternative. It is strong evidence that
the risk is explicitly recognised and operationally mitigated.

### Mechanical criterion scan

The complete public DELTA release contains:

- **15 tasks**;
- **273 criteria**:
  - 192 substance;
  - 51 citation;
  - 30 form.

A simple high-recall English-text scan finds:

- 90 criteria using semantic verbs such as explain / identify / address / discuss / conclude;
- 40 criteria (14.7% of all criteria) containing an obvious heuristic flexibility marker
  such as "or otherwise", "or equivalent", multiple alternatives, "for example", or an
  explicit route-tolerant formulation;
- at least one criterion explicitly states that **any legally reasoned route** to the required
  conclusion is acceptable.

This heuristic is not a quality score and undercounts semantic flexibility that is expressed
without one of those phrases. It is included only to show that the public contract is not a
literal single-reference-answer matcher.

### Public disputes

Two current DELTA criterion disputes were inspected.

#### DELTA #1 — Article 3:97 BW paragraph mismatch

The criterion attributes the enabling rule for advance delivery to paragraph 2 instead of
paragraph 1.

Consequence:

> a legally correct answer can fail while a wrong attribution can pass.

This superficially resembles false rejection, but it is **not #385 evidence**.

Cause:

> **wrong oracle / wrong legal proposition**

The correct repair is to fix the law, not broaden the accepted-answer set.

#### DELTA #2 — conditional criterion with no activation rule

A criterion applies "insofar as" the answer raises dynamic interpretation, but the task does
not elicit that argument. Different judges resolve the vacuous case differently.

Cause:

> **activation / gradability ambiguity**

Again, not incomplete acceptable-set authoring.

### DELTA conclusion

DELTA materially weakens the hypothesis that modern expert-authored legal rubrics are
structurally blind to valid alternatives.

It does not eliminate the possibility of case-level omissions.

Sources:
- https://github.com/legalbenchmarks/delta
- https://github.com/legalbenchmarks/delta/blob/main/docs/judge.md
- https://github.com/legalbenchmarks/delta/blob/main/CONTRIBUTING.md
- https://github.com/legalbenchmarks/delta/issues/1
- https://github.com/legalbenchmarks/delta/issues/2

---

## 3. Legal Benchmarks — explicit alternative-aware policy

Legal Benchmarks' public methodology states that its lawyer-authored fixed binary criteria
are intended to recognise that legal work may have more than one professionally defensible
answer.

Where several approaches are defensible, the criteria are meant to accommodate them while
still identifying omissions/errors that must fail.

Its current application methodology also:

- runs tasks twice;
- uses independent judging;
- escalates pass-changing disagreement to qualified lawyers.

This is design-level evidence, not proof that every hidden criterion is complete.

But it is a strong falsifier against the claim that current commercial legal evaluation
simply assumes one answer path.

Source:
https://www.legalbenchmarks.ai/methodology

---

## 4. Structural risk — PLawBench

PLawBench provides the clearest public legal **risk surface**.

Its public scoring protocol describes:

- "strict literal comparison" with expert-curated rubrics;
- item-by-item inspection;
- explicit-content requirements;
- prohibition on the judge supplementing or inferring unstated content.

For practical case analysis, points are awarded only for information explicitly represented
in the response.

This design has legitimate benefits:

- auditability;
- stable scoring;
- less judge improvisation;
- fine-grained diagnostic feedback.

But it creates a theoretical acceptance-boundary risk when:

> a professionally valid analysis reaches the required legal quality through a materially
> different decomposition than the expert rubric.

The paper does not, in the evidence inspected here, provide a clean independently adjudicated
example of such a valid alternative being falsely rejected.

Therefore PLawBench supports:

> **STRUCTURAL_RISK**

not:

> **OBSERVED_LEGAL_FALSE_REJECTION**

Source:
https://openreview.net/pdf?id=qUh6dBFflA

---

## 5. Structural risk — LexRubric

LexRubric contains:

- 649 instances;
- 12,337 expert-written atomic criteria;
- around 19 criteria per instance on average;
- three independent legal-expert annotation rounds;
- explicit requirements that rubric sets cover key aspects of an "ideal answer", avoid
  omissions, remain atomic, objective/binary and self-contained.

This is serious expert curation.

It also exposes the general finite-enumeration problem:

> the accepted construct is represented through a finite set of authored atomic requirements.

The benchmark's high judge agreement is evidence that judges can apply the contract
consistently.

It is **not by itself evidence that the contract includes every professionally acceptable
strategy**.

No clean public false-rejection example was located in the inspected evidence.

Result:

> **STRUCTURAL_RISK + STRONG EXPERT-CURATION COUNTEREVIDENCE**

Source:
https://openreview.net/pdf/95f123dad974a26b546b1020123024678e46341c.pdf

---

## 6. JudgmentBench is not direct #385 evidence

JudgmentBench reports a major difference between rubric scoring and comparative judgment on
holistic quality ordering.

That result was central to #381.

It does not, by itself, identify a particular legal answer as:

- professionally acceptable under an independent reference judgment;
- failed by one too-narrow criterion;
- accepted after the missing route is added.

So it is evidence for:

> **representation validity matters**

rather than a clean observed instance of:

> **acceptance-set omission caused false rejection**

Do not double-count #381 evidence as #385 evidence.

Source:
https://arxiv.org/abs/2605.25240

---

## 7. Harvey LAB defect audit — useful negative classification

Several current public Harvey issues were inspected because their symptoms can resemble
acceptance-boundary failures.

### Issue #146 — count/precision allowlists conflict

Seven firm-knowledge contracts contain fixed counts/rates that do not reconcile with matters
admitted by a precision allowlist.

The issue itself is careful not to decide every matter's source truth.

Primary defect:

> **cross-criterion / typed-set inconsistency**

Not #385 evidence.

### Issue #147 — full score without requested escrow analysis

Task 142 can satisfy all checked criteria while omitting central requested quantitative work.

Primary defect:

> **undercoverage / false acceptance**

This is the opposite direction from #385.

### Earlier #375 HSR values

The source-backed HSR mismatch is:

> **wrong/stale legal oracle**

not incomplete acceptable-set authoring.

### Harvey conclusion

These defects strengthen the case for general evaluation-contract auditing.

They do not supply a clean legal false-rejection observation.

Sources:
- https://github.com/harveyai/harvey-labs/issues/146
- https://github.com/harveyai/harvey-labs/issues/147

---

## 8. Non-legal mechanism evidence

### Judging Is Not Enumerating

The 2026 paper demonstrates a general recognition-versus-enumeration asymmetry:

> systems can be substantially better at judging whether a candidate is acceptable than at
> exhaustively authoring the acceptable set in advance.

Its strongest false-rejection measurements are not legal expert-rubric evidence.

Those rates therefore must not be imported into Needle.

The useful transfer is the **probe concept**:

> start from known-correct alternatives and test whether the authored verifier admits them.

Source:
https://arxiv.org/abs/2608.01000

### Rubrics on Trial

This independent 2026 rubric-design work explicitly identifies over-specific rubrics that can
penalise a valid alternative strategy as a rubric failure mode.

It validates proposed criteria through synthetic response comparisons to screen out:

- non-discriminative criteria;
- style-only criteria;
- over-specific criteria.

Again, this is general LLM-evaluation evidence rather than legal prevalence evidence.

Source:
https://arxiv.org/abs/2607.15092

---

## 9. Evidence classification

| Evidence | Observed valid-alternative false rejection? | #385 use |
| --- | --- | --- |
| DELTA policy / criteria | No | strong safeguard / negative control |
| DELTA #1 | No — wrong legal oracle | exclude from #385 positive evidence |
| DELTA #2 | No — activation ambiguity | exclude |
| Legal Benchmarks methodology | No | strong safeguard |
| PLawBench strict matching | No observed case located | structural risk |
| LexRubric finite atomic ideal-answer decomposition | No observed case located | structural risk + expert-curation counterevidence |
| JudgmentBench | No specific acceptance-boundary case | belongs primarily to #381 |
| Harvey #146 | No — inconsistency | exclude |
| Harvey #147 | No — false acceptance | exclude |
| #375 Harvey HSR | No — wrong/stale oracle | exclude |
| Judging Is Not Enumerating | Yes outside legal expert-rubric setting | mechanism only |
| Rubrics on Trial | General valid-alternative failure mode | mechanism only |

### Clean public legal positives found

> **0**

That zero must not be turned into a prevalence estimate.

It means:

> this bounded public audit did not locate evidence strong enough to support the legal-domain
> claim.

---

## 10. What the protocol already owns

No new Needle protocol layer is earned.

After #375 and #381, the canonical protocol already requires:

- a **valid-alternative policy** before execution;
- that an otherwise acceptable answer not fail merely because the key encodes one
  unnecessarily narrow formulation;
- positive mutation/variation checks where practical;
- qualified adjudication where uncertainty can change the result;
- non-compensatory/fatal constraints;
- versioned task/criterion state.

That is already the minimal sensible defense against the mechanism.

Creating another named "acceptance-boundary protocol" would be duplication.

---

## 11. What would reopen the claim

The lane becomes materially stronger if a future external observation supplies:

1. an answer independently accepted by qualified legal reviewers;
2. a legal rubric/criterion that rejects it;
3. evidence that the task instructions permit the alternative;
4. a narrow criterion repair that admits the valid answer;
5. a paired invalid answer that remains rejected after the repair.

That would distinguish:

> **acceptance-boundary repair**

from simply making the benchmark more permissive.

A public corpus of rubric disputes with adjudicated alternative answers would be especially
valuable.

---

## Final disposition

# **PUBLIC_EVIDENCE_INSUFFICIENT**

What survives:

- incomplete acceptable-set authoring is a credible general evaluation failure mechanism;
- some legal rubric designs expose structural risk;
- positive-alternative probing is a sound defensive technique;
- Needle's existing protocol already includes the relevant minimal safeguard.

What does not survive:

- a claim that expert legal rubrics currently have demonstrated material false-rejection
  prevalence;
- a Needle-specific advantage;
- another protocol layer;
- a product or service claim.

## Allocation recommendation

Close #385 without implementation.

Do not manufacture a positive through synthetic legal alternatives graded by the same system.

The next project allocation should be reconsidered from the remaining lanes, with increasing
weight on whether the **internal public-evidence frontier has been reached**.
