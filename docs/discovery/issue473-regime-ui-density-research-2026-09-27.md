# #473 — Regime UI density research and knowledge base

Date: 2026-09-27  
Status: **FOUNDATION COMPLETE — PROPOSITION FOLLOWS**

## 1. Problem statement

Sponsor review of the first medical-devices regime surface identified a straightforward usability failure:

> **too much text is visible at once**

The current page is semantically careful, but its hierarchy does not make enough decisions for the user.

Measured current source:

- 2,441 words total in `mvp/regime-constellation/index.html`;
- approximately 2,087 words exposed in the initial DOM state after removing collapsed `details` bodies and hidden alternate Change Review cases;
- 127 paragraphs;
- 61 headings;
- 53 article/card blocks;
- 47 links;
- 9 buttons;
- 7 major sections.

These numbers are diagnostics, not standards.

The qualitative failure is more important:

> **orientation, explanation, evidence boundaries, research diagnostics and maintainer review mechanics all compete for attention on the same page.**

The interface makes the user perform the prioritisation that the design should perform.

## 2. Basic interaction principle — overview before detail

Ben Shneiderman's visual information-seeking work provides a durable starting point:

> overview first -> zoom/filter -> details on demand.

For this project the useful interpretation is not “draw a giant graph and let users zoom”.

It is:

1. let the user form a regime-level mental model;
2. let them choose the branch/family/task they care about;
3. reveal the legal/evidence detail for that selection.

Sources:
- https://doi.org/10.1109/VL.1996.545307
- https://www.cs.cornell.edu/colloquium/2003FA/shneiderman.htm

### Implication

The default page should not simultaneously explain:
- the whole regime;
- every family;
- every safety caveat;
- all review-propagation controls;
- all research diagnostics.

Those are different information-seeking stages.

## 3. Progressive disclosure — useful, but not a dumping ground

GOV.UK and the Europa Component Library both support progressive disclosure for secondary content while warning against hiding information everybody needs.

GOV.UK:
- accordions are appropriate when users need an overview of related sections and selectively reveal relevant ones;
- details are for information only some users need;
- hiding large amounts of essential information is a failure;
- simpler structure or separate pages can be better than layers of accordions.

Europa Component Library:
- Expandables are specifically intended to reduce visual complexity and scrolling;
- optional technical/legal material is a valid use;
- important information must not be hidden;
- nested disclosure compounds cognitive load.

Sources:
- https://design-system.service.gov.uk/components/accordion/
- https://design-system.service.gov.uk/components/details/
- https://ec.europa.eu/component-library/eu/components/expandable/usage/

### Implication

Needle should disclose **evidence detail and rationale**, not hide the primary legal meaning.

Good default:
> “2023/607 — changes MDR + IVDR transition”

Expandable:
> exact provisions, evidence classification, why the relation is represented, CELEX metadata.

Bad default:
> paragraph explaining the full legal nuance before the user even knows why the act matters.

## 4. Scannability and page structure

W3C cognitive-accessibility guidance recommends:
- logical sections;
- clear visual hierarchy;
- whitespace and boundaries;
- headings that make the page outline understandable;
- avoiding dense pages.

WCAG guidance also stresses descriptive headings/labels and notes that narrower text blocks and spacing can improve tracking for users with cognitive or visual disabilities.

Sources:
- https://www.w3.org/WAI/WCAG2/supplemental/patterns/o2p03-page-structure/
- https://www.w3.org/WAI/WCAG2/supplemental/patterns/o3p10-whitespace/
- https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
- https://www.w3.org/WAI/WCAG21/Understanding/headings-and-labels

### Implication

The current page has many individually well-labelled blocks but too many **peer-level** blocks.

A strong hierarchy needs:
- fewer primary regions;
- a visibly dominant task;
- short content units;
- secondary rationale visually demoted.

## 5. EU design-system patterns

The current Europa Component Library is the official EU design system.

Useful patterns for this project:

### Content items

ECL content items are designed for quick overview and decision-making:
- consistent ordering;
- essential information first;
- recognisable repeated structure;
- metadata secondary.

Source:
https://ec.europa.eu/component-library/eu/components/content-item/usage/

### Cards

ECL says:
- show only the most relevant information;
- minimise links;
- use small groups;
- avoid overuse;
- too many cards can create scrolling and short-term-memory burden.

Source:
https://ec.europa.eu/component-library/eu/components/card/usage/

### In-page navigation

ECL says:
- useful on long pages with 3+ H2 sections;
- headings should reflect user goals;
- H2 labels should tell a coherent story;
- in-page navigation must not compensate for poor structure.

Source:
https://ec.europa.eu/component-library/eu/components/navigation/inpage-navigation/usage/

### Timeline

ECL's timeline guidance:
- short distinct event headings;
- timestamps always visible;
- detail may be secondary;
- use chronological ordering.

Source:
https://ec.europa.eu/component-library/ec/components/timeline/usage/

### Implication

Needle currently overuses the **card as paragraph container**.

The next version should use:
- compact repeated rows/items for families and relationships;
- cards only for genuinely separate primary choices;
- timelines as date + event first, detail second;
- no standalone “how to read this” legend if inline labels can carry the semantics.

