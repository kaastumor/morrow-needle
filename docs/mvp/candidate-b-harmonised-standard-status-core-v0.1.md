# Candidate B — Harmonised Standard Status Card v0.1

Status: **DISPOSABLE INTERNAL MVP CORE — USER VALUE UNPROVEN**

## Job

For one product-compliance regime and one European standard, answer:

> **As of date T, does this standard's Official Journal reference confer a presumption of
> conformity, is that presumption restricted, or is there no such OJ-reference presumption?**

Then show:

- what official event owns the state;
- when it became effective;
- any restriction/scope;
- what **does not** follow.

## Why this is Candidate B rather than generic monitoring

Monitoring/RSS answers:

> something changed.

The status card answers:

> **what legal status does the official publication state create for this standard under this
> governing rule at this date?**

#407 already removed generic source monitoring from Needle-specific value.

The candidate core therefore begins **after** an official event/reference state is available.

## Canonical owner

No new ontology is introduced.

The legal-state owner remains:

> `schemas/authoritative-dynamic-set-v0.1.schema.json`

Historical interface decision:

> `docs/decisions/authoritative-dynamic-set-v0.1-interface-freeze.md`

That contract was originally earned on:

- Toy Safety OJ-reference restriction;
- REACH Candidate List membership.

#409 adds a third orthogonal standards-state regression:

- GAR EN 497:2022 formal decision **not to publish** the reference.

## Human-facing card

### Regime

`<legislation / governing provision>`

### Standard

`<EN identifier>`

### As of

`<date>`

### OJ-reference state

One of:

- **CITED**
- **CITED_WITH_RESTRICTION**
- **NOT_CITED**

These are view states derived from canonical membership/status; they are not a new legal ontology.

### Presumption consequence

One of:

- **AVAILABLE_WITHIN_COVERED_SCOPE**
- **RESTRICTED_TO_STATED_SCOPE**
- **NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE**

### Latest owning event

`<decision/publication + effective date>`

### Scope / reason

`<direct official scope statement>`

### Evidence

`<binding act / OJ decision references>`

### Non-implications

Preserve relevant forbidden inferences, especially:

- a European standard's existence/adoption does not by itself create OJ-reference legal effect;
- no OJ presumption does not mean use of the standard is forbidden;
- no OJ presumption does not mean no alternative conformity route exists;
- a restriction/non-publication event is not a textual amendment of the parent regulation.

## Derived-state rules

For a standards-reference authoritative set:

- `INCLUDED + ACTIVE/UNRESTRICTED` -> `CITED / AVAILABLE_WITHIN_COVERED_SCOPE`;
- `INCLUDED + RESTRICTED` -> `CITED_WITH_RESTRICTION / RESTRICTED_TO_STATED_SCOPE`;
- `NOT_INCLUDED` -> `NOT_CITED / NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE`.

The card must still show the latest transition scope because two `NOT_CITED` states can differ
materially:

- no citation has yet occurred;
- the Commission has formally decided not to publish the reference;
- a previously cited reference has been withdrawn.

v0.1 does **not** invent separate canonical enum values for those subtypes.

## Historical query

The card must accept an `as_of` date and apply only transitions effective on/before that date.

This is a core Needle distinction:

> current status must not overwrite historical status.

## Strong baseline

The baseline gets full credit for:

- Commission harmonised-standards pages;
- formal-objection page;
- RSS feeds;
- EUR-Lex/OJ;
- standards-body alerts;
- accessible compliance tools.

The card earns product relevance only if users prefer its decision-ready/history/evidence output
enough to matter.

## Current examples

### Toy Safety — EN 71-1:2014+A1:2018

Before 10 September 2025:

> `CITED / AVAILABLE_WITHIN_COVERED_SCOPE`

From 10 September 2025 for the specified wave-roller clauses/scope:

> `CITED_WITH_RESTRICTION / RESTRICTED_TO_STATED_SCOPE`

### GAR — EN 497:2022

Before 24 July 2026:

> `NOT_CITED / NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE`

From 24 July 2026:

> still `NOT_CITED / NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE`, but now with a direct Commission
> decision not to publish the reference.

The unchanged high-level result with a materially different evidence/state reason is exactly why
the owning event and history remain first-class.

## Current claim

Supported:

> existing Needle state machinery can represent and render this legal-status job without a new
> ontology.

Not supported:

- that this card is unique;
- that current competitors get these cases wrong;
- that a user will pay for it;
- that it reduces expert time;
- that this should become a general compliance platform.