# Cycle 1 — Explorer boxed workflow result

Issue: #136  
Parent: #134  
Channel: `EXPLORER_USE`  
Date: 2026-09-24  
Evidence mode: `AGENT_SYNTHETIC / BOXED_WORKFLOW`  
Claim type: `PRODUCT_WORKFLOW`

## Question

Can the actual Corpus Explorer v0.1 mechanically reduce discovery and
provenance-inspection friction relative to direct corpus/repository inspection,
without losing the decisive trap or evidence ownership?

This run does **not** test human preference, adoption, switching behavior or
external-user value.

## Environment

The exact 42,191-byte single-file Explorer snapshot previously built from
canonical main was used:

`needle-corpus-explorer-dogfood.html`

It contains the canonical 27-case corpus snapshot and the transport-only
substitutions already recorded for dogfood.

The container provides Chromium and Playwright. Sandbox policy blocked Chromium
navigation to both localhost and `file://` URLs. The test therefore loaded the
exact HTML bytes into a fresh headless Chromium page through Playwright
`page.set_content`.

This is a transport substitution, not a UI reconstruction. The embedded
JavaScript executed successfully, the corpus validated as 27 cases / 14 trap
classes, and no browser console/page errors were observed.

## Task A — Explorer route

### Practical job

Find a corpus case relevant to the claim that continued listing of a harmonised
standard preserves the full presumption of conformity, then determine the
decisive trap, evidence role and durable evidence owner.

### Interaction

1. open fresh Explorer page;
2. search for `presumption`;
3. result set narrows from 27 to 3 cases;
4. open:
   `EN 60335-1 remains listed while a clause-specific presumption is restricted`.

### Result exposed by the detail view

- decisive trap:
  continued listing does not preserve unrestricted presumption where a specific
  restriction is already operative;
- trap class: `DYNAMIC_REFERENCE_STATUS`;
- provenance: Issue #88, `EVALUATION`;
- exposure/reuse status visible;
- evaluation mode: `SURFACED_TRAP_ADJUDICATION`;
- evaluation result: `R_PASS_M_PASS`;
- durable evidence owners:
  - Issue #88;
  - phase-A prompt fixture;
  - phase-A answer-key fixture;
  - phase-A result fixture;
- two related cases are linked explicitly **by trap class**.

### Validity-floor check

Passed mechanically.

The detail view did not hide or collapse:

- provenance role;
- exposure/reuse state;
- evaluation mode;
- evaluation result;
- evidence ownership;
- relationship basis for related cases.

The referenced Issue #88 and all three fixture paths were independently fetched
from canonical GitHub and exist.

## Task B — direct repository/corpus route

### Matched practical job

Find a case relevant to the claim that provisional application or an EU internal
conclusion for one agreement can be inherited as entry into force of a parallel
comprehensive/umbrella agreement, then determine the decisive trap, evidence
role and durable evidence owner.

This is a different case family from Task A to avoid answer carry-over.

### Realistic direct route attempted

1. GitHub repository code search:
   `provisional application entry into force international agreement`;
2. no result;
3. narrower repository search:
   `provisional application`;
4. no result;
5. open known canonical `corpus/index-v0.1.json`;
6. inspect the corpus content for provisional-application / entry-into-force
   terms;
7. identify:
   `EU-Mercosur ITA provisional application does not equal EMPA entry into force`;
8. follow its evidence references to Issue #91 and
   `research/parallel-international-agreement-lifecycle-2026-09-23.md`.

### Result

The direct corpus contains the required information and provenance:

- trap class: `PARALLEL_INSTRUMENT_LIFECYCLE`;
- role: `DERIVATION`;
- decisive trap: ITA and EMPA are separate instruments and ITA provisional
  application cannot be inherited as EMPA entry into force;
- evidence owner: Issue #91 plus the research memo.

The research memo was independently fetched and confirms the two-instrument
lifecycle distinction.

## Relative-friction observation

### Difference — observed mechanically

The Explorer route exposed case discovery + interpretation + provenance in one
bounded flow:

> generic search → 3 candidates → detail → evidence owners.

The direct repository route remained fully capable, but the attempted repository
search did not surface the case. The successful route required knowing or
discovering the canonical corpus file, reading structured JSON, locating the
matching object and then following its evidence references.

This is a real **mechanical indirection difference** in the tested environment.

### Importance — UNKNOWN

The boxed run cannot establish whether an intended human user cares about this
difference.

### Behavioral consequence — UNKNOWN

The boxed run cannot establish whether a user would choose the Explorer rather
than repository inspection.

### Adoption/switching friction — UNKNOWN

The boxed run cannot establish whether opening/learning a separate Explorer is
worthwhile to a human.

## Counter-evidence

The direct corpus/repository route still answered the matched task correctly and
preserved the same canonical truth.

A repository user who already knows `corpus/index-v0.1.json`, uses local text
search, or has stronger GitHub navigation habits may experience much less
friction than this boxed route suggests.

The Explorer's apparent mechanical advantage may therefore be ordinary
presentation convenience rather than material user value.

## Red-team interpretation

Do not upgrade:

> fewer mechanical steps

into:

> meaningful human product value.

Do not interpret the failed GitHub code-search attempts as a universal repository
baseline failure; they are an observation about this tested route only.

The boxed result is useful because it shows that the Explorer projection is not
merely decorative: it successfully composes case discovery, evidence semantics
and provenance navigation without introducing a second truth layer.

It does **not** resolve H-16.

## Boxed-stage disposition

**PARK**

Reason:

- a plausible relative-workflow advantage survives;
- the validity floor passed;
- the evidence needed for `importance`, `behavioral consequence` and
  `adoption/switching friction` is inherently human;
- obtaining that evidence should be decided at #139 rather than imposed before
  knowing whether it can still change project direction.

## Implication for #139

Treat #136 as an explicit evidence-limited channel result:

- mechanical relative advantage: **SUPPORTED IN BOXED SYNTHETIC TEST**;
- correctness/provenance regression: **NOT OBSERVED**;
- human importance: **UNKNOWN**;
- human behavioral consequence: **UNKNOWN**;
- adoption/switching: **UNKNOWN**;
- general H-16: **UNRESOLVED**.

#139 may now decide whether human usability evidence has enough expected
information gain to justify a later bounded session.

Do not manufacture that evidence merely to close H-16.
