# Issue #329 — direction review after first real USE null

Date: 2026-09-26  
Selected mode: **DISCOVER — EXTERNAL PRECEDENT / ROLE TEST**  
Next WIP: **#331 — does external eval practice support Needle's regression-corpus role?**

## Trigger

#325 deliberately moved Needle from inward-facing corpus audits to **USE**.

#327 then ran the first real post-release use test under a precommitted design:

- one mechanically selected current EU legal-information task;
- strongest ordinary official-source research first;
- Stage A frozen before any Needle consultation;
- Reference Pack v0.1 used only afterward;
- no second/friendlier task allowed.

Result:

> **BASELINE_SUFFICIENT**

The pack added only analogy/terminology on that task and no non-duplicative source,
state, reconstruction, provenance or inspection value.

That null is binding for the tested task and may not be replaced.

## What the null changes

One real-use null is **not** enough to conclude:

- the Reference Pack has no use generally;
- the corpus has no regression/reference value;
- every strong ordinary research record makes Needle redundant.

But it is enough to change immediate allocation.

Running a second nearby USE task now would weaken the original no-friendlier-task safeguard.
A multi-task use programme could be scientifically designed later, but #327 did not
pre-register one and its null should be allowed to stand before any new sampling campaign.

The correct question is therefore no longer:

> can we find a task where the pack helps?

It is:

> what externally recognised job, if any, is an exposed known-failure corpus actually
> supposed to perform?

## External scan

A bounded orientation scan found two mature adjacent practice families.

### Public legal-AI benchmarks

Examples include:

- LegalBench — an open collaborative benchmark of legal-reasoning tasks:
  https://hazyresearch.stanford.edu/legalbench/
- LawBench — a public multi-task legal LLM benchmark:
  https://aclanthology.org/2024.emnlp-main.452/
- Korean Canonical Legal Benchmark — a recent benchmark with supporting precedents and
  instance-level rubrics:
  https://aclanthology.org/2026.eacl-short.17/
- DELTA / Legal Benchmarks — practitioner-grade realistic legal-research evaluation:
  https://www.legalbenchmarks.ai/research

These surfaces are primarily designed to **evaluate/compare capability** under a defined
task/evaluation contract.

### General LLM regression/eval engineering

Mature eval tooling explicitly supports reusable test datasets across model/prompt/code
changes.

Examples:

- OpenAI Evals supports repeatable eval definitions over datasets and different model /
  parameter configurations:
  https://platform.openai.com/docs/api-reference/evals
- Langfuse datasets can be built from production traces where the application performed
  poorly, paired with expected outputs, then reused in experiments:
  https://langfuse.com/docs/evaluation/experiments/datasets
- Langfuse's evaluation loop explicitly feeds production edge cases back into datasets so
  future experiments catch them:
  https://langfuse.com/docs/evaluation/core-concepts
- Langfuse also documents CI regression gates over reusable datasets:
  https://langfuse.com/docs/evaluation/overview

This second practice family is much closer to Needle's **known-failure regression**
language than public legal capability benchmarks are.

## The unresolved bridge

The scan does **not** yet prove that Needle maps cleanly to mature regression practice.

#311 already established an important mismatch:

- all 81 Needle cases are useful exposed regression/reference **material**;
- only the 10 EVALUATION cases clearly share runnable task + expected/grading contracts;
- 71 DERIVATION cases have heterogeneous evidence owners and no uniform executable oracle;
- post-hoc synthesis must not be misrepresented as historical experimental design.

External regression engineering often expects a concrete test item with:

- input/task;
- expected behavior/outcome;
- evaluator/pass condition;
- versioning;
- provenance.

Needle has strong provenance/exposure semantics, but uneven execution contracts.

That gap is now more decision-relevant than another internal class audit.

## Mode comparison

### DISCOVER — selected

A bounded externally anchored role test can change Needle's public identity and future
allocation.

Possible results include:

- external practice supports "regression/reference corpus" as written;
- only a subset qualifies as regression tests and the public identity should narrow;
- the corpus is best understood as a known-failure reference/fixture catalog;
- no meaningful external role distinction survives.

This is a real discriminating question and uses evidence outside Needle's own issue graph.

### CONSOLIDATE — not selected

#327 does not create a present governance contradiction.

The current repository already says:

- the pack does not prove workflow/model superiority;
- it is a reference/navigation layer;
- all cases are exposed/regression-only;
- only a subset has executable contracts.

There is nothing yet to consolidate until #331 resolves whether the role terminology itself
should change.

### USE — not selected now

A second immediate use task would risk looking like post-null result-seeking.

That does not permanently close USE. A future predeclared orthogonal sample or repeated-use
programme could be justified by a distinct hypothesis.

But the next unit of effort should first clarify what job repeated use would even be
testing.

### REVIEW / RELEASE — not selected

No release defect was discovered in #327.

The pack behaved correctly: it made conservative reference analogies and did not generate a
false legal claim.

A v0.2 before the role question is resolved would risk packaging terminology rather than
learning.

### MAINTAIN — not selected

No concrete correctness, integrity, security or cost trigger emerged from #327.

## Why external role research has higher value now

Needle has already established three different facts that must not be collapsed:

1. **#214:** corpus/index treatment showed no latent diagnostic/correctness advantage.
2. **#327:** one real post-answer use task showed no additional supported pack value.
3. **#311:** the corpus is not a uniform executable regression suite.

At the same time, external AI engineering clearly uses known/observed failures as reusable
regression datasets.

The project therefore needs to answer whether its current surviving asset genuinely belongs
to that external practice family, and under what exact contract.

This can make the project smaller.

If executable task/oracle/evaluator semantics are essential, Needle may need to narrow the
81-case identity rather than expanding implementation.

## Decision

# **SELECT DISCOVER — EXTERNAL PRECEDENT / ROLE TEST**

Next WIP:

> **#331 — does external eval practice support Needle's regression-corpus role?**

#331 must compare legal capability benchmarks with production-style regression/eval
practice and apply those external contracts back to Needle's actual 81-case structure.

It must not:

- infer product demand from analogy;
- build an eval harness;
- synthesize historical tasks/oracles;
- add cases/classes;
- reinterpret #214;
- retry #327.

The next question is deliberately outside Needle's taxonomy:

> **what kind of artifact is Needle, in terms that established external practice would
> actually recognise?**

No corpus, taxonomy, Reference Pack byte or product surface changes in #329.
