# Issue #359 — direction review after conditional-use consolidation

Date: 2026-09-26  
Disposition: **SELECT DISCOVER — EXTERNAL JOB / CONSUMER EVIDENCE**

## Decision

The highest-value next mode is **DISCOVER**.

The next bounded WIP is:

> **#361 RUN-02 — external evaluator/maintainer job evidence**

The question is no longer whether Needle can make a richer failure-analysis packet. The
project already has bounded evidence for that in #339 and #353, plus the important #349
null.

The unresolved question is whether that demonstrated conditional contribution maps to a
real external job that recurs outside Needle's own evaluation chain.

## Wide-angle check: the recent chain is becoming packet-centric

The sequence #339 -> v0.2 -> #349 -> #353 -> #357 was productive:

- #339 found material reusable structure beyond a strong postmortem;
- v0.2 removed repository-navigation burden;
- #349 showed that simple failures do not deserve ceremonial packet work;
- #353 supported a conditional value boundary on an authority-relationship failure;
- #357 compressed those results into a strong-postmortem-first use rule.

But another packet-boundary experiment now has declining information value.

The project knows substantially more about **when its artifact can add structure** than
about **who repeatedly needs that structure, what they do today, and whether the residual
burden matters enough to change behavior**.

That is now the larger uncertainty.

## Mode comparison

### DISCOVER — selected

External job/consumer discovery can answer the missing project-level question:

> Is there a concrete evaluator/maintainer job where preserving legal failure mechanism,
> evidence lineage, reuse/exposure state, consequential boundaries and safe regression
> conversion materially improves the strongest existing workflow?

The evidence target must be actual work and recurring burden, not merely the existence of
benchmarks, papers, evaluation products or competitors.

The strongest baseline must be allowed to combine:
- a competent source-linked postmortem;
- ordinary issue/QA tracking;
- mature evaluation/benchmark tooling;
- runnable regression cases and evaluators;
- direct legal-source review.

Competitor existence is a baseline, not a veto. Novelty is not required.

### USE — not selected now

A falsifier of the #357 conditional rule remains scientifically legitimate, but it would
mostly refine a boundary already adequate for current allocation.

It would not answer whether anyone outside the project's own tests has a repeated job for
the packet.

USE becomes higher-value after a concrete external job survives discovery and incumbent
attack, because the use can then test that job rather than another internally framed
packet case.

### REVIEW / RELEASE — not selected

Reference Pack v0.2 has already demonstrated successful navigation in #349 and #353.

No repeated external-use burden currently justifies:
- v0.3;
- another navigation layer;
- a structured external-failure store;
- software/workflow expansion.

Release work before job evidence would turn an artifact into its own demand signal.

### CONSOLIDATE — not selected

#357 just reconciled the durable use contract across README, charter and Way of Working.

No unresolved owner conflict is large enough to dominate the external-value uncertainty.

Further consolidation now would be audit-of-audit recursion.

### MAINTAIN — not selected

No concrete correctness, evidence-integrity, security, cost or operability trigger
currently outranks the value question.

## Competing identities

Three plausible identities remain:

1. **incumbent:** known-failure reference corpus + exposed regression fixtures + minimal
   evaluation discipline, with conditional failure-analysis use;
2. **smaller:** frozen reference corpus + evidence pointers only, where ordinary external
   QA/postmortem tooling owns failure maintenance;
3. **adjacent:** a compact evaluator/maintainer reference discipline that helps convert
   legally non-trivial known failures into safe, inspectable regression assets.

Current evidence does not justify choosing identity 3 merely because #339/#353 were
positive. External job evidence is the discriminating next question.

## Bounded next WIP

#361 RUN-02 must investigate one externally grounded evaluator/maintainer job.

It should identify:
- actor;
- trigger;
- repeated job-to-be-done;
- strongest current baseline;
- observed burden in that baseline;
- residual Needle contribution, if any.

It must not infer demand from precedent alone.

End with one of:
- `EXTERNAL_JOB_HYPOTHESIS_SUPPORTED`;
- `EXTERNAL_JOB_HYPOTHESIS_REVISE`;
- `NO_EXTERNAL_JOB_SIGNAL`;
- `INDETERMINATE`.

If a job survives, the next run attacks it with the strongest incumbent combination before
any product/release work.

## What does not change

No change to:
- #214 hard null;
- #327 generic legal-research-use null;
- #339/#349/#353 bounded observations;
- #357 strong-postmortem-first rule;
- frozen 81-case / 26-class scientific corpus;
- Reference Pack v0.2;
- structured-layer status;
- public-product stop;
- superiority/population claims.

No v0.3, corpus growth, new class or structured external-failure database is authorised.
