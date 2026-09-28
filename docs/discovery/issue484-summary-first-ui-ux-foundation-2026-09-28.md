# #484 — Summary-first public landing UI/UX research foundation

Date: 2026-09-28  
Mode: **DISCOVER -> PROPOSE -> RED TEAM -> IMPLEMENT -> COMPARE**

## 1. Scope

Primary surface:
- `/medical-devices/` after #481.

Comparators:
- `/regime-v2/` for deeper legal relationships;
- `/regime/` as historical density comparator;
- strong public/legal information patterns.

Binding content/legal contract from #477/#479/#481 remains unchanged.

This run asks a presentation question:

> Can the summary-first page become materially easier to scan and navigate without hiding material legal qualifications or turning law into a dashboard?

## 2. Observation limitation

The repaired Vercel deployment could not be authenticated through the connected Vercel project scope available to this agent.

Therefore P0 does **not** claim direct screenshot/visual observation.

The baseline below is derived from:
- accepted deployed/CI state;
- actual HTML DOM;
- actual CSS;
- structural metrics.

This limitation must remain explicit in the later comparison.

## 3. P0 — repaired-page structural baseline

Measured from the accepted #481 HTML:

| Measure | Baseline |
| --- | ---: |
| Total rendered text | ~1,130 words |
| Text before first main section (`#covered`) | ~180 words |
| Text through the coverage/roles section | ~496 words |
| Links | 34 |
| External links | 24 |
| H2 headings | 7 |
| H3 headings | 9 |
| `article` blocks | 11 |
| `aside` cautions | 4 |
| Header/on-page navigation links incl. brand | 6 |
| Source-section links | 6 |

### Repeated enclosed-panel treatment

The CSS gives a full enclosing border to:
- 3 state-strip metadata items;
- 2 MDR/IVDR rule cards;
- 2 date cards;
- 3 predecessor-lineage boxes;
- 3 verification metadata items.

That is **13 enclosed boxes** before counting horizontal separators, warning rails and change rows.

The page therefore improved content order without yet creating a strong visual priority gradient.

### Structural strengths already present

Preserve:
- semantic headings;
- skip link;
- native anchors;
- no JS dependency;
- one-column mobile breakpoints;
- no horizontal graph scrolling;
- visible legal boundary cautions;
- descriptive source links;
- source-adjacent verification;
- summary-first order.

### Main UX risks

1. **Equal-weight fragmentation**  
   Metadata, legal branches, dates, warnings and lineage all receive similarly strong visual containers.

2. **Navigation competes with the page header**  
   Five in-page links sit in the global top bar even though this is a single long-form explainer.

3. **Long-form content still resembles a styled legal memo**  
   The information order is better, but the page lacks a stable reading rail and clear separation between orientation, legal branches and verification.

4. **Source-link noise**  
   Twenty-four external links are defensible for traceability but visually compete with explanatory copy.

5. **Dates split across cards and warnings**  
   2021/2022 application dates and the 2026 operational milestone are semantically one chronology but visually separated into two cards plus two caution blocks.

6. **Mobile is structurally safe but not deliberately prioritised**  
   Grids collapse, but the current top navigation simply wraps rather than becoming a deliberate mobile contents pattern.

## 4. P1 — precedent research

### R1 — Europa Component Library: in-page navigation
Source:
https://ec.europa.eu/component-library/eu/components/navigation/inpage-navigation/usage/

Applicable guidance:
- appropriate for long single-topic pages with three or more H2 sections;
- expose H2s as a high-level anchored overview;
- H2 labels should reflect user goals/questions and tell a coherent story when read as a list;
- do not use navigation to compensate for weak structure.

Disposition:
> **REUSE PATTERN, NOT EU BRANDING.**

### R2 — ECL page header
Source:
https://ec.europa.eu/component-library/ec/components/site-wide/page-header/usage/

Applicable guidance:
- page title and introduction establish page purpose;
- primary page metadata may sit with the header;
- not every optional element needs to be shown.

