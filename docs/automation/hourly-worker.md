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
5. `docs/way-of-working.md`;
6. the active gate issue and relevant decision/audit documents;
7. latest main CI / operational state relevant to the task;
8. this runbook.

Do not use stale chat handoffs as authority over the repository.

## Selection rule

First resume, repair, or finish an unfinished automation pull request.

Only when no unfinished automation PR exists may the worker select **one**
highest-priority eligible open issue whose title begins:

`AUTO READY —`

Dependencies and the active gate must be satisfied.

For the authorised MVP #103 / discovery #104 horizon, use this priority order:

1. #105
2. #106
3. #107
4. #108
5. #109
6. #110
7. #111
8. #112
9. #113
10. #114
11. #115
12. #116

Discovery issues #111–#116 are not eligible until #110 records
`TECHNICAL_MVP_CANDIDATE`.

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

### Capability-bound acceptance criteria

Acceptance criteria describe the capability/evidence required, not whatever the
current session happens to be able to execute.

If a required check needs:

- a private environment;
- browser/manual interaction;
- sponsor judgment;
- repository-administration access;
- an external system unavailable to the worker;

do **not** replace it with an easier proxy and call the criterion satisfied.

Instead:

1. complete everything that is valid in the current execution boundary;
2. preserve the exact remaining criterion;
3. record what evidence is missing and why;
4. move that check to the correct execution boundary;
5. stop promotion until the required evidence exists.

A narrower executable test may supplement the criterion, never silently weaken
it.

### Ordered, resumable chunks

For broad audits, tool-heavy research, large file reads or multi-file changes,
work in coherent dependency-ordered chunks.

Each chunk should end at a verifiable checkpoint such as:

- evidence pinned;
- failure reproduced;
- decision recorded;
- implementation committed;
- CI checked;
- canonical state reconciled.

Do not turn this into meaningless micro-steps.

The purpose is to make interruption, tool timeout or context loss recoverable
from repository state without repeating or guessing prior work.

## Branch and merge discipline

- branch from current `main`;
- use a short-lived `auto/<issue>-<slug>` branch;
- one AUTO issue per run;
- add regression tests/fixtures where behavior can regress;
- run repository sanitation and relevant tests;
- open a PR;
- inspect CI and repair real repository failures;
- normally squash-merge only when acceptance criteria are satisfied and CI is
  green;
- if GitHub Actions fails before any repository step executes, the narrow
  CI-degraded exception in `docs/way-of-working.md` may be used only after
  equivalent deterministic checks pass and the PR records the failure mode;
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

Likewise, an analytical method cannot jump from EXPERIMENTAL to
VALIDATED_FOR_AUTOMATION merely because its code works. Promotion follows the
method-maturity evidence defined in the project charter.

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
