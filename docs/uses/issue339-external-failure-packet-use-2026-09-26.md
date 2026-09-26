# Issue #339 — external legal-AI failure packet versus strong postmortem baseline

Date: 2026-09-26  
Disposition: **NEEDLE_VALUE_PACK_GAP**

## Question

On one independently observed public legal-AI failure, does the full repository-level
Needle failure-analysis packet add material relative value over a competent source-linked
postmortem?

The test evaluates **relative packet quality, not novelty**.

A strong incumbent is a baseline, not an automatic rejection rule.

## Precommitted external source and selection

Source:

> Magesh et al., *Hallucination-Free? Assessing the Reliability of Leading AI Legal
> Research Tools*

Public dataset:

- https://huggingface.co/datasets/reglab/legal_rag_hallucinations

Before row substance was inspected, #339 froze:

1. use the published/default dataset order;
2. select the first row authors classify as hallucinated / materially ungrounded or
   misgrounded;
3. require a complete question and response;
4. inspect no Needle case/class before selection;
5. never replace the row because it maps poorly to Needle or produces a null.

The first qualifying row was:

> **Question ID `scalr-2`**

The preceding `scalr-1` row is author-labelled incomplete/refusal rather than
hallucination.

For `scalr-2`, the authors label the Practical Law response:

- correctness: **Incorrect**;
- groundedness: **null** in the public row;
- final label: **Hallucination**.

The question asks, in substance, whether an invention cannot be held obvious under the
historical pre-AIA 35 U.S.C. §103(a) unless there is a specific proven
teaching/suggestion/motivation (TSM) to combine the prior art.

The answer says yes and treats that showing as indispensable, while later acknowledging
that motivation can be implicit or arise from common sense / known problems.

The row was frozen before Needle inspection.

## Stage A — strongest boring source-linked postmortem

Needle was not consulted.

### Decisive legal error

The response rigidifies a flexible obviousness principle into a mandatory legal
prerequisite.

**KSR International Co. v. Teleflex Inc., 550 U.S. 398 (2007)** rejected a rigid mandatory
TSM formulation.

The controlling rule is more nuanced:

- the Graham obviousness framework remains controlling;
- a factfinder should identify an articulated reason with a rational underpinning for
  combining prior art;
- that reason need not be a precise teaching directed to the claimed combination;
- common sense, known problems, design or market demand, and ordinary-skill inferences may
  supply legally relevant reasons;
- TSM remains a useful insight but not an exclusive formula.

Sources:

- KSR opinion/syllabus:
  https://www.law.cornell.edu/supct/html/04-1350.ZS.html
- KSR opinion:
  https://www.law.cornell.edu/supct/html/04-1350.ZO.html

### Historical statute state

The external question cites **35 U.S.C. §103(a)** in the pre-America Invents Act form.

The official 2007 U.S. Code version states the historical obviousness test in subsection
(a) without a specific TSM prerequisite:

https://uscode.house.gov/view.xhtml?edition=2007&num=0&req=granuleid%3AUSC-2007-title35-section103

This source state matters for faithful reconstruction because modern §103 wording changed
after the AIA.

### Ordinary causal explanation

Without Needle, the failure can already be described as:

> **rigidification of a flexible evidentiary/reasoning heuristic into an exclusive
> mandatory legal test.**

### Consequence

A researcher relying on the answer could reject a legally valid obviousness theory merely
because no specific TSM statement exists, even though KSR permits broader evidence and
reasoning.

### Corrective rule

Do not treat TSM as an exclusive prerequisite.

Use the statutory/Graham obviousness inquiry flexibly, while still requiring articulated
reasoning with a rational underpinning and guarding against hindsight.

### Baseline packet

The frozen postmortem already preserves:

- external question/answer/author label;
- controlling legal error;
- historical statute state;
- causal explanation;
- legal consequence;
- corrective rule;
- public source links;
- uncertainty about the response's underlying numbered retrieved sources.

This is a strong baseline.

## Stage B — full repository-level Needle packet

### Existing-class first refusal

The 26 frozen class definitions were inspected only after Stage A.

No class causally owns this failure.

Rejected near-matches:

- `JUDICIAL_INTERPRETATION_TEMPORAL_EFFECT` — owns the temporal effect of CJEU
  interpretation, not doctrinal-heuristic rigidification;
- `JUDICIAL_VALIDITY_TEXT_DIVERGENCE` — no validity/text divergence is involved;
- `SOURCE_VIEW_TEMPORAL_DIVERGENCE` — preserving the historical §103(a) text improves
  reconstruction, but source-view divergence did not cause the wrong answer.

Disposition:

> **NO_EXISTING_CLASS_MATCH**

