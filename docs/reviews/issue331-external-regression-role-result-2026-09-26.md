# Issue #331 — external regression-role precedent test

Date: 2026-09-26  
Disposition: **NARROW_TO_REFERENCE_FIXTURES**

## Question

Does current external legal-AI / LLM-evaluation practice support a concrete role for an
**exposed, source-backed known-failure corpus** like Needle that is distinct from a public
capability benchmark, a generic reference catalog and fresh blind evaluation?

If so, does that evidence support calling the full 81-case Needle asset a
"regression/reference corpus", or should regression language attach only to cases/fixtures
that preserve an executable test contract?

## Internal facts held fixed

This review does not reinterpret Needle's scientific history.

From #311 and the frozen reference:

- 81 total exposed cases;
- 71 DERIVATION cases;
- 10 EVALUATION cases;
- all 81 preserve a stable failure mechanism, exposure state and evidence owner;
- the 10 EVALUATION cases clearly preserve historical runnable task + expected/grading
  contracts at repository level;
- derivation evidence owners are heterogeneous;
- Reference Pack v0.1 contains **0/81 self-contained executable regression tests by
  schema**;
- synthesizing new prompts/oracles for all 71 derivation cases would be post-hoc
  engineering, not recovery of the historical scientific design.

#214 remains a hard null for corpus-assisted latent diagnostic/correctness advantage.
#327 remains `BASELINE_SUFFICIENT` for its first mechanically selected real post-answer
Reference Pack use.

## Fixed external source sample

The source sample was recorded before the identity decision and was not expanded to seek a
preferred answer.

### Legal capability / benchmark practice

#### LegalBench

Primary project pages:

- https://hazyresearch.stanford.edu/legalbench/
- https://hazyresearch.stanford.edu/legalbench/tasks/

LegalBench is explicitly a benchmark for evaluating legal reasoning. Its tasks have
datasets of input-output pairs. Prompt templates and evaluation code are available for
ordinary tasks, while open-generation tasks have a manual gradebook.

Relevant contract:

> task input + desired output + prompt/evaluation method.

This is a capability/evaluation surface, not merely a catalog of interesting legal failure
descriptions.

#### Korean Canonical Legal Benchmark (KCL)

Primary paper:

- https://aclanthology.org/2026.eacl-short.17/

KCL combines:

- 283 multiple-choice questions;
- 1,103 aligned precedents;
- 169 open-ended essay questions;
- 550 aligned precedents;
- 2,739 instance-level rubrics;
- released benchmark data and evaluation code.

The important feature for #331 is not benchmark size. It is that supporting legal evidence
is paired with **questions and evaluation contracts**.

#### DELTA

Primary project/methodology:

- https://www.legalbenchmarks.ai/research/delta-dutch-legal-research-benchmark
- https://www.legalbenchmarks.ai/methodology

DELTA evaluates open-ended legal-research tasks under common execution conditions.

Each task is assessed against explicit legal/citation requirements, with separate form
assessment. A task passes only when its applicable requirements are satisfied.

Again, source grounding does not replace the executable evaluation contract. The benchmark
contains both.

### General LLM regression / eval engineering

#### OpenAI datasets/evaluation workflow

Current documentation:

- https://developers.openai.com/api/docs/guides/evaluation-getting-started

Datasets pair examples with persisted graders so prompt/model variants and added edge cases
can be run against the same evaluation criteria.

The exact product surface can evolve; the relevant practice is stable for this review:

> repeatable inputs plus an evaluator are used to compare changed systems.

#### Langfuse

Primary documentation:

- https://langfuse.com/docs/evaluation/overview
- https://langfuse.com/docs/evaluation/experiments/datasets
- https://langfuse.com/docs/evaluation/core-concepts

Langfuse explicitly describes evaluation as a repeatable check that catches regressions.

Its dataset model uses test inputs and expected outputs. Experiments run the application on
those items and score the outputs with evaluators.

Most importantly for Needle, Langfuse documents a common workflow in which teams:

1. select real production traces where the application did not behave as expected;
2. add an expert expected output;
3. put the failure into a reusable dataset;
4. run later application/model/prompt versions on that same item;
5. feed newly discovered edge cases back into the dataset so future experiments catch
   them.

That is strong external evidence that **known and exposed failures are entirely legitimate
regression inputs**.

Exposure is not the problem.

The executable contract is the boundary.

## Five distinct jobs

### 1. Capability benchmarking

Purpose:

> compare systems on a defined task population/collection using explicit scoring.

Typical contract:

- task/input;
- target/criteria;
- evaluation procedure;
- aggregate interpretation.

LegalBench, KCL and DELTA are examples.

Needle's full 81-case corpus is not a representative capability benchmark and must not be
described as one.

### 2. Fresh evaluation

