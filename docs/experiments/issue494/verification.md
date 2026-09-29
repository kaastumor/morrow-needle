# #494 implementation verification — 29 September 2026

## Repository and source state

GitHub `main` was read through the connected repository tool at `c10f0979d70580a13c4817b878c7bdf261723ee3`; #494 was open with four comments and no posted feature-review checkpoint or open #494 PR. Local checkout was clean but at older `2852f9c`. Its bundled Git lacked `git-remote-https`, so network fetch was unavailable. The new files are isolated under this folder; the remote review branch is based on canonical main, not the older local parent. #490 remained the active prototype allocation and #492 was not changed.

The two [provider vote pages](https://howtheyvote.eu/votes/163059) and [March page](https://howtheyvote.eu/votes/166226) were read: dates, ballot labels, totals and eight group distributions agree with the frozen ledger. The [provider methodology](https://howtheyvote.eu/about) was read. It says corrections are not collected/displayed, and says amendment results are not displayed. The current March page nevertheless exposes a link labelled “View all roll-call votes, including amendments”; its destination and completeness were not checked. That tension is retained rather than turned into an absence claim.

Direct openings of the selected Parliament pages and both ELI HTML publication pages returned JavaScript/robot interstitials in this run. The issue comments report earlier primary-text transfers and recounts; those were not independently rerun from authentic source bytes here. No interstitial was bypassed. Links in the pages are exact official/provider destinations; successful destination retrieval in a participant's browser remains unverified.

## Executed checks

- `node docs/experiments/issue494/build-pages.js` generated both static pages.
- `node --test docs/experiments/issue494/build-pages.test.js`: 2/2 passed after a whitespace-sensitive test assertion was corrected. The tests inspect both generated arms, their section-local caveats, source links and arithmetic from the rendered tables. They do not substitute for a browser or source authentication.
- `node --test mvp/medical-devices-summary/app.test.js`: 17/17 passed in the local older checkout. This is a regression check, not evidence that canonical main's newer #490 surface was exercised.
- `node mvp/candidate-b/build-static-demo.js --help`: completed the local static build of Candidate B and regime comparison surfaces with five fixtures. It is unrelated to #494's static pages and was run against the older checkout.
- `git diff --check`: passed for tracked changes; the newly added #494 files were also checked after staging.

Browser use refused the local `file:///.../specimen.html` page under the browser URL policy and explicitly prohibited reaching the same page through an alternate route. No browser rendering, source-link activation, keyboard/focus or narrow-layout/reflow acceptance is claimed. The CSS and native HTML navigation were inspected statically; browser acceptance remains open. No participants were recruited or run.

No reader benefit, integration savings, complete within-file search, authenticated source retention, current political stance, member/party reconciliation or licensing compatibility was established. Public redistribution remains gated by licensing review.

## Follow-up provenance/licensing and pre-run freeze — 29 September 2026

A later connected-source review read the European Parliament Open Data rules, the Parliament legal notice and HowTheyVote's current methodology/licence page. Parliament's Open Data rules state CC BY 4.0 for EP open data; the general legal notice permits reuse of EU-owned textual material with source acknowledgement while allowing item-specific conditions. HowTheyVote states ODbL for voting data distributed through downloads/API and Database Contents License treatment for individual database contents unless otherwise noted; photos and vote summaries are excluded. The specimen now treats its two tables as bounded EP-primary research reconstructions from the reported #494 recounts and retains HowTheyVote as an external comparator/navigation aid rather than importing its downloadable/API database. This narrows the immediate dependency but does not provide legal clearance or change Needle's `INSPECTABLE_ONLY_FOR_NOW` repository state.

The reading protocol now freezes a 16-reader, between-subject diagnostic pilot proposal with 8 readers per arm, three critical comprehension items, separately recorded correctness/unresolved/source-opening/navigation/time outcomes, a hard wrong-attribution stop and a pre-specified continuation threshold. No participant recruitment or execution is authorised by that freeze.

PR-head Vercel preview deployment for the earlier head was observed READY but remained behind Vercel authentication even through the connected deployment tooling. Therefore browser rendering, keyboard/focus, reflow and external source-link activation remain **unverified**, not failed. A new preview for later commits must be tied to its exact head before it can count as evidence.
