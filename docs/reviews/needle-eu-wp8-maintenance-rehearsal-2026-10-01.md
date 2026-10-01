# #515 — WP8 EUDAMED maintenance rehearsal

Date: 1 October 2026  
Canonical pre-repair revision: `a5007ecc13e84fbd60956700df3198b6620e5a1f`

Status: **REPAIR_IMPLEMENTED — verification pending**

## Maintenance event

Needle's four-source medical search contains a preserved IGJ guidance capture whose live
page still says:

> “As of January 2026 (expected date)”

for required EUDAMED registration.

Fresh source review on 1 Oct 2026 found that the European Commission's current EUDAMED
overview and mandatory-use announcement state that the first four modules became mandatory
from **28 May 2026**.

Sources checked:
- Commission overview:
  <https://health.ec.europa.eu/medical-devices-eudamed/overview_en>
- Commission mandatory-use announcement:
  <https://health.ec.europa.eu/latest-updates/eudamed-four-first-modules-will-be-mandatory-use-28-may-2026-2025-11-27_en>
- live IGJ guidance:
  <https://english.igj.nl/medical-technology/market-authorisation/registration-of-economic-operator-in-eudamed>

Authority distinction: both are official guidance, not authentic act text; the Commission
source owns the current EUDAMED module status more directly, while the IGJ passage is a
national-regulator guidance page containing an obsolete forecast.

## Pre-repair blast radius

Exact replay on the pre-repair revision:

- `EUDAMED` -> RESULTS with `igj:s5` ranked **3rd of 5**;
- the card displayed a warning but the stale forecast remained primary evidence;
- the specific timing query already returned stronger Commission/actor material and did not
  rank `igj:s5` in the first five;
- exact `2017/745` and `2017/746` routes were not owned by the stale IGJ block.

Stored pre-repair state:
- `igj:s5.evidenceEligible = true`;
- `igj:b7` and `igj:b8` were also eligible;
- captured wording was already preserved verbatim with an adjacent editorial warning.

## Repair decision

The stale forecast is not rewritten and the IGJ source is not removed.

Smallest repair:
1. mark only `igj:s5` as `evidenceEligible:false`;
2. mark its child blocks `igj:b7` and `igj:b8` ineligible;
3. retain explicit maintenance metadata:
   - `RETIRED_FROM_ACTIVE_EVIDENCE`;
   - checked date 2026-10-01;
   - reason;
   - current Commission evidence URL;
4. make exact-reference lookup honor block-level `evidenceEligible:false`, matching the
   existing ranked-section eligibility contract.

Other IGJ sections remain eligible because the demonstrated conflict is section-specific.

## Post-repair replay

Branch replay after the repair:

- `EUDAMED` -> RESULTS; `igj:s5` absent; other IGJ sections remain available;
- specific EUDAMED timing query remains RESULTS and still retrieves current Commission/actor
  material;
- exact `2017/745` and `2017/746` routing remains unchanged;
- `engine.sourceContext("igj:s5")` still exposes the preserved captured forecast and its
  maintenance metadata for audit.

## Affected outputs

Directly affected:
- broad in-coverage searches that previously ranked `igj:s5`;
- future exact-reference searches if a retired block contains an exact identifier.

Not affected:
- the IGJ source record as a whole;
- other IGJ sections;
- MDR/IVDR internal act pages;
- customs contrast;
- current Commission EUDAMED captures;
- source language registry or ranking weights.

## Legal/editorial review decisions

- do not silently edit a publisher's captured wording;
- current operational status should prefer the directly responsible Commission evidence;
- retirement is section-specific, not source-wide;
- a stale official source remains useful historical/audit evidence but should not compete
  as current primary evidence once the conflict is known;
- maintenance metadata must explain why evidence was retired.

## Engineering / rework record

Product changes:
- `mvp/product-home/search/index.json`: section/block retirement + maintenance metadata;
- `mvp/product-home/search/search.js`: exact-reference path now respects evidence
  eligibility;
- `mvp/product-home/search.test.js`: preserved-capture, no-primary-stale-result,
  exact-reference-retirement and current-timing regressions.

No framework, database, monitoring service, source crawler or new provider was added.

Implementation rework before this checkpoint: none beyond the planned bounded repair.
Actual elapsed human-equivalent time and metered model/tool cost are **UNKNOWN** where not
exposed.

## Source-access / provider constraints

- public Commission and IGJ pages were accessible through existing web research;
- no paid API or subscription was required;
- the retained search index is still a curated snapshot, not live ingestion;
- this rehearsal does not demonstrate automated change detection or complete source
  currentness;
- source authority/currentness still requires editorial/legal judgment when official sources
  conflict or update asynchronously.

## Operating-feasibility conclusion

This correction is proportionate with the existing bounded architecture: one source review,
one section-level retirement, one generic eligibility consistency fix and focused replay.

**No monitoring infrastructure is justified by this single rehearsal.** The demonstrated
need is for explicit evidence lifecycle metadata and a reviewable correction path, not a
general crawler/service. If repeated corrections later show that manual source checks are
the dominant cost or stale evidence escapes frequently, that would be the evidence needed
to reconsider monitoring.

## Verification still required

Run the normal CI/static build and exact affected-query replay on the final branch head.
If green, WP8 can proceed to sponsor review with this maintenance-cost result.
