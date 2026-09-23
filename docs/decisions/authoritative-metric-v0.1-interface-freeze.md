# Decision — Authoritative Metric Observation + Metric Rule Evaluation v0.1

**Date:** 2026-09-23  
**Status:** ADOPTED  
**Issue:** #79

## Problem

Needle had canonical owners for:

- source bytes;
- textual/structural mutations;
- temporal state;
- procedure state;
- authoritative dynamic-set membership/status.

It did not have an honest causal owner for a different pattern:

> a binding legal rule remains textually unchanged while an authority publishes
> or determines a numeric value that the rule uses as an operative input.

Two independent official cases demonstrate that this is not a domain-specific
oddity.

## Proof case 1 — EU ETS TNAC

Decision (EU) 2015/1814 requires annual publication of the Total Number of
Allowances in Circulation.

For 2025, Commission Communication C/2026/2957 publishes:

`TNAC = 1 023 494 202 allowances`.

The relevant Article 1(5) band requires:

`TNAC - 833 000 000`

to be placed in the Market Stability Reserve.

The derived result is:

`190 494 202 allowances`.

The Communication independently corroborates that exact result.

## Proof case 2 — vehicle CO2 manufacturer performance

Commission Implementing Decision (EU) 2024/865 publishes for
BUGATTI AUTOMOBILES SAS in calendar year 2022:

- distance to target: +448.746 g CO2/km;
- registrations: 8 vehicles.

Regulation (EU) 2019/631 Article 8 fixes:

`excess emissions × EUR 95 × registrations`.

The deterministic derived amount is:

`EUR 341 046.96`.

That exact monetary amount is not promoted to direct Commission evidence.

## Decision

Introduce two deliberately separate contracts.

### Authoritative Metric Observation v0.1

Canonical direct numeric truth:

- metric identity;
- value and unit;
- subject;
- reference period;
- authority;
- determination character;
- exact official source;
- binding legal relevance.

It does **not** own legal rule evaluation.

### Metric Rule Evaluation v0.1

Canonical derived numeric legal evaluation:

- governing binding rule;
- references to authoritative metric observations;
- simple numeric predicate result;
- formula statement;
- metric inputs and legal constants;
- derived numeric result;
- optional official corroboration.

It does **not** own metric truth or temporal application.

## Why they are separate

The same observation may be re-evaluated if the law later changes.

The same fixed rule produces a different output from a later observation.

Correcting official metric truth must not mutate the rule.

Changing a rule must not rewrite historical metric observations.

## Deliberate limits

v0.1 is **not a general rules engine**.

There is no executable expression language and no arbitrary code field.

The contract records a bounded, auditable deterministic arithmetic claim.

Pinned regressions independently recompute the two proof cases.

Supported predicate vocabulary is intentionally small:

- greater/less than;
- greater/less than or equal;
- equality;
- inclusive numeric band.

If a future legal rule requires non-scalar logic, this schema should fail rather
than accumulate an ad-hoc expression language.

## Existing contracts retained

### Source Observation v0.1

Still owns immutable source bytes. It does not own extracted metric semantics.

### Authoritative Dynamic Set v0.1

Still owns membership/status transitions. Numeric observations are not coerced
into members.

### Temporal v0.1

Still owns publication/application/transition dates. Metric Evaluation explicitly
sets `owns_temporal_application = false`.

### Change Atom v0.3

Retained for textual-mutation-derived semantic claims.

Metric Rule Evaluation is a parallel causal path. No fake source mutation is
created simply to make a metric-conditioned effect look like a Change Atom.

## Reopen rule

Reopen only when an official case proves one of:

- authoritative legal input cannot be represented as one numeric value + unit;
- a numeric rule predicate cannot be represented by the bounded comparison
  vocabulary;
- deterministic output cannot be preserved without executable formula semantics;
- multiple observations cannot be referenced without collapsing their separate
  provenance;
- metric truth and rule-evaluation truth cannot remain independently versioned.
