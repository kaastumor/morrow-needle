# #437 — Navigator P1/P2 reader job, alternatives and LVD evidence contract

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT — CONTENT COMPLETION BEFORE FURTHER UI EXPANSION**

## 1. Question

> What exact known-act reader job should the first Navigator page optimise for, what is the strongest realistic alternative, and what consequential LVD content/evidence is still missing before further UI work?

This is a discovery result under the adopted plan:

`docs/plans/eu-legislation-navigator-prototype-v0.1.md`

It does not establish external user value.

## 2. Primary reader job

The first page should optimise for a reader who already has a specific EU act and needs orientation before deciding whether to read the underlying sources in depth.

Primary job:

> **I have Directive 2014/35/EU. Tell me what it is for, whether it is current, what and whom it covers, which dates mean what, where it came from, what materially connects to it, what practical legal mechanisms flow from it, and where I can verify each consequential point.**

This is narrower than:
- finding which legislation applies to a product;
- determining full conformity;
- national implementation advice;
- case-law research;
- a complete legal knowledge graph.

## 3. Concrete reader tasks

A credible first LVD page should let a reader answer these eight tasks without first reconstructing several separate official pages.

### T1 — Identify the act and its current documentary state

Answer:
- common name;
- formal citation;
- act type;
- whether EUR-Lex lists the act as in force;
- current consolidated version date;
- difference between authentic OJ act and documentary consolidation.

### T2 — Understand purpose and scope

Answer:
- what the Directive is trying to achieve;
- voltage ranges covered;
- major equipment/phenomena explicitly excluded;
- the fact that “within the voltage range” does not by itself establish that a specific product is fully governed by this Directive.

### T3 — Identify the economic actors the Directive regulates

Orient the reader to the Directive's role-specific obligations for:
- manufacturers;
- authorised representatives;
- importers;
- distributors.

Do not turn this into personalised compliance advice.

### T4 — Distinguish the dates

Explain separately:
- adoption;
- publication;
- entry into force;
- transposition deadline;
- application of national implementing measures;
- repeal of the predecessor;
- later amendment/application dates.

A reader must not infer legal application from the adoption or publication date alone.

### T5 — Understand legal lineage

Answer:
- 73/23/EEC as the earlier act in the displayed lineage;
- 2006/95/EC as codification;
- 2014/35/EU as recast;
- repeal of 2006/95/EC from 20 April 2016.

“No successor represented” must remain different from “no successor exists”.

### T6 — Understand the selected legal context

Explain why the page shows, without calling them ancestors:
- Article 114 TFEU;
- Regulation (EC) No 765/2008;
- Decision No 768/2008/EC;
- Regulation (EU) No 1025/2012;
- Directive (EU) 2024/2749.

### T7 — Understand the represented conformity mechanism

Explain:
- Article 12 presumption of conformity;
- OJ publication of harmonised-standard references;
- the presumption is limited to safety objectives covered by the standard/part;
- Article 12 is a conformity mechanism, not automatic proof that a product complies with every applicable requirement;
- link into the two existing LVD standard-status examples.

### T8 — Verify and bound the explanation

A reader can identify:
- official source for each consequential claim;
- legal/source version used;
- legal as-of / verified-through semantics;
- what has not been researched or represented.

## 4. Strongest realistic alternatives

The baseline is not “read the raw Directive unaided”.

### Baseline A — official-source workflow

A competent reader can combine:

1. **EUR-Lex legal act / consolidated text**
   - exact legal text;
   - document status and consolidated versions;
   - document relationships;
   - national transposition navigation.

2. **EUR-Lex summary**
   - concise aim;
   - voltage scope;
   - high-level economic-operator responsibilities;
   - application dates;
   - background and current 2024/2749 amendment note.

3. **European Commission LVD / harmonised-standards page**
   - short name and base act;
   - applicability from 20 April 2016;
   - repealed Directive 2006/95/EC;
   - guidance links;
   - current OJ harmonised-standard publication navigation.

4. **OEIL procedure material, when legislative history matters**
   - recast purpose;
   - alignment with the New Legislative Framework / “Goods Package”;
   - procedure history.

