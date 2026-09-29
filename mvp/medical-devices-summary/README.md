# Visual-first medical-devices landing page

Issues: #477, #484  
Route: `/medical-devices/`

Purpose:
> test whether a public legislation explainer can preserve legal qualifications while moving most explanatory load from prose into a concise branch choice, timeline and law map.

## Public reading order

1. identity, purpose and editorial boundary;
2. MDR / IVDR starting-point choice;
3. six-milestone legal/operational timeline;
4. public legislation hierarchy / relationship map;
5. role summaries with secondary detail disclosed on demand;
6. direct source directory and visible coverage limit.

## Detail levels

- **Public** is the default. It keeps critical product, transition, proposal and compliance qualifications visible, while secondary source/context metadata stays out of the initial reading path.
- **Expert** adds background summaries, timeline/source detail, deeper relationship links and evidence metadata without changing the core legal-status wording.

## Visual contract

The timeline and law map must replace prose rather than duplicate it.

The visual states are text-labelled as well as styled:
- core law / application;
- predecessor;
- operational milestone;
- proposal — not law.

On narrow screens the timeline and law map collapse to one readable column; horizontal graph scrolling is not part of the public experience.

## Comparators

- PR #489 before this visual revision — structurally improved but still text-heavy baseline;
- `/regime-v2/` — deeper task-layered relationship browser;
- `/regime/` — earlier dense macro view;
- official workflow — Commission overview + economic-operator guidance + EUR-Lex MDR/IVDR.

## Important design choice

This remains a **regime overview**, not a legal act.

It therefore does not receive:
- one “in force” badge;
- one adoption date;
- one application date;
- one expiry date.

Those belong to the member acts.

## Evidence ownership

Substantive content remains mapped in:

`docs/evidence/issue477-medical-devices-summary-content-map-2026-09-27.md`

Frozen task contract:

`docs/evaluation/medical-devices-summary-first-v0.1/tasks-and-answer-key.md`

The page is an editorial projection over official evidence, not a replacement legal source.

## Captured guidance search in M1

The page mounts the retained dependency-free multilingual engine and source-bound evidence presenter from the 29 September 2026 package (`needle-evidence-view-2026-09-29.zip`, SHA-256 `7c4f8e0b04da936df88dd59840adc548ff9dea75d76253c3dedab196e215a0d1`). The five root `src/` modules are in `search/`; the rejected `experiments/field-ranking/src/` modules are excluded. `search/index.json` contains only the captured English Commission actor-registration, EUDAMED-overview and economic-operators guidance pages, observed 29 September 2026. The consumer/native-language experiment and Dutch IGJ page are not public M1 search coverage. Original lines and source identifiers are preserved; the capture is web-tool-extracted narrative, not raw HTML or a live legal source feed. The Commission text is attributed © European Union, CC BY 4.0.

`search/resources.json` provides the common 24-language registry and external language resources. Only English source text is included here, so selecting another question language gives an explicit coverage state unless the reader opts in to labelled English evidence. The interface copy is English. Approximate matches, heading/context-only hits, incomplete previews and exact-reference mentions are labelled. Reference mentions are guidance locators, not authentic act text. MDR and IVDR direct EUR-Lex links remain available without scripts. Search has no query storage, model call or telemetry.

Run `node --test mvp/medical-devices-summary/search.test.js`, the browser MVP suite in `docs/automation/VERIFICATION.md`, and `node mvp/candidate-b/build-static-demo.js`. The built route is `/medical-devices/`. The component's inherited package tests and replay are separate checks; they do not prove quality for this narrower public source pool or all 24 languages. M1 act detail views and broader #492 adversarial cases remain separate work.
