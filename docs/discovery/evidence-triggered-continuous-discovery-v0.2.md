# Evidence-triggered continuous discovery v0.2

Status: **SPONSOR-AUTHORISED DISCOVERY OPERATING PLAN**  
Date: 2026-09-24  
Supersedes: the intentionally idle post-#104 state only for the bounded discovery
cycle defined here. It does **not** supersede the project charter, evidence rules,
or stopped public-product decision.

## 0. Routine execution path

Use this section as the entry point for repeated discovery sessions, including
5.6 sessions. It reduces repeated reading and output; it is not evidence that a
particular model performs better. Sections below remain the detailed rules.
Use the original long prompts for horizon reviews, not as per-run output quotas.

### Load the decision context

Read current main/PR state, the current backlog entry, active parent/child issue,
and this section. On a new session read the charter, way-of-working and applicable
evidence/exposure rules; on resumption check their SHAs and reload changes. Then
read only the relevant source records and detailed sections below. Never reuse
an old queue or skip a governing rule to save context. If state disagrees with a
live PR, resolve ownership/dependency before selecting work; do not take it over.

### Select one question

Start from what the evidence actually supports: an existing asset, internal
use, technical feasibility or demonstrated external value. Do not assume a
validated useful core merely because the prompt calls it proven.

Name the decision that support and rejection would change. Prefer a consequential
uncertainty with accessible evidence and a cheap discriminating observation.
Existing useful distinctions qualify; novelty and a new class are not required.
Choose at most three search hypotheses, then pursue one. Creative structural,
failure-led and distant analogies are welcome when they predict a testable
boundary; they need target evidence before becoming opportunities.

### Choose the evidence mode before testing

- **Exploration:** search, map mechanisms and inspect feasibility. Record exposed
  candidates and failed routes. Findings can earn derivation evidence or a later
  test, not independent confirmation of themselves. A short exposed pilot may
  check full eligibility when metadata alone is insufficient; keep its record
  and exclude it from later fresh validation.
- **Confirmation/comparison:** first freeze task/sample selection, claim type,
  strongest realistic comparator, resource budget, primary outcome/materiality,
  exposure controls and failure rule. Use the evaluation protocol where relevant.
  Do not change these after decisive evidence. Existing frozen experiments keep
  their original rules; this pathway cannot repair them retrospectively.

A documentary mechanism test need not claim that a model failed. A superiority
claim needs comparator evidence. A workflow claim may succeed with the same
correct answer, but must include setup/switching burden and preserve validity.

### Search, challenge, decide

For a routine scout, default to two purposeful search batches, each addressing
at most three explicit questions. Inspect the decisive sources; search snippets
are not verification. Batch independent reads. Avoid repeating a query/failed
transport unless new evidence or a changed condition makes it informative.
An authorised task may set a different budget before substantive work.

After each batch ask whether the new evidence changes the decision. Stop a
branch on saturation, inaccessible decisive evidence or an untestable connection.
At the budget boundary record a disposition or a justified bounded continuation;
do not silently renew the budget. Keep the existing one-follow-up limit. Tool
failure/sample incompleteness is indeterminate, not evidence against the claim.

Before concluding, test the strongest rival and nearest counterexample. Ask:
would an equally resourced ordinary workflow explain or achieve the same result?
Did selection, cueing, prior exposure or unequal access produce the advantage?
Can another reader check the decisive evidence? Label self-review honestly.

### Leave one resumable record

Use the existing issue or its existing result document, not both as duplicate
narratives. Keep this compact structure; expand only where the evidence needs it:

> Decision / supported premise; claim and evidence mode; source links and exposure;
> strongest alternative and budget; falsifier/primary outcome; new evidence and
> strongest rival; disposition and inference limit; exact next action or re-entry
> trigger, with ownership and inspected SHA.