Observed strengths:
- authoritative/official;
- broader documentary/legal coverage than the prototype;
- current document navigation already exists;
- EUR-Lex summary is already reasonably plain-language;
- Commission page is particularly strong for standards publication navigation.

Observed integration burden:
- purpose/scope, current text, legislative lineage, standards publication state and legislative-history context live on different surfaces;
- relation meaning is not presented as one task-oriented explanation;
- the reader must decide which date/source role answers which question;
- a concise “what this means together” view is not the primary presentation.

This is an integration/workflow hypothesis, not a claim that official information is unavailable.

### Baseline B — competent source-linked note

A capable researcher can create a short note from the same sources with:
- purpose/scope;
- exclusions;
- key dates;
- lineage;
- framework context;
- Article 12;
- source links.

This is a very strong comparator because it can approximate much of the Navigator page without software.

The remaining product question is therefore not:
> “Can Needle explain the Directive at all?”

It is:
> **“Does a maintained, structured page make this orientation/verification job materially easier or safer than a competent source-linked note and the official-source bundle?”**

## 5. Source-backed LVD content sheet

### 5.1 Identity and current documentary state

**Claim:** Directive 2014/35/EU is the Low Voltage Directive, a recast act concerning electrical equipment designed for use within certain voltage limits.

**Official owner:** EUR-Lex legal act  
https://eur-lex.europa.eu/eli/dir/2014/35/oj/eng

**Current state observed 2026-09-27:**
- EUR-Lex lists the legal act as in force;
- current consolidated text exposed at 30 May 2026;
- consolidation is documentary/informational and authentic OJ acts remain legally authoritative.

**Presentation rule:** distinguish:
- act status;
- consolidation/version date;
- verification date.

Do not label deployment time as legal freshness.

### 5.2 Purpose

**Claim:** Article 1 states that the Directive aims to ensure electrical equipment on the market meets requirements providing a high level of protection for the health and safety of persons, domestic animals and property, while guaranteeing functioning of the internal market.

**Owner:** Article 1, current consolidated text  
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014L0035-20260530

**Plain-language form:**
> It sets EU safety and market rules for electrical equipment within specified voltage ranges, combining safety protection with free movement in the internal market.

This is an editorial simplification and must retain the linked Article 1 wording as evidence.

### 5.3 Technical scope

**Claim:** The Directive applies to electrical equipment designed for:
- 50–1,000 V alternating current;
- 75–1,500 V direct current;
except the equipment and phenomena listed in Annex II.

**Owner:** Article 1.

### 5.4 Major express exclusions

Annex II lists:
- electrical equipment for use in an explosive atmosphere;
- electrical equipment for radiology and medical purposes;
- electrical parts for goods and passenger lifts;
- electricity meters;
- plugs and socket outlets for domestic use;
- electric fence controllers;
- radio-electrical interference;
- specialised electrical equipment for ships, aircraft or railways complying with international safety provisions in which Member States participate;
- custom-built evaluation kits for professionals used solely at research and development facilities.

**Owner:** Annex II, authentic act/current consolidated text.

**Presentation rule:** these are express LVD scope exclusions. Do not infer the complete alternative legal regime for each excluded category unless separately researched.

### 5.5 Economic operators

The Directive defines and regulates:
- manufacturer;
- authorised representative;
- importer;
- distributor.

High-level orientation:

**Manufacturer**
- design/manufacture in accordance with Article 3 / Annex I safety objectives;
- prepare technical documentation;
- carry out conformity assessment;
- draw up EU declaration of conformity and affix CE marking when conformity is demonstrated;
- keep specified documentation for 10 years.

Owner: Article 6.

**Importer**
- place only compliant equipment on the market;
- verify the manufacturer's conformity assessment, technical documentation, CE marking and required documentation before placing equipment on the market;
- additional identification/information/cooperation duties apply.

Owner: Article 8.

**Distributor**
- act with due care;
- verify CE marking, required documents/instructions/safety information and specified manufacturer/importer obligations before making equipment available;
- additional corrective/information/cooperation duties apply.

Owner: Article 9.

**Boundary:** a Navigator overview should orient the reader to these actor roles, not enumerate every obligation or decide which role applies to the reader.

### 5.6 Legal basis

**Claim:** Article 114 TFEU.

Owner:
- act metadata / citation;
- Article 114 TFEU.

