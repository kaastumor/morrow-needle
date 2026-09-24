# Cycle 3 Run 3B — official registry coverage negative inference

Issue: #179  
Parent: #177  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven anchors

- #93 official tracker/update-horizon failure;
- #174 derived-view boundary work;
- `DYNAMIC_REFERENCE_STATUS`;
- #85 recognised-external-determination/source-role discipline.

The search question was:

> When does absence from an official register/list safely support a negative
> legal conclusion, and when does it only prove absence from the register's
> declared coverage?

The target is not generic incompleteness.

## Target 1 — EU Union Register of medicinal products

The European Commission describes the Union Register as listing medicinal
products that received a Commission marketing authorisation through the
**centralised procedure**.

It separately exposes:

- mutual-recognition product indexes;
- national registers;
- nationally authorised products for which specific Commission decisions were
  required.

Official sources:

- https://health.ec.europa.eu/medicinal-products/union-register_en
- https://ec.europa.eu/health/documents/community-register/html/

### Unsafe negative inference

```text
product absent from Union Register
    ↓ INVALID
product has no EU / Member-State marketing authorisation
```

Absence from the centralised register cannot by itself exclude authorisation
through a national or mutual-recognition route.

### Safe narrower inference

Subject to identity/update verification, absence may be evidence that the
product is not present **as a centrally authorised medicinal product in that
register**.

The legal predicate matters.

## Target 2 — EU Safety Gate

Safety Gate is the EU rapid alert system for dangerous non-food products.

Its official architecture is event/measure based:

- national authorities detect a dangerous product;
- corrective measures are notified;
- information is circulated;
- a summary is published to the public portal.

The 2025 report states that:

- serious-risk measures are required notifications;
- less-than-serious-risk measures may also be notified;
- the public portal publishes summaries of alerts;
- some product sectors such as pharmaceuticals, medical devices, food and feed
  are outside Safety Gate because they use separate systems.

Official sources:

- https://commission.europa.eu/topics/business-and-industry/product-safety_en
- https://op.europa.eu/webpub/just/safety-gate-2025-report/en/
- Commission Delegated Regulation (EU) 2024/3173:
  https://eur-lex.europa.eu/eli/reg_del/2024/3173/oj/eng

### Unsafe negative inference

```text
product absent from Safety Gate
    ↓ INVALID
product is safe / legally compliant / has never posed a relevant risk
```

The portal is not an exhaustive registry of all safe/unsafe products.

Its content depends on:

- detection by market surveillance;
- corrective measures;
- notification rules;
- product-sector scope;
- public-alert publication.

The absence is therefore bounded by the alert system's reporting universe.

## Boundary 1 — authentic complete set for a narrow predicate

ECHA's REACH Candidate List provides the opposite shape.

ECHA states:

- only the Candidate List published on its website is deemed authentic;
- legal obligations may arise immediately from inclusion;
- the list is published under Article 59(10) REACH.

Source:

- https://echa.europa.eu/candidate-list-table

For the narrow predicate:

> is this substance within the current Candidate List scope?

the authentic list is designed to own that set.

However, even this control shows that **identity resolution matters**:

- entries can cover hydrated forms;
- group entries may cover multiple CAS/EC identities;
- identifier inventories can be non-exhaustive.

So:

> no exact CAS-string hit

is not always equivalent to:

> substance not covered by any Candidate List entry.

The control supports careful negative inference, not naive search-string
absence.

## Boundary 2 — registry completeness can change over time

EUDAMED illustrates a temporal coverage boundary.

The Commission states that:

- UDI/device registration was voluntary from October 2021;
- the first four EUDAMED modules became mandatory from 28 May 2026.

Sources:

- https://health.ec.europa.eu/medical-devices-eudamed/overview_en
- https://health.ec.europa.eu/medical-devices-eudamed/udidevice-registration_en

Therefore the evidentiary meaning of "not found in EUDAMED" cannot be assumed
constant across time.

Run 3B does not attempt a device-specific legal conclusion beyond this
documented transition.

## Strongest baseline

The boring baseline is straightforward:

1. identify exactly what legal/administrative universe the registry covers;
2. identify whether inclusion is constitutive, declaratory, event-based or only
   informational;
3. check coverage exclusions;
4. check update/transition horizon;
5. resolve entity/substance identity;
6. infer absence only for the exact covered predicate.

A careful domain expert can do this without Needle.

No product value is claimed.

## Structural correspondence

The shared mechanism is:

```text
official registry/list queried
    ↓
no matching entry observed
    ↓
registry coverage/completeness contract omitted
    ↓
negative observation promoted to broader legal negative
```

The failure can come from different coverage dimensions:

- procedure route;
- sector;
- reporting trigger;
- temporal rollout;
- identity/group scope.

The common error is **predicate widening**.

## Existing taxonomy check

### OFFICIAL_TRACKER_UPDATE_LAG

Does not own.

A registry can be perfectly current yet still not cover the broader universe the
researcher infers.

### DYNAMIC_REFERENCE_STATUS

Does not own.

The error does not require a referenced item's authoritative status to change.

### PRIVATE_ORIGIN_LEGAL_RECOGNITION

Does not own.

The issue is registry coverage, not public-law recognition of a private output.

No existing class directly captures negative inference beyond registry scope.

## One falsifiable hypothesis

Working label:

`OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM`

Hypothesis:

> Legal research can produce consequential false-negative conclusions by
> treating absence from an official registry/list as evidence of absence from a
> broader legal universe than the registry's declared coverage.

## Smallest discriminating experiment

If selected by #183:

1. run a metadata-only transport smoke test for the selected official registries;
2. pre-register three fresh registry questions from different coverage shapes:
   - procedure-scoped authorisation registry;
   - event/reporting-scoped safety registry;
   - one authentic/complete narrow-set control;
3. freeze the exact legal predicate being tested;
4. freeze the registry coverage contract;
5. construct a realistic negative lookup;
6. determine whether the negative observation supports:
   - the narrow predicate;
   - the broader user claim;
7. test whether one shared failure mechanism explains both positives.

### Success

- two independent registries produce materially wrong broad negative
  conclusions;
- the registries themselves are not stale or defective;
- the error is caused by widening the predicate beyond coverage;
- the control shows a case where absence is valid for the narrow covered set.

### Kill

Reject if:

- every case is merely a stale-data problem already owned by #93;
- no realistic decision changes;
- each registry needs unrelated domain-specific reasoning with no reusable
  mechanism;
- or the result reduces to generic "read the website scope" advice without a
  consequential failure pattern.

## Run 3B disposition

# **ADOPT_FOR_EXPERIMENT**

Retain:

`OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM`

The candidate is orthogonal to update lag:

> current and accurate data can still support a wrong conclusion when the
> queried universe is narrower than the inferred legal predicate.

Do not add a class yet.

Do not build:

- registry aggregator;
- product search;
- medicine/device lookup;
- Safety Gate tooling;
- registry ontology.

Only a bounded fresh generality test may be considered at #183.
