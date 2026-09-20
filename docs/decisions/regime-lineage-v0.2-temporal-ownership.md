# Decision — Regime Lineage v0.2: genealogy references time, it does not own time

**Date:** 2026-09-20
**Status:** ADOPTED
**Issues:** #5, #16, #18

## Context

The first Half-Life P2 implementation pass exposed a latent truth-ownership conflict that the post-P1 audit initially missed.

Discovery-era regime-lineage v0.1 persisted:
- application_start;
- application_end;
- applicability_continuity;
- gap start/end.

P0-E subsequently converged and froze Temporal Assertions as the canonical legal-time model. Leaving temporal values inside regime lineage would create a second application timeline that could drift.

## Decision

Supersede schemas/regime-lineage-v0.1.schema.json with schemas/regime-lineage-v0.2.schema.json for canonical use.

v0.1 remains repository history only.

Regime Lineage v0.2 owns:
- regime genealogy;
- source/target regime identity;
- genealogical evidence;
- references to relevant canonical Temporal Assertions.

It does **not** own:
- application start/end dates;
- gap dates;
- overlap dates;
- an applicability-continuity verdict.

Those are derived from P0-E at read time.

## Direction of dependency

Canonical:

Temporal Assertions → derived continuity/gap analytics

Regime genealogy → tells the analytic which regimes are genealogically related

Not canonical:

Regime lineage dates → Temporal Assertions

or

Persisted Half-Life metrics → legal-time truth

## ePrivacy migration

Canonical temporal fixture:
- fixtures/temporal/eprivacy-temporary-regime-v0.1.json

Canonical genealogy fixture:
- fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.2.json

Historical discovery fixture:
- fixtures/lineage/reg2021-1232-to-reg2026-1881-gap-v0.1.json
- status: SUPERSEDED_DISCOVERY_PROVENANCE

The v0.2 edge references:
- eprivacy-2021-extended-application-end
- eprivacy-2026-application-start

The 118-day gap is recomputed with the temporal resolver and is not stored on the lineage edge.

## Regression

tests/test_regime_lineage_v02.py proves:
1. v0.2 contains no application dates, gap dates or applicability-continuity field;
2. every temporal reference resolves;
3. the 118-day gap is reproduced from Temporal Assertions;
4. changing canonical temporal input changes the derived gap without modifying lineage.

Half-Life tests now derive metrics from canonical temporal assertions and treat the older discovery metrics only as a regression snapshot.

## Freeze rule

Future genealogy contracts may reference temporal claims but may not copy canonical legal-time values for convenience.

If a product view needs a duration, gap, overlap or extension ratio, it derives it from P0-E.
