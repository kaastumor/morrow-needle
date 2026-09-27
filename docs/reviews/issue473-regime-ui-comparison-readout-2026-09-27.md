# #473 — Regime UI v0.1 vs v0.2 comparison readout

Date: 2026-09-27  
Disposition: **READY_FOR_SPONSOR_COMPARISON — PRESENTATION HYPOTHESIS SUPPORTED INTERNALLY / USER VALUE UNPROVEN**

## 1. Sponsor-observed failure

The accepted `/regime/` prototype was legally careful but visually overloaded.

Sponsor observation:

> too much text on screen

#473 treated that as an information-architecture failure rather than a request for smaller typography or shorter paragraphs.

## 2. Run completed

The requested sequence was completed:

1. **baseline measurement**;
2. **UI/IA foundations and knowledge building**;
3. **pattern study** of strong legal/public-service interfaces;
4. **one concrete proposition**;
5. **adversarial red team**;
6. **separate comparison implementation**;
7. **real build/deployment validation**.

Durable inputs:

- `docs/discovery/issue473-regime-ui-density-research-2026-09-27.md`
- `docs/design/issue473-regime-ui-proposition-v0.2-2026-09-27.md`
- `docs/reviews/issue473-regime-ui-proposition-red-team-2026-09-27.md`

## 3. Primary research conclusion

> **The problem was not too much legal information. It was too much legal information occupying the same visual priority at the same time.**

The earlier information-design work remains right about:
- typed relations;
- temporal separation;
- text equivalents;
- evidence adjacency;
- explicit non-binding/proposal state;
- bounded completeness;
- avoiding a force-directed legal graph.

But its practical “always visible” interpretation was too broad.

Revised rule:

> **Always available is not the same as always expanded.**

## 4. Proposition tested

v0.2 uses four task layers:

1. **Overview**
   - what is this regime?
2. **Explore**
   - what connects to this branch/family?
3. **Change review**
   - what should I reopen after this upstream change?
4. **Expert / research**
   - where is this maintained projection incomplete or evidence-gated?

Only one task layer is active at a time.

## 5. Structural comparison

These are implementation diagnostics, not external usability thresholds.

| Measure | Current `/regime/` | v0.2 default | Change |
| --- | ---: | ---: | ---: |
| Approx. initially visible words | 2,087 | **266** | **-87.3%** |
| Total HTML text words | 2,441 | 1,239 | -49.2% |
| Paragraphs | 127 page-wide | **14 default** | strongly reduced |
| Headings | 61 page-wide | **6 default** | strongly reduced |
| Article/card elements | 53 page-wide | **2 default** | strongly reduced |
| Links | 47 page-wide | **2 default** | strongly reduced |
| Buttons | 9 page-wide | **5 default** | task-focused |
| Primary default content blocks | many peer sections | **4** | explicit hierarchy |

The exact old/new counting scripts are simple HTML structural diagnostics and should not be mistaken for measured cognitive load.

## 6. What remains visible despite compression

The red team required four first-impression invariants.

### A. Transition qualification

Visible on Overview:

> replacement does not make every predecessor effect vanish immediately; transitional rules preserve some effects for bounded cases.

### B. Scope cues

Overview now gives compact Article-1-style subject matter cues:

**MDR**
> medical devices for human use and accessories; specified Annex XVI product groups where the Regulation's conditions apply.

**IVDR**
> in-vitro diagnostic medical devices for human use and accessories; performance studies also fall within the Regulation's subject matter.

This is orientation, not personalised applicability advice.

### C. Current vs proposal

Overview visibly separates:
- **Enacted change:** Regulation 2024/1860;
- **Proposal — not enacted:** COM(2025) 1023.

### D. Evidence / completeness boundary

Visible:
- evidence date;
- EU-level boundary;
- evidence-bounded / not-complete warning;
- official MDR/IVDR source links.

Therefore the compression did not earn itself by silently deleting the main legal qualifications.

