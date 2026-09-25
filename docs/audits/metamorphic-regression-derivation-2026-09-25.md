# Issue #313 — metamorphic regression derivation

Date: 2026-09-25  
Disposition: **ADOPT_METAMORPHIC_DERIVATION**

## Question

Can already-frozen, exposed Needle cases support rigorous metamorphic regression relations
without adding scientific cases, inventing historical answer keys, or converting exposed
material into fresh evaluation?

## Strict definition

For this project, a derived metamorphic regression relation requires all of:

1. an already accepted/exposed source case;
2. a scenario held sufficiently fixed to isolate one named legally material state
   variable;
3. an evidence-backed mutation of that variable;
4. an evidence-backed consequential expected relation/outcome on both sides;
5. no new legal research needed to create either side.

A shared trap class is **not** enough.

The relation is post-hoc regression engineering. It is never historical experimental
design and never fresh validation.

## Bounded audit

Four mechanically diverse candidates were tested.

### MR-01 — sub-day temporal boundary: PASS

Source case: `adv-licence-1300-boundary`.

The original exposed #88 task already supplies the controlled pair:

- same authority;
- same Tuesday;
- otherwise valid applications;
- 12:59 Brussels time versus 13:01.

The frozen answer key requires:

- 12:59 -> deemed lodged Tuesday;
- 13:01 -> deemed lodged Wednesday.

Only the receipt time crosses the legally material 13:00 boundary.

This is an unusually strong metamorphic relation because no synthetic task construction is
needed: both sides were already part of the exact historical evaluation prompt.

### MR-02 — DSA application boundary: PASS

Source case: `dsa-stripchat-status-application-lag`.

The existing temporal fixture records:

- `DESIGNATED_BUT_SECTION5_NOT_YET_APPLICABLE` through 2024-04-20;
- Section 5 application start at 2024-04-21.

Selecting the adjacent dates 20/21 April holds Stripchat's designation state constant while
the APPLICATION dimension changes.

Expected relation:

> designated/Section-5-not-yet-applicable -> designated/Section-5-applicable.

This directly tests the class's central anti-collapse property: designation and
application are independent legal-state dimensions.

The same fixture also contains a second possible end-boundary relation after termination,
but v0.1 deliberately records only one relation per source case to avoid inflating the
derived layer.

### MR-03 — dynamic reference status: PASS

Source case: `toy-wave-roller-dynamic-standard-gateway`.

The existing fixture explicitly proves the invariants:

- Directive 2009/48/EC Article 13 text is unchanged;
- its text hash is preserved;
- EN 71-1:2014+A1:2018 identity is unchanged.

The changed variable is the authoritative OJ reference status for the wave-roller scope:

- before: published without the wave-roller restriction;
- from 2025-09-10: same standard reference with a restriction.

The derived local effect changes accordingly: the unchanged Article 13 gateway produces a
narrower presumption for the specified clauses.

This is a true metamorphic relation because the fixture was built precisely to isolate
external status from parent-text and identifier mutation.

### MR-04 — Member-State participation state: PASS WITH BOUNDARY

Source case: `ireland-aamm-protocol21-post-adoption-opt-in`.

The #273 result preserves:

- same Union act: Regulation (EU) 2024/1351;
- same Member State: Ireland;
- adoption state: Ireland did not participate and was not bound under the preserved
  Protocol 21 position;
- later Article 4 notification / Commission Decision (EU) 2024/2088;
- Decision entry into force: 2024-08-22;
- later state: Ireland participates.

The controlled variable is the legally confirmed participation state over time.

Boundary:

> This relation tests participation/binding state, **not** whether every substantive
> obligation of Regulation 2024/1351 became applicable on 22 August 2024.

Without that boundary the pair would conflate participation with downstream application
and recreate the kind of state collapse Needle exists to preserve.

## Negative controls

### Same class, different agreements — NOT metamorphic

`eu-mercosur-parallel-agreement-lifecycle` and
`eu-mexico-parallel-agreement-lifecycle` share
`PARALLEL_INSTRUMENT_LIFECYCLE`.

They are useful independent/analogous cases, but they differ in:

- counterparties;
- instruments;
- procedure;
- dates;
- lifecycle states.

Calling them a metamorphic pair would use class similarity as a substitute for controlled
mutation. Rejected.

### Multi-dimensional composition — NOT a one-variable pair

`matrimonial-property-participation-law-forum-composition` deliberately composes:

- participation;
- choice of law;
- choice of forum.

Its value is that the state dimensions coexist and must remain separate. Turning the case
into one metamorphic pair without additional preserved facts would arbitrarily choose or
invent a counterfactual state. Rejected for v0.1.

### Plausible counterfactual from trap text — INVALID

For `brussels-i-choice-of-forum`, one could easily imagine "valid clause" versus
"invalid/protected-party clause".

But the canonical case record does not preserve a single controlled factual scenario for
both sides. Creating one from the class definition would be new task synthesis and could
smuggle in unresearched facts. Rejected.

## Added value over ordinary case-by-case regression

Ordinary known-case regression asks:

> Does the system still get this exposed case right?

A valid metamorphic relation adds a narrower property:

> When one evidenced legal-state variable changes and the controlled facts remain fixed,
> does the answer change (or remain invariant) in the exact expected way?

This has useful regression value because it targets **state-collapse errors** rather than
only full-answer correctness.

Examples:

- crossing 13:00 must change deemed lodgement day;
- crossing an application boundary must change applicability without changing designation;
- changing an OJ reference restriction must change the derived presumption without a
  parent-text mutation;
- changing confirmed participation state must change the participation answer without
  rewriting the act identity.

This is a real additional regression discipline even though it provides no new scientific
validation.

## Leakage / scientific boundary

Every relation is derived from already exposed material.

Therefore:

- all relations are `REGRESSION_ONLY`;
- success says nothing about fresh latent detection;
- the derived map may not be counted as four additional corpus cases;
- a system trained or prompted with the map cannot be evaluated on these relations as if
  they were unseen;
- relation count is not evidence of class importance or model performance.

## Artifact

The bounded derived map is:

`fixtures/regression/frozen-reference-metamorphic-v0.1.json`

It contains four manually evidenced relations. It is intentionally **not**:

- a new schema;
- an exhaustive generator;
- a new corpus index;
- a benchmark;
- a model-evaluation runner.

## Disposition

**ADOPT_METAMORPHIC_DERIVATION**

The concept survives when the burden is strict: relations must be earned from existing
evidence that already isolates the mutation.

Do not generalise from these four examples into "all 26 classes are metamorphic". Future
relations may be added only when an existing accepted evidence owner already contains the
controlled transition or a separately authorised new research task establishes it.

The scientific reference remains exactly **81 cases / 26 classes**.
