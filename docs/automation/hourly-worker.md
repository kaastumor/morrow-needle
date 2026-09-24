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

For discovery, start at section 0 of
`docs/discovery/evidence-triggered-continuous-discovery-v0.2.md`. On a new session,
read the governing documents above. Within the same resumed task, compare their
SHAs and reload changed rules/state plus task-relevant evidence; do not repeatedly
load the entire history. A new task or changed gate requires a fresh scope check.
Use the compact issue/result record there for resumable checkpoints. The worker's
AUTO READY eligibility boundary still applies; a model choice does not expand it.

## Selection rule

First inspect unfinished automation PRs and their active ownership. Resume,
repair or finish work owned by this worker or explicitly handed off or confirmed
abandoned. An unfinished PR is not permission to take over another live session.

Select at most **one** eligible open issue whose title begins `AUTO READY —`.
Use the current `BACKLOG.md` priority order and the active parent gate's scope;
dependencies must be satisfied. Historical completed queues, including
#105–#116, are not an active task list. Resolve or record dependencies on live
work before selecting a separate task.

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
  equivalent deterministic checks pass in a real runtime and the PR records the
  commands/evidence;
- connector/file inspection alone is never sufficient to merge executable MVP
  changes under degraded CI; if a real runtime is unavailable, leave the PR
  open/blocked and do not advance the dependency chain;
- close the AUTO issue after merge;
- reconcile parent gate/backlog/assumptions/ADR only when evidence changed them.

### Concurrent sessions

Record task ownership, intended file scope and inspected base SHA in the existing
issue or PR. Before writing or merging, inspect the latest main, PR head and
changed files. Preserve unrelated newer edits; never force over unexplained
changes. If another session owns overlapping work, use a separate scope or
record the dependency. Age alone does not establish abandonment. These records
coordinate work; they are advisory, not an atomic lock.

## Actions cost discipline

- Run relevant deterministic checks locally before publishing when a checkout is available.
- Batch coherent file changes into one commit before opening the PR; avoid
  one commit per file and repeated pushes merely to narrate progress.
- Sanitation and unit tests run on PRs and main pushes, not feature-branch
  pushes. Keep the final PR check and main verification.
- Do not dispatch live probes or rerun successful workflows without a concrete
  evidence need. Repair the cause before retrying a failed run.
- No eligible task means stop; it does not justify a diagnostic Actions run.

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