Use `ADOPT_FOR_EXPERIMENT / REVISE / REJECT / PARK`; separately state incomplete
execution if applicable. Link unchanged evidence instead of rewriting it. A
blocked task may be parked while Morrow selects another authorised evidence-led
question; the scheduled executor may select only eligible AUTO READY work.
Do not equate one exhausted branch with a project-wide idle state.

Update canonical state only where the decision changes it. Batch coherent files
in one commit/PR; preserve sanitation and relevant tests. No live dispatch or
paid evaluation just to show activity. At horizon synthesis use the full health
review; do not repeat it after every scout.

## 1. Purpose

Needle will actively pursue discovery again, but it will not return to
feature-ideation as the source of work.

Discovery is allowed to start only from evidence in one of four channels:

1. a fresh, interesting legal adversary;
2. real use of the Corpus Explorer;
3. a concrete external research need;
4. an observed failure of the current approach.

These are **evidence channels, not four roadmaps**.

All signals enter one shared opportunity funnel. WIP remains 1. A channel that
has no evidence creates no work.

The goal is not to keep agents busy. The goal is to increase confidence about
which problems, if any, deserve a Needle-specific intervention.

## 2. Discovery outcome

The discovery outcome is:

> **Find recurring or consequential legal-research problems where either the
> strongest boring baseline/current corpus materially fails, or where a
> Needle-specific response demonstrates a meaningful relative advantage over a
> correct existing alternative, and identify the smallest evidence-backed
> response without rebuilding the stopped broader product.**

For correctness, validity and legal-research claims, "relative advantage" cannot
substitute for correctness: the simpler baseline must materially fail the claim
being tested before Needle-specific correctness machinery earns value.

For product/workflow claims, the incumbent alternative may reach the same correct
answer. Value may instead come from a demonstrated reduction in time, effort,
expertise, reconstruction, navigation or verification burden that is important
enough to change behaviour.

This outcome deliberately permits three successful end states:

- a new experiment is justified;
- existing Needle is sufficient;
- the opportunity is rejected or parked.

No feature count, case count, interview count, commit count or discovery
throughput is a project-value metric.

## 3. Industry basis

This operating model combines several established discovery practices rather
than treating any one framework as doctrine.

### 3.1 Discover → Define before Develop → Deliver

The Design Council Double Diamond is used as the macro shape:

- **Discover:** widen the evidence base and understand the problem;
- **Define:** converge on the actual opportunity/problem;
- **Develop:** compare possible responses and test assumptions;
- **Deliver:** only after discovery has reduced the relevant risks.

Reference:
https://www.designcouncil.org.uk/resources/the-double-diamond/

Needle's discovery gate normally ends before product delivery. A delivery issue
is a later decision.

### 3.2 Understand users, current behaviour and constraints before building

The GOV.UK Service Manual is used as the baseline for problem discovery:

- understand who the users are and what they are trying to achieve;
- understand how they do it now;
- identify frustrations/problems;
- understand technology, policy, legal and process constraints;
- do not start building a service merely to learn what the problem is.

References:
https://www.gov.uk/service-manual/agile-delivery/how-the-discovery-phase-works
https://www.gov.uk/service-manual/user-research/user-research-in-discovery
https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service

The GOV.UK 4–8 week discovery range is **not** copied as a Needle cadence.
Needle's scope is smaller and event-driven; the purpose determines the length.

### 3.3 Outcome → opportunities → solutions → assumption tests

Teresa Torres' Continuous Discovery / Opportunity Solution Tree model is used to
keep discovery anchored in an outcome and unmet needs rather than a feature
backlog.

Needle uses:

- one outcome at the root;
- evidence-backed opportunities/problems beneath it;
- possible responses only after an opportunity is defined;
- assumption tests at the leaves.

References:
https://www.producttalk.org/getting-started-with-discovery/
https://www.producttalk.org/discovering-solutions/
https://www.producttalk.org/assumption-testing/

Continuous discovery is interpreted here as **continuous readiness to learn**,
not continuous production of work.

### 3.4 Riskiest assumptions first

Assumptions are ranked by:

