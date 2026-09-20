# Temporal model convergence v0.1

**Date:** 2026-09-20  
**Status:** ACTIVE FOUNDATION DECISION  
**Issue:** #5

## Decision

Use `schemas/temporal-assertion-v0.1.schema.json` as the canonical P0-E temporal contract.

The earlier `schemas/temporal-applicability-v0.1.schema.json` and its DSA fixture are retained as discovery provenance because they correctly falsified the assumption that applicability always has a universal absolute date. They are not a second core model.

## Why the assertion model supersedes the precursor

A single "applicability" object is too narrow. Needle must preserve independent temporal dimensions:

- publication;
- legal force;
- application;
- text-state validity;
- transition;
- derogation;
- deadlines.

Each assertion has:
- an explicit subject;
- one temporal dimension;
- a boundary (point/start/end);
- an absolute or event-relative trigger;
- explicit scope/default/override semantics;
- evidence state and official source references;
- a resolution state that may be `CONTEXT_REQUIRED` or `CONFLICTING`.

Overrides are explicit relationships between assertions. The resolver does not infer precedence from article labels or apparent specificity.

## Adversaries currently passing in CI

### GDPR — force != application
Regulation 2016/679 enters into force before it applies generally. A query in 2017 therefore returns legal-force active but application inactive.

### DSA — scope and entity context
Regulation 2022/2065 has:
- a general 17 February 2024 application date;
- an explicit set of provisions applying from 16 November 2022;
- anticipated application for designated VLOP/VLOSE providers four months after provider-specific notification when earlier than the default date.

If the notification event is missing, the resolver returns `CONTEXT_REQUIRED` and may expose the default only as a fallback, never as the resolved entity-specific answer.

### Regulation 2025/905 — text state != application
The amendment batch takes effect in July 2025, while Annex I Part I point 6.8 expressly applies only from 13 August 2025. Needle therefore permits a provision text state to exist before that provision is applicable.

### Temporary-regime gap
The 2021/1232 regime, as extended, ended on 3 April 2026. Regulation 2026/1881 entered into force on 31 July 2026. Genealogical succession therefore crosses a real applicability gap from 4 April through 30 July.

### Regulation 2023/2773 — retroactive effect
The act was adopted and published in December 2023 but expressly applies from 1 January 2023. The temporal model therefore permits application to predate entry into force.

This creates the next foundation question: an ex-post query about legal effect for June 2023 is different from a contemporaneous query asking what law had actually been enacted or was knowable in June 2023.

## Current unresolved risk: bitemporal perspective

Needle eventually needs at least two query perspectives:

1. **EX_POST_LEGAL_EFFECT** — taking later retroactive legislation/corrections into account when asking what legal effect attaches to historical date X.
2. **AS_KNOWN_AT_TIME** — reconstructing the legal/source state that was enacted and available as of observation date Y.

Do not solve this by forcing application date >= entry-into-force date; that would destroy legitimate retroactive legal effects.

The likely architecture is valid/legal time + observation/knowledge time, but this must be stress-tested before freezing P0-E.

## Remaining P0-E attacks

- bitemporal retroactivity perspective;
- transition periods with overlapping old/new rules;
- partial repeal or provision-specific end dates;
- conflicting official temporal assertions if a robust case is found.

Only after those survive should P0-E close and unblock P0-I implementation.
