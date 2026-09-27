# #473 — Regime UI proposition v0.2

Date: 2026-09-27  
Status: **PROPOSED FOR ADVERSARIAL TEST**

## Product proposition

Replace the current long-page regime surface with a **task-layered workspace**:

> **Overview -> Explore -> Change review -> Expert research**

Only one task layer is active at a time.

The legal/evidence model does not change.

The information hierarchy does.

## 1. Default screen — Overview

The default screen should answer one question:

> **What is this regime and how is it structured?**

It should not teach the user how Needle works.

### Header

Always visible:

**EU medical-devices regime**

One sentence:

> Three predecessor directives were replaced by two current core regulations, with later transition, implementation, EUDAMED and guidance layers around them.

Secondary metadata:
- EU-level;
- evidence checked 27 September 2026;
- bounded view.

Primary task navigation:
- Overview
- Explore
- Change review

Separate low-prominence link:
- Expert / research

### Regime spine

Use a compact 3 -> 2 visual structure.

Top row:
- 90/385/EEC
- 93/42/EEC
- 98/79/EC

Typed relation labels:
- replaced by MDR
- replaced by IVDR

Current row:
- MDR — Regulation 2017/745
- IVDR — Regulation 2017/746

Each current branch shows only:
- common name;
- formal citation;
- one-line “what it covers in this map”;
- official source.

No explanatory paragraph.

### Downstream families

Use four compact rows, not four prose cards:

- **Implementing measures** — 17 listed in frozen Commission overview
- **Delegated acts** — 7 listed
- **EUDAMED / system operation**
- **Guidance** — non-binding

Each row has:
- family label;
- branch coverage marker;
- one short descriptor;
- “Explore” action.

No family child text on Overview.

### Current / future distinction

One compact callout:

- **Current enacted change:** Regulation 2024/1860 — affects both MDR and IVDR transition/EUDAMED context.
- **Proposal:** COM(2025) 1023 — not enacted law.

This prevents proposal/current-state collapse without adding a full proposal card.

### Coverage boundary

One line:
> Evidence-bounded EU-level view. It does not represent every legally relevant document.

## 2. Explore

Question:

> **What connects to this regime or branch?**

Layout:
- branch filter: Whole regime / MDR / IVDR;
- family selector;
- one selected family list;
- optional sibling context.

No simultaneous family grid.

Each child row:

**[Act citation]**  
[branch badge] · [typed relationship phrase]  
[Official source] [Why this connection?]

“Why this connection?” expands:
- exact legal basis/provision where material;
- relationship explanation;
- counting/cross-reference nuance.

Default rows should remain one or two visual lines.

## 3. Change review

Question:

> **What should I reopen after this change?**

Retain the three frozen controls.

Replace paragraph cards with a queue table/list:

| State | Review item | Why |
| --- | --- | --- |
| Review directly | MDR current-state explanation | 2024/1860 directly amends MDR |
| Review directly | IVDR transition explanation | 2024/1860 directly amends IVDR |
| Review downstream | EUDAMED state | amendment changes rollout mechanics |
| Context | 2025/2371 | later represented trigger |
| Stop | unrelated families | no provision-specific dependency |

Human-facing labels are primary.

Internal codes remain available in detail:
- `DIRECT_REVIEW`
- `DOWNSTREAM_REVIEW`
- `CONTEXT_ONLY`
- `NO_PROPAGATION`

Each row has optional:
> **Why?**

Detailed provision/source basis is hidden until requested.

No “blast radius” visual score.

## 4. Expert / research

This is a distinct secondary layer.

It contains:
- coverage diagnostics;
- branch-sample omissions;
- review-state methodology;
- structural-gap abstention;
- research boundaries.

It must not compete visually with public orientation.

Entry label:
> **Expert / research view**

Intro:
> Maintenance and evidence-quality diagnostics for this bounded projection.

No alarm styling.

## 5. Navigation model

Use a small task switcher at the top:

- Overview
- Explore
- Change review

The active layer is visually and programmatically selected.

Expert/research remains a separate low-prominence action.

This is app/task navigation, not a replacement for long-document headings.

Requirements:
- active state in text + border, not colour alone;
- URL hash updated per view;
- browser back/forward works;
- keyboard native buttons/links;
- focus moved to new view heading only when explicitly selected;
- mobile stacks controls vertically.

## 6. Visual hierarchy

### Level 1 — regime identity
Large title + one sentence.

### Level 2 — current structure
3 -> 2 spine.

### Level 3 — navigation choices
families / changes.

### Level 4 — selected detail
child acts, rationale, sources.

### Level 5 — research/evidence mechanics
expert-only or expandable.

Do not put Level 4/5 prose into Level 2 cards.

## 7. Card rule

Use cards only for:
- MDR;
- IVDR;
- the currently selected change control if helpful.

Do not card:
- every family;
- every review state;
- every diagnostic;
- every explanatory caveat.

Use rows/lists for repeated information.

## 8. Text rule

Default:
- labels;
- noun phrases;
- one-sentence summaries.

Detail:
- paragraphs.

Source/provenance:
- links + expandable evidence.

A user should be able to infer the regime shape by reading only:
- title;
- spine labels;
- family labels;
- current/proposal status.

## 9. Testable compression target

Current approximate initial visible text:
> **2,087 words**

v0.2 default Overview target:
> **<= 450 words**

Target reduction:
> **>= 78%**

Secondary targets:
- <= 12 primary blocks;
- <= 6 primary actions;
- <= 1 visible research/maintenance concept on default screen: the coverage boundary;
- zero raw internal queue codes on Overview;
- zero full child-act lists on Overview.

The content is not deleted. It is redistributed by task.

## 10. Acceptance question

The v0.2 experiment succeeds internally only if:

> A sponsor can look at the default screen and understand the regime shape before reading detailed prose, while still reaching every legal/evidence distinction preserved in v0.1 within one or two deliberate interactions.

This is a presentation/readability checkpoint, not external user validation.
