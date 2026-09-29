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


## Real-browser verification and reflow repair — 29 September 2026

Remote Desktop Commander connected to **Jeroen-PC** and exposed the existing local Chrome/Playwright runtime. To avoid mutating an existing checkout, exact PR head `bdbcbddf0c4e6aaa9db8a5f8efcb2bfaa0392ef3` was downloaded from GitHub codeload into an isolated scratch directory. The #494 generator and tests passed there before browser work.

Headless Google Chrome was then driven through Playwright against a local HTTP server serving the frozen `specimen.html` and `baseline.html`. At 1440×900, 390×844 and 320×700, both arms loaded with two decision sections/tables, keyboard Tab focus landed on a real link with a visible solid focus outline, and direct `#january`/`#march` navigation produced the intended target outline. Four representative source links (both official-publication URLs and both HowTheyVote vote pages) emitted the exact expected browser requests; requests were intercepted/aborted, so this proves activation but not destination retrieval.

The first browser pass found a real reflow defect: with root text size set to **200% (32px)**, both arms produced document-level horizontal overflow at 390px and 320px. Diagnosis isolated long legal/status tokens and headings such as `INSPECTABLE_ONLY_FOR_NOW`, `P9_TA(2024)0018` and `2022/0092(COD)`; table overflow itself was already contained in the intended `.table-wrap` scroll region. A candidate table-width fix was tested and rejected as unnecessary. The minimal retained repair is `overflow-wrap:anywhere` on headings, paragraphs, definition-list text and links.

A clean minimality replay restored the exact original stylesheet, applied **only** that text-wrap rule, and reran the full browser matrix. Result: no document-level horizontal overflow at 1440px, 390px or 320px, including 200% root text, in either arm. At 320px the tables intentionally remain horizontally scrollable inside their local wrapper; the page itself does not overflow. This is browser evidence for the rendered static pages, not WCAG conformance or participant comprehension.

The repository patch records only the minimal text-wrap repair plus a static regression assertion. A final exact-head replay is still required after these repository commits before the browser gate can be marked closed.


## Exact-head browser gate closure — 29 September 2026

After the minimal reflow repair was committed, exact PR head `57314714fd5b6376c47a1aff98d0d6d0b7db4737` was downloaded afresh from GitHub codeload into a new isolated directory on Jeroen-PC. No existing checkout was changed. The #494 generator and test suite passed **3/3**, including the new text-reflow safeguard.

The same Chrome/Playwright matrix was then rerun on that exact archive:
- both `specimen.html` and `baseline.html` at 1440×900, 390×844 and 320×700;
- normal text and root text enlarged to 200% (computed 32px);
- document-level horizontal overflow absent at every width/size combination;
- at 320px, each vote table remains intentionally horizontally scrollable inside `.table-wrap`, without causing page-level overflow;
- first keyboard Tab reaches a link with a visible solid focus outline in both arms;
- direct `#january` and `#march` navigation resolves to the intended decision section and applies the target outline;
- browser activation emitted the exact expected requests for both selected EUR-Lex publication URLs and both HowTheyVote vote-page URLs. Those requests were deliberately intercepted/aborted; destination retrieval was **not** claimed.

This closes the previously open **rendering / keyboard-focus / fragment-navigation / narrow reflow / 200%-text / representative source-link activation** browser gate for the static experiment pages. It is not WCAG conformance, source-destination availability, participant comprehension or reader-benefit evidence.

Screenshots and machine-readable browser output were retained only in the isolated local verification workspace on Jeroen-PC; they are not production assets or source evidence.


## Pre-merge comparability red-team — 29 September 2026

A final content comparison of the frozen HTML arms found the same **13 unique external source destinations** in both arms. The competent handoff contains repeated links at its source-first entry point, but no source destination unavailable to the linked specimen. This is treated as the intended navigation/presentation difference, not an evidence-budget difference.

The same review identified one avoidable design risk before any participant observation: the earlier 8/8 allocation was balanced but manually authored, so arrival order could become an unnecessary confound. No participant had been contacted or observed. The allocation was therefore replaced before execution by a reproducible deterministic randomisation: SHA-256 of the frozen seed `needle-494-reading-pilot-v1-2026-09-29` plus each participant ID, with the first eight hash-ranked IDs assigned Arm A and the rest Arm B. The resulting arrival-ID sequence is recorded in `pilot-runbook.md`. No political, expertise or outcome variable enters assignment.


## Reader-pilot delivery preparation — 29 September 2026

After PR #495 was merged to main as `2d30abe339865e0b2fdd53485cd8c113af721ddd`, Vercel production was observed READY at deployment `dpl_Ey13o594BdnZaL77ZrRYATDCqAXC`. The merged research files themselves were not copied by the existing static build: direct production requests to `/docs/experiments/issue494/specimen.html` and `baseline.html` returned 404. Therefore participant execution could not start from the merged research artifact alone.

A second delivery-specific red-team found another leakage risk: the research pages expose navigation to the comparison arm, evidence ledger and protocol/answer key. Those links are useful to reviewers but invalid for a between-subject participant treatment.

The bounded delivery patch therefore:
- generates participant-only copies from the frozen specimen/baseline without changing their factual decision content;
- removes comparison/research navigation and the #494 research-record hyperlink;
- preserves the exact official/provider source destinations used by the treatments;
- publishes only `/research/issue494/a/` and `/research/issue494/b/` plus their stylesheet through the existing static build;
- adds tests that reject leaked comparison/protocol/evidence routes and require source-destination parity.

Isolated Jeroen-PC verification on branch head `72a1dca71b7ba308306f05446f3889ad2ce46737` executed:
- `node --test docs/experiments/issue494/build-participant-pages.test.js mvp/candidate-b/build-static-demo.test.js`: **4/4 pass**;
- `node mvp/candidate-b/build-static-demo.js`: pass;
- both participant route directories were generated under `dist/research/issue494/`.

Sponsor authorization now covers recruitment/contact and execution of the frozen 16-reader pilot. **No paid panel, incentive, purchase or new vendor account is inferred from that authorization.** No participant has yet been contacted or observed.
