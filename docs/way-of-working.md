# Morrow // Needle — Way of Working

Status: **CANONICAL DELIVERY + DISCOVERY OPERATING MODEL**

This document defines how the project turns evidence into a small usable product
without rebuilding the discarded architecture.

## Operating principles

1. **Evidence before scope.** Product work must expose demonstrated value, not
   manufacture a new value thesis.
2. **Thin vertical slices.** Prefer a complete small user outcome over horizontal
   architecture layers.
3. **WIP = 1 per autonomous worker.** One issue, one branch, one PR.
4. **Trunk-oriented flow.** Short-lived branches from current `main`; squash
   merge after acceptance.
5. **Strong boring baseline.** Browser platform, Python stdlib and existing
   repository capabilities come before frameworks/services.
6. **Fail closed.** Broken/malformed evidence must be visible rather than silently
   approximated.
7. **Delivery and discovery are different tracks.** Delivery implements accepted
   scope. Discovery produces evidence about possible scope.
8. **Stop is a valid outcome for a hypothesis, not for the sponsored program.** A rejected hypothesis is successful evidence. The programme then moves to one bounded purposeful mode under WIP=1; that mode need not be another experiment.

## Purposeful continuity

Morrow // Needle is sponsor-funded and must not use `IDLE BY DESIGN` as a default
project state.

That sponsor constraint does **not** create an automatic discovery or experiment
conveyor.

When a bounded horizon ends, reconcile the result and choose exactly one purposeful mode
that best serves the current evidence:

- **DISCOVER** — investigate one consequential unresolved question;
- **CONSOLIDATE** — reconcile, compress, retire or simplify accumulated state;
- **USE** — apply accepted assets to a real task within their supported scope;
- **REVIEW / RELEASE** — assess or prepare a coherent finished deliverable;
- **MAINTAIN** — preserve correctness, evidence validity, integrity, cost or operability.

The canonical transition is:

> **finish -> reconcile -> choose one purposeful mode -> WIP=1**

not:

> **finish -> automatically invent another experiment**

and not:

> **finish -> leave the project indefinitely idle**

Selection must be grounded in the current evidence and sponsor constraints. Local WIP
discipline does not prove that the selected mode is the best project-level allocation.

Continuity preserves:

- WIP = 1 for active execution;
- strongest boring/incumbent baseline first;
- explicit falsifiers and negative outcomes where a claim is tested;
- no post-hoc harder replacement cases;
- no feature, ontology or schema growth merely to stay busy;
- no standing expensive monitoring/CI work when a cheaper mode is sufficient;
- explicit completion/re-entry criteria.

A completed work item may end in `ADOPT`, `REVISE`, `REJECT`, `PARK`,
`SIMPLIFY` or `STOP`, with a subtype where useful. The project-level successor is
chosen separately.

`BACKLOG.md` is the sole mutable owner of the current mode, WIP and immediate
priority. Orientation and constitutional documents must link to it rather than copy its
live state.

## Incumbent and residual-value test

Discovery must distinguish **doctrinal/market existence** from project value.

> **Existing is not useless. Different is not valuable. Novel is not demanded.**

The strongest incumbent doctrine, method, competitor or ordinary research rule is the
baseline. Its existence is neither an automatic REJECT nor evidence that Needle adds
value.

For a taxonomy/corpus candidate:

- **REJECT** when the incumbent plus existing Needle classes losslessly predicts and
  expresses the consequential legal-information failure, leaving no bounded residual
  regression/reference value;
- **REVISE/ADMIT** only when a reusable residual state survives, its positive and
  boundary evidence are explicit, and the label materially helps organise or test
  regression cases rather than merely renaming known doctrine;
- never claim novelty merely because Needle uses a different label;
- never deny corpus value merely because the underlying doctrine is mature.