1. how important they are to the opportunity/response succeeding; and
2. how weak the current evidence is.

Only the assumptions capable of killing the idea deserve early testing.

Reference:
https://www.producttalk.org/glossary-discovery-risky-assumption/

### 3.5 Product risks before implementation

SVPG's four product risks are considered when material to the claim:

- **value** — will the user/researcher choose or benefit from this;
- **usability** — can the intended user use it successfully;
- **feasibility** — can the smallest useful version be built with current
  capabilities;
- **viability** — can the project support the operating, legal, cost and
  governance consequences.

References:
https://www.svpg.com/four-big-risks/
https://www.svpg.com/the-product-operating-model-an-introduction/

Needle adds one project-specific risk:

- **validity / evidence integrity** — would the response contaminate evaluation,
  duplicate truth, overstate legal correctness, weaken provenance, or create a
  claim stronger than the evidence supports.

This fifth risk is not presented as an industry standard. It is a Needle
constraint derived from the project's research purpose.


### 3.6 Alternatives, relative advantage and adoption

Discovery must not infer:

- competitor/alternative exists → no opportunity;
- feature is different/novel → opportunity;
- baseline reaches the same answer → no product value.

The relevant comparator is the **real alternative used for the job**, which may
be direct official-source research, repository inspection, search, a capable
LLM, another product, a manual workflow, an expert, or doing nothing.

For a material product/workflow opportunity, keep four questions separate:

1. **Difference** — is the proposed experience actually different from the
   current alternative?
2. **Importance** — does the intended user care about that difference in the
   relevant circumstance?
3. **Behavioural consequence** — is the advantage large enough to influence
   adoption, switching, repeated use, willingness to continue, or another
   meaningful behaviour?
4. **Adoption/switching friction** — is the advantage still meaningful after
   accounting for the cost and inconvenience of changing behavior?

A difference that is real but unimportant is not strategic value. A useful
difference that is too small to overcome adoption/switching friction may also not
be enough.

Novelty is therefore descriptive evidence, not a promotion criterion.

Value may arise from an activity system around otherwise ordinary capabilities:
workflow fit, combination, integration, trust/governance, delivery, or
complementarity with the proven core. Do not require every individual feature to
be unique; do require the combined advantage to be observed or falsifiably
testable.

Do not turn this into a mandatory strategy-canvas exercise. Use the lens only
where user/product value is actually at stake.


### 3.7 Claim type, validity floor and linked discovery search

Before collecting discriminating evidence, declare the claim type:

- `CORRECTNESS_VALIDITY` — claims that Needle produces safer, more correct,
  better-grounded or more reproducible research/evaluation outcomes;
- `PRODUCT_WORKFLOW` — claims that Needle improves how a user completes a job
  even when the substantive answer may match the incumbent alternative.

Do not rescue a failed correctness claim by relabelling it as workflow value
after results are known. A later workflow claim requires its own hypothesis and
evidence.

A product/workflow advantage also has a **validity floor**. It cannot be promoted
when it materially worsens correctness, uncertainty handling, provenance,
evidence lineage or evaluation integrity.

#### Optional linked discovery search

After an evidence signal or sufficiently proven mechanism exists, Discover /
Diverge may use a bounded linked-search operator to ask:

> What does the evidence we already possess make newly investigable?

This is **not a fifth evidence channel**.

Linked search may inspect, when useful:

- near transfer to closely related cases or artifacts;
- functional/workflow adjacency;
- failure-led and boundary cases;
- evidence-backed recombinations;
- structural or distant analogues sharing the same causal/relational mechanism.

Its output is only a `SEARCH_HYPOTHESIS`.

A `SEARCH_HYPOTHESIS` enters the ordinary opportunity funnel only after
**target evidence** is found through an authorised evidence channel. An analogy,
transfer story or recombination is not itself target-context evidence.

For non-near transfers, record only enough to falsify the connection:

- source mechanism;
- target mechanism;
- shared causal/relational structure;
- material non-transferable differences;
- nearest predicted boundary/failure;
- observation that would falsify the transfer.

