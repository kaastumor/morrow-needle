# Issue #375 — pre-partner external-reality honing checkpoint

Date: 2026-09-26  
Mode: **DISCOVER — EXTERNAL REALITY / PRE-PARTNER HONING**

## Sponsor decision

The sponsor explicitly deferred direct partner outreach.

The project should first become more externally credible by using **public external workloads,
benchmark contracts and maintenance failures as surrogate reality**, without allowing Needle
to choose its own favorable cases.

This supersedes the previously selected immediate pilot-partner acquisition step. It does
not invalidate #375's finding that vendor-side independent evaluation is a real commercial
job.

## Binding state

Preserve:

- #214 hard null for corpus-assisted latent diagnostic/correctness advantage;
- #327 generic companion-use null;
- #339/#353 bounded positives;
- #349/#362 strong-baseline nulls;
- #364 anti-rescue rule;
- #366 smaller identity primary;
- #373 commercial job exists, Needle-specific value unproven;
- frozen corpus: **81 cases / 26 classes**;
- Reference Pack v0.2 remains frozen/current;
- licensing remains **INSPECTABLE_ONLY_FOR_NOW**.

No partner outreach, corpus growth, v0.3, product implementation or structured external
failure database is authorised by this checkpoint.

---

## External benchmark baseline is stronger than Needle should assume

### DELTA

The public Dutch Legal AI Benchmark (DELTA) currently exposes:

- 15 Dutch legal-research tasks;
- 273 binary criteria in v1.1.0;
- lawyer validation;
- explicit `law_as_of` cut-offs;
- controlling-authority citation criteria;
- support for multiple professionally defensible approaches;
- blind grading;
- criterion disputes;
- semantic versioning when task/criterion content changes.

Sources:

- https://github.com/legalbenchmarks/delta
- https://www.legalbenchmarks.ai/methodology
- https://www.legalbenchmarks.ai/research/delta-dutch-legal-research-benchmark

Conclusion:

> source citation, legal cut-offs, binary PASS/FAIL, lawyer review, explicit grading criteria
> and ordinary versioning are **strong-incumbent practice**, not Needle differentiation.

### Harvey LAB

Harvey LAB currently exposes:

- long-horizon client-matter-style tasks;
- expert-written atomic rubrics;
- all-pass grading;
- public task/harness/evaluation infrastructure;
- task contribution and rubric-quality guidance;
- ongoing task/rubric evolution.

Sources:

- https://github.com/harveyai/harvey-labs
- https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark

Conclusion:

> realistic work-product evaluation, granular rubrics and benchmark infrastructure are also
> strong-incumbent practice.

---

## Coverage reality

The 15 public DELTA tasks are primarily Dutch national-law research assignments with a
single fixed research cut-off.

They do not visibly exercise most of Needle's 26 EU legal-state mechanisms, including many
of:

- cross-order incorporation;
- differentiated Member-State participation;
- Directive invocability;
- EU primacy/disapplication;
- sub-state territorial regimes;
- Union-nexus applicability;
- procedural silence;
- procedural-clock suspension;
- dynamic external-reference status;
- machine compliance artifacts;
- authority handoffs;
- cross-border recognition activation;
- language/expression-local corrective state;
- sub-day temporal boundaries.

That absence is **not** evidence that Needle has found a market gap.

DELTA's public set has only 15 tasks and a declared Dutch-law scope. Private benchmark sets
are not observable. Harvey LAB covers a much broader task distribution.

Therefore:

> **benchmark non-coverage is a research lead, not a Needle advantage.**

The 26-class corpus should not be expanded or polished merely to maximize apparent distance
from public benchmarks.

---

## Real external evaluation-contract failures

The pre-partner review found concrete public benchmark defects despite otherwise strong
evaluation practices.

### Derivation case A — DELTA #1: criterion/source mismatch

Issue:
https://github.com/legalbenchmarks/delta/issues/1

A criterion attributed the legal function of Article 3:97(1) BW to Article 3:97(2).

Consequence:

- a legally correct answer could fail;
- a legally incorrect source attribution could pass.

Needle v0.2 already says PASS/FAIL should have an evidence owner, but it did not explicitly
require exact article/paragraph identity where that distinction changes the rule.

Earned gate:

> **criterion evidence correctness**

### Derivation case B — DELTA #2: legally true but vacuous criterion

Issue:
https://github.com/legalbenchmarks/delta/issues/2

A conditional criterion was substantively correct, but the prompt did not elicit its
trigger. Different judges therefore disagreed on how to score the inactive condition.

Earned gate:

> **activation and gradability**

A criterion must specify what happens when its condition does not fire.

### Derivation case C — Harvey LAB #147: rubric can all-pass without the requested answer

Issue:
https://github.com/harveyai/harvey-labs/issues/147

The task requested quantitative escrow benchmarking, calculations, sample sizes, source
documents and reasoning. The current criteria could all pass while those central outputs
were omitted.

Earned gate:

> **task-to-criterion coverage**

Where practical, delete a central requested element from an otherwise acceptable answer and
confirm the rubric fails.

### Derivation case D — Harvey LAB #146: internally inconsistent task contract

Issue:
https://github.com/harveyai/harvey-labs/issues/146

Seven task contracts contained fixed counts/rates that did not reconcile with precision
allowlists and population membership.

Earned gate:

> **cross-criterion consistency**

Shared counts, denominators, allowlists, required/optional/negative sets and thresholds must
reconcile.

### Derivation case E — Harvey LAB #145: infrastructure failure scored as subject failure

Issue:
https://github.com/harveyai/harvey-labs/issues/145

An unreadable deliverable caused by missing `pandoc` was converted into judge text and
received confident criterion FAILs rather than an evaluation error.

