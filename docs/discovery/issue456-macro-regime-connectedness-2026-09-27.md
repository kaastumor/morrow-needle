# #456 — Macro/regime connectedness discovery

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT — MEDICAL-DEVICES REGIME AS FIRST MACRO FIXTURE**

## 1. Question

> Can Needle compress a dense EU legal regime into a useful macro view of legal structure, branching, downstream instruments, operative dependencies, temporal state and evidence gaps without degenerating into a generic knowledge graph or making unsupported legal-gap claims?

This line is independent of the frozen LVD formative test under #453.

It may reuse Needle's existing temporal/lineage/provenance discipline, but it may not modify the frozen LVD test artifact or count as human-value evidence for it.

## 2. Candidate scan

The purpose of the scan was not to rank EU legislation. It was to find one regime that exposes enough structural variety to falsify a macro-view design quickly.

### A. Medical devices — MDR / IVDR

Official Commission sources expose a particularly useful structure.

Current core regime:
- Regulation (EU) 2017/745 — Medical Devices Regulation (MDR);
- Regulation (EU) 2017/746 — In Vitro Diagnostic Medical Devices Regulation (IVDR).

Predecessor transition:
- MDR replaced Directive 90/385/EEC and Directive 93/42/EEC with effect from 26 May 2021;
- IVDR replaced Directive 98/79/EC with effect from 26 May 2022;
- transition provisions allow specified legacy devices/regime effects to continue in bounded circumstances.

The Commission's current overview groups:
- transition/amendment regulations;
- implementing regulations and decisions;
- delegated regulations;
- other acts such as the EUDAMED functionality decision;
- corrigenda;
- guidance and implementation material.

The overview currently names, before guidance and proposals:
- **17 unique implementing regulations/decisions** in its implementing-measures section;
- **7 unique delegated/delegated-amending regulations** in its delegated-act section;
- **4 major transition/amendment regulations** highlighted above those sections;
- **1 EUDAMED functionality decision** in “other acts”;
- **4 corrigenda**.

Thus the official overview alone exposes a regime with roughly thirty named downstream/change documents before counting predecessor directives, guidance, standards, factsheets or the 2025 proposed revision.

Important relation diversity:
- replaces/repeals;
- amends;
- implementing measure under;
- delegated act under;
- amends downstream act;
- functionality/transition trigger;
- corrigendum;
- non-binding guidance for.

Important temporal complexity:
- separate MDR and IVDR dates of application;
- legacy-device transitional periods;
- multiple later amendments to transition;
- EUDAMED module timing;
- a current legislative proposal that must remain clearly separate from enacted law.

Important source-quality advantage:
- the Commission already provides a strong hand-curated overview;
- EUR-Lex provides the authentic acts/consolidated versions;
- MDCG guidance is explicitly described as non-legally-binding.

This is useful because the macro prototype must add **structure and temporal/legal distinctions**, not merely rediscover links.

Official sources:
- https://health.ec.europa.eu/medical-devices-new-regulations/overview_en
- https://health.ec.europa.eu/medical-devices-sector/directives_en
- https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en
- https://eur-lex.europa.eu/eli/reg/2017/745/oj
- https://eur-lex.europa.eu/eli/reg/2017/746/oj

### B. MiFID II / MiFIR

Official Commission sources present:
- Directive 2014/65/EU (MiFID II);
- Regulation (EU) No 600/2014 (MiFIR);
- separate delegated/implementing-act pages;
- regulatory technical standards;
- implementing technical standards;
- equivalence decisions;
- current amendment/revision activity.

MiFIR's Commission page publishes a dedicated “full list” of implementing/delegated acts plus separate delegated-act, RTS and equivalence documents.

The regime is therefore highly suitable for a later **Level-1 -> Level-2** stress test.

Why not first:
- much of the downstream structure is highly technical financial-market implementation;
- the full-list inventories are primarily in PDFs;
- relation interpretation would require more domain-specific work before the visualization itself could be tested cleanly.

Official sources:
- https://finance.ec.europa.eu/financial-markets/financial-markets-policy/securities-markets/investment-services-and-regulated-markets_en
- https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/markets-financial-instruments-directive-ii_en
- https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/markets-financial-instruments-regulation_en

### C. REACH

Regulation (EC) No 1907/2006 is a very strong single-act hub.

ECHA's official legislation page groups:
- the core REACH Regulation;
- implementing legislation;
- registration/data-sharing rules;
- test-method regulation;
- fee regulation;
- Board-of-Appeal rules;
- subsequent amendments.

EUR-Lex exposes a long sequence of consolidated versions, with the current source showing frequent amendment activity.

Why not first:
- much of the visible network is annex/amendment evolution around one extremely large core instrument;
- it is therefore a stronger later test of temporal/amendment compression than of mixed relationship families;
- a naive graph would risk becoming an amendment chronology rather than a regime map.