If the abstraction cannot predict both a plausible positive transfer and a
nearest boundary, it is too vague to drive search.

#### Search budget

- no permanent discovery graph or ontology;
- at most **three active search hypotheses** at once;
- the cap is a ceiling, not a quota;
- distant search is optional, not required for portfolio diversity;
- stop a branch when repeated searches add examples rather than mechanisms,
  connection to proven evidence becomes indirect, no cheap discriminating test
  exists, or the branch requires multiple unproven assumptions.

Recombination is allowed only when existing evidence supports a concrete
interaction: one element removes a demonstrated limitation of another, or the
combination enables an observed job neither handles alone.

A successful technical/research transfer establishes transferability only. It
must still pass the ordinary user/job, alternatives, relative-value, adoption
and strategic-fit tests before it becomes a product hypothesis.

Dedicated adversarial review:
`docs/discovery/discovery-method-amendments-red-team-2026-09-24.md`.

## 4. One opportunity funnel

The four evidence channels feed a single funnel. Optional linked search may
generate a hypothesis, but cannot bypass the evidence gate:

```text
EVIDENCE SIGNAL
    ↓
OPTIONAL LINKED SEARCH
    ↓
SEARCH_HYPOTHESIS
    ↓
TARGET EVIDENCE REQUIRED
    ↓
CANDIDATE OPPORTUNITY
    ↓
DISCOVER / DIVERGE
    ↓
DEFINED OPPORTUNITY
    ↓
RISK + ASSUMPTION MAP
    ↓
SMALLEST EVIDENCE TEST
    ↓
DISPOSITION
    ├─ REJECT
    ├─ PARK
    ├─ REVISE
    └─ ADOPT_FOR_EXPERIMENT
```

An `ADOPT_FOR_EXPERIMENT` result still does not authorize production
implementation.

A later experiment may propose a delivery candidate. Delivery requires a
separate gate/issue and the claim-specific evidence in section 13: demonstrated
baseline failure for correctness/validity claims, or meaningful relative workflow
advantage under the validity floor for product/workflow claims.

## 5. Opportunity record

GitHub issues remain the canonical opportunity record. Do not create a second
opportunity database or product-discovery tool.

Every discovery opportunity must contain:

### Evidence trigger

- channel: `LEGAL_ADVERSARY | EXPLORER_USE | EXTERNAL_NEED | CURRENT_FAILURE`;
- concrete observation/source;
- date and context;
- whether the evidence is direct or proxy;
- if linked search preceded the signal, the originating `SEARCH_HYPOTHESIS`
  and the target evidence that converted it into a real opportunity.

A search hypothesis without target evidence is not an opportunity.

### Claim type

Declare one before the discriminating test:

- `CORRECTNESS_VALIDITY`; or
- `PRODUCT_WORKFLOW`.

Do not reinterpret the claim type after results to preserve a favored idea.

### User/research job

Describe the job/problem without proposing a solution:

> When [context], a [researcher/user] needs to [job] so that [outcome].

For non-user research opportunities, replace "user" with the concrete research
task/system obligation.

### Existing behaviour / strongest baseline / real alternative

Record:

- how the job is done now;
- the alternative the actor would realistically choose, including manual work or
  doing nothing;
- official-source/manual/repository/tool workflow used;
- what is already good enough;
- whether the opportunity claims **correctness/validity improvement** or
  **product/workflow relative advantage**;
- for product/workflow claims: the concrete difference, why the user might care,
  and what behavioural consequence would make that difference material;
- relevant adoption or switching friction;
- why the current alternative may still be insufficient even when it reaches
  the correct substantive answer.

### Consequence

State the consequence of failure:

- wrong legal conclusion;
- unsafe certainty;
- lost provenance;
- material reconstruction/review burden;
- inability to inspect/use the corpus;
- external research/reproducibility blocker.

"Would be nicer" is not enough.

### Counter-evidence

