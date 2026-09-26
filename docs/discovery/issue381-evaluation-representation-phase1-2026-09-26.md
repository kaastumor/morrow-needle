# Issue #381 — Phase 1 evaluation-representation synthesis

Date: 2026-09-26  
Mode: **DISCOVER — LEGAL EVALUATION REPRESENTATION VALIDITY**

## Result

# **REPRESENTATION_CHOICE_MATTERS**

The external evidence does not support a universal winner between atomic rubrics,
comparative judgment, hierarchical issue structures and qualified holistic review.

It supports a narrower and more consequential conclusion:

> **evaluation representation is part of the measurement contract. A method can be reliable
> at the judgment it elicits while still be invalid for the decision the benchmark claims
> to support.**

Needle's current evaluation-integrity gate is therefore incomplete in one place: it checks
whether a criterion-based contract is coherent, but it does not first require the evaluator
to justify why **criterion-based decomposition is the right representation of quality for
the task/decision**.

No product, corpus or benchmark claim follows.

---

## 1. External evidence map

### Comparative judgment — JudgmentBench

JudgmentBench is unusually useful because the same practicing-lawyer population evaluated
the same 30 legal tasks under both:

- task-specific rubric scoring;
- pairwise comparative judgment.

Its initial construction-validity experiment reports much stronger recovery of the intended
three-level quality ordering under comparative judgment:

- mean task-level Spearman correlation: **0.908** comparative judgment;
- **0.150** rubric scoring;
- comparative judgment required less than half the annotation time.

This is strong evidence that, on these judgment-rich legal work products, holistic relative
comparison can preserve quality differences that atomised criteria fail to recover.

But JudgmentBench itself supplies the strongest red team against overgeneralisation:

- the target is recovery of a **constructed quality ordering**, not release/pass-fail safety;
- quality levels were induced through prompts along six intended dimensions;
- pairwise judgments aggregate into rankings/latent utilities and are harder to decompose
  into reusable failure criteria or audit after aggregation;
- rubrics provide transparency, consistency and a documented basis for each score;
- no methodology-independent ground truth exists for open-ended expert legal quality.

Therefore the supported inference is:

> **comparative judgment is strong evidence for holistic ranking validity, not evidence that
> it is the correct representation for every legal evaluation objective.**

Source:
https://arxiv.org/abs/2605.25240

### Atomic rubrics — PLawBench and LexRubric

PLawBench uses 850 realistic legal-practice questions across consultation, case analysis and
document generation, with roughly 12,500 expert-designed rubric items.

Its explicit purpose is fine-grained assessment of:

- issue/fact identification;
- structured legal reasoning;
- legally coherent document generation.

LexRubric similarly uses 649 open-ended legal instances with 12,337 expert-written atomic
criteria across six dimensions, explicitly treating **diagnostic localisation** as a core
benefit.

These benchmarks provide positive evidence that atomised criteria can be useful when the
measurement objective is:

> **where, specifically, did the legal work fail?**

They do not independently prove that the sum of those criteria is the best construct for
holistic professional quality.

Sources:
- https://aclanthology.org/2026.acl-long.458/
- https://arxiv.org/abs/2606.09389

### Hierarchical issue representation — LEGIT

LEGIT converts legal judgments into hierarchical issue trees containing opposing arguments
and court conclusions.

The representation separately evaluates:

- **issue coverage**;
- **correctness**.

Its results show those dimensions can move differently: the reported experiments find that
retrieval can improve overall reasoning/coverage while rubric-based RL improves correctness
with reduced coverage.

This is evidence that flattening legal reasoning into one undifferentiated score can hide an
important trade-off.

Source:
https://arxiv.org/abs/2512.01020

### Calibrated rubrics — CalibratedRubric

CalibratedRubric is especially important because it attacks a simplistic reading of
JudgmentBench.

Rather than treating all criteria as equally useful, it estimates rubric measurability and
selects compact task-adaptive rubric banks.

On JudgmentBench, its measurability filtering reports an improvement in human-gold agreement
from **kappa 0.604 to 0.743**.

It also reports that task-adaptive rubric selection can improve rank fidelity and reduce the
number of criteria needed in other open-ended evaluation settings.

This does not erase JudgmentBench's comparative-judgment result. It shows that:

> **"rubrics" are not one fixed representation; rubric selection/calibration itself is a
> measurement-design problem.**

Source:
https://arxiv.org/abs/2607.29252

### Commercial practice — Legal Benchmarks

Legal Benchmarks makes a deliberately different choice:

- fixed lawyer-authored binary substance criteria;
- criteria accommodate professionally defensible alternative approaches;
- task pass requires **every applicable substance criterion**;
- two independent attempts;
- judge disagreements capable of changing task pass are escalated to a qualified lawyer;
- form is kept separate from substance.

That architecture is well suited to a strict **minimum-acceptable-work / release-gate**
question.

