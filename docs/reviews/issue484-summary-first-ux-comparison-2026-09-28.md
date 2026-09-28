# #484 — Summary-first medical-devices P4/P5 comparison

Date: 28 September 2026. Status: **implementation candidate; sponsor qualitative acceptance pending**.
Requested execution setting: Codex, GPT-6 Sol High. Independently observed model/effort: **UNKNOWN**; usage: **UNKNOWN**. The host did not expose these settings. This is the bounded P4/P5 continuation of the [Run 1 P0–P3 and frozen criteria](https://github.com/kaastumor/morrow-needle/issues/484#issuecomment-5876758447), not a new UX criterion or legal coverage programme.

## Pinned comparison and method

- Repaired baseline: `main` commit `8954dc5a16cf2ba6e9b04c4be2d62dcd5df5fc02`; HTML blob `1053049460992f72e85421a6b03d3b4bd77652d3`, CSS blob `b3ef8af35b3278e122242ed90f09a3c32e97a1ec`. Current `main` was checked against these blobs before editing. PR #488 remained open and its separate review-heading correction was not included.
- Same local Chrome executable, headless, 100% zoom, light theme, device scale 1; viewports 1440×900, 390×844 and 320×700. Baseline and candidate each loaded with their own relative CSS. Full-page images and fold/DOM measurements were captured locally. The candidate's built `/medical-devices/` and `/regime-v2/#explore` routes were also exercised through a local static server. The earlier supplied desktop screenshot in Run 1 was not used as a pixel-matched comparator because its viewport/zoom and deployed SHA were unknown.
- This is an internal structural and rendered comparison. It does not measure comprehension, task completion, preference or time. Full-page image height is descriptive, not a UX score.

## Before / after against frozen criteria

| Criterion | Repaired baseline | P4 candidate and P5 observation | Disposition / limit |
| --- | --- | --- | --- |
| First contact | Five topbar jumps and three boxed metadata items precede the purpose summary. At 390×844, the first viewport reaches only the beginning of the purpose body. | Brand, title and purpose precede a compact visible independent/editorial/evidence note and the on-page list. At 390×844, the first viewport reaches the purpose's official source and editorial note; navigation follows. At 1440×900, the purpose, source, note and start of the contents list are visible. | Structural improvement observed. Reader comprehension unobserved. |
| Role reconstruction | Definitions and practical duties occupy separate sections with dates between them. | One `#roles` section places definition, responsibility and source together for manufacturer, authorised representative, importer and distributor; other affected groups and role-overlap/non-exhaustiveness stay visible. The old `#requirements` fragment resolves within this section. | Pass on DOM and rendered sequence; no user task observation. |
| Competing emphasis / reading demand | Run 1 identified 13 fully boxed metadata, branch, date and lineage units, plus bordered actions and cautions. | Header/footer metadata, branches, dates and predecessor links read as text rather than cards. The deeper relationship handoff is the one bordered action. At 1440px the narrower column raises full-page height from 4,394 to 6,128 CSS px; at 390px it falls from 8,441 to 8,085; at 320px from 9,257 to 9,218. | Grouping and emphasis change observed. Desktop scroll increases substantially; this is a tradeoff, not evidence of worse comprehension by itself. |
| Qualifications and legal status | Product, role, transition, EUDAMED, proposal and coverage boundaries are visible in the baseline. | All remain visible without `details` or buttons. MDR Annex XVI and IVDR lab/research boundaries are adjacent to their branches. Role overlap precedes the role list. Transition follows application dates; the EUDAMED four/not-six statement follows its milestone. The proposal is introduced as non-enacted and its ongoing state is explicitly tied to the 28 September evidence checkpoint. | No material qualification hidden or detached in source/render inspection. A fresh live procedure check was not performed; the editorial date was not advanced. |
| Sources | 34 anchors, including 24 external occurrences; several labels are generic. | 35 anchors, including 25 external occurrences. Official act/guidance links remain beside the claims, with document/purpose labels. Background summaries are labelled separately; the IVDR summary's 2022 update is stated. Article 10 links honestly say they open the act text. Footer directory remains supplementary. | One-click claim-level access retained. External destinations were inspected in markup, not live-opened in the browser run. No reduction in link occurrences is claimed. |
| Mobile/reflow | Mobile stacks former grids. At 320 CSS px there is no horizontal overflow, but top navigation and metadata precede the summary. | One reading column at all tested widths. No horizontal overflow at 1440, 390 or 320px; no clipping in captured pages. Same heading/section order on desktop and mobile. | Rendered reflow and scan order observed. Text enlargement, screen-reader reading and dark-theme contrast remain unobserved. |
| Navigation, handoff and keyboard | Five topbar jump targets; skip link and focus CSS exist. | Six descriptive in-page targets all exist and `#roles` navigation lands correctly. First Tab focuses “Skip to content” with a solid outline; Enter reaches `#main`. The built relationship link reaches `/regime-v2/#explore` and loads the deeper view at all three widths. Six contents targets measure 29 CSS px high at 390px. | Keyboard smoke path and destination pass. Full keyboard traversal, assistive-technology use and systematic contrast audit were not performed. |

## Verification

- Focused `node --test mvp/medical-devices-summary/app.test.js`: **17/17 pass**. Assertions cover section sequence, contiguous roles/duties/sources, legal boundaries, dated proposal status, anchors, source access, and one-column CSS.
- Broader browser suite from `docs/automation/VERIFICATION.md`: **110/110 pass**.
- `node mvp/candidate-b/build-static-demo.js`: pass; copied the medical-devices route with the existing regime comparison surfaces.
- `python scripts/check_repo_sanitation.py` using the bundled Python runtime: pass before commit. The new comparison file was untracked during this check.
- Local Chrome route/keyboard/reflow exercise: pass for the specific checks above. No automated accessibility tool or human participant was used.

## P5 recommendation and checkpoint

**ADOPT as the internal structural candidate, pending sponsor qualitative acceptance.** The frozen first-contact, role-contiguity, source, qualification, date, navigation and reflow criteria are supported by source/DOM and local rendering. The longer desktop scroll and unobserved comprehension remain explicit. No claim of user value, legal completeness, current law re-verification or external readiness follows. A material legal-qualification defect found in review would override this recommendation.

Branch `auto/484-summary-first-ux` is the reviewable checkpoint. Initial automatic approval review blocked PR creation because it did not recognize explicit authorization for potential collaborator notifications. The sponsor then explicitly authorized finishing this PR and reported no repository collaborators; no reviewers are requested. #484 remains open; no merge or deployment is implied. The next step is sponsor review of the focused PR and unresolved observations. Run 3 remains conditional on an accepted P5 result.


## Direct P5 accessibility completion — 29 September 2026

A bounded recovery closed the three previously unobserved browser items on the exact PR candidate. Vercel reported the preview deployment for code checkpoint `7d760d5c0f17274116a2945d972a8c3e25b16b44` successful. The browser sandbox could not navigate external HTTPS directly, so the rendered checks used Chromium `set_content` with byte-identical Git source from that deployed commit rather than claiming remote-page rendering. The candidate CSS blob at the final code checkpoint is `30d21b7f167390cb76d54eb398951a40c81d5930`.

### Observed defect and bounded fix

At 200% root text size, the pre-fix candidate had no overflow at 1440×900 but long non-link tokens caused horizontal page scrolling at 390×844 and 320×700. No content was clipped. The smallest demonstrated fix was inherited `overflow-wrap: anywhere` on `body`; a focused regression assertion was added. An initial over-escaped regression assertion caused one CI/Vercel failure and was corrected without changing application behavior.

After the fix, Chromium at 200% text size reported, at all three tested viewports (1440×900, 390×844, 320×700): **zero horizontal page overflow, zero clipped elements, and all 35 links still rendered**. The 320px result therefore also preserves the previously required narrow reflow under the stronger 200% text stress.

### Rendered contrast

Fresh light- and dark-theme computed-style checks found no text or focus-indicator failures against the conservative 4.5:1 text and 3:1 focus thresholds used for this recovery. Minimum observed text/focus contrast was approximately **9.40:1 in light theme** (white canvas) and **7.84:1 in dark theme** (RGB 18/18/18 canvas). Focused links render a solid ~3px current-color outline with positive offset.

### Complete keyboard traversal

Sequential Tab traversal covered all **35** anchors in DOM order at both 1440×900 and 390×844. Every focused link remained rendered and auto-scrolled fully within the viewport; no trap or obscured-focus case was observed. Enter generated activation for all 35 links under navigation-suppression instrumentation, including all **25 external official-source links**. The earlier built-route smoke observation for the skip link, in-page targets and `/regime-v2/#explore` destination remains applicable; this recovery did not claim successful live opening of external EU destinations because outbound browser navigation is blocked in the execution sandbox.

### Verification and disposition

Current-head repository sanitation and Unit tests passed after the fix, and Vercel returned success. The structural candidate therefore returns to **ADOPT as the internal structural candidate, pending sponsor qualitative acceptance**. Reader comprehension, assistive-technology traversal, fresh live legal-procedure verification and real-user value remain outside this internal P5 result. No merge or publication follows from this evidence.


## Sponsor revision and visual-first iteration — 29 September 2026

Sponsor review withheld acceptance after the accessibility-complete candidate: direction was liked, but the page remained too text-heavy, visually under-designed, and lacked both a timeline graph and a legislation hierarchy graph. The sponsor also required budget-friendly tooling. Figma was connected and a Starter-plan design file was created, but the next MCP design-system call hit the Starter-plan call limit and offered a paid upgrade; no upgrade was authorized. The implementation therefore used the existing GitHub/Vercel + native design-guidance/browser-verification path.

### Surviving proposition

The public entry now treats diagrams as information-bearing structure rather than decoration:

- a compact hero answers purpose and exposes the independent editorial boundary;
- MDR and IVDR appear as the first substantive branch choice;
- a six-milestone timeline distinguishes predecessor, core-law/application, proposal and operational states with text labels as well as styling;
- a legislation map shows the EU medical-device framework root, MDR/IVDR branches, predecessor directives, implementing/delegated children, Regulation (EU) 2024/1860 as a cross-cutting enacted change, and COM(2025) 1023 as a dashed “Proposal — not law” node;
- role definitions collapse to four summary rows with native disclosure for secondary detail;
- Public / Expert view separates secondary source/context metadata without hiding the product, transition, proposal or compliance qualifications;
- source access remains directly available in the public layer.

Rendered public DOM text at the exact candidate measured **445 whitespace-separated words** with role disclosures closed and Expert-only content hidden; Expert mode measured 487 words before opening native details. This is a descriptive text-load proxy, not reading-time or comprehension evidence. The hero itself is regression-bounded at 105 words or fewer.

### Exact rendered checkpoint and visual verification

Checkpoint: `d074fbfa4cb2cf6e79da9c5931927c94d60d72c0`.

Exact Git blobs independently matched the locally rendered bytes:

- HTML `5bffbe27a2c0cd7af97d430a901a7c080ef9f0b0`
- CSS `8173079196a8a2fe89c61a66a9bc91b076a49fda`
- interaction script `f82e881624a56d6a5bb7d8e2af388a614b7857b5`

Vercel reported the exact checkpoint READY. The execution sandbox still blocks external Chromium navigation, so visual inspection used Chromium `set_content` with those byte-identical Git blobs. Desktop 1440×900 and mobile 390×844 full-page renders were inspected. The timeline reads horizontally on desktop and vertically on mobile; the law map uses a root/branch structure on desktop and a single-column hierarchy on mobile. No horizontal page overflow occurred at 1440, 390 or 320 CSS px, including at 200% root text size. Public mode exposes 25 links and no hidden Expert-only content. A fresh isolated interaction check confirmed the Expert button changes the root detail state and exposes six Expert-only elements.

### Verification

At the exact checkpoint:
- GitHub Unit tests run 746: **success**;
- Repository sanitation run 1002: **success**;
- Vercel deployment: **success / READY**;
- focused medical-devices contract: 18 structural tests within the broader suite.

### Current disposition

**REVIEW AGAIN — sponsor acceptance is requested on the new visual-first candidate, not the prior text-heavy candidate.** The internal evidence supports a materially different page architecture and a functioning responsive visual model, but reader comprehension and preference remain untested. No merge or publication is implied.