Every opportunity must record the strongest reason it may **not** deserve work.

### Risk profile

Record only material risks:

- value;
- usability;
- feasibility;
- viability/operations;
- validity/evidence integrity.

Do not pretend all five are equally risky.

### Riskiest assumption

State the one or two assumptions most capable of killing the proposed direction.

### Smallest evidence step

Choose the cheapest credible test that can change the decision:

- evidence review/data mining;
- observed user task;
- one-question follow-up;
- low-fidelity/disposable prototype;
- source-grounded legal research;
- deterministic research spike.

### Kill rule

Define before running the test what result will cause `REJECT`, `PARK` or
`REVISE`.

## 6. Evidence channel A — fresh legal adversary

### Purpose

Find new, consequential legal-information failure mechanisms or prove that the
existing corpus/protocol already handles them.

### Sourcing

Prefer:

- under-covered source systems/domains/jurisdictions from the corpus bias audit;
- new official legal events with identity/time/source-state complexity;
- real discrepancies encountered during ordinary legal research;
- orthogonal failure mechanisms rather than harder variants of exposed cases.

### Scientific firewall

Before any comparator/model run:

1. record why the candidate is legally/research-interesting;
2. record the suspected failure mechanism;
3. record decisive primary/authoritative evidence;
4. record whether this is derivation or proposed validation evidence.

Do not retain a candidate because a baseline happened to fail it.

A new trap class still needs independent support consistent with existing corpus
admission practice. One severe case can expose a representational foundation
defect, but one interesting case does not automatically earn a general failure
family.

### Success

A useful outcome can be:

- new source-grounded corpus case;
- new independently supported failure family;
- evidence that an existing class already explains it;
- parity / no new Needle requirement;
- rejection because the trap is artificial or inconsequential.

## 7. Evidence channel B — real Explorer use

### Purpose

Resolve H-16 with observed behaviour rather than technical completion.

### What counts as evidence

Strong evidence:

- an intended user attempts a realistic task in the Explorer;
- we observe what they try to do, where they hesitate, what they misunderstand,
  and whether they can reach the correct evidence owner;
- a comparison with the current repository/corpus baseline is available where
  feasible.

Weak evidence:

- asking whether the UI "looks good";
- feature requests without observing the underlying job;
- Morrow testing its own interface;
- automated browser checks;
- sponsor preference stated without use.

### Sponsor dogfood boundary

The sponsor is a legitimate expert/dogfood user and can expose real defects.

However:

- one sponsor session can justify fixing a concrete correctness/usability defect;
- it does **not** establish general external user value;
- general H-16 promotion needs evidence from additional target users or repeated
  independent use.

Do not synthesize human usability evidence when participants are unavailable.

### Initial task families

Observed tasks should include:

1. find a case relevant to a stated legal/research problem;
2. explain the decisive trap without repository archaeology;
3. identify DERIVATION versus EVALUATION status and evaluation mode;
4. reach the durable evidence owner;
5. compare two related cases without inventing a relationship.

The direct corpus/repository workflow remains the strongest simpler comparator.

## 8. Evidence channel C — external research need

### Purpose

Detect real needs from legal researchers, benchmark/evaluation researchers,
practitioners or adjacent maintainers that Needle could uniquely help with.

### Evidence hierarchy

From strongest to weakest:

1. observed external workflow/problem;
2. direct request with concrete job/context;
3. repeated independent requests;
4. issue/discussion showing attempted work and friction;
5. paper/blog/trend describing a general problem;
6. our inference that someone "would probably want" something.

Levels 5–6 may nominate an opportunity. They cannot validate value.

### Promotion rule

A direct external request may open an opportunity.

A broader product/workflow response normally needs either:

- a second independent signal from a distinct user/context; or
- one high-consequence reproducibility/research blocker where failure cannot be
  safely worked around.

Do not build integrations because another benchmark or lab has a format.

## 9. Evidence channel D — observed failure of the current approach

### Purpose