Disposition:
> **LEARN FROM — compact title/introduction/meta hierarchy.**

### R3 — ECL links
Source:
https://ec.europa.eu/component-library/ec/components/navigation/link/usage/

Applicable guidance:
- link text should be self-explanatory;
- standalone groups of related links should scan as lists;
- prominent CTA treatment should be used sparingly.

Disposition:
> **REUSE — reduce button-like emphasis and group verification links.**

### R4 — ECL expandable / accordion
Sources:
https://ec.europa.eu/component-library/eu/components/expandable/usage/
https://ec.europa.eu/component-library/eu/components/accordion/usage/

Applicable guidance:
- progressive disclosure is for optional/contextual/supplementary information;
- do not hide information required to complete the task;
- do not add disclosure overhead merely to shorten a reasonably sized page.

Disposition:
> **DO NOT USE FOR LEGAL QUALIFICATIONS.**

No accordion is earned merely because the page is long.

### R5 — GOV.UK accordion/details
Sources:
https://design-system.service.gov.uk/components/accordion/
https://design-system.service.gov.uk/components/details/

Applicable guidance:
- prefer simplifying content, headings and anchor links before accordions;
- details are for information only some users need;
- do not hide information most users need.

Disposition:
> **BENCHMARK — reinforces visible critical content + headings/contents first.**

### R6 — GOV.UK contents-list pattern
Source:
https://design-guide.publishing.service.gov.uk/components/content-list/

Applicable guidance:
- contents links help users make sense of long content and jump to relevant sections.

Disposition:
> **REUSE CONCEPT.**

### R7 — WCAG/W3C
Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/section-headings
- https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-link-only
- https://www.w3.org/WAI/WCAG21/Understanding/reflow
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum

Applicable guidance:
- headings create orientation/mental handles;
- descriptive links improve independent navigation;
- vertically scrolling content should reflow at 320 CSS px;
- pointer targets should meet 24x24 CSS px minimum or spacing exceptions.

Disposition:
> **REGRESSION FLOOR.**

### R8 — legislation.gov.uk
Sources:
https://www.legislation.gov.uk/ukpga/1978/30/contents
https://www.legislation.gov.uk/help

Useful pattern:
- separates table of contents, content, version choice and changes/currentness;
- places an explicit changes/currentness message near the legal navigation rather than forcing users to infer freshness.

Disposition:
> **LEARN FROM — currentness belongs in orientation, not decorative status.**

### R9 — EUR-Lex summaries/current-law baseline
Example search surface:
https://eur-lex.europa.eu/search.html?DTS_SUBDOM=EU_LEGI_SUM&SUBDOM_INIT=EU_LEGI_SUM&scope=EU_SUMMARY&type=advanced

Useful pattern:
- distinguishes explanatory summaries from legal documents and surfaces review metadata;
- remains the authoritative workflow baseline, not a design strawman.

Disposition:
> **BENCHMARK / SOURCE AUTHORITY.**

### R10 — National Archives / ONS long-page navigation
Sources:
https://design-system.nationalarchives.gov.uk/components/sidebar/
https://service-manual.ons.gov.uk/design-system/components/table-of-contents

Useful pattern:
- desktop contents rail for long content;
- on smaller devices the navigation moves above content as a table of contents;
- avoid independently scrolling navigation regions that can disorient users.

Disposition:
> **REUSE RESPONSIVE NAVIGATION SHAPE.**

## 5. P2 — primary proposition

# **CALM DOCUMENT + CONTENTS RAIL**

One proposition only.

### Header

Replace the three boxed state-strip items with:
- explicit **Independent editorial overview** eyebrow;
- page title;
- one-sentence introduction;
- a compact wrapping metadata line for:
  - MDR + IVDR;
  - evidence checked date;
  - selected EU-level coverage.

Purpose:
- make editorial/non-official status visible;
- reduce three competing boxes to one metadata hierarchy.