https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:12012E114

### 5.7 Core lifecycle dates

Keep meanings separate:

| Date | Meaning | Owner |
| --- | --- | --- |
| 26 Feb 2014 | adoption/date of Directive | legal act metadata |
| 29 Mar 2014 | publication in OJ L 96 | publication metadata |
| 18 Apr 2014 | entry into force, twentieth day after publication | Article 28 |
| 19 Apr 2016 | deadline to adopt/publish specified national transposition measures | Article 26 |
| 20 Apr 2016 | Member States apply those measures | Article 26 |
| 20 Apr 2016 | Directive 2006/95/EC repealed from this date | Article 27 |
| 9 Oct 2024 | date of Directive (EU) 2024/2749 | amending act |
| 29 May 2026 | transposition deadline for 2024/2749 | 2024/2749 Article 11 |
| 30 May 2026 | measures implementing 2024/2749 apply; current LVD consolidation date | 2024/2749 Article 11 / EUR-Lex consolidation |

Source:
https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024L2749

### 5.8 Lineage

**2006/95/EC**
- identifies itself as a codified version after substantial amendment of 73/23/EEC.

**2014/35/EU**
- expressly identifies itself as a recast;
- repeals 2006/95/EC from 20 April 2016.

Owners:
- Directive 2006/95/EC recital/title;
- Directive 2014/35/EU recital 1 and Article 27.

### 5.9 Selected framework/context

These are not all one relation type.

**Regulation (EC) No 765/2008**
- recital 2 of 2014/35/EU describes it as laying down rules on accreditation, market surveillance, controls of products from third countries and general CE-marking principles.

**Decision No 768/2008/EC**
- recital 3 describes it as providing common principles/reference provisions for product legislation and says Directive 2006/95/EC should be adapted to it.

**Regulation (EU) No 1025/2012**
- Article 2 of the LVD uses its harmonised-standard definition;
- recitals 16–17 connect the harmonised-standard/formal-objection mechanism to the European standardisation framework.

**Directive (EU) 2024/2749**
- amends the LVD for internal-market-emergency procedures, including conformity-assessment/presumption/common-specification/market-surveillance mechanisms;
- Member States were required to apply its implementing measures from 30 May 2026.

### 5.10 Article 12 and standards

Article 12 states that electrical equipment conforming to harmonised standards or parts whose references have been published in the OJ is presumed to conform to the Article 3 / Annex I safety objectives covered by those standards or parts.

Important boundary:
- the presumption is scoped to objectives covered by the cited standard/part;
- it is not a statement that the product is fully compliant with every applicable legal requirement.

Additional context:
- Articles 13 and 14 contain fallback presumption mechanisms involving published IEC safety provisions and, in the specified circumstances, national standards.

**Product decision:** the first page should mention that alternative mechanisms exist, but should not expand them into full subpages unless a later task earns that depth.

### 5.11 Current amendment state

EUR-Lex exposes a current consolidated LVD text dated 30 May 2026 and linked modifications by Directive (EU) 2024/2749.

The EUR-Lex summary states that 2024/2749 measures had to be transposed by 29 May 2026 and apply from 30 May 2026.

**Presentation implication:** “Current” should include both:
- base act remains in force;
- displayed current text includes a later amendment.

## 6. Claim-to-owner mapping

The first page should not own legal truth independently.

| Displayed information | Truth/evidence owner | Presentation role |
| --- | --- | --- |
| act identity/status/version | EUR-Lex/ELI + existing identity/source handling | project/friendly label |
| purpose/scope/exclusions | Article 1 + Annex II | editorial plain-language explanation referencing source |
| economic-operator orientation | Articles 2, 6–10 | bounded overview |
| dates | Temporal assertions / official provisions and metadata | formatted lifecycle sequence |
| codification/recast/repeal | lineage owner + official recitals/articles | readable lineage |
| framework context | official recitals/provisions + provenance | typed context cards |
| current amendment | amending act + consolidated/source state | “amended by / applies from” |
| Article 12 mechanism | authoritative legal text + dynamic-set status owners | downstream dependency view |
| individual standard status | existing Candidate-B dynamic-set fixtures | status cards |

### Representational note

