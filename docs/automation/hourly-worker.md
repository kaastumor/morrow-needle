# Morrow // Needle — Hourly autonomous worker

Status: **CANONICAL EXECUTION RUNBOOK**

The scheduled worker is an executor, not the product owner. GitHub repository
state overrides chat memory and the scheduler prompt.

## Source-of-truth order

At the start of every run inspect, in order:

1. open pull requests, especially any `auto/*` work;
2. `docs/project-charter.md`;
3. `BACKLOG.md`;
4. `docs/assumptions.md`;
5. the active gate issue and relevant decision/audit documents;
6. latest main CI / operational state relevant to the task;
7. this runbook.

Do not use stale chat handoffs as authority over the repository.

## Selection rule

First resume, repair, or finish an unfinished automation pull request.

Only when no unfinished automation PR exists may the worker select **one**
highest-priority eligible open issue whose title begins:

`AUTO READY —`

Dependencies and the active gate must be satisfied.

If no eligible AUTO READY issue exists, do not manufacture work. Inspect for a
blocker only if the active gate explicitly requires it, then stop the run.

## Method

For one task:

> Question → smallest useful proposal → adversary → experiment/implementation →
> evidence → decision → sanitation → project-state reconciliation.

Material adversarial findings use one disposition:

- survives
- revise
- reject
- park
- experiment

Green CI is necessary for merge, not proof that the idea was good.

## Branch and merge discipline

- branch from current `main`;
- use a short-lived `auto/<issue>-<slug>` branch;
- one AUTO issue per run;
- add regression tests/fixtures where behavior can regress;
- run repository sanitation and relevant tests;
- open a PR;
- inspect CI and repair failures;
- squash-merge only when acceptance criteria are satisfied and CI is green;
- close the AUTO issue after merge;
- reconcile parent gate/backlog/assumptions/ADR only when evidence changed them.

## Scope restrictions

The worker may not silently:

- change the project north star;
- skip or close a strategic gate;
- promote a hypothesis/experiment into a trusted domain contract;
- introduce major infrastructure;
- weaken evidence, privacy or abstention rules;
- create a new strategic horizon;
- redefine success/failure criteria;
- start adjacent tasks because time remains.

When such a decision is required, record the evidence/blocker on the parent
issue and stop.

## Lean architecture rule

Prefer existing code and standard-library/platform capability. Add a dependency,
service, database, queue, vector store, framework or external provider only when
the issue records the concrete requirement that the simpler baseline failed.

## Evidence / privacy

Needle's current corpus is intended to be public-source safe.

Never commit:

- secrets or credentials;
- private/customer documents;
- unpublished personal material;
- private derived text/annotations;
- local machine paths or configuration containing identifying/private data.

Derived artifacts inherit the sensitivity of their inputs.

CI fixtures must be synthetic or explicitly public-safe.

## Gate boundaries

A gate cannot promote itself merely because its implementation issues are
closed.

The gate requires:

1. its integrated adversarial reconciliation;
2. a Project Health Check under `docs/project-health.md`;
3. backlog/assumption/risk reconciliation;
4. an explicit continue / simplify / redirect / stop decision.

## End-of-run report

Record only:

- issue worked;
- material change;
- evidence/tests;
- adversarial disposition/decision;
- blocker, if any;
- next eligible AUTO READY issue, if one exists.

Activity volume is not progress.
