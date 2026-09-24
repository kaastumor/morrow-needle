# Red-team review — evidence-triggered discovery v0.2

Date: 2026-09-24  
Target:
`docs/discovery/evidence-triggered-continuous-discovery-v0.2.md`

## Question

Does the proposed discovery operating model genuinely improve Needle's ability to
find valuable work, or does it merely replace a feature backlog with a more
sophisticated discovery bureaucracy?

## Verdict

**SURVIVES WITH REVISIONS ALREADY INCORPORATED.**

The model is worth trying for one bounded cycle because it changes the source of
work from ideas to evidence and retains explicit kill rules.

It should **not** become permanent governance yet.

The strongest attacks below materially changed the design.

## Attack 1 — four evidence channels become four backlogs

### Failure mode

"Legal adversary / Explorer use / external need / current failure" looks like
clean portfolio structure. In practice it could create four queues that each
feel entitled to throughput.

That would recreate roadmap pressure in discovery form.

### Required revision

The channels are sourcing tags only.

- one shared opportunity funnel;
- WIP=1;
- no per-channel throughput targets;
- a channel with no evidence produces no issue;
- the initial four sensing tasks are a bounded sampling round, not permanent
  workstreams.

**Applied.**

## Attack 2 — active adversary hunting biases the corpus toward puzzles

### Failure mode

If Morrow is told to "find interesting adversaries," it can optimize for obscure
edge cases, adversarial wording or cases likely to make a comparator fail.

The corpus would become difficult without becoming useful.

### Required revision

- candidate rationale and decisive source evidence before model/comparator runs;
- prefer orthogonal under-covered domains/source systems;
- do not retain a candidate because the baseline failed it;
- preserve parity and "existing class already covers this" as successful results;
- new failure families still require independent support.

**Applied.**

## Attack 3 — sponsor dogfood is mistaken for user validation

### Failure mode

The sponsor is deeply informed and atypical. A successful session can overstate
the Explorer's general usability; a feature request can be mistaken for a need.

### Required revision

- sponsor session is valid dogfood and can expose a real defect;
- it cannot alone resolve general H-16;
- observe task behaviour instead of asking for desired features;
- additional intended users or repeated independent use are required for broader
  user-value claims;
- if external users are unavailable, H-16 remains unresolved.

**Applied.**

## Attack 4 — public research signals are laundered into "external demand"

### Failure mode

Papers, blog posts, benchmark repositories and public issues are easy for an
agent to find. Calling them external user evidence would let Morrow manufacture
market pull without ever interacting with a user.

### Required revision

Use an evidence hierarchy.

- public trend/research evidence may nominate an opportunity;
- direct request or observed workflow is stronger;
- broad response normally needs independent corroboration;
- "someone would probably want this" never passes the value gate.

**Applied.**

## Attack 5 — current-failure hunting rewards architecture cleanup

### Failure mode

A broad "find failures" mandate can turn every stale file, awkward script or
unimplemented capability into a discovery trigger.

This would incentivize refactoring the historical Full Needle surface.

### Required revision

Eligible failures must affect:

- correctness;
- provenance/evidence integrity;
- evaluation validity;
- observed Explorer use;
- repeated research/admission burden;
- current active system reliability.

Dormant untidiness, hypothetical scale and technically possible features do not
qualify.

**Applied.**

## Attack 6 — "industry standard" becomes cargo cult

### Failure mode

Double Diamond, Opportunity Solution Trees, user interviews and four-risk
language can produce ceremony without better decisions.

A process can look professional while only renaming existing opinions.

### Required revision

Use frameworks as decision aids, not required artifacts.

- no mandatory diagram;
- no discovery KPI dashboard;
- no requirement to populate every risk category;
- no fixed 4–8 week phase merely because GOV.UK describes that as typical;
- only create an artifact when it owns a decision or evidence boundary.

**Applied.**

## Attack 7 — assumption testing can still start from a bad solution

### Failure mode

Teams can become efficient at testing assumptions about a solution nobody needs.

### Required revision

The opportunity/problem must first survive Define:

> In [context], [actor] cannot reliably [job] using [strong baseline] because
> [observed failure], causing [consequence].

Only then may solution assumptions be tested.

**Applied.**

## Attack 8 — "ADOPT_FOR_EXPERIMENT" becomes soft approval to build

### Failure mode

The previous discovery runway already produced two conditional
ADOPT_FOR_EXPERIMENT outcomes. Without a hard boundary, the label can become a
parking lot of pre-approved features.

### Required revision

- ADOPT_FOR_EXPERIMENT authorizes only a falsifiable experiment;
- experiment requires explicit trigger + assumption + kill rule;
- delivery requires a later gate and evidence that the strong baseline failed;
- no discovery note may create production code by implication.

**Applied.**

## Attack 9 — prototypes quietly become architecture

### Failure mode

Industry discovery encourages prototypes. In a code-centric repository a
prototype can easily become "90% done" production code and acquire maintenance
gravity.