The existing regime-lineage v0.2 vocabulary can express `RECAST_AS` but not a literal `CODIFIED_AS` relation.

For this horizon:
- do not mislabel codification as reenactment/replacement;
- do not add a generic edge;
- keep the displayed codification claim source-backed/editorial until a second concrete case demonstrates that canonical `CODIFIED_AS` persistence is necessary.

One LVD page alone does not yet justify a schema change.

## 7. Freshness semantics

The page needs three visibly different concepts.

### Legal state as of
The date for which a statement is intended to describe operative legal state.

### Evidence verified through
The latest date on which the displayed source set/claims were substantively checked.

### Source/version date
A source-specific date, such as:
- OJ publication date;
- consolidated-text date;
- amendment application date.

Do not collapse these into “last updated”.

Recommended first-page wording:

> **Legal view:** as of 27 September 2026  
> **Evidence verified:** 27 September 2026  
> **Current EUR-Lex consolidation used:** 30 May 2026

This is deliberately explicit for the prototype; future simplification may be tested.

## 8. What is still missing from the current deployed page

The lifecycle page already covers much of tasks T1, T4–T7.

The most consequential missing content is:

1. **purpose text anchored directly to Article 1;**
2. **major exclusions from Annex II;**
3. **actor orientation** for manufacturers/importers/distributors;
4. clearer distinction between **legal as-of**, **verified-through** and **source version**;
5. explicit mention that Articles 13/14 provide additional presumption routes when Article 12 harmonised standards are unavailable;
6. a compact **correction / evidence-boundary** path suitable for eventual public operation.

These are content-completeness gaps, not evidence for another graph feature.

## 9. Strong contrary explanation

> A good source-linked note already solves this job, and the structured page merely turns the same note into boxes and timelines.

This remains credible.

The current sponsor reaction shows that the integrated page can feel materially more useful than scattered context, but that is one sponsor-use observation and cannot resolve the comparator question.

Therefore:
- do not claim superiority;
- preserve a competent source-linked note as the later comparator;
- do not add features merely to make the software comparator look richer.

## 10. Unresolved questions / explicit limits

### Not required to resolve before the next content prototype

- exhaustive national transposition state;
- complete case-law interpretation;
- every amendment or related act;
- every applicable product law;
- all harmonised standards;
- Dutch-language presentation.

### Must remain explicit

- “in force” does not mean every provision has one simple application date;
- a consolidated text is informational/documentary, not itself the authentic amending act;
- exclusion from LVD scope does not identify the full alternative legal regime;
- a harmonised-standard presumption is bounded to covered safety objectives;
- no successor represented != no successor exists;
- current EU-level orientation != personalised/national compliance conclusion.

## 11. P1/P2 disposition

> **ADOPT_FOR_EXPERIMENT — COMPLETE THE LVD CONTENT CONTRACT, THEN RUN P3 PRESENTATION DECISION**

Why:
- the known-act job is coherent and can be completed without national/case-law expansion;
- strong official alternatives already cover most facts, so the product claim correctly narrows to integration/orientation/verification;
- the existing deployed page already covers much of the structural context;
- remaining gaps are concrete content/evidence gaps, not a need for more architecture.

### Next bounded step

P3 should compare the same frozen LVD facts in:

1. a competent concise source-linked note;
2. the current progressive-disclosure page;
3. an Overview / Legal-detail split only as a wireframe or very cheap presentation experiment.

Default null:

> **one progressively disclosed page is sufficient; a view toggle must earn itself by reducing navigation/comprehension burden without hiding qualifications.**

No second act until this first content/presentation contract reaches the later readiness gate.

## Sources inspected 2026-09-27

Official:
- Directive 2014/35/EU / EUR-Lex: https://eur-lex.europa.eu/eli/dir/2014/35/oj/eng
- current consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014L0035-20260530
- EUR-Lex summary: https://eur-lex.europa.eu/summary/EN/2403020205_2
- Commission LVD / harmonised-standards page: https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/low-voltage-lvd_en
- Directive (EU) 2024/2749: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024L2749
- OEIL procedure summary: https://oeil.secure.europarl.europa.eu/oeil/en/procedure-document-summary/pdf?id=1345845

The evidence set is sufficient for this P1/P2 decision. Additional search is not justified merely to lengthen the source list.