It is not designed to answer:

> which of two already-acceptable pieces of legal work is better overall?

The benchmark's methodology therefore supports conditional representation choice rather
than a universal rubric thesis.

Source:
https://www.legalbenchmarks.ai/methodology

---

## 2. Representation-to-decision map

| Decision / measurement job | Representation with strongest conceptual fit | Primary strength | Primary failure mode |
| --- | --- | --- | --- |
| Is every mandatory legal requirement satisfied? | **Atomic conjunctive criteria** | auditable hard gates; localises exact omission | false rejection if acceptable alternatives are under-specified |
| Did one fatal legal error occur? | **Atomic fatal criterion / veto + human adjudication** | catastrophic error cannot be averaged away | requires reliable identification of truly fatal criteria |
| Where exactly did the work fail? | **Fine-grained atomic rubrics** | diagnostic localisation | decomposition may omit tacit/interactive quality |
| Which of two professionally plausible outputs is better overall? | **Comparative judgment** | preserves tacit/holistic judgment; lower elicitation burden in JudgmentBench | weak failure localisation; pairwise ranking does not itself define an absolute acceptance threshold |
| Did the analysis identify and correctly resolve the relevant legal issues? | **Hierarchical issue tree** | separates coverage from correctness; preserves issue dependency | constructing a defensible issue tree can itself be expert-intensive and contestable |
| Is the deliverable professionally acceptable for use? | **Qualified holistic adjudication + explicit veto checks** | maps directly to professional acceptance | hard to standardise/scale; judge variance and opaque rationale |
| Benchmark/release decision spanning several of the above | **Hybrid** | can preserve vetoes + diagnosis + holistic acceptability | more expensive; risks double-counting and incoherent aggregation |

No row means "always use this representation".

The mapping is a hypothesis about construct fit, not an empirically proven universal rule.

---

## 3. Task properties that should determine representation choice

### Property A — decomposability

If quality can be losslessly expressed as independently checkable requirements, atomic
criteria are natural.

Examples:

- required filing fields;
- mandatory propositions;
- fixed calculations;
- required citations;
- explicit legal conditions.

If quality emerges from interactions among framing, judgment, prioritisation, strategy and
persuasiveness, forced decomposition may lose signal.

### Property B — multiple defensible strategies

The more legitimate ways there are to produce a high-quality answer, the greater the risk
that an atomic answer key encodes one preferred route and falsely rejects another.

Comparative or qualified holistic judgment becomes more attractive, although critical legal
constraints may still require veto criteria.

### Property C — catastrophic single-error risk

Where one legal error makes an otherwise polished output unusable, a pure aggregate or
preference score is unsafe.

A representation needs an explicit non-compensatory check.

This is particularly aligned with Needle's known-failure/regression use.

### Property D — issue coverage

Where omission of an issue is itself consequential, a hierarchical issue structure may be
more informative than either:

- flat criteria with no dependency;
- holistic preference with no explicit coverage model.

### Property E — evaluation purpose

The same work product may legitimately need different representations for different
questions.

Example:

- **ranking:** which output is stronger overall?
- **release:** is either safe enough to use?
- **debugging:** which legal capability failed?
- **training:** which supervision signal best improves the system?
- **procurement:** does the product satisfy minimum requirements consistently?

A benchmark that does not state which question it answers cannot justify its representation.

---

## 4. Red team of JudgmentBench

The headline 0.908 vs 0.150 result is not enough to replace rubrics.

### Construction target

The experiment measures recovery of prompt-induced intended quality levels.

That is meaningful construction-validity evidence, but not a methodology-independent legal
truth standard.

### Relative versus absolute judgment

Pairwise comparison can reliably say:

> A is better than B.

It does not automatically answer:

> A is legally safe enough to release.

A collection of mutually poor answers can still be ranked.

### Fatal-error masking

An output may be holistically preferable while containing one legally fatal defect.

For a safety/release gate, that defect may properly dominate all stylistic, strategic and
completeness advantages.

### Auditability

JudgmentBench itself notes that pairwise-preference aggregates are harder to decompose and
audit than fixed criteria.

That matters strongly for Needle because Needle's surviving role includes regression and
failure preservation.

### Result

JudgmentBench strongly falsifies:

> **rubric decomposition can be presumed adequate for holistic expert legal quality.**

It does not falsify:

> **atomic criteria are appropriate for known-failure regression, mandatory legal
> requirements or fatal-error gates.**

---

## 5. Red team of rubric evidence

Rubric benchmarks also have a construct-validity problem.

Agreement with human rubric judgments can establish:

> the automated evaluator reproduces the rubric judgments.

It does not by itself establish:

> the rubric is a complete representation of professional legal quality.

Fine-grained criteria can produce very good **diagnostic validity** while remaining poor at
holistic ranking.

