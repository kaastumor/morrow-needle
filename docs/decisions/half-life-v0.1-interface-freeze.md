# Decision — Freeze Half-Life v0.1 derived analytic

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #10

## Decision

Freeze the first Half-Life product contract around:

- `schemas/half-life-composition-v0.1.schema.json`
- `schemas/half-life-view-v0.1.schema.json`
- `src/needle/analytics/half_life.py`
- `fixtures/analytics/eprivacy-half-life-v0.1.json`
- `fixtures/temporal/eprivacy-temporary-regime-v0.1.json`
- `fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.2.json`
- `tests/test_half_life_view.py`
- `.github/workflows/half-life-view.yml`

The first frozen analytic is the temporary ePrivacy derogation history spanning Regulation 2021/1232, extension by Regulation 2024/1307, and the successor Regulation 2026/1881.

## Ownership rule

Half-Life is a **disposable derived view**.

It owns:

- duration arithmetic;
- extension deltas;
- episode composition;
- derived gap presentation;
- duration ratios;
- public narrative;
- analytic coverage metadata.

It does **not** own:

- legal application dates;
- temporal inclusivity;
- official source evidence;
- regime genealogy;
- rule lineage;
- terminal legal outcome;
- future extensions/successors.

Those remain canonical in P0-E Temporal Assertions, reference-only Regime Lineage v0.2, and any future rule-lineage/status contracts.

## Stable v0.1 principles

### 1. Composition is reference-only

The persisted Half-Life composition stores IDs and fixture references, not dates or durations.

Changing a canonical Temporal Assertion must change the derived view without editing the composition or genealogy.

### 2. Regime genealogy does not own legal time

The first P2 implementation exposed a latent ownership defect in Regime Lineage v0.1.

That contract was superseded by Regime Lineage v0.2:

- genealogy owns ancestry;
- Temporal owns application boundaries;
- Half-Life derives gaps/continuity at read time.

The 118-day 2026 gap therefore exists only as a derivation from canonical temporal assertions.

### 3. Extensions are an assertion history

An extension is recognized only when a later END assertion explicitly overrides the preceding END assertion and moves the effective end later.

v0.1 supports repeated extension chains and fails closed when override ancestry is broken.

### 4. Inclusivity is executable

Duration arithmetic uses each temporal boundary's inclusive/exclusive semantics.

Half-Life does not assume that printed dates are always included.

### 5. Every displayed boundary is evidence-linked

Each projected start/end carries:

- canonical Temporal Assertion ID;
- resolution state;
- evidence state;
- official source references.

The public analytic therefore remains traceable without turning the projection into a source-of-truth store.

### 6. Genealogy is visible but separate

The view exposes the referenced genealogy edge's:

- relation type;
- evidence state;
- source regime IDs;
- target regime IDs.

It copies no application dates into genealogy.

### 7. View horizon is not final expiry

The first ePrivacy view currently ends at the evidenced 3 April 2028 application end of Regulation 2026/1881.

v0.1 labels that point as a **view horizon**.

It explicitly does not infer:

- final expiry;
- no future extension;
- no later successor;
- transition to permanent law.

Terminal outcome remains `UNRESOLVED_AFTER_VIEW_HORIZON`.

### 8. Rule survival is not inferred from regime succession

The ePrivacy genealogy supports `REENACTED_AS` at regime level.

It does not prove proposition-by-proposition continuity.

v0.1 therefore exposes rule continuity coverage as `NOT_ASSERTED`.

### 9. Temporary is descriptive, not evaluative

Half-Life may say an instrument/regime was temporary when official legal/source evidence supports that characterization.

It must not imply that extension, reenactment, lapse or permanence is improper.

## First frozen output

The ePrivacy view derives:

- original planned duration: 1,098 days;
- first-regime duration after extension: 1,706 days;
- extension beyond original planned end: +608 days;
- non-applicability gap: 118 days;
- successor applicability represented in the current view: 613 days;
- total applicable time represented: 2,319 of 2,437 calendar days;
- first-regime duration ratio: 1.5537.

All numbers are recomputed from canonical temporal assertions.

## Scope limitations retained deliberately

v0.1 does not yet establish:

- proposition-level rule survival across successor regimes;
- permanent-law transition;
- true final expiry;
- overlapping Half-Life episodes;
- ranking across many temporary regimes;
- a cross-domain temporary-regime discovery/index layer.

Those are follow-on capabilities, not reasons to weaken v0.1.

## Reopen rule

Reopen Half-Life v0.1 only if a real official-source case cannot be represented without:

- copying canonical legal time into the analytic;
- copying dates into genealogy;
- smoothing over a real gap;
- losing boundary inclusivity;
- or implying terminal/rule-continuity facts not supported by canonical evidence.
