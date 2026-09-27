# Candidate B lifecycle view — information-design research

Date: 2026-09-27  
Owner: #434  
Status: **DESIGN RESEARCH — IMPLEMENTATION NOT YET STARTED**

## Conclusion

There is no single accepted standard for a "legal lifecycle graph".

The defensible design stack is instead:

1. **ELI / ELI-I** for legal-resource identity and typed legal relationships;
2. **ISO 9241-110 / 9241-112 / 9241-125** for interaction and information-presentation principles;
3. **ISO 24495-1** for plain-language information;
4. **WCAG 2.2** as the product accessibility target, while recognising that the currently harmonised EU public-sector accessibility standard EN 301 549 v3.2.1 is based on WCAG 2.1;
5. established legal-publishing patterns from **EUR-Lex** and **legislation.gov.uk**;
6. progressive disclosure only for secondary detail, following mature public-service design practice.

The correct Candidate-B pattern is therefore:

> **text-first legal information architecture + typed lifecycle/relationship visualisation + progressive evidence disclosure**

not:

> **graph-first legal knowledge graph**

## 1. Legal semantics: ELI first

The Publications Office lists the European Legislation Identifier (ELI) ontology as the common model for exchanging legislation metadata on the web. EU Vocabularies currently identifies **ELI v1.5** as the latest ontology.

The official ELI model exposes typed legal-resource relations including:

- `changes / changed_by`;
- `amends / amended_by`;
- `repeals / repealed_by`;
- `commences / commenced_by`;
- `consolidates / consolidated_by`;
- `based_on / basis_for`;
- `applies / applied_by`;
- `transposes / transposed_by`;
- citation/case-law relations.

ELI-I extends ELI to represent the impact of legislative acts, including text modifications and consolidation impact.

### Needle rule

For a displayed relationship:

1. prefer an ELI/official legal relation where it accurately captures the meaning;
2. otherwise use an existing Needle typed relation that preserves a consequential distinction, e.g. `RECAST_AS`;
3. introduce a new relation only after an actual representational failure;
4. never use generic `RELATED_TO` or `INFLUENCES` as legal truth.

User-facing headings may use plain language such as **What shapes this act**, but the underlying edge remains typed.

Sources:
- https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http%3A%2F%2Fpublications.europa.eu%2Fresource%2Fdataset%2Feli
- https://op.europa.eu/documents/3938058/11669184/eli-diagrams.pdf
- https://eur-lex.europa.eu/content/eli-register/implementing_eli.html

## 2. Information presentation: ISO 9241 family

### ISO 9241-110:2020

Current interaction principles include:
- suitability for the user's task;
- self-descriptiveness;
- conformity with user expectations;
- learnability;
- controllability;
- use-error robustness;
- user engagement.

For Candidate B, the strongest implications are:
- the main answer should be obvious without interaction;
- information order follows the legal task rather than the storage model;
- users control expansion and detail;
- unexpected legal-state assumptions fail visibly.

### ISO 9241-112:2025

The current presentation-of-information standard focuses on perception and understanding.

Publicly available standard previews enumerate the presentation principles as:
- detectability;
- discriminability;
- conciseness;
- unambiguous interpretability;
- freedom from distraction;
- consistency.

Implications:
- current status and the focal act must dominate;
- lineage, lifecycle, context and downstream effect must be visually distinguishable;
- every relation label must be unambiguous;
- provenance detail must not compete visually with the answer;
- partial/hidden information must make it clear that more information exists.

### ISO 9241-125:2017

The visual-presentation standard covers:
- arranging and labelling information;
- lists and tables;
- graphical objects;
- coding techniques including colour and markers;
- organisation based on human perception and memory.

It explicitly does not provide a prescriptive graph-visualisation recipe.

### Needle rule

Use **semantic groups and labels first**, visual connectors second.

Sources:
- https://www.iso.org/standard/75258.html
- https://www.iso.org/standard/87518.html
- https://www.iso.org/standard/64839.html

## 3. Plain language: ISO 24495-1:2023

ISO 24495-1 is the international plain-language standard and explicitly applies to digital information and can apply to legislative/technical material.

Candidate-B text should therefore:

- answer the user's likely question before explaining the data model;
- use the familiar legal name before machine identifiers;
- explain specialist terms where the distinction matters;
- keep legal precision while shortening syntax;
- separate fact from implication and limitation.

### Needle rule

Prefer:

> **Low Voltage Directive 2014/35/EU**

with secondary metadata:

> CELEX 32014L0035 · ELI link

rather than presenting `CELEX:32014L0035` as the primary human label.

Source:
- https://www.iso.org/standard/78907.html

## 4. Accessibility: WCAG / EN 301 549

For this product, target **WCAG 2.2 AA** as current web best practice.

Relevant requirements include:

### Relationships cannot exist only visually

WCAG 1.3.1 requires information, structure and relationships conveyed through presentation to be programmatically determinable or available in text.

Therefore:
- an SVG line cannot be the only expression of `RECAST_AS`;
- the DOM must contain a readable relation sentence/list;
- a screen-reader user must obtain the same legal relationship.

### Do not use colour alone

WCAG 1.4.1 forbids colour as the only means of distinguishing meaning.

Therefore:
- lineage/context/dependency lanes may have colour;
- they must also have text labels, headings, line styles, icons or other non-colour cues.

### Reflow

WCAG 1.4.10 requires reflow without two-dimensional scrolling at the defined narrow viewport, except where two-dimensional layout is essential.

Therefore:
- desktop may use a horizontal lifecycle;
- mobile should convert it to a vertical ordered sequence rather than squeeze or horizontally scroll the whole legal map.

### Pointer targets

WCAG 2.2 adds a 24×24 CSS-pixel minimum target-size criterion, subject to its documented exceptions.

### EU regulatory context

For public-sector sites under the EU Web Accessibility Directive, the currently harmonised EN 301 549 v3.2.1 remains based on WCAG 2.1. WCAG 2.2 is newer and useful as a product target but should not be mislabeled as the currently harmonised EU legal baseline.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships
- https://www.w3.org/WAI/WCAG22/Understanding/use-of-color
- https://www.w3.org/WAI/WCAG21/Understanding/reflow
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- https://digital-strategy.ec.europa.eu/en/policies/web-accessibility-directive-standards-and-harmonisation

## 5. Established legal-publishing conventions

### EUR-Lex

EUR-Lex already treats document relationships as typed information. Its document-information/search model exposes categories such as legal basis, amendments, corrections, affected-by-case, cited instruments and other document relationships.

EUR-Lex has also experimented with a relationship graph:
- focal act as the central node;
- relations grouped by type;
- colour-coded relation categories;
- expandable subcategories;
- document nodes linking to the source.

This validates relationship visualisation as a legal-navigation concept, but it does **not** establish that a large graph is the best Candidate-B default.

The Candidate-B opportunity is to be more task-oriented:
- explain what the relation means;
- distinguish time;
- expose the state consequence;
- combine lifecycle and downstream operational state.

Sources:
- https://eur-lex.europa.eu/content/help/search/expert-search.html
- https://eur-lex.europa.eu/content/newsletter/newsletter_2023-02.pdf

### legislation.gov.uk

The UK official legislation service uses several patterns worth retaining conceptually:

- a visible **What Version** distinction;
- a visible statement of how current the displayed law is;
- explicit notice when future/outstanding changes exist;
- a **Timeline of Changes** whose dates correspond to operative change points;
- original vs revised text separated.

This supports Candidate B's existing insistence that:
- current and future-fixed state are different;
- freshness belongs near the primary answer;
- time points need labels explaining what legally happened at them.

Source:
- https://www.legislation.gov.uk/help

## 6. Progressive disclosure

The GOV.UK Design System's details pattern exists to make pages easier to scan by hiding detail only some users need. It explicitly warns not to hide information that most users need.

### Needle rule

**Always visible:**
- act identity;
- current status;
- evidence/freshness date;
- plain-language summary;
- core lineage;
- key lifecycle dates;
- material direct relationships;
- future-known event if consequential.

**Expandable:**
- raw CELEX/ELI identifiers;
- source locators;
- evidence classification;
- relation definitions;
- detailed legal caveats;
- less-important related instruments.

Source:
- https://design-system.service.gov.uk/components/details/

## 7. Recommended Candidate-B page architecture

### A. Act header — always visible

Display:

**Low Voltage Directive**  
**Directive 2014/35/EU**

Then:
- document type;
- current state;
- evidence/freshness date;
- official-source link.

Do not lead with CELEX.

### B. At a glance — necessary information text

Two to four plain-language sentences answering:

1. What is this?
2. Where did it come from?
3. What is its current legal/lifecycle state?
4. What is the most important downstream mechanism on this page?

This must be useful without reading the visual map.

### C. Life of this act

Use a chronological sequence with explicit event labels.

Do not collapse:
- adoption;
- publication;
- entry into force;
- application;
- repeal/end.

Desktop may use a compact horizontal timeline.

Mobile must render the same information as a vertical ordered list.

### D. Came from / goes to

A compact lineage lane.

Each connection contains:
- human relation label;
- source act;
- target act;
- evidence link.

Unknown successor state must be expressed as bounded absence:

> **No successor is represented in this evidence view.**

not:

> **No successor exists.**

### E. What shapes this act

This heading is user-facing grouping, not an edge type.

Each item must explain its typed legal relationship in one sentence.

Example pattern:

> **Common legislative framework**  
> This act was aligned with [instrument].  
> **Relationship:** [typed relation]  
> **Why it matters here:** [one-sentence consequence]

### F. What flows from this act

Show operative dependencies from the focal provision into downstream legal state.

For Candidate B:

> Article 12 -> OJ harmonised-standard reference mechanism -> individual standard status.

The relation must remain readable as text without the arrows.

### G. Why this status / evidence

Each consequential displayed fact should expose:
- official source;
- human-readable source title;
- exact locator/provision where useful;
- ELI/CELEX as secondary metadata;
- evidence/freshness date;
- direct vs derived status where material.

### H. Coverage boundary

Always-visible short text:

> **This is an evidence-bounded view, not a complete map of every document that may be legally relevant.**

Longer limitations may be expandable.

## 8. Required textual equivalent of the visual

The lifecycle map must have a structured text representation in the DOM.

Recommended form:

### Legal lineage

1. **Directive A**
   - relationship: codified as
2. **Directive B**
   - relationship: recast as
3. **Directive C — current focal act**

### Key lifecycle events

- **Adopted:** [date]
- **Published:** [date]
- **Entered into force:** [date]
- **Applicable from:** [date]
- **Predecessor repealed:** [date]
- **Future end/successor:** [state or bounded unknown]

### Material legal relationships

- **[Instrument] — [typed relation]**
  - Why it matters: [...]
  - Evidence: [...]

### Downstream mechanism

- **[Provision] — [typed dependency]**
  - Resulting legal state: [...]
  - Evidence: [...]

The visual presentation may reorganise this material, but it may not contain legal meaning absent from the text.

## 9. Visual coding recommendation

Do not make a free-form network graph the primary view.

Use four stable semantic regions:

1. **Lineage** — before / after the focal act;
2. **Lifecycle** — chronological time;
3. **Context** — instruments that legally shape/implement/interpret;
4. **Downstream effect** — mechanisms or states flowing from the act.

For every edge:
- show the relation as text;
- use an arrow only where direction is meaningful;
- never encode relation type through colour alone;
- avoid crossings where possible;
- keep the focal act visually dominant;
- use progressive disclosure for second-order nodes.

## 10. Necessary information text: content contract

For every focal act, the first implementation should attempt to supply the following text fields, with explicit absence where unsupported:

| Information | Default visibility | Why |
| --- | --- | --- |
| Common/short title | visible | human recognition |
| Formal act citation | visible | precise identity |
| Document type | visible | legal character |
| Current lifecycle/legal status | visible | primary task |
| Evidence checked/as-of date | visible | freshness |
| One-paragraph plain-language summary | visible | comprehension |
| Predecessor(s) + typed relation | visible | lineage |
| Successor/end state | visible if known; bounded unknown otherwise | future/continuity |
| Adoption date | visible in timeline | chronology |
| Publication date | visible in timeline | source state |
| Entry into force | visible in timeline | legal force |
| Application date | visible in timeline | operative state |
| Repeal/end date | visible when applicable | operative state |
| Material framework/context acts | visible but secondary | legal position |
| Material downstream dependencies | visible | operational meaning |
| Future-fixed changes | visible when consequential | temporal safety |
| Official source per major claim | visible/linkable | verification |
| ELI/CELEX + exact locator | secondary/expandable | technical verification |
| Relation definition | expandable | learnability |
| Coverage/unknown boundary | visible | prevents completeness illusion |
| Legal-advice disclaimer | compact, secondary | scope |

## 11. Design standard for #434

The first lifecycle implementation should be accepted only if it satisfies all of these:

- **task-first:** primary answers precede provenance mechanics;
- **text-first semantics:** every graphical relation exists in readable HTML;
- **ELI-aligned relation vocabulary:** reuse official relation semantics where accurate;
- **typed exceptions:** Needle-specific relations such as recast remain explicit where needed;
- **temporal separation:** legal dates keep distinct meanings;
- **evidence adjacency:** verification is one interaction away;
- **freshness adjacency:** as-of state sits near the answer;
- **progressive disclosure:** secondary evidence is hidden only when it is not required for the main task;
- **responsive transformation:** timeline/map becomes an ordered vertical representation on narrow screens;
- **no colour-only semantics:** labels survive monochrome rendering;
- **bounded completeness:** the interface describes what it covers and does not imply exhaustive legal relevance;
- **plain language:** machine identifiers are secondary to recognisable legal names;
- **no new truth store:** the UI remains a read-side projection.

## Research disposition

> **PROCEED TO INFORMATION-ARCHITECTURE / CONTENT PROTOTYPE BEFORE CODE**

The next step should not be a graph library or schema.

It should be a static content-and-layout prototype for Directive 2014/35/EU containing the complete necessary text above.

Only after the textual information architecture works should connectors/visual relation styling be added.