Here **lossless** is intentionally narrow. Loss means loss of a **pre-specified
consequential distinction in a regression question**: for example a different expected
answer, evidence requirement, state transition, boundary condition or pass/fail outcome.
Loss of descriptive nuance, doctrinal vocabulary or implementation detail is not enough
to protect a separate class.

Likewise:

- failure to prove redundancy is **not** evidence of residual value;
- preserving a useful regression case does **not** automatically justify preserving its
  current organising class;
- cases may remain valuable after class consolidation;
- the burden is symmetric: admission requires positive residual value, while compression
  requires evidence that the consequential distinction survives under a broader owner.

A coverage gate selecting an uncovered dimension creates **no presumption of
admission**. The follow-up research run starts from the null that no new class is needed
and must re-run incumbent/existing-class first refusal.

## Mode binding

A Project Health, coverage, red-team or owner decision that selects a mode or sole next
WIP is binding until that work completes or a later explicit gate records why it is
superseded.

Do not silently leave discovery, depth, compression, consolidation, use, release or
maintenance because a more interesting task appears. Reconcile the mode change first and
preserve any abandoned/deferred question explicitly.

A sponsor/owner decision may explicitly supersede a previously selected successor. That
is governance, not evidence that the earlier candidate was scientifically wrong.

A depth lane must also earn its continuation. If **three consecutive depth runs**, each
selected before substantive research begins, produce only additional illustrations and
none produces a changed definition, sharper exclusion boundary, consequential correction
to a regression expectation, rejection, retirement or compression signal, the claimed
information advantage of depth is falsified. Run an explicit direction review before a
fourth confirmation-style depth run.

## Checkpointed burst execution

Autonomous work is executed in **checkpointed bursts** so chat/transport failures do
not erase or duplicate substantive work.

1. **One coherent milestone per turn.** Examples: research -> durable
   checkpoint/result, or PR -> one CI check -> merge/resumable SHA. Do not chain
   several experiments merely because the session is still open.
2. **Persist important state early.** Before a long research/implementation run, create
   or confirm the owning issue and branch/checkpoint so GitHub remains the recovery
   boundary.
3. **Read narrowly.** Prefer targeted files, line ranges, issue slices and bounded
   source sets over repeatedly loading large repository payloads.
4. **Batch compatible reads, not milestones.** Internal retrieval may be batched, while
   the user-visible turn remains bounded to one milestone.
5. **Do not poll CI repeatedly.** Inspect CI once near the end. If it is still running,
   persist the exact PR/head SHA and stop at that resumable boundary.
6. **Checkpoint after material progress.** After a merge or meaningful discovery result,
   end with a 2–4 line durable checkpoint. The next `continue` starts from GitHub
   canonical state, not chat memory.
7. **Recover from GitHub first.** After a stream/tool failure, inspect current repo,
   branch, PR and issue state before retrying. Never blindly repeat interrupted writes,
   experiments or PR creation.

Checkpointing changes execution reliability, not scientific standards. WIP=1,
pre-registration, incumbent baselines, negative evidence and anti-growth rules remain
in force.

## Selective reasoning escalation

Routine project work stays on the current model/capability. Do not escalate merely
because a task is important, long, novel or uncomfortable.

During **project analysis, wide-lens review or red teaming**, proactively suggest
**GPT-6 Astra at medium reasoning** when a specific difficult question is both:

1. consequential enough that a weak answer could materially change project
   direction, architecture, experiment design or interpretation of evidence; and
2. reasoning-limited enough that deeper synthesis, adversarial comparison,
   abstraction or multi-constraint analysis could plausibly improve the decision.

An escalation suggestion must stay focused. Briefly state:

- the exact unresolved question;
- why deeper reasoning is warranted for that question;
- what decision/output Astra should produce; and
- a compact handover prompt that preserves the relevant evidence, alternatives,
  constraints and falsifier.

Prefer one bounded Astra task over handing over an entire project or review.