## 7. Lineage repair from final integrity pass

The first v0.2 draft used decorative “replaced by” arrows that did not programmatically state which predecessor went to which current regulation.

Final repair made the mapping textual:

- **90/385/EEC — Replaced by MDR**
- **93/42/EEC — Replaced by MDR**
- **98/79/EC — Replaced by IVDR**

The visual arrow is no longer the sole carrier of legal relationship meaning.

## 8. Explore result

The old route presents multiple downstream families simultaneously.

v0.2:
- one family at a time;
- one branch filter at a time;
- max six representative rows in the largest first expansion;
- sibling branch rows remain visible but de-emphasised;
- each row preserves:
  - branch;
  - act identity;
  - typed relationship phrase;
  - official source;
  - optional `Why?`.

Material omissions remain local:
- 2022/2346 exposes its 2023/1194 amendment inside its detail;
- delegated-family sampling exposes 2023/503 as an IVDR positive control.

Research taxonomy is not required to understand those legal caveats.

## 9. Change Review result

The change-review capability survives, but its default representation changes from paragraph cards to queue rows.

Human labels are primary:
- Review directly
- Review downstream
- Context
- Stop here
- Outside sample

Internal codes such as `DIRECT_REVIEW` and `NO_PROPAGATION` remain in `Why?` detail.

The page still explicitly says:

> a review candidate is not a conclusion that legal effect changed.

## 10. Expert / research result

Research diagnostics are no longer peers of public orientation.

Expert / research contains:
- coverage omission;
- branch coverage;
- represented transition trigger;
- structural-gap candidate: **None asserted**;
- signal-method boundary.

Ordinary legal detail stays with the relevant act/family rather than being dumped into Expert.

## 11. Accessibility / interaction

v0.2:
- native buttons;
- textual active state plus border;
- hash-addressable views;
- browser history / `hashchange`;
- focus moves to selected view heading on explicit task change;
- no colour-only legal status;
- branch filtering dims rather than removes sibling legal rows;
- mobile becomes one-dimensional;
- no horizontal graph-scroll requirement.

No full WCAG conformance claim is made from these structural tests.

## 12. Validation

Exact accepted candidate head:

> `0a7087ad1d9841d8b468901c125961283407f0c6`

Gates:
- Vercel: **SUCCESS**
- repository sanitation: **SUCCESS**
- mirrored GitHub test/build: **SUCCESS**
- Node assertions: **93 passed / 0 failed**
- static comparison bundle: **SUCCESS**

Preview:

> `https://morrow-needle-git-auto-473-ui-density-reset-jeroen91-2293.vercel.app/regime-v2/`

Comparator:

> `https://morrow-needle-git-auto-473-ui-density-reset-jeroen91-2293.vercel.app/regime/`

The connected Vercel/browser authorization does not permit independent rendering of this preview from the agent environment. The implementation was therefore inspected through source, regressions and successful deployment gates; sponsor visual inspection remains required.

## 13. Internal result

The presentation hypothesis is **internally supported**:

- the default task is much smaller;
- research mechanics no longer compete with public orientation;
- the legal/evidence protections targeted by the red team remain;
- deeper information remains reachable;
- the original route remains intact for direct comparison.

This does **not** establish:
- user comprehension;
- external preference;
- task-time improvement;
- legal correctness beyond the verified fixture facts;
- commercial value.

## 14. Sponsor comparison questions

Compare the two live routes and judge:

1. Can you understand the regime shape on v0.2 before reading prose?
2. Is v0.2 calm enough, or still too busy?
3. Does hiding child acts behind **Explore** feel natural or make useful content harder to discover?
4. Do the compact MDR/IVDR scope cues help?
5. Does **Change review** now feel understandable, or still like an internal maintainer tool?
6. Is **Expert / research** the right place for projection diagnostics?
7. Should this task-layered model replace the original long-page approach?

No further expansion should happen before this comparison.
