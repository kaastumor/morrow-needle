# Morrow // Needle — Hourly autonomous worker

This runbook does not enable or change a schedule. Before each saved-task migration,
use [SCHEDULED_TASK_TEMPLATE.md](SCHEDULED_TASK_TEMPLATE.md); repeat the project's
critical constraints in the saved prompt. New scheduled research defaults to **20 minutes,
one bounded item**, followed by an honest checkpoint. Existing saved tasks require
separate manual testing and approval before configuration changes.

Use [TASK_TEMPLATE.md](TASK_TEMPLATE.md) and [VERIFICATION.md](VERIFICATION.md).
The canonical operating policy owns routing, retry, deduplication, memory and authorization.
Merge/deploy/publication and other consequential actions require explicit scoped sponsor
authorization; a green PR is READY_FOR_REVIEW, not automatic permission to merge.

Status: **CANONICAL EXECUTION RUNBOOK**

The scheduled worker is an executor, not the product owner. GitHub repository
state overrides chat memory and the scheduler prompt.

## Verified autonomous handoff

Use one designated executor for the current WIP. Prefer that executor to read the
input, execute the bounded task, save the result and verify its durable receipt.
Separate producers require a working consumer and approved delivery route first.
Keep issues/PRs/BACKLOG as owners; do not introduce another queue.

A comment/readback test proves only that operation. Verify branch/PR writes, local
execution, browser observations and private persistence when the selected task
requires them. A prompt cannot grant access, select a model or enforce a budget.
Test one real existing-result handoff and one substantive recovery cycle before
claiming end-to-end operation. Use the scheduled-task contract for activation and
cost review; timer activation alone is not acceptance.

A new explicit sponsor-authorized contract may replace a historical campaign's
read-only envelope. Actual permission or automatic-approval denial still stops the
affected operation: never switch tools, credentials or destinations to evade it.
Without a permitted durable route, stop new intake and report the capability gap.

Resume pending results before producing another. Record exact task/input/output
revision and a separate attempt identity; verify saved bytes or readback and the
consumer disposition. Receipt is not substantive acceptance. Default new
unacknowledged-output capacity is one; unknown legacy backlog blocks new intake,
not explicitly selected recovery of an existing item. Inspect open work and its
latest checkpoint before treating stale main/PR text as unfinished execution.

## Delegated trial and successor selection

When a current sponsor contract explicitly delegates autonomous follow-up, use its
recorded scope and expiry, including ordinary next-task selection within the charter.
For the authorized trial see [native-trial-2026-09-29.md](native-trial-2026-09-29.md).
The issue authorization and saved task are operational authority for that trial;
this pending documentation is not a claim that a PR has merged.

Reconcile primary evidence, disposition and next action before producing another
output. The one-output cap covers unprocessed output, not every open PR. Processing
does not grant merge, scientific/source acceptance or human approval. If the current
WIP is blocked, retain its re-entry condition and explicitly suspend it before one
earned nonconflicting alternative; do not accumulate blocked successors.

Broad opportunity selection runs at most once per local day or on materially changed
evidence, requirements or capability. Compare at most three candidates and select one;
task-driven research for active development is not restricted to that daily scan.
A new hourly invocation is not a new evidence trigger. No valuable executable option
means a cheap NO_CHANGE, not another audit or manufactured task.

## Source-of-truth order

At the start of every run inspect, in order:

1. open pull requests, especially any `auto/*` work;
2. `BACKLOG.md` — sole mutable owner of current mode/WIP/priority;
3. `docs/project-charter.md`;
4. `docs/way-of-working.md`;
5. `docs/assumptions.md`;
6. the active issue and relevant decision/audit documents;
7. latest main CI / operational state relevant to the task;
8. this runbook.

Do not use stale chat handoffs as authority over the repository.

For discovery, the standing rules are in `docs/way-of-working.md` plus the active issue.
`docs/discovery/evidence-triggered-continuous-discovery-v0.2.md` is a reference method:
use its detailed search/confirmation guidance only when the active task needs it.

On a new session, read the governing documents above. Within the same resumed task,
compare their SHAs and reload changed rules/state plus task-relevant evidence; do not
repeatedly load the entire history. A new task or changed gate requires a fresh scope
check. The eligibility rules below and any current scoped sponsor delegation apply;
a model choice alone does not expand them.

## Selection rule

First inspect unfinished automation PRs and their active ownership. Resume,
repair or finish work owned by this worker or explicitly handed off or confirmed
abandoned. An unfinished PR is not permission to take over another live session.

Select at most **one** bounded eligible task. An `AUTO READY —` issue or an
explicitly delegated active-issue slice is eligible. Under a current sponsor contract
that delegates ordinary allocation, the worker may also select and record the next
justified question within the charter and accepted parent gate. Record scope,
baseline/adversary, acceptance, ownership and stop conditions before execution,
using the current issue and a reviewable BACKLOG update. A label or another sponsor
prompt is not required for that delegated ordinary choice.

Use current BACKLOG priority and inspect latest issue/PR evidence before trusting
stale summaries. Resolve live dependencies; completed queues such as #105–#116 are
not active work. Finish or explicitly suspend blocked WIP before an earned alternative.
Do not create a new strategic horizon or weaken an acceptance gate. If no valuable,
feasible authorized task exists, stop this run with NO_CHANGE.

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
- one bounded eligible task per run;
- add regression tests/fixtures where behavior can regress;
- run repository sanitation and relevant tests;
- open a PR;
- inspect CI and repair real repository failures;
- leave the PR READY_FOR_REVIEW when acceptance and CI pass; squash-merge only
  with explicit scoped authorization;
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
