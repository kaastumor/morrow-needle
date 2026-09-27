# Candidate B — product-readiness audit v0.1

Date: 2026-09-27  
Issue: #425

Purpose:

> assess the current Candidate-B artifact against the sponsor-corrected threshold for becoming credible enough to deserve external attention later.

This audit does **not** claim external user value.

## Result

> **8 PASS / 2 PARTIAL — PRODUCT-SHAPED, DEPLOYMENT-READY, NOT YET EXTERNALLY PRESENTABLE**

The remaining gaps are experiential/infrastructure gaps, not evidence for another feature expansion.

## Threshold review

| # | Requirement | Result | Evidence / limitation |
| --- | --- | --- | --- |
| 1 | obvious product/job framing without facilitator narration | **PASS** | The primary task is now “enter a known harmonised standard and inspect its OJ-reference state”; internal fixture/case language is no longer the main interaction. |
| 2 | ordinary-browser operation with no local Python/GitHub setup | **PARTIAL** | A generated static deployment bundle and Vercel config now exist, but no hosted deployment is currently connected or verified. |
| 3 | neutral and credible safety/evidence boundaries | **PASS** | The interface explicitly says it is frozen demonstration data, not live monitoring, not full product compliance, and points users back to official evidence. |
| 4 | known-standard lookup that feels like a product task rather than a fixture picker | **PASS** | Search accepts standard references and useful regime/standard aliases; example shortcuts remain optional. |
| 5 | representative state coverage | **PASS** | The five canonical records preserve cited, cited-with-restriction, formal non-publication/not-cited, and current-state-with-already-fixed-future-transition examples. |
| 6 | official evidence one click away | **PASS** | Cards retain direct EUR-Lex links derived from canonical evidence refs. |
| 7 | clear freshness/evidence-date semantics | **PASS** | Each result shows a supported frozen evidence window and the selected status date. Unsupported dates fail closed. |
| 8 | no claim of live monitoring if it is not live | **PASS** | The page and generated build manifest explicitly state that live monitoring is false. |
| 9 | acceptable desktop/mobile basic usability | **PASS** | A local Chromium/Playwright smoke test exercised the current UI flow at 1440px and 390px. No horizontal overflow or console/page errors were observed; the status card, evidence links, future-transition block and restricted-state rendering remained usable at the narrow viewport. |
| 10 | short self-serve evaluation path taking minutes, not a 30–45 minute favour | **PARTIAL** | The flow is structurally short—search or example -> status -> evidence—but actual completion/friction has not been browser-timed or externally observed. |

## Browser smoke-test evidence

A local browser harness was used after the initial audit.

Representative checks:

- desktop viewport: **1440 px**;
- narrow/mobile viewport: **390 px**;
- mobile `document.body.scrollWidth` equalled `window.innerWidth` (**390 px**), so no horizontal overflow was observed;
- EN 60335-2-60:2003 rendered **Cited** on 26 September 2026 with an **Already-fixed next event** on **18 January 2027**;
- four official-evidence links rendered for that representative record;
- EN 50434:2014 rendered **Cited — restriction applies** and retained the **300 r/min** scope;
- no browser console/page errors were observed.

This smoke test validates basic rendering and interaction mechanics. It is not a substitute for a hosted deployment or a fresh human usability observation.

## Important negative conclusion

The correct response to the three partials is **not more product scope**.

No evidence currently supports adding:

- applicable-standard discovery;
- monitoring/alerts;
- portfolio management;
- accounts or collaboration;
- standards content;
- full conformity assessment;
- commercial packaging.

Those would not resolve the actual remaining uncertainty.

## Smallest next work

The next internally justified step is:

> **HOST THE CURRENT NARROW ARTIFACT + VERIFY THE HOSTED BUNDLE**

Local browser mechanics are now smoke-tested.

Remaining evidence:

1. deploy the generated static bundle to a normal browser-accessible preview;
2. verify that the hosted bundle behaves like the local smoke-tested surface;
3. keep the first human interaction low-friction and separate from any cold 30–45 minute research ask;
4. only then decide whether the self-serve path is credible enough for later human validation.

## Current infrastructure limitation

The connected Vercel capability currently reports no accessible team/project.

Therefore the repository is:

> **DEPLOYMENT-READY, NOT DEPLOYED**

Do not create GitHub Actions deployment machinery merely to bypass this unless the sponsor explicitly chooses that trade-off; the sponsor has previously asked to limit GitHub Actions cost.

## External-user boundary

External recruitment remains materially later.

Even after browser verification, #425 only establishes that the artifact is credible enough to show.

It does not automatically trigger cold outreach.

When external validation eventually returns, preserve the sponsor correction:

- prefer a very low-friction self-serve interaction;
- prefer warm introduction where available;
- compensate cold professional research when asking for meaningful time;
- do not ask an unknown specialist for 30–45 unpaid minutes merely because the project needs evidence.