Let the project itself reveal what needs work.

Eligible signals:

- wrong or unsafe legal conclusion;
- evidence lineage/provenance defect;
- evaluation contamination or construct failure;
- Explorer causes a material interpretation failure;
- repeated case-admission/research rework;
- CI/automation behaviour that undermines the active research outcome;
- an existing contract cannot honestly represent a real source-backed case.

Ineligible signals:

- hypothetical future scale;
- dormant code that looks untidy;
- a feature being technically possible;
- one-off cosmetic inconvenience.

### Severity rule

One demonstrated correctness/provenance/evidence-integrity failure can justify
immediate investigation.

Workflow convenience or authoring friction requires recurrence before it becomes
a project opportunity.

## 10. Discovery method per opportunity

### Step 1 — Discover / diverge

Collect enough evidence to understand:

- user/research context;
- current workaround;
- related cases;
- constraints;
- competing explanations;
- adjacent precedent.

Do not brainstorm implementations first.

Optional linked search may be used here only from a concrete evidence anchor or
proven mechanism. It produces `SEARCH_HYPOTHESIS` records, not opportunities.
No target evidence means no promotion into Define.

### Step 2 — Define / converge

Write one falsifiable problem statement.

For correctness / evidence-integrity claims:

> In [context], [actor] cannot reliably [job] using [strong baseline] because
> [observed failure], causing [consequence].

For product / workflow claims where the alternative may still be correct:

> In [context], [actor] can accomplish [job] using [current alternative], but
> [observed burden/friction] creates [consequence]. Needle may create
> [specific relative advantage] large enough to change [relevant behaviour].

If neither statement can be written from evidence, park or reject.

### Step 3 — Relative-value check and risk map

For product/workflow opportunities, explicitly separate:

1. difference;
2. user importance;
3. behavioural consequence;
4. adoption/switching friction.

Do not treat correctness parity as automatic product-value parity.

Then identify which of the five risk dimensions could invalidate the response
and select the riskiest assumption(s) by importance × evidence weakness.

### Step 4 — Smallest evidence test

Choose one bounded test.

Prefer, in order:

1. existing data/evidence;
2. observation/interview;
3. manual workflow;
4. low-fidelity/disposable prototype;
5. technical research spike.

Production feature implementation is not a discovery technique.

Disposable prototype code must not silently become production architecture. It
may live on an experiment branch or be preserved only as evidence; it does not
enter the maintained product without a delivery decision.

### Step 5 — Decision

End with exactly one:

- `ADOPT_FOR_EXPERIMENT`
- `REVISE`
- `REJECT`
- `PARK`

Record what evidence would be required to reopen a rejected/parked idea.

## 11. Discovery budget and cadence

This phase is **bounded continuous discovery**, not an endless programme.

### WIP

- one active discovery opportunity at a time;
- one issue, one branch/PR when repository changes are required;
- human research may be pending while an autonomous sensing task runs, but it
  may not be replaced by synthetic user evidence.

### Per-opportunity budget

An opportunity gets:

- one initial discovery run;
- at most one follow-up evidence run before a mandatory disposition.

A third run requires genuinely new external/source evidence and must explain why
the previous decision boundary changed.

This prevents "research until yes."

### Initial cycle

Cycle 1 contains four sensing tasks and one synthesis gate:

1. fresh legal-adversary scout;
2. Explorer observed-use round;
3. external research-needs scan;
4. current-approach failure audit;
5. cycle synthesis / Project Health Check.

The cycle ends after these tasks even if no opportunity survives.

It does not automatically schedule Cycle 2.

## 12. Initial cycle acceptance

Cycle 1 is complete when:

- each evidence channel has been sampled once;
- every discovered opportunity has a canonical issue or an explicit rejection;
- human evidence is clearly separated from proxy/synthetic evidence;
- no feature was implemented to manufacture evidence;
- negative/parity findings are preserved;
- the synthesis compares competing project identities;
- the synthesis chooses `continue / simplify / redirect / stop`;
- any proposed next experiment identifies its trigger, riskiest assumption, kill
  rule and stronger-baseline comparator.