Earned gate:

> **execution validity before subject failure**

Harness/extraction/conversion failure must surface as `INVALID_RUN`, `UNSCORABLE` or
equivalent, not as a model failure.

### Maintenance case F — Harvey LAB #143: semantic task-contract drift

Issue:
https://github.com/harveyai/harvey-labs/issues/143

A rubric update changed effective input/target contracts across 250 tasks.

This is **not itself a defect**. It is evidence that legal-evaluation contracts can change
semantically and therefore supports a version-control rule:

> **semantic revision control**

Instructions, rubrics, answer keys and required deliverables are score-bearing task state
and must be pinned/reconciled when results are compared. The failure condition is undisclosed
or invalid comparison across changed contracts, not legitimate maintenance.

### Derivation case G — Harvey LAB #158: answer variance versus judge variance

Issue:
https://github.com/harveyai/harvey-labs/issues/158

Repeated runs showed substantial criterion-level PASS/FAIL flipping, while the observed
pipeline combined newly generated answers with newly generated judge decisions.

Earned gate:

> **stability decomposition**

When a small delta could drive a decision, freeze identical subject output and separate
judge variance from answer/system variance.

---

## Needle replay against those failures

Before this checkpoint, the canonical Needle evaluation protocol strongly covered:

- claim falsifiability;
- derivation versus validation;
- exposure;
- sealed inputs;
- comparator parity;
- consequential scoring;
- source drift;
- model/version distinction.

It only partially covered evaluation-contract integrity.

| External defect | Previous Needle discipline | Result |
| --- | --- | --- |
| wrong statutory paragraph | evidence-owner principle, but no explicit exact-criterion source check | **PARTIAL** |
| conditional criterion never activates | no explicit inactive-condition rule | **MISS** |
| rubric omits central requested work | no task-to-criterion coverage gate | **MISS** |
| criteria contradict one another | no explicit cross-criterion consistency gate | **MISS** |
| converter failure becomes subject FAIL | fail-closed principle exists generally, not explicit in evaluation protocol | **PARTIAL / MISS** |
| score-bearing task contract changes | model/source drift covered, rubric/instruction semantic drift not explicit | **PARTIAL** |
| answer/judge variance conflated | cross-judge ideas existed in external benchmarks, not canonical Needle rule | **MISS** |

Therefore the external-reality phase found a **real weakness in Needle itself**.

The appropriate honing target is not another legal trap class.

It is:

> **evaluation-contract integrity**

---

## Implemented repair

The canonical evaluation protocol now contains an explicit evaluation-contract integrity
gate compressed into five working groups:

1. contract adequacy, including both undercoverage and false rejection of valid answers;
2. evidence and temporal scope;
3. execution validity with an explicit evaluated-system boundary;
4. versioned audit record, including post-reveal preservation;
5. decision-sensitive uncertainty / stability decomposition.

The Way of Working now makes this a first-refusal gate before interpreting benchmark,
regression or comparative scores.

This is intentionally labelled **ordinary evaluation hygiene**.

It is not claimed as a Needle-specific advantage.

Reference Pack v0.2 remains unchanged.

---

## Post-gate applicability example

After writing the gate, Harvey LAB PR #135 was inspected:

> harveyai/harvey-labs #135 — `fix(tasks): align market-definition rubric with source matter`

Source:
https://github.com/harveyai/harvey-labs/pull/135

Its title already announces a rubric/source repair. It is therefore **defect-cued** and
cannot serve as an unbiased holdout, fresh-detection or false-alarm check.

It remains a useful applicability example. The substantive report showed:

- the rubric graded a different transaction from the packaged source corpus;
- unsupported people, dates, figures, documents and theories remained in criteria;
- source-data conflicts existed and could not safely be silently resolved;
- the repair required a criterion-to-source evidence matrix.

The new integrity gate would flag the documented repair through:

- **criterion evidence correctness**;
- **cross-criterion consistency**;
- and, where score-bearing task material changed, **semantic revision control**.

Disposition:

> **ILLUSTRATIVE_APPLICABILITY_ONLY — NOT A HOLDOUT**

This is one bounded public maintenance example. It supplies no unbiased detection-rate,
false-alarm or population-validation evidence.

---

## What should be honed next

The external evidence argues **against** polishing the 26-class taxonomy for its own sake.

The next pre-partner honing target should be Needle's own evaluation estate:

> apply the new integrity gate to a small, preselected set of Needle's strongest comparative
> evaluations and regression contracts.

The purpose is not to rerun those experiments.

It is to ask whether their task/criterion/evidence contracts satisfy the standard Needle now
expects from others.

Recommended bounded sample:

- #88 surfaced-trap suite;
- #214 latent corpus-assisted diagnostic pilot;
- #362 paired evaluator/oracle-maintenance falsifier.

Questions:

- does every central claimed outcome have explicit score coverage?
- are legal criteria pinned to the exact supporting authority/state?
- are conditional criteria gradable?
- do answer keys/criteria reconcile internally?
- can transport/harness failure be separated from subject failure?
- are task-contract revisions pinned?
- where relevant, is judge/system variance separable?

Any defect found should be repaired as evaluation provenance/contract hygiene without
changing the historical result unless the defect is genuinely result-material.

This is **honing**, not a new experiment.

---

## Current conclusion

The pre-partner external-reality phase has already earned one concrete improvement.

Needle should currently become better at:

> **knowing when an evaluation result itself is trustworthy**

rather than becoming larger, more taxonomic or more product-like.

The vendor-evaluation DELIVERY hypothesis remains downstream and unproven.

Partner outreach remains deferred until this internal evaluation-integrity audit is complete.
