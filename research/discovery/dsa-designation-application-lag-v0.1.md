# Discovery — the designation can end before the obligations do

**Date:** 2026-09-23  
**Issue:** #78  
**Status:** adversary pinned; Authoritative Dynamic Set v0.1 survives by composing with Temporal v0.1

## The question

Issue #77 established a new canonical object for authoritative dynamic sets.

The next adversary asks whether we accidentally made membership state do too much.

The Digital Services Act provides an unusually clean test because Article 33(6)
deliberately separates:

1. designation or termination;
2. publication of the designated-services list;
3. application or cessation of the special Section 5 obligations.

The third event occurs only four months after notification.

## Stripchat produces both possible divergence windows

The Commission designated Stripchat as a VLOP on 20 December 2023.

The Commission later stated that the additional obligations became applicable
to Stripchat on **21 April 2024**.

So there is a period in which:

```
authoritative set state: INCLUDED / DESIGNATED
special Section 5 obligations: NOT YET APPLICABLE
```

Then the Commission terminated Stripchat's designation on **27 May 2025**.

Its current supervision page states that the VLOP obligations ceased four
months after that decision.

This creates the mirror-image period:

```
authoritative set state: NOT INCLUDED / DESIGNATION TERMINATED
special Section 5 obligations: STILL APPLICABLE
```

With the four-month calculation pinned from the official dated decision, the
application end is represented as an exclusive boundary on **27 September
2025**.

## Why this matters

A system that asks only:

> Is Stripchat currently in the VLOP set?

cannot reconstruct whether Section 5 obligations applied on a historical date.

For example, on 1 June 2025:

- designation state says **no longer designated**;
- application state says **Section 5 obligations still active**.

Neither state is wrong.

They answer different questions.

## Architecture result

**Authoritative Dynamic Set v0.1 survives.**

The key is to interpret its `effective_from` field narrowly:

> the authoritative set/member state changes from this date.

It is **not**:

> every downstream legal effect changes from this date.

Temporal v0.1 already owns the downstream application interval.

The two contracts therefore compose as:

```
authoritative set transition
        │
        │ causal predicate / classification state
        ▼
temporal assertion
        │
        │ separate application boundary
        ▼
derived question: do Section 5 obligations apply on date X?
```

No dynamic-set schema change is required.

## Strong guardrail

The new canonical invariant is:

> **set-state time is not application time**

even where legal effect is conditioned on authoritative set membership.

The DSA demonstrates that a removed member can remain subject to the dependent
regime during a statutory tail, and a newly added member can wait before the
dependent regime starts.

## Why this is a useful non-break

The previous wild run found a genuine missing primitive.

This run shows that the primitive is narrow enough to survive a hostile temporal
case without absorbing temporal semantics.

That is stronger evidence for the architecture than another successful
same-shape fixture.

## Pinned artifacts

- `fixtures/dependency/dsa-vlop-vlose-authoritative-dynamic-set-v0.1.json`
- `fixtures/temporal/dsa-stripchat-designation-application-lag-v0.1.json`
- `tests/test_dsa_designation_application_lag.py`

No X-Ray work and no new product surface are justified by this case.