If Explorer participants are unavailable, record that limitation and keep H-16
unresolved. Do not substitute agent/browser testing for human evidence.

## 13. Promotion to experiment or delivery

### Discovery → experiment

`ADOPT_FOR_EXPERIMENT` requires:

- evidence-backed problem/opportunity; a linked-search hypothesis alone is
  insufficient;
- claim type frozen before the discriminating test;
- explicit alternative explanation;
- strongest baseline documented;
- one or two riskiest assumptions;
- smallest falsifiable test;
- predeclared kill rule;
- validity/contamination boundary.

### Experiment → delivery candidate

A later experiment may propose delivery only when:

1. the observed problem is recurring or materially consequential;
2. **for correctness/validity claims:** the strong baseline materially fails for
   the tested context;
3. **for product/workflow claims:** either the baseline fails or Needle
   demonstrates a meaningful relative advantage over the real alternative,
   including evidence that the difference matters to the user and is plausibly
   large enough to affect behaviour despite adoption/switching friction;
4. no material correctness, provenance, uncertainty-handling or
   evidence-integrity regression falls below the validity floor;
5. usability risk has evidence if humans must operate it;
6. feasibility is known for the smallest useful slice;
7. operational/viability cost is acceptable;
8. evidence validity/provenance remains intact;
9. the implementation can stay smaller than the problem it solves.

A delivery candidate still requires a separate project decision/issue.

## 14. Discovery quality checks

Do not create discovery KPIs.

When selecting a future follow-up, name the research decision that support or
rejection would change and what existing evidence cannot already decide. A
consequence may be improved coverage, scoring, diagnosis or a regression case;
it need not be commercial demand. A new class is neither necessary nor
sufficient. Do not reject a useful case solely because an existing class explains
it. This check does not amend already frozen experiment criteria.

At synthesis ask:

- Did evidence change a decision?
- Did any attractive idea get rejected or reduced?
- Was the real alternative / strongest baseline genuinely tested?
- Where did the baseline fail on correctness or evidence integrity?
- Where did it remain substantively correct but Needle show a meaningful
  workflow/product relative advantage?
- For any claimed advantage: was the difference real, important to the user and
  large enough to plausibly change behaviour despite adoption/switching costs?
- Did we learn about a real user/research job rather than collect opinions?
- Did we preserve negative evidence?
- Did any proposed complexity earn itself?
- Is the smaller project identity still sufficient?

If discovery only produces more backlog, the discovery system is failing.

## 15. Automation boundary

There is no permanent scheduled discovery worker by default.

Automation may execute an already-ready evidence task. It must not invent a new
opportunity because the queue is empty.

Human evidence channels remain human:

- Explorer use cannot be simulated by the agent;
- external direct demand cannot be inferred from trend articles;
- legal validation cannot be replaced by an LLM claiming an expert would agree.

## 16. Canonical ownership

- this document owns the discovery operating plan;
- the active parent GitHub issue owns the bounded cycle;
- child issues own concrete sensing/discovery work;
- `BACKLOG.md` owns current execution order;
- `docs/assumptions.md` owns only material live beliefs;
- `docs/value-evidence.md` changes only when discovery changes the project
  thesis/direction;
- delivery artifacts remain separate.

No new product-management database, opportunity schema or dashboard is needed.

## 17. Stop condition for the discovery system itself

After Cycle 1, stop or simplify this discovery model if:

- evidence channels mostly produce manufactured/hypothetical opportunities;
- external/user evidence cannot be obtained and autonomous research merely
  rephrases internal beliefs;
- the same opportunities repeatedly return after rejection without new evidence;
- discovery overhead exceeds the research work it protects;
- the strong baseline continues to solve every meaningful problem and no
  Needle-specific response earns itself.

The discovery process is itself an experiment and does not receive permanent
status merely because it is industry-informed.