Do **not** suggest Astra for routine retrieval, repository inspection, mechanical
implementation, formatting, status reconciliation, ordinary source checking or
work already decided by clear evidence.

Astra is an analysis resource, not evidence. Its output remains subject to the
same source, exposure, comparator, falsification and Project Health rules as any
other model-assisted analysis.

## Work item types

### MVP GATE

A bounded user outcome with objective technical acceptance plus any explicitly
separate manual/sponsor acceptance.

### AUTO READY

An atomic executable issue. It must satisfy Definition of Ready and must not
require strategic product judgment.

### DISCOVERY GATE

A bounded runway of questions about potential product value.

### Discovery AUTO READY

Evidence-only work. It may end in a proposed experiment but may not implement the
feature being investigated.

## Definition of Ready

An AUTO issue is ready only when all are true:

- parent gate/horizon is already authorised;
- outcome is stated in user/research terms;
- acceptance criteria are observable;
- dependencies are complete;
- required public inputs/tools are available;
- no hidden sponsor/manual decision is required to finish the issue;
- scope fits one autonomous run or can be resumed safely from a PR;
- security/privacy constraints are explicit;
- the issue does not require changing the north star.

If any condition fails, the issue is blocked rather than “mostly ready.”

## Definition of Done

For an implementation issue:

- acceptance criteria satisfied;
- smallest implementation used;
- regressions/tests added where behavior can regress;
- relevant validators/tests/sanitation executed;
- PR diff reviewed against scope;
- CI inspected honestly;
- no secrets/private/local paths introduced;
- documentation changed only where canonical state changed;
- PR squash-merged;
- issue closed;
- next dependency becomes eligible.

For a discovery issue:

- question and alternative explanation stated;
- relevant internal evidence and external precedent inspected;
- smallest useful experiment/research performed;
- limitations/counterargument recorded;
- disposition records one primary family: `ADOPT / REVISE / REJECT / PARK`, with a
  subtype where it changes meaning (for example `ADOPT_FOR_EXPERIMENT`,
  `ADOPT_FOR_DERIVATION` or `REVISE_EXISTING_CLASS`);
- no feature implementation slipped into the discovery PR.

## CI-degraded exception

Green CI is the normal merge gate.

A narrow exception exists only when GitHub Actions fails **before any repository
step executes**, as already observed in September 2026.

The worker may use the exception only when all are true:

1. the job exposes no executed repository steps (for example steps are null/empty
   or no runner executes the job);
2. there is no assertion/test/build failure from repository code;
3. for any change to executable code, browser JavaScript, test code, scripts or
   workflow configuration, the required deterministic checks are actually
   executed in a real runtime and pass; file/connector inspection alone does
   **not** count as execution evidence;
4. documentation-only changes may use structural/manual inspection when no
   executable behavior changed;
5. the PR records the exact CI failure mode and the commands/runtime evidence
   used instead;
6. the change does not require an unavailable manual/browser acceptance criterion.

A workflow that executes project steps and fails is a real red build. It may
never be waived under this exception.

For MVP implementation issues #105–#110 specifically: if Actions is unavailable
and the worker cannot execute the relevant repository tests/sanitation in an
actual runtime, it must leave the PR open/blocked. It may not merge based on
static inspection and may not advance to the dependent issue.

## Branch/PR convention

- branch: `auto/<issue>-<short-slug>`;
- one AUTO issue per branch/PR;
- PR title starts with the issue number;
- squash merge;
- no unrelated cleanup bundled into delivery work.

## MVP architecture rule

For Corpus Explorer v0.1:

- static HTML/CSS/JavaScript;
- canonical corpus JSON is read directly;
- no copied legal truth dataset;
- no server/backend/API;
- no auth;
- no frontend framework;
- no model call;
- no analytics/telemetry;
- no new dependency unless the issue proves platform/stdlib insufficient.

## Discovery rule

Discovery starts from evidence, not from a feature list.

