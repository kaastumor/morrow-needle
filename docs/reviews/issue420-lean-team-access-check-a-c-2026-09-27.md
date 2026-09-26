# Issue #420 — Lean-team access check for Candidates A and C

Date: 2026-09-27

Purpose:

> close the asymmetry identified by the sponsor after #418: Candidate B received a detailed target-segment access test, while A and C had only partially received the same lower-overhead / smaller-team baseline treatment.

This is a **public-access correction**, not a reopening of A or C deep work.

## Result

### Candidate A

Disposition:

> **LEAN_TEAM_RESIDUAL_PLAUSIBLE_BUT_EXTERNAL**

The low-access baseline is stronger than an "enterprise eval stack" comparator.

A capable small legal-AI/evaluation team can already obtain, cheaply or freely:

- public legal-evaluation task/rubric examples through DELTA;
- public evaluation frameworks and pilot scorecards from Legal Benchmarks;
- generic datasets, experiments, scoring and regression workflows through low-cost/free tools such as Langfuse, LangSmith and Promptfoo;
- ordinary Git/version control, issue tracking, spreadsheets/notes and capable general-purpose models.

Relevant public sources inspected:

- https://github.com/legalbenchmarks/delta
- https://www.legalbenchmarks.ai/methodology
- https://www.legalbenchmarks.ai/research/evaluation-framework
- https://langfuse.com/pricing
- https://www.langchain.com/pricing
- https://www.promptfoo.dev/pricing/

Therefore Candidate A gets **zero value credit** for:

- owning an evaluation dataset;
- storing criteria;
- running experiments;
- comparing versions;
- basic versioning/change logs;
- generic human-review workflow;
- generic CI/regression infrastructure.

What remains after this subtraction is narrower:

> **maintenance-decision semantics around a score-bearing legal/evaluation change**

Specifically:

- what changed in the evaluation contract;
- what evidence/time owns the change;
- which score-bearing criteria/results are affected;
- whether old outputs remain comparable;
- whether they can be rejudged or require reruns;
- what adjudication state remains.

Public/open tooling does not establish that small teams lack this discipline.

It also does not establish that the Maintenance Delta reduces enough expert/reopening burden to matter.

That question is owned by a real maintainer's existing process.

Promotion trigger remains:

> one real evaluation owner + one real maintenance event + the owner's actual incumbent process and acceptance decision.

### Candidate C

Disposition:

> **LEAN_TEAM_RESIDUAL_PLAUSIBLE_BUT_EXTERNAL**

The small-team generic regression baseline is also strong.

Public low-cost/open tooling supports:

- production trace capture;
- converting traces into datasets;
- expected-output storage;
- repeatable experiments;
- side-by-side comparisons;
- regression thresholds;
- CI/CD release gates;
- self-hosted or free entry tiers.

Relevant public sources inspected:

- https://langfuse.com/docs/evaluation/experiments/datasets
- https://langfuse.com/docs/evaluation/experiments/experiments-ci-cd
- https://langfuse.com/pricing-self-host
- https://www.promptfoo.dev/pricing/
- https://www.langchain.com/pricing

Therefore Candidate C gets **zero value credit** for generic:

- incident-to-test plumbing;
- datasets;
- regression runners;
- CI integration;
- experiment/version comparison.

The residual is specifically:

> **legal failure -> safe maintained legal oracle/regression conversion**

That work includes:

- identifying what legally failed;
- selecting the authoritative evidence owner;
- resolving governing legal/evaluation time;
- preserving professionally valid alternatives;
- defining the opposite error that must still fail;
- deciding whether the incident changes an answer, criterion, acceptance boundary or result interpretation;
- deciding historical comparability / rejudge / rerun action;
- preserving unresolved legal disagreement rather than inventing certainty.

Strong mature legal-evaluation practice already performs much of this work. Legal Benchmarks publicly documents lawyer-authored criteria, professionally defensible alternatives and qualified-lawyer adjudication for pass-changing disagreement:

- https://www.legalbenchmarks.ai/methodology

So Candidate C cannot claim that legal-oracle discipline is absent from mature incumbent practice.

The remaining smaller-team question is whether a lean legal-AI team can **practically perform this conversion reliably and proportionately** when a real failure occurs.

Public product documentation does not establish that gap or Needle's value within it.

Promotion trigger remains:

> one real legal-AI incident owner + the team's actual postmortem/regression process + external acceptance of the resulting maintained oracle.

## Sponsor question answered

Were A and C checked on "lower requirements for value" for smaller teams?

> **After #420: yes, at the public capability/access level.**

The correction is important:

- neither A nor C may use "enterprise tooling exists" as a reason to dismiss smaller-team value;
- neither may use "small teams lack enterprise tooling" as a shortcut to value either;
- cheap/open generic tooling now receives full credit;
- the surviving residuals are domain/process semantics, not infrastructure.

## Relationship to Candidate B

This correction does not change #418's external-evidence frontier.

A and C remain live, not rejected.

It does restore symmetry before Candidate B resumes as the sponsor-selected active lane.

No product build, outreach, corpus growth, schema growth or license change is earned by this review.
