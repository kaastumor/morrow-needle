# Issue #335 — residual value of a provenance-rich legal known-failure corpus

Date: 2026-09-26  
Disposition: **REVISE_REFERENCE_CONTRACT**

## Question

For a researcher/evaluator who wants to understand and preserve consequential legal-AI /
legal-research failure modes, does Needle's provenance-rich known-failure reference corpus
provide a concrete residual job beyond the strongest boring combination of:

- public legal capability/research benchmarks;
- legal-AI hallucination/error studies and datasets;
- general AI incident/failure memory;
- competent source-linked project postmortems?

If no residual survives, Needle should narrow to a project archive + case-specific
regression fixtures.

## Fixed source sample

The sample was recorded before substantive comparison.

### Legal benchmark / evaluation practice

1. **LegalBench**
   - https://hazyresearch.stanford.edu/legalbench/
   - https://hazyresearch.stanford.edu/legalbench/tasks/

2. **DELTA**
   - https://www.legalbenchmarks.ai/research/delta
   - https://www.legalbenchmarks.ai/research/delta-dutch-legal-research-benchmark

3. **Korean Canonical Legal Benchmark (KCL)**
   - https://aclanthology.org/2026.eacl-short.17/

### Primary legal-AI failure / hallucination studies

4. **Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models**
   - DOI: 10.1093/jla/laae003
   - https://arxiv.org/abs/2401.01301
   - dataset:
     https://huggingface.co/datasets/reglab/legal_hallucinations

5. **Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools**
   - DOI: 10.1111/jels.12413
   - https://arxiv.org/abs/2405.20362
   - dataset:
     https://huggingface.co/datasets/reglab/legal_rag_hallucinations

### General AI incident / failure memory

6. **AI Incident Database (AIID)**
   - https://incidentdatabase.ai/
   - snapshots: https://incidentdatabase.ai/research/snapshots
   - founding paper: https://arxiv.org/abs/2011.08512

### Strong boring project baseline

7. **Competent source-linked postmortem / issue record**
   - observed/questioned failure;
   - decisive sources;
   - target date/version;
   - consequence;
   - corrective rule;
   - links.

No additional source was added to seek a favorable result.

## What the substitutes already do well

### LegalBench / KCL / DELTA — stronger capability/evaluation contract

LegalBench provides legal-reasoning tasks as datasets of input-output pairs, with prompts
and evaluation code for ordinary tasks and manual gradebooks for open-generation tasks.

KCL pairs legal questions with supporting precedents and, for its essay component,
instance-level rubrics plus released evaluation code.

DELTA uses real Dutch legal-research questions, common execution conditions and explicit
substance/citation/form criteria.

These artifacts are stronger than Needle for:

- capability measurement;
- repeatable task execution;
- model comparison;
- scoring;
- benchmark-style interpretation.

They are not primarily histories of an already understood failure.

### Large Legal Fictions — stronger empirical hallucination measurement

The released dataset preserves, at row level:

- exact query;
- model;
- model output;
- example correct answer;
- hallucination/correctness signal;
- task type;
- court/case citation;
- year;
- source dataset.

The companion code supports replication of the evaluation pipeline.

This is an excellent evaluation/failure-characterization artifact.

Its primary job is to measure hallucination behavior across a sampled task population and
develop a typology. It does not generally package each failed row as a legal-state
postmortem with a separate decisive primary-source chain, source-version history, explicit
near-boundary control and contamination/exposure history.

### Hallucination-Free? — stronger tool-vulnerability evaluation

The study preregisters real-life legal research queries and evaluates outputs from several
legal AI products.

The public dataset preserves:

- question ID/category;
- exact question;
- tool/model;
- complete response;
- correctness label;
- groundedness label;
- final hallucination classification.

The paper's groundedness rubric distinguishes:

- grounded;
- ungrounded;
- misgrounded;
- fabricated authority.

The study therefore preserves much more than a simple accuracy label and directly analyzes
citation/source fidelity.

Again, the primary contract is **evaluation and error characterization**. The public row
schema does not generally turn each observed failure into a domain-specific legal-state
reconstruction packet with explicit source-state history and family boundary evidence.

### AI Incident Database — strongest reference-corpus substitute

AIID materially defeats any claim that Needle is valuable merely because it:

- records failures;
- assigns stable IDs;
- aggregates multiple source reports;
- classifies failures;
- preserves dates;
- is searchable;
- keeps public citations;
- provides point-in-time snapshots.

AIID's explicit mission is collective memory of real-world AI harms/near harms so repeated
bad outcomes can be avoided.

This is directly analogous to the broad "learn from known failures" purpose.

Therefore:

> **failure memory + provenance + searchable taxonomy is not by itself a Needle residual.**

### Ordinary source-linked postmortem — strongest single-case substitute

A competent project postmortem can preserve one Needle-like case losslessly if it records:

- the exact failure/question;
- decisive primary/official evidence;
- target date/version;
- consequence;
- why the incorrect conclusion arose;
- corrective rule;
- durable links.

