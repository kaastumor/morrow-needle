# Issue #371 — GitHub Actions cost / automation audit

Date: 2026-09-26  
Disposition: **KEEP_CURRENT_AUTOMATION**

## Question

Which active GitHub Actions still protect a current Needle obligation, and which can be
retired or narrowed after the project contracted to:

> **known-failure reference corpus + exposed regression fixtures + minimal evaluation
> discipline**

The sponsor has repeatedly asked to avoid unnecessary GitHub Actions cost.

## Inventory

The repository currently contains **25 workflow files**.

### Passive historical workflows

**23/25** are already manual-only via `workflow_dispatch`.

They preserve historical/research diagnostics such as:

- Cellar/feed probes;
- operational-pilot/replay workflows;
- Half-Life / Thread / Retrieval / Source Anomaly / dependency-ripple projections;
- historical foundation/gold-corpus probes;
- live legal-source diagnostics.

They do **not** run on push, pull request or schedule.

Therefore their existence does not create standing Actions cost unless somebody explicitly
dispatches them.

This matches the current passive-historical rule established by earlier governance work.

### Automatic workflows

Only two workflows run automatically.

#### Repository sanitation

Triggers:
- every pull request;
- pushes to `main`;
- manual dispatch.

Purpose:
- repository integrity/sanitation across all file classes.

Runtime cap:
- 2 minutes.

This is the only universal PR gate.

#### Unit tests

Triggers:
- pull requests and `main` pushes only when relevant paths change:
  - `src/**`;
  - `tests/**`;
  - `scripts/**`;
  - `schemas/**`;
  - `corpus/**`;
  - `mvp/**`;
  - release-check / project config owners.

Purpose:
- Python tests;
- canonical corpus validation;
- browser-projection tests.

Runtime cap:
- 5 minutes.

Docs-only/governance changes do not trigger this workflow.

## Recent run-cost sample

The latest 100 Actions runs were all from the two automatic workflows:

- Repository sanitation / pull request: **43**
- Repository sanitation / push: **38**
- Unit tests / pull request: **12**
- Unit tests / push: **7**

So **45/100 recent automatic runs** were post-merge `push` executions after an ordinary PR
gate had already run.

That is the clearest remaining cost opportunity.

## Can the push duplicates be removed safely?

Only if the project can rely on all relevant changes reaching `main` through a protected
PR path.

Current administration evidence does not support making that assumption:

- repository rulesets endpoint returns no rulesets;
- branch-protection details return **403 / inaccessible to the integration**;
- project governance itself therefore treats branch-protection status as **UNVERIFIED**.

Removing `push` validation now would mean a direct/unprotected push to `main` could bypass:

- sanitation; and
- for code/corpus/schema paths, the full test/corpus-validation gate.

That trades a verified correctness safeguard for an unverified assumption.

## Historical manual workflows

Removing `workflow_dispatch` from the 23 passive workflows would reduce accidental manual
run risk but would not reduce standing Actions consumption.

Those workflows are already:

- non-scheduled;
- non-PR;
- non-push;
- explicitly marked passive/historical.

Their manual diagnostics remain useful provenance/recovery capability at effectively zero
automatic cost.

No further retirement is earned solely for cost.

## Options considered

### Remove `main` push triggers

Potential benefit:
- approximately 45% fewer runs in the recent 100-run sample.

Rejected **for now** because main protection cannot be verified.

### Remove PR triggers and validate only after merge

Cheaper before merge but fails the purpose of a gate.

Rejected.

### Merge sanitation and unit tests

Would add conditional-path machinery and couple cheap universal sanitation to a heavier
test workflow.

No evidence this reduces meaningful runner cost without added complexity.

Rejected.

### Remove historical manual workflows

No standing cost benefit.

Rejected.

### Keep current automation

Preserves:
- universal sanitation;
- path-filtered scientific/code validation;
- manual-only historical diagnostics;
- no standing schedule.

Selected.

## Disposition

# **KEEP_CURRENT_AUTOMATION**

The current workflow design is already appropriately narrowed for the smaller Needle
identity.

Do not optimize the visible count of 25 workflow files as though it represented 25 active
automation obligations.

## Re-entry trigger for further cost reduction

Revisit post-merge duplicate removal only if one of these becomes verifiable:

1. `main` has enforced protection/rules requiring the PR checks;
2. repository administration becomes inspectable through the integration;
3. an equivalent fail-closed mechanism prevents direct pushes from bypassing validation.

At that point, PR-only sanitation/unit testing could plausibly remove roughly the observed
45% post-merge duplicate-run share without lowering integrity.

Until then:

> **correctness protection outranks speculative runner savings.**

No workflow files, scientific state, corpus state or release bytes change in #371.
