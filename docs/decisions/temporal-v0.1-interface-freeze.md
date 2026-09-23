# Decision — Freeze Temporal Semantics v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #5

## Decision

Freeze the P0-E temporal foundation around two stable interfaces:

- `schemas/temporal-assertion-v0.1.schema.json`
- `schemas/temporal-query-v0.1.schema.json`

with deterministic evaluation in:

- `src/needle/temporal/resolver.py`

Future temporal edge cases should normally extend fixtures, source adapters, or higher-level rule models. A core temporal-contract change now requires an official adversarial case that cannot be represented without semantic distortion.

## Stable v0.1 model

A temporal assertion expresses one boundary on one dimension:

- PUBLICATION
- LEGAL_FORCE
- APPLICATION
- TEXT_STATE
- TRANSITION
- DEROGATION
- DEADLINE

Each assertion has:
- a legal subject;
- point/start/end boundary;
- absolute-date or event-relative trigger;
- explicit scope;
- explicit default/override relationship;
- resolution state;
- evidence state;
- official source references.

No generic `effective_date` exists.

## Query perspective is mandatory

Historical queries must state which timeline they mean:

### EX_POST_LEGAL_EFFECT
Evaluate date X using the full later-known legal history, including retroactive acts and later corrections.

### OFFICIAL_SOURCE_STATE_AS_OF
Evaluate date X only using official sources available by cutoff Y.

This does **not** claim what any person actually knew. It reconstructs the official-source state as of a date.

An ambiguous historical query with no perspective fails the query contract.

## Adversaries passed in CI

### Force vs application
GDPR demonstrates that an act may be legally in force while not yet generally applicable.

### Scoped provision override
The Digital Services Act demonstrates that explicit provisions may apply before the act-wide default.

### Entity-relative trigger
The DSA also demonstrates that applicability may depend on a provider-specific notification event. Missing context returns `CONTEXT_REQUIRED`; Needle does not invent a universal date.

### Text state vs application
Implementing Regulation 2025/905 demonstrates that amended text may exist in the legal text state before a specific inserted requirement becomes applicable.

### Gapped regime succession
The 2021/1232 → 2026/1881 temporary-regime lineage demonstrates that genealogical succession may cross a real legal void.

### Retroactive application
Implementing Regulation 2023/2773 applies from 1 January 2023 although it was adopted and published in December 2023. Therefore APPLICATION may predate LEGAL_FORCE.

The bitemporal query contract correctly distinguishes:
- ex-post application to June 2023;
- official-source state as of June 2023, when that later act was not yet officially available.

### Overlapping transition layers
The Medical Devices Regulation demonstrates simultaneous applicability of a new regime and a bounded legacy transition. It also shows different end dates for:
- a narrower Article 120(3) placement derogation;
- the broader old-directive transition needed for Article 120(3)-(4).

Temporal states are therefore not exclusive global statuses.

## Durable invariants

1. Publication, force, application, text-state validity, deadlines, transition and derogation are separate dimensions.
2. Act-level dates must not be blindly propagated to every provision or mutation.
3. Overrides are explicit evidence relationships; specificity is not inferred from labels.
4. Relative temporal rules retain their source event and offset.
5. Missing entity/event context produces a context-required state.
6. Legal genealogy does not imply continuous applicability.
7. Retroactive application is valid data; do not enforce application >= entry into force.
8. Historical legal-effect time and official-source availability time are separate query axes.
9. Transition regimes may overlap with the successor regime and may end in layers.
10. Temporal conflicts and unresolved source availability must remain visible.

## Post-freeze rule

Reopen the core temporal contract only when an official source demonstrates a legal-time phenomenon that cannot be represented through:
- a new assertion;
- an explicit scope/override;
- an event-relative trigger;
- a query perspective;
- or a bounded regime/transition assertion.

P0-E no longer blocks downstream work.


## Reopen trigger — Issue #81 (2026-09-23)

Temporal v0.1 is **reopened** by the official HVMFS 2025:4 real-time fishery
closure.

The source fixes legally operative boundaries to the minute:

- start: 18 February 2025 at 01:00 Swedish time;
- cessation: after 4 March 2025 at 00:59 Swedish time.

Commission Delegated Regulation (EU) 2019/2201 Article 8 expresses the same
mechanism in UTC: start at 24:00 UTC on the decision day and automatic cessation
at midnight UTC after 14 days.

The v0.1 schema and resolver are date-only and cannot distinguish legal states
within one calendar day. Rounding would change answers and is prohibited.

Issue #81 therefore satisfies the post-freeze rule: an official legal-time
phenomenon cannot be represented through another date-only assertion, scope,
relative trigger, perspective or bounded transition.

v0.1 remains valid for date-precision cases. The next temporal version must add
explicit offset-aware instant precision without rewriting historical date truth.


## Reopen resolution — Temporal v0.2

Issue #81 is resolved by the precision-aware Temporal v0.2 contract:

- `schemas/temporal-assertion-v0.2.schema.json`
- `schemas/temporal-query-v0.2.schema.json`
- `src/needle/temporal/resolver_v0_2.py`
- `docs/decisions/temporal-v0.2-interface-freeze.md`

v0.1 remains valid provenance and a stable representation for DATE-precision
cases. It is superseded as the canonical interface whenever an official source
requires sub-day precision.

v0.2 adds only explicit `DATE` versus offset-aware `INSTANT` precision.
It does not infer timezones or reinterpret legacy dates as midnight instants.

Canonical validation after hardening:
- 569 Python tests passed;
- repository sanitation passed;
- post-P1 foundation audit passed.

The spatial research that exposed the failure may resume.