Official sources:
- https://echa.europa.eu/regulations/reach/legislation
- https://eur-lex.europa.eu/eli/reg/2006/1907/oj

### D. CRR / CRD prudential regime

The Commission maintains separate delegated/implementing-act surfaces for:
- Regulation (EU) No 575/2013 (CRR);
- Directive 2013/36/EU (CRD).

The current CRR page exposes separate full-list, delegated-act, implementing-act, RTS, ITS and equivalence collections. The published RTS document alone is hundreds of kilobytes, illustrating the depth of the Level-2 layer.

Why not first:
- it is an excellent future **extreme-density** stress test;
- starting there would make it hard to distinguish a failure of the macro-view concept from a failure caused by domain size and specialised banking terminology.

Official sources:
- https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/capital-requirements-regulation_en
- https://finance.ec.europa.eu/regulation-and-supervision/financial-services-legislation/implementing-and-delegated-acts/capital-requirements-directive-crd-4_en
- https://finance.ec.europa.eu/banking/banking-regulation/prudential-requirements_en

## 3. First experimental fixture

Use the **EU medical-devices regime (MDR / IVDR)**.

This is a fixture choice, not a claim that the regime is more important, better designed, or more complex than the alternatives.

It is selected because one bounded official-source set contains all of the structural adversaries the prototype needs:

1. several predecessor directives;
2. two present-day sibling core regulations;
3. transition overlap/legacy effects;
4. later amendments affecting one or both core branches;
5. implementing measures;
6. delegated measures;
7. downstream acts that are themselves amended;
8. an operational decision whose legal significance is tied to EUDAMED timing;
9. corrigenda;
10. a large non-binding guidance layer that must remain visually/legal-semantically separate;
11. a current proposal that must not be shown as enacted law.

## 4. The first macro view must aggregate

Do **not** draw thirty individual child nodes at first render.

The macro view should expose **families**.

### Level 0 — regime summary

Show only:

- predecessor regime;
- MDR branch;
- IVDR branch;
- joint transition/change layer;
- implementing layer;
- delegated layer;
- EUDAMED/system-operation layer;
- guidance layer;
- current proposal separately marked as proposed.

At this level, a family may show:
- represented item count;
- current/future/historical mix;
- evidence-coverage status;
- whether the family applies to MDR, IVDR or both.

Target:
> no more than roughly 8–10 visual objects at first render.

### Level 1 — family / branch

Expand one family.

Examples:

**Implementing measures**
- conformity assessment / notified bodies;
- EUDAMED;
- UDI;
- reference laboratories;
- common specifications;
- expert panels;
- products without intended medical purpose.

**Transition/change**
- 2020/561;
- 2022/112;
- 2023/607;
- 2024/1860.

This level may show individual acts, but should still group by legal function where evidence supports the grouping.

### Level 2 — individual act

Show:
- act identity;
- relation to core act(s);
- affected branch;
- current legal/document state;
- important dates;
- exact enabling/affected provision where represented;
- official source;
- downstream amendments where relevant.

### Level 3 — provision / evidence

Descend to:
- exact parent provision/delegation;
- exact child provision;
- operative dependency;
- amendment target;
- source version;
- evidence/provenance.

This is where Needle's existing act-centric pattern becomes useful again.

## 5. Relationship inventory for v0

Do not invent a universal ontology.

For the first medical-devices fixture, presentation needs only relationships actually evidenced by the bounded source set.

### Genealogy

- **REPLACED_BY / REPEALED_BY**
- predecessor -> current core act

### Change

- **AMENDED_BY**
- core or downstream act -> amending act

### Downstream authority

Human-facing relations such as:
- **IMPLEMENTED_BY**
- **SUPPLEMENTED_BY / DELEGATED_ACT_UNDER**

Use only where the source/provision supports the meaning.

Do not infer from the document title alone.

### Correction

- **CORRECTED_BY**
- act -> corrigendum

### Operational trigger

A narrow relation is needed for items such as an EUDAMED functionality decision where the decision changes the practical/legal transition state of specified systems.

Do not create a permanent schema enum yet.

Presentation v0 may use:
> **ACTIVATES / DECLARES FUNCTIONAL FOR TRANSITION PURPOSES**

only with exact provision/evidence.

### Guidance

- **GUIDANCE_FOR**

This relation must be visually segregated and explicitly labelled:
> **non-binding guidance**

It must never share a visual style that makes it look like delegated/implementing legislation.

### Proposal

- **PROPOSED_CHANGE_TO**

Proposal nodes live in a separate future/procedure lane.

They are not “future law” and may never receive the same current/legal-state styling as enacted amendments.

## 6. Macro presentation hypothesis

Prefer a **structured constellation / regime tree**, not a force-directed graph.

Desktop concept:

```text
PREDECESSOR REGIME
┌────────────────┬────────────────┬────────────────┐
90/385/EEC       93/42/EEC        98/79/EC
     \               /                 |
      \             /                  |
       └── replaced by ──┐      replaced by
                         |            |
                      MDR 2017/745   IVDR 2017/746
                         \            /
                          \          /
                    JOINT TRANSITION / CHANGE
                    2020 · 2022 · 2023 · 2024
                         |            |
         ┌───────────────┼────────────┼───────────────┐
         |               |            |               |
   Implementing      Delegated     EUDAMED         Guidance
   17 represented    7 represented  system lane      non-binding
         |               |            |
      [expand]          [expand]     [expand]

                   PROPOSED REVISION
                    clearly separate
```

The counts are navigation summaries, not legal weights.

## 7. “Gap” taxonomy

The macro view must not turn missing data into legal conclusions.

### COVERAGE_GAP

Meaning:
> this part of the regime is outside the current bounded inventory.

Example:
- a guidance family is intentionally not fully enumerated.

Allowed display:
> **Not fully covered**

Never:
> “No other guidance exists.”

### EVIDENCE_GAP

Meaning:
> a relationship or state has been identified as relevant, but the current evidence is insufficient to assert it safely.

Allowed display:
> **Relationship awaiting source verification**

### REVIEW_GAP

Meaning:
> something upstream changed after a dependent item was last reviewed, so the dependent claim should be rechecked.

This is one of the most promising research signals.

Example:
> core provision amended 2026; downstream implementing measure last verified against pre-amendment text.

Allowed display:
> **Review needed — upstream legal state changed**

Never:
> “Downstream act is invalid/outdated.”

### STRUCTURAL_GAP_CANDIDATE

Meaning:
> an authoritative parent provision appears to require/enable a downstream measure, but no corresponding child has been identified **after the relevant coverage/source search**.

This is a research queue item, not a legal conclusion.

Required display:
> **Expected downstream measure not yet identified in this evidence set**

Only after official-source review could a stronger claim be considered.

### TEMPORAL_REVIEW_SIGNAL

Meaning:
> lineage/dependency structure plus date evidence suggests an overlap, gap or future transition that deserves human review.

Never infer applicability from graph geometry.

## 8. Research diagnostics that may be earned later

If the first regime projection is source-complete enough, derive review signals such as:

- upstream act changed after downstream child last reviewed;
- parent delegation represented but child not yet source-verified;
- downstream act still references predecessor terminology;
- one branch has a future transition while sibling branch does not;
- a transition amendment affects both core regulations but only one displayed family has been refreshed;
- guidance is newer than the binding instrument it interprets;
- a corrigendum affects a provision used by a downstream dependency;
- a proposed amendment touches a high-dependency provision.

These must remain:
> **signals to inspect evidence**

not:
> automatic findings of legal defects.

## 9. Graph-spaghetti falsifier

The macro view fails if the default state needs:
- more than roughly 8–10 visible top-level objects;
- more than 4–5 relationship concepts visible simultaneously;
- individual labels for every implementing/delegated act;
- line crossings that require a legend to decipher;
- hidden legal qualifications that only appear after graph interaction.

If that happens:
- collapse to grouped lanes/counts;
- prefer a structured source-linked regime ledger;
- keep the graph only as secondary navigation or reject it.

The grouped list is a serious baseline.

## 10. Strong baseline

The European Commission's medical-devices overview is already strong.

It provides:
- current core acts;
- predecessor transition;
- transition amendments;
- implementing measures;
- delegated acts;
- other acts;
- corrigenda;
- guidance links.

Therefore the macro experiment earns no value merely by collecting the same links.

The hypothesised additional value is:

> **typed structure + branch context + temporal state + progressive drill-down + explicit evidence/coverage/review gaps in one coherent model.**

## 11. Initial bounded data slice

Do not ingest the whole regime.

For the first abstract prototype, represent:

### Predecessor/core
- 90/385/EEC
- 93/42/EEC
- 98/79/EC
- Regulation 2017/745
- Regulation 2017/746

### Joint/current change layer
- Regulation 2020/561
- Regulation 2022/112
- Regulation 2023/607
- Regulation 2024/1860

### Downstream samples
Choose one or two from each family:
- EUDAMED;
- common specifications;
- UDI;
- notified-body/conformity-assessment;
- reference laboratories;
- expert panels;
- delegated UDI/device-classification examples.

### Correction/guidance/proposal
- one corrigendum;
- one clearly non-binding MDCG guidance item;
- the 2025 proposed MDR/IVDR revision as a procedure/proposal node only.

The default macro view may still display official family counts from the Commission overview without rendering every child.

## 12. Disposition

> **ADOPT_FOR_EXPERIMENT**

Next bounded question:

> Can a static macro/meso prototype represent this medical-devices slice with 8–10 first-render objects, clear legal/non-binding/proposal separation, and useful drill-down — while the grouped source-linked Commission page remains a credible baseline?

Do not expand the data set merely to make the graph impressive.

A successful first prototype should make the regime **feel smaller and more understandable**, not demonstrate how many nodes Needle can draw.