### Navigation

Remove in-page links from the site/top bar.

Keep the site bar shallow:
- Needle Navigator;
- independent editorial explainer label.

Add an H2-only **On this page** navigation rail beside the reading column on desktop.

On narrower screens:
- rail becomes an inline contents list before the article;
- no independently scrolling mobile panel.

### Reading column

Use a narrower readable measure and stronger whitespace.

The H2 sequence itself should narrate the page:
1. What these rules do
2. Who and what is covered?
3. Dates and current operation
4. What the rules require
5. Later changes and current procedure
6. How the rules fit together
7. Sources and coverage

### MDR vs IVDR

Retain side-by-side comparison on wide screens because the branches are genuinely parallel.

Reduce from full card containers to lightweight comparison panels:
- strong heading;
- regulation identifier;
- branch label;
- visible boundary;
- source links.

Stack on mobile.

### Regulated roles

Retain the compact role list.
Use rows rather than additional cards.

### Dates

Replace two date cards + separate current milestone warning with one chronological list:
- 26 May 2021 — MDR general application;
- 26 May 2022 — IVDR general application;
- 28 May 2026 — first four EUDAMED modules mandatory.

Keep the legacy-transition warning permanently visible below the chronology.

This makes the relationship between landmark dates and current operation scannable without inventing one regime date.

### Requirements

Use quiet role-effect rows with separators, not a 2x2 visual card grid.

### Later developments

Keep the selected/non-exhaustive contract.
Present three simple rows:
- 2024/1860 enacted;
- selected 2025–2026 enacted examples;
- COM(2025) 1023 proposal/ongoing procedure.

Status is conveyed in text, never colour/icon alone.

### Relationships

Compress predecessor mapping from three enclosed boxes to two readable lines:
- 90/385/EEC + 93/42/EEC -> MDR
- 98/79/EC -> IVDR

Keep the deeper `/regime-v2/` handoff prominent but do not duplicate its inventory.

### Sources

Keep sources visible.

Group them into:
- core law;
- official context/procedure.

Replace three boxed verification metadata items with a compact definition list.

Do **not** hide the source list behind an accordion in this pass.

## 6. P3 — red team

### Attack: the contents rail becomes another dashboard/sidebar
Mitigation:
- plain text links;
- no icons, progress state or dynamic scroll-spy;
- H2-only;
- static inline contents on narrower screens.

### Attack: lower visual density hides legal caveats
Mitigation:
- laboratory boundary, role exclusion warning, transition warning and proposal status remain directly visible;
- no `details`, accordion or tabs for material qualifications.

### Attack: side-by-side MDR/IVDR implies false equivalence
Mitigation:
- comparison only signals two core branches, not equal scope or obligations;
- each branch retains its own scope/boundary copy and official sources.

### Attack: chronology creates a fictional single regime timeline
Mitigation:
- every row labels the owning act/system;
- heading says **Dates and current operation**, not regime effective date;
- legacy transition warning remains explicit.

### Attack: design looks officially EU-branded
Mitigation:
- no ECL visual branding, EU blue, EU logos or official marks;
- page explicitly says independent editorial overview/explainer.

### Attack: fewer boxes makes links hard to find
Mitigation:
- standalone evidence links are consistently grouped;
- descriptive link text remains;
- focus treatment retained;
- key navigation/source targets get generous vertical target area.

### Attack: mobile contents becomes another long preamble
Mitigation:
- concise seven-link H2 list;
- appears after the compact page header and before substantive content;
- no nested levels.

### Attack: this is cosmetic churn
Falsifier:
- reject if structural comparison shows only style changes without reducing competing containers/navigation burden or improving semantic scan path.

## 7. Implementation authorization

The proposition survives the red team.

Implement the **CALM DOCUMENT + CONTENTS RAIL** directly against `/medical-devices/`.

No new framework, JS navigation, UI library, legal data, route or product feature is earned.