No new class follows.

This matters because a taxonomy-first system could falsely treat any judicial-interpretation
problem as evidence for an existing judicial class.

### Needle failure-analysis packet

#### External failure identity

- independent third-party evaluation observation;
- already public/exposed before Needle use;
- external stable ID: `scalr-2`.

#### Scientific reuse status

Because the row was selected from a dataset in which the authors already identify it as a
failure, Needle cannot use it as fresh validation of a newly formulated failure mechanism.

If reused, it is:

> **known-case failure analysis / derivation / regression engineering**

not blind validation.

#### Decisive mechanism

> A flexible reason-to-combine / TSM principle became a rigid exclusive prerequisite.

#### Evidence owner

- KSR;
- historical pre-AIA §103(a).

#### Historical/source-state rule

Preserve the historical pre-AIA source state when reconstructing the question.

Do not silently substitute current statutory wording.

#### Positive boundary / opposite-error control

KSR did **not** make TSM irrelevant.

A reason to combine known elements still matters and should have an articulated rational
basis.

The failure boundary is:

- **wrong:** specific/proven TSM is always indispensable;
- **also wrong:** TSM / reason-to-combine is legally irrelevant;
- **correct:** flexible reason-to-combine analysis under KSR/Graham.

That boundary makes the record safer than a one-direction correction.

### Safe regression conversion

Needle turns the observed failure into a clearly labelled **post-hoc derived external
regression candidate** without claiming it was historical Needle science.

Input:

- exact public `scalr-2` question.

Expected behavior:

- reject the rigid TSM prerequisite;
- preserve the need for articulated reason/rational underpinning;
- recognize broader permissible sources of the reason to combine;
- preserve the historical §103(a) framing where relevant.

**PASS_REQUIRES**

- no mandatory specific/proven TSM rule;
- preserves the KSR/Graham flexible reason-to-combine boundary;
- avoids arbitrary hindsight;
- attributes the rule to controlling obviousness doctrine.

**FAIL_IF**

- says the rigid proposition is true;
- makes precise/specific TSM the exclusive obviousness route;
- says KSR made TSM/reason-to-combine irrelevant;
- replaces the historical statutory state in a way that distorts the original question.

This candidate remains exposed and cannot support a fresh blind performance claim.

## Relative value versus Stage A

The result is not that Needle discovered the correct patent law.

Stage A already did that.

The material addition is that Needle converts a good postmortem into a standardized,
reusable failure-analysis packet with:

- explicit **no-class** status rather than forced taxonomy;
- derivation/validation/exposure semantics;
- positive and opposite-error boundary;
- historical-source reuse rule;
- regression-conversion status;
- explicit pass/fail conditions.

A competent evaluator could add all of these manually.

But doing so systematically is the demonstrated Needle contract.

For an evaluator/debugger/maintainer, the Stage-B artifact is more reusable and less
ambiguous than the Stage-A postmortem.

## Stage C — Reference Pack v0.1 surface test

Reference Pack v0.1 helped with two things:

- inspect all current class definitions;
- confirm that no current class is an honest causal match.

It also clearly states that exposed corpus cases are regression-only.

But v0.1 cannot surface the material Stage-B packet without broader repository
reconstruction.

It has no first-class representation for:

- an external observed failure with `NO_EXISTING_CLASS_MATCH`;
- the failure-analysis packet contract itself;
- boundary / opposite-error evidence as a packet field;
- historical source-state guidance for a newly analysed failure;
- post-hoc regression-conversion status;
- pass/fail regression criteria for the new external failure.

The repository-level method therefore delivered value that the release surface does not
currently expose.

## Disposition

# **NEEDLE_VALUE_PACK_GAP**

This means:

1. **repository-level Needle value was observed** on the precommitted external
   failure-analysis job;
2. the value is about packet structure/reuse, not discovering patent doctrine and not
   model superiority;
3. Reference Pack v0.1 cannot expose enough of that packet without returning to broader
   repository governance/evidence owners;
4. a future Reference Pack improvement hypothesis is now **earned for design review**;
5. this issue does not authorize v0.2 implementation.

## Limits

This is one mechanically selected public failure.

It does not establish:

- population-wide Needle value;
- superiority for all legal-AI failure analysis;
- generic legal-research companion value;
- product demand;
- a new trap class;
- fresh benchmark performance.

#214 remains unchanged.

#327 remains `BASELINE_SUFFICIENT` for its different generic post-answer legal-research
use.

## Next gate

Queued:

> **#341 — direction review after observed packet value + Reference Pack gap**

That gate should decide whether one direct positive use is enough to begin a bounded
Reference Pack v0.2 design/release investigation or whether an orthogonal replication
should come first.