Detailed reference method:
`docs/discovery/evidence-triggered-continuous-discovery-v0.2.md`

That document is a **reference method**, not a second standing source of current queue or
constitutional authority. Ordinary discovery execution is governed here plus the active
issue. Use the reference method's search budgets, exploration/confirmation distinctions
and compact result pattern when they fit the task. Frozen historical experiments retain
their own exact rules.

Evidence may enter through:

- a fresh legal adversary;
- real Explorer use;
- a concrete external research need;
- an observed failure of the current approach.

These are sourcing channels into one WIP=1 opportunity funnel.

Discovery follows:

> evidence signal → discover/diverge → define opportunity → strongest baseline →
> riskiest assumption → smallest evidence test → counterargument → disposition


Optional linked discovery search may run inside `discover/diverge` from a
concrete evidence anchor or proven mechanism. It is not an evidence channel and
may create only a `SEARCH_HYPOTHESIS`. That hypothesis cannot enter the
opportunity funnel until target evidence is found through one of the four
authorised channels.


### Transport smoke test for external sample selection

When a bounded experiment depends on an external API/search/index to enumerate a
deterministic validation sample, verify the transport **before** freezing the
candidate-selection protocol.

The smoke test may inspect only:

- whether the query/API shape executes;
- response schema/fields needed by the later selection rule;
- count/pagination mechanics;
- access/size/quota constraints.

It must not retain candidate identities, inspect substantive candidate content,
or tune the future sample.

Discard smoke-test results. Then preregister and rerun the transport under the
frozen rule.

This metadata-only check is distinct from an explicitly exploratory eligibility
pilot. A pilot may inspect content, but must retain its exposure record and its
cases cannot become fresh validation. Choose the mode before inspection. This
option applies to future designs and never overrides a frozen experiment.

If transport later fails after sample exposure, preserve the failure rather than
iteratively redesigning transport until a convenient sample appears.

Keep at most three active search hypotheses; do not create a discovery graph,
force distant analogies, or turn recombination into feature ideation.

Before a discriminating test, freeze the claim as
`CORRECTNESS_VALIDITY` or `PRODUCT_WORKFLOW`. A failed correctness claim may
not be rescued post hoc as workflow value. Workflow value also cannot override a
material correctness/provenance/evidence-integrity regression.

Use established product-discovery risks where material:

- value;
- usability;
- feasibility;
- viability/operations;

plus Needle's explicit validity/evidence-integrity risk.

Do not mechanically fill every risk category. Test the assumptions that are both
important and weakly evidenced.

Every discovery issue ends in exactly one:

`ADOPT_FOR_EXPERIMENT / REVISE / REJECT / PARK`

An ADOPT_FOR_EXPERIMENT result does not create implementation permission. A later
delivery candidate needs a separate gate and the discovery plan's section 13
claim-specific evidence: baseline failure for correctness/validity superiority,
or meaningful relative workflow advantage for a recurring or consequential job
under the validity floor. Equal correctness does not rule out workflow value.

Human-evidence claims remain human. Browser automation cannot substitute for
observed usability, and public trends cannot be relabelled as direct external
demand.

Disposable prototypes are permitted only when they are the cheapest credible
test. They must not silently become maintained product architecture.

Per opportunity, use one initial discovery run and at most one follow-up before
mandatory disposition unless genuinely new external/source evidence changes the
decision boundary.

## Gate review

At the end of a meaningful horizon:

- run `docs/project-health.md` when its trigger applies;
- reconcile the live owner (`BACKLOG.md`) plus any durable owner whose meaning actually
  changed; do not update README/charter merely to copy current queue state;
- choose `continue / simplify / redirect / stop` for the horizon;
- then choose exactly one purposeful successor mode under the continuity rule. The
  successor may be discovery, consolidation, use, review/release or maintenance.

Activity count, commits and issue throughput are never project-value evidence.