Needle cannot justify itself by claiming that one of its cases is reconstructable.

## What Needle actually adds

The residual does not live in any one field.

It lives in a **standardized domain-specific failure-analysis contract across cases**.

At repository level, an accepted Needle case/family can preserve:

1. **the consequential legal-information distinction**
   - the exact state/source/effect distinction whose collapse would produce the error;

2. **authoritative evidence ownership**
   - links to the source/fixture/audit chain that establishes the distinction;

3. **historical/source-state context**
   - where relevant, the target time, source representation, legal status or version that
     must not be replaced by today's state;

4. **derivation/evaluation/exposure provenance**
   - whether the case discovered a mechanism or tested one;
   - whether it was sealed/evaluated;
   - whether it is now exposed / regression-only;

5. **boundary / negative evidence**
   - accepted evidence about where the failure family stops, often in the owning research
     record rather than the pack schema;

6. **cross-case failure-family organization**
   - stable grouping around a causal representation error rather than only subject matter,
     legal doctrine or model-error label;

7. **a safe conversion path into regression engineering**
   - when an executable contract already exists or is deliberately derived later, the
     exposure/scientific status is preserved rather than conflated with fresh validation.

No fixed incumbent in the sample losslessly supplies that whole contract.

## Why this is not a novelty claim

The components all have precedents:

- benchmarks preserve tasks/evaluation;
- hallucination studies preserve errors/outputs/labels;
- incident databases preserve real failures and source reports;
- postmortems preserve detailed individual failures;
- regression systems convert known failures into future tests.

Needle does not establish value by combining components nobody else combines.

The residual is narrower:

> **for legal failure analysis and evaluation/debugging work, the project preserves the
> exact legal-state failure mechanism and its evidence/boundary/exposure history in a
> reusable cross-case form.**

That is a different job from capability scoring, broad hallucination taxonomy or general
incident memory.

## Strongest attack — ordinary postmortems plus benchmark literature

Could a competent evaluator simply keep source-linked postmortems and use public benchmark
/error literature when needed?

For a single case: **yes**.

That is why the residual is not "better case notes".

What is lost without the corpus layer is the deliberately shared failure-analysis
structure:

- stable cross-case failure identities;
- consistent evidence/provenance/exposure semantics;
- explicit recognition that a case may be derivation rather than validation;
- reusable family boundaries;
- visibility of negative/parity evidence;
- controlled conversion into exposed regression fixtures.

A team could reproduce all of this in ordinary postmortems.

But once it does so consistently across failures, it has recreated the relevant part of
the reference-corpus contract.

This means Needle's residual is **structural and methodological**, not proprietary.

## Critical limitation — Reference Pack v0.1 is not the whole contract

Reference Pack v0.1 does not self-contain every property above.

It preserves:

- case identity;
- class membership;
- decisive trap;
- provenance/exposure;
- evidence-owner navigation;
- evaluation metadata where applicable.

Boundary/negative evidence and detailed source-state history often remain in repository
evidence owners.

Therefore:

> the **repository evidence estate** supports the full failure-analysis contract;
> Reference Pack v0.1 is only a compact navigation/reference layer into it.

Do not upgrade the pack into a self-contained failure-analysis dataset by wording alone.

## #327 consequence

#327 tested a different job:

> use the pack after ordinary legal research to see whether it adds material value to a
> current legal-information task.

It returned **BASELINE_SUFFICIENT**.

That result now helps define the external contract:

> Needle is **not demonstrated as a generic companion for ordinary legal research**.

The residual found here is aimed at:

- evaluators;
- debugging/failure analysis;
- benchmark/test designers;
- maintainers converting a known legal failure into a regression fixture;
- researchers studying failure mechanisms.

That is narrower than the project's earlier general "researcher/evaluator/developer"
orientation.

## Outcome

# **REVISE_REFERENCE_CONTRACT**

A residual survives, so Needle does **not** contract to a project archive.

But the externally meaningful job should be stated narrowly:

> **Needle is a provenance-rich legal failure-analysis reference corpus for understanding,
> challenging and reusing consequential legal-information failure mechanisms, with
> case-specific exposed regression fixtures and minimal evaluation discipline.**

Operationally:

- the corpus is primarily a **failure-analysis / evaluation-design / debugging reference**;
- it is not demonstrated as a generic research companion;
- it is not a capability benchmark;
- it is not an incident database of deployed harms;
- it is not a turnkey regression suite;
- Reference Pack v0.1 remains a navigation layer, not the full evidence bundle.

## What does not change

No change to:

- frozen corpus membership or taxonomy;
- Reference Pack v0.1 bytes;
- historical #88/#97 evaluations;
- #214 hard null;
- #327 bounded use null;
- #331 reference/fixture distinction;
- product status;
- model claims.

## Next gate

Queued:

> **#337 — direction review after reference-contract revision**

That gate should explicitly test whether the next highest-value move is a real **failure
analysis USE** against an independently observed external legal-AI failure, rather than
another generic legal-research use test.