## 6. Legal-publishing baselines

### EUR-Lex

EUR-Lex separates:
- text;
- document information;
- dates;
- relationship categories;
- classifications.

It does not require the user to ingest all metadata before reaching the legal document.

Example:
https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:22017X0427(01)

Strength:
> authoritative typed information exists in stable categories.

Weakness for our task:
> the user still has to reconstruct what matters for their question.

### legislation.gov.uk

The UK service exposes:
- current/revised version information;
- outstanding changes;
- timeline of changes;
- change/effect tables.

Its help material explicitly explains that unapplied effects are surfaced at the relevant legislation/provision, rather than requiring every change record to occupy the default reading layer.

Sources:
- https://www.legislation.gov.uk/help
- https://www.legislation.gov.uk/understanding-legislation
- https://www.legislation.gov.uk/changes

Strength:
> **state and change warnings are adjacent to the affected thing.**

That is more useful for Needle than one page-wide diagnostics wall.

## 7. Dense-network research

A survey of human-centred graph-visualisation experiments concludes that graph readability depends on visual/data complexity and task, not merely node count.

A controlled node-link vs matrix study found matrix-style representations outperform node-link diagrams on many tasks once graphs become larger/dense, while path-finding remains a relative strength of node-link layouts.

Sources:
- https://doi.org/10.1016/j.visinf.2018.12.006
- https://doi.org/10.1057/palgrave.ivs.9500092

### Implication

Needle should not assume that “properly building the web” means drawing more edges.

For this product:
- use node-link shape only for the **small regime spine** where ancestry/splitting is the task;
- use structured lists/rows for dense downstream families;
- use filtered review queues for change impact;
- do not make the user parse a universal graph.

## 8. Reassessment of #435

#435 correctly established:
- text semantics must survive the visual;
- relation types must be explicit;
- dates cannot collapse;
- evidence must stay adjacent;
- provenance should be inspectable;
- generic `RELATED_TO` is unsafe;
- force-directed graph is a poor default.

Those remain binding.

But one #435 implementation implication now needs revision:

> too many categories were classified as **always visible**.

That protected against hidden legal caveats but created a new failure:
> **everything important became visually primary.**

Revised rule:

> **Always available is not the same as always expanded.**

### Always visible

Only information needed to understand the current object and avoid a materially wrong first impression:

- regime identity;
- evidence/as-of date;
- the 3 -> 2 predecessor/current structure;
- binding vs guidance vs proposal distinction where shown;
- visible coverage boundary;
- active branch/family selection;
- material unresolved state affecting the current selection.

### One interaction away

- individual child acts;
- exact provision locators;
- relation rationale;
- source metadata;
- detailed transition mechanics;
- why a review signal propagated/stopped;
- current research diagnostics.

### Dedicated expert/research layer

- coverage diagnostics;
- maintenance queue;
- structural-gap abstention logic;
- internal review-state taxonomy.

The public orientation surface should not require a user to understand Needle's research operating vocabulary.

## 9. Core UI model

The page should be designed around three different user questions:

### Question A — “What is this regime?”

Default **Overview**.

Needed:
- lineage shape;
- two current core acts;
- high-level downstream families;
- one current/proposal distinction;
- evidence date.

### Question B — “What connects to this?”

**Explore**.

Needed:
- branch selector;
- one selected family at a time;
- compact content-item rows;
- typed relationship;
- source link;
- detail disclosure.

### Question C — “What should I re-check after this change?”

**Change review**.

Needed:
- upstream event selector;
- small review queue;
- one-line inclusion reason;
- explicit stop/non-propagation rows;
- detailed why/provision behind disclosure.

Research diagnostics answer a fourth, different question:
> “Where is our maintained projection incomplete or in need of evidence work?”

That belongs in **Expert / Research**, not the public default.

## 10. Quantitative design hypotheses

These are project test thresholds, not external standards.

For this exact fixture:

### Default Overview target
- <= 450 visible words;
- <= 12 primary visual blocks;
- <= 6 primary interactive choices;
- no paragraph longer than 2 sentences;
- no “how to read this” legend section;
- no research-maintenance taxonomy visible by default.

### Explore target
- one family expanded at a time;
- <= 6 child rows visible before further disclosure;
- each row:
  - act name;
  - branch;
  - one relation phrase;
  - source action;
  - optional detail.

### Change Review target
- one upstream change at a time;
- queue rows collapsed to:
  - human state label;
  - object;
  - <= 1 sentence reason;
- provision/evidence rationale behind “Why?”;
- exclusions remain visible but compact.

### Expert/Research target
- diagnostics moved out of default task flow;
- still one interaction away from regime page;
- no information deleted.

## 11. Research conclusion

> **The current problem is not “too much legal information”. It is too much legal information occupying the same visual priority at the same time.**

The next test should preserve the evidence model but change the presentation model to:

> **small overview spine -> task mode -> one selected detail set -> evidence on demand**

not:

> **one long page where every valid research product is a peer section.**

Next:
> create one concrete UI proposition, red-team it, then build it as a separate comparison route from the same medical-devices evidence.