CalibratedRubric makes this distinction sharper rather than weaker:

- poor criteria can be filtered;
- useful criteria can be selected more efficiently;
- but better rubric measurability is still not proof that every latent professional quality
  dimension has been represented.

Therefore:

> **judge agreement, rubric reliability and construct validity must remain separate claims.**

---

## 6. Red team of Needle's current protocol

### Representation-agnostic rules that survive

The following principles remain valid regardless of whether evaluation uses rubrics,
preferences, issue trees or holistic adjudication:

- start with a claim that can lose;
- separate derivation from fresh validation;
- distinguish surfaced adjudication from latent detection;
- seal tasks/conditions before execution;
- use a strong comparator;
- score consequential behavior rather than aesthetics;
- predeclare outcome interpretation;
- stop rather than move goalposts;
- preserve exposure/reuse status;
- preserve legal/source time;
- pin model/tool versions;
- define the evaluated-system boundary;
- preserve versioned audit records;
- distinguish subject variance from judge variance.

These are evaluation-governance rules rather than rubric rules.

### Rubric-specific assumptions in section 12

The current integrity gate contains several checks that are specifically criterion-oriented:

- "every decision-critical deliverable must affect at least one observable criterion";
- mutation tests framed as causing "something to fail";
- conditional-criterion activation/gradability;
- cross-criterion counts/denominators;
- proposition-level score-bearing evidence;
- repeated judging of fixed criterion decisions.

Those checks are useful when a rubric is the chosen representation, but cannot be treated as
the complete evaluation-integrity gate for preference or holistic evaluation.

### Missing upstream question

Before section 12 currently asks whether the evaluation contract is coherent, the protocol
needs a prior declaration:

> **What decision is this evaluation intended to support, and why is the chosen
> representation valid for that decision?**

Without that declaration, a benchmark can be internally coherent yet measure the wrong
construct.

---

## 7. Minimal conceptual repair

Phase 1 earns a protocol clarification, not a new evaluation system.

Before criterion-level integrity checks, every consequential evaluation should declare:

1. **decision objective**
   - ranking;
   - minimum acceptance/release;
   - regression/failure detection;
   - diagnostic localisation;
   - issue coverage/correctness;
   - professional usefulness;
   - or another explicit objective;

2. **representation**
   - atomic rubric/checklist;
   - comparative judgment;
   - hierarchical issue structure;
   - qualified holistic adjudication;
   - hybrid;

3. **non-compensatory constraints**
   - whether any fatal criterion/error must veto an otherwise strong output;

4. **valid-alternative policy**
   - whether multiple professionally defensible strategies are expected and how the
     representation avoids false rejection;

5. **aggregation semantics**
   - what a total score, preference ordering or pass/fail actually means;
   - which dimensions may and may not compensate for one another.

Only then should the representation-specific integrity checks apply.

---

## 8. Is a new empirical experiment earned?

**Yes, but not autonomously with model self-grading.**

A meaningful discriminating experiment needs a methodology-independent-enough professional
reference judgment.

The strongest design is a **paired representation challenge** on the same frozen legal work
products, with two deliberately different task families:

### Family A — fatal-error / conjunctive task

Construct or select work where:

- most of the output can be professionally strong;
- one source-backed legal defect makes the deliverable unacceptable.

Prediction:

- criterion/veto evaluation should preserve the fatal error;
- unconstrained holistic comparison may prefer the polished defective output over a less
  polished safe output.

### Family B — multiple-defensible-strategies task

Construct or select work where:

- two materially different legal strategies are both professionally acceptable;
- an answer key/rubric risks encoding one strategy too narrowly.

Prediction:

- overly narrow atomic evaluation may falsely reject one acceptable response;
- comparative/holistic qualified judgment should recognise both.

### Required adjudication

The ground reference must come from qualified legal evaluators who:

- see the work products without knowing which representation will be tested;
- independently decide acceptability and/or fatal defect status;
- preserve disagreement;
- do not derive the ground decision from the rubric being evaluated.

Without such adjudication, the experiment would be circular.

This means the **experimental execution itself is externally gated**, even though the
scientific question is well formed.

---

## Phase 1 disposition

# **REPRESENTATION_CHOICE_MATTERS**

What is supported:

> legal-evaluation representations preserve different kinds of signal and fail differently;
> representation choice must be justified against the evaluation decision.

What is not supported:

- comparative judgment is globally better than rubrics;
- rubrics are invalid for legal AI;
- atomic criteria can measure all dimensions of professional legal quality;
- pairwise preference is safe for release gating;
- issue trees are universally superior;
- Needle has a proprietary evaluation method.

## Recommended project action

Adopt the minimal representation-declaration repair in the canonical evaluation protocol.

Then treat a true paired representation comparison as **external-adjudication dependent**,
not something the project should self-grade into existence.

No product build or corpus change is earned.
