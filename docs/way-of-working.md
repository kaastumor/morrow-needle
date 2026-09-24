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
8. **Stop is a valid outcome.** A rejected feature hypothesis is successful
   discovery.

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
- disposition is exactly one of:
  `ADOPT_FOR_EXPERIMENT / REVISE / REJECT / PARK`;
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

Active plan:
`docs/discovery/evidence-triggered-continuous-discovery-v0.2.md`

Start at section 0 for the routine execution path and compact result record.
It owns progressive context loading, search budgets and exploration versus
confirmation. Read detailed sections as applicable; long review prompts are not
mandatory per-scout deliverables. Start from the supported evidence level, not
an assumed externally validated core.

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

- run `docs/project-health.md`;
- reconcile README, charter, backlog, assumptions and value evidence;
- choose `continue / simplify / redirect / stop`;
- prefer an idle queue to invented work.

Activity count, commits and issue throughput are never project-value evidence.