### Required revision

Prototype code must be disposable:

- experiment branch or non-production artifact;
- no automatic merge into maintained product;
- no new production dependency;
- delivery gate must choose the implementation afresh.

**Applied.**

## Attack 10 — discovery never ends

### Failure mode

"Continuous discovery" can justify permanent investigation. A team can always
ask one more question and avoid a hard decision.

### Required revision

Per opportunity:

- one initial run;
- maximum one follow-up run;
- then mandatory disposition;
- a third run requires genuinely new external/source evidence.

Cycle 1 itself is bounded to four sensing tasks plus synthesis.

**Applied.**

## Attack 11 — synthetic human evidence slips in through agent capability

### Failure mode

Morrow can inspect UI, simulate tasks and research public opinions. That can be
mistaken for actual user observation.

### Required revision

Explicit human boundary:

- automated/browser tests are technical evidence only;
- Morrow cannot manufacture a user session;
- direct external need cannot be inferred from general trends;
- unavailable human evidence stays unavailable.

**Applied.**

## Attack 12 — evidence thresholds become arbitrary pseudo-science

### Failure mode

Hard numeric rules such as "5 users" or "3 requests" look objective while having
no principled relationship to the risk.

### Required revision

Use consequence and independence rather than universal sample numbers.

Examples:

- one real correctness/provenance failure can justify investigation;
- workflow convenience needs recurrence;
- sponsor dogfood can find defects but not prove general value;
- a broader external-demand claim requires independent corroboration;
- new trap-class admission follows the corpus's established independent-support
  discipline.

No synthetic score is introduced.

**Applied.**

## Attack 13 — opportunity capture duplicates the corpus/governance model

### Failure mode

A new opportunity database, schema, labels taxonomy and dashboard would make
discovery itself another product.

### Required revision

Use ordinary GitHub issues as the canonical opportunity record.

The discovery plan defines required reasoning fields, not a new machine-readable
opportunity ontology.

**Applied.**

## Attack 14 — negative evidence disappears faster than positive evidence

### Failure mode

Rejected opportunities are psychologically easy to forget. Attractive ideas can
return later under a new name.

### Required revision

Each issue must preserve:

- counter-evidence;
- kill rule;
- final disposition;
- condition required for reopening.

Project-level negative evidence enters the value ledger only when it changes
project direction, avoiding both amnesia and status-document bloat.

**Applied.**

## Attack 15 — this phase can still become "discovery theatre"

### Failure mode

The project may produce many excellent research notes while never encountering
real external use or a baseline failure. The discovery process itself can become
the output.

### Kill condition

At Cycle 1 synthesis, simplify or stop this discovery model if:

- most opportunities are agent-generated rather than evidence-generated;
- no human/external signal can be obtained and this materially limits the tested
  claims;
- the strongest baseline keeps winning;
- the process adds more documentation/governance than discriminating evidence;
- no discovery result changes a decision.

This is the most important system-level kill rule.

## Why the plan still survives

The proposal survives because the revised model has four useful properties:

1. it actively seeks evidence rather than waiting passively for inspiration;
2. it prevents evidence channels from becoming feature portfolios;
3. it makes negative outcomes first-class;
4. it is itself bounded and falsifiable.

The key condition is discipline: **the first cycle must be allowed to end with
no new build.**

If the sponsor push is interpreted as "something must ship," this plan fails.
If it means "actively search for the strongest next evidence," the plan is
aligned with Needle's current project thesis.

## Final red-team disposition

**ADOPT_FOR_EXPERIMENT**

Run exactly one bounded Cycle 1 under v0.2, then perform a Project Health Check.

Do not schedule Cycle 2 in advance.


## Amendment — parity is not one-dimensional

### Attack 16 — correctness parity is misread as product-value parity

**Attack:** the discovery plan can become too conservative if "strong baseline
did not fail" is interpreted as a universal no-value result.

A manual/repository/official-source workflow may reach the same correct answer
while imposing materially greater time, navigation, expertise, verification or
reconstruction burden. Rejecting a product/workflow opportunity solely because
the substantive conclusion matches would confuse **correctness parity** with
**workflow/value parity**.

The inverse error is equally dangerous: a faster or nicer experience is not
valuable merely because it differs.

**Revision:** keep two gates distinct.

For correctness, validity and legal-research advantage claims, the strong
baseline must materially fail the tested claim before Needle-specific correctness
machinery earns value.

For product/workflow claims, compare the real current alternative on:

1. actual difference;
2. importance to the intended user;
3. behavioural consequence;
4. adoption/switching friction.

A product claim survives only when the observed relative advantage is important
enough to plausibly change behaviour. Competitor existence, novelty and feature
difference are evidence about the landscape, not verdicts.

This revision applies immediately to #136 and #139.

**Red-team disposition:** survives. The change makes the discovery model less
likely to create false negatives without weakening the evidence burden.