Purpose:

> test a new claim on evidence/tasks not selected after the result is known.

Needle's sealed historical #88/#97 evaluations belong here for their original claims.

After reveal, those cases no longer provide fresh blind evidence.

### 3. Production regression testing

Purpose:

> check that a previously understood failure does not recur when the system changes.

Exposure is expected rather than disqualifying.

The normal contract is:

- runnable input/task;
- expected output/behavior or explicit criterion;
- evaluator/pass condition;
- repeatable execution against a changed model/prompt/application;
- useful version/provenance metadata.

This is the strongest external match for Needle's historical use of "regression".

### 4. Reference/debugging material

Purpose:

> preserve what went wrong, why it mattered and where the supporting evidence lives.

This can be highly valuable without being directly executable.

A failure description plus decisive evidence can help a researcher/debugger recognize,
explain or reconstruct a known problem. It does not become a regression test until an
execution contract exists.

### 5. Incident/failure memory

Purpose:

> keep observed failures so they can inform future analysis and, where useful, be converted
> into tests.

External regression workflows often begin here. The conversion step to a dataset item +
expected result/evaluator is explicit.

This is the closest conceptual description of many Needle DERIVATION cases.

## Applying the external contract to Needle

### All 81 cases

All 81 clearly qualify as:

> **source-backed known-failure reference material**

Each preserves:

- stable identity;
- a consequential failure mechanism;
- provenance/exposure state;
- evidence owner.

That is a coherent external-facing asset.

### Ten EVALUATION cases

The revealed #88/#97 cases preserve:

- exact runnable prompts/tasks;
- expected conclusions/answer keys;
- grading/pass rules;
- execution/result provenance.

They clearly qualify as:

> **exposed executable regression cases**

They may be rerun to detect recurrence of an already known failure.

They do not regain fresh-blind status.

### Seventy-one DERIVATION cases

The derivation set is heterogeneous.

Some owners contain sufficiently structured fixtures that an implementation-specific
regression can be run.

Many preserve only:

- research question;
- decisive trap;
- legal evidence;
- boundaries;
- accepted result.

Those are excellent failure/reference records, but external regression practice does not
support calling a description of a known failure a runnable regression test merely because
one could later construct a test from it.

### Metamorphic layer

The four post-hoc metamorphic relations are genuine derived regression engineering because
they explicitly preserve:

- controlled input/state mutation;
- evidence-backed expected relation;
- repeatable property to check.

They are correctly labelled as post-hoc and add no new scientific validation.

They strengthen the claim that Needle contains regression **fixtures/artifacts**.

They do not convert all 81 cases into one executable regression corpus.

## Why #311's wording is now too broad

#311 was internally careful:

> regression/reference corpus means exposed failure cases suitable for known-case
> regression and reference use, not a uniform executable suite.

That was a defensible project-local definition.

The external comparison adds a stronger semantic baseline.

Across the fixed sample, "regression" is operationally tied to rerunning a changed system
against a test item whose expected behavior can be evaluated.

The external evidence therefore supports:

> known failures are valid regression **sources**;

but not:

> every preserved known-failure record is itself a regression **test**.

Keeping "regression/reference corpus" as the primary 81-case identity makes an external
reader do too much reinterpretation of the word "regression".

## Narrowest accurate identity

Use:

> **adversarial legal-research known-failure reference corpus + exposed regression
> fixtures + minimal evaluation discipline**

Interpretation:

- **known-failure reference corpus** describes the 81-case whole;
- **exposed regression fixtures/cases** describes only evidence owners that preserve a
  runnable expected check;
- **minimal evaluation discipline** remains available for genuinely new comparative claims.

This keeps the externally supported regression role without stretching it over the entire
corpus.

## What does not change

This terminology repair does not change:

- corpus membership;
- the 26-class taxonomy;
- provenance roles;
- exposure state;
- Reference Pack v0.1 bytes;
- historical evaluation results;
- the four metamorphic relations;
- #214;
- #327.

Reference Pack v0.1 remains a valid frozen historical release. Its own README already says
it is a derived reference layer and not a complete legal benchmark. Do not rewrite its
frozen bytes merely to update current project terminology.

## Disposition

# **NARROW_TO_REFERENCE_FIXTURES**

External practice supports Needle's underlying intuition that observed failures should be
remembered and reused.

It does **not** support attaching "regression corpus" uniformly to 81 heterogeneous records
when most do not preserve a runnable input + expected/evaluator contract.

Durable rule:

> **Reference status is corpus-wide. Regression status is case/fixture-specific.**

The project should therefore present the 81-case whole as a **known-failure reference
corpus** and reserve **executable regression** for the revealed evaluation contracts and
other specifically structured fixtures.

No harness, new case/class, product surface or fresh performance claim follows.
