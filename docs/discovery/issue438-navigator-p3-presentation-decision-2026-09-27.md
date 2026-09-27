# #438 — Navigator P3 presentation decision

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT — SINGLE PROGRESSIVE-DISCLOSURE PAGE**

## 1. Question

> For the same frozen Low Voltage Directive facts, what is the smallest presentation that lets a known-act reader orient and verify the law without hiding consequential qualifications?

Compared representations:

1. competent concise source-linked note;
2. current progressive-disclosure page pattern;
3. cheap Overview / Legal-detail split wireframe.

The legal/content inventory is frozen from #437. This is a presentation decision, not new legal research.

## 2. Frozen fact inventory used by all three representations

Every representation must preserve the same consequential content:

- Directive 2014/35/EU identity and current documentary state;
- Article 1 purpose and voltage scope;
- Annex II major exclusions;
- bounded economic-operator orientation;
- Article 114 TFEU legal basis;
- separate adoption/publication/entry-into-force/transposition/application/repeal dates;
- 73/23/EEC -> 2006/95/EC -> 2014/35/EU lineage;
- selected 765/2008, 768/2008, 1025/2012 and 2024/2749 context;
- Article 12 harmonised-standard presumption;
- Articles 13/14 as additional represented presumption routes;
- two existing LVD standard-status examples;
- legal-as-of, evidence-verified and source-version semantics;
- explicit coverage limits.

A presentation is not allowed to improve apparent simplicity by omitting a meaning-changing item.

---

## 3. Representation A — competent concise source-linked note

This is an intentionally strong baseline.

### Low Voltage Directive 2014/35/EU — concise orientation note

**What it is.**  
Directive 2014/35/EU is the EU Low Voltage Directive. It is a recast directive concerning electrical equipment designed for use within specified voltage limits. EUR-Lex currently lists the act as in force. The current documentary consolidated text used for this note is dated **30 May 2026**.

**Purpose and scope.**  
Article 1 combines two objectives: a high level of protection for people, domestic animals and property, and functioning of the internal market. The Directive applies to electrical equipment designed for **50–1,000 V AC** or **75–1,500 V DC**, subject to the exclusions in Annex II.

Major Annex II exclusions include equipment for explosive atmospheres, radiology/medical purposes, certain lift parts, electricity meters, domestic plugs/socket outlets, electric-fence controllers, radio-electrical interference, certain specialised ship/aircraft/rail equipment and specified custom-built R&D evaluation kits. An exclusion from LVD scope does not by itself identify which other legal regime applies.

**Who it regulates.**  
The Directive distinguishes economic-operator roles including manufacturers, authorised representatives, importers and distributors. Manufacturers carry the primary design/conformity-documentation duties; importers and distributors have role-specific verification, traceability, corrective and cooperation duties. This orientation does not determine which role a particular reader occupies or list every obligation.

**Key dates.**
- **26 Feb 2014 — adopted.**
- **29 Mar 2014 — published** in OJ L 96.
- **18 Apr 2014 — entered into force.**
- **19 Apr 2016 — transposition deadline** for the specified national measures.
- **20 Apr 2016 — those measures applied; Directive 2006/95/EC was repealed from the same date.**
- **9 Oct 2024 — Directive (EU) 2024/2749 adopted**, amending the LVD for internal-market-emergency procedures.
- **29 May 2026 — transposition deadline** for the 2024 amendment.
- **30 May 2026 — those measures apply** and the current EUR-Lex consolidated text reflects the amendment.

These dates are different legal events. Adoption or publication should not be read as the application date.

**Where it came from.**  
Council Directive 73/23/EEC is the earlier act in the displayed lineage. Directive 2006/95/EC codified that earlier regime. Directive 2014/35/EU expressly recast the 2006 directive and repealed it from 20 April 2016. No successor is represented in this evidence set; that is not a claim that none exists or could be proposed.

**What connects to it.**
- **Article 114 TFEU — legal basis.**
- **Regulation (EC) No 765/2008 — product-law framework context** for accreditation, market surveillance, third-country product controls and general CE-marking principles.
- **Decision No 768/2008/EC — common legislative framework** to which the predecessor regime was adapted in the recast.
- **Regulation (EU) No 1025/2012 — standardisation framework** used by the harmonised-standard mechanism.
- **Directive (EU) 2024/2749 — amends the LVD** for specified internal-market-emergency procedures.

These are not one generic kind of “influence”.

**How standards matter.**  
Article 12 provides a presumption of conformity with the Article 3 / Annex I safety objectives covered by harmonised standards or parts whose references are published in the Official Journal. The presumption is limited to the objectives actually covered and does not itself prove full product compliance. Articles 13 and 14 provide additional represented presumption routes involving published IEC provisions and, in the specified circumstances, national standards.

Two frozen examples in the current prototype show why the OJ-reference state matters:
- EN 60335-2-14:2006 — not cited in the represented state;
- EN 60335-2-60:2003 — cited on 26 Sep 2026 with withdrawal already fixed for 18 Jan 2027.

**Verification and limits.**  
Legal view: **as of 27 Sep 2026**.  
Evidence verified: **27 Sep 2026**.  
Current EUR-Lex consolidation used: **30 May 2026**.

This note is EU-level orientation. It does not determine national implementation, every related act, every judgment, every applicable product rule, every harmonised standard or a reader's individual compliance position.

### Source set

- Directive 2014/35/EU: https://eur-lex.europa.eu/eli/dir/2014/35/oj/eng
- Current consolidated text: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02014L0035-20260530
- EUR-Lex summary: https://eur-lex.europa.eu/summary/EN/2403020205_2
- Commission LVD / harmonised standards: https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/low-voltage-lvd_en
- Directive (EU) 2024/2749: https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32024L2749

### What this baseline demonstrates

A well-written note can carry almost all of the legal meaning without bespoke software.

Its weaknesses are not correctness by construction; they are interaction/inspection costs:
- dates, lineage, actor roles and legal context compete in one reading stream;
- a reader must scan prose to return to one category;
- official evidence is mostly collected at section/end rather than attached to individual visual objects;
- standard-status examples are links rather than an integrated task;
- progressive “short answer first, evidence on demand” behavior is limited.

Those are hypotheses about usability, not demonstrated user deficits.

---

## 4. Representation B — single progressive-disclosure page

### Existing pattern

The deployed #434 page already provides:

- persistent act identity/status;
- a readable “at a glance” explanation;
- facts block;
- typed lineage;
- lifecycle timeline;
- typed legal-context cards;
- Article 12 dependency chain;
- links into actual status examples;
- expandable evidence;
- visible coverage boundary.

### Content-complete wireframe using the frozen #437 facts

No new navigation mode is needed.

```text
LOW VOLTAGE DIRECTIVE
Directive 2014/35/EU · recast                         IN FORCE

Legal view: 27 Sep 2026
Evidence verified: 27 Sep 2026
EUR-Lex consolidation used: 30 May 2026

AT A GLANCE
2–4 sentences:
- purpose
- voltage scope
- current state / current amendment
- what the page can and cannot tell you

[Key scope]
50–1,000 V AC | 75–1,500 V DC
[Major exclusions ▾]
[Who the Directive regulates ▾]

LIFE OF THIS ACT
2014 adopted
2014 published
2014 entered into force
2016 transposition deadline
2016 application + predecessor repeal
2024 amending directive
2026 amendment application

WHERE IT CAME FROM
73/23/EEC
  ↓ codified as
2006/95/EC
  ↓ recast as
2014/35/EU
No successor represented in this evidence view.

WHAT SHAPES THIS ACT
Article 114 TFEU         [legal basis]
Reg 765/2008             [product-law framework]
Decision 768/2008        [common legislative framework]
Reg 1025/2012            [standardisation mechanism]
Directive 2024/2749      [amended by]

WHAT CHANGES IN PRACTICE
Economic operators:
Manufacturer | Authorised representative | Importer | Distributor
[Show role orientation ▾]

CONFORMITY ROUTES REPRESENTED HERE
Article 12 — harmonised standards / OJ references
Articles 13–14 — additional presumption routes
[Why this matters ▾]

FROZEN LVD STANDARD EXAMPLES
EN 60335-2-14:2006
EN 60335-2-60:2003

OFFICIAL EVIDENCE
[Claim-level links + exact locators ▾]

COVERAGE / CORRECTION
What was checked; what was not checked; how to report a suspected error.
```

### Why this pattern remains plausible

It has one canonical reading order while still allowing different depths:
- the occasional reader can stop after At a glance / scope / dates;
- the verifier can continue into relation types and evidence;
- meaning-changing qualifications stay adjacent to the relevant section;
- the act/date/evidence context remains visible in one page;
- the standards-status tool can remain part of the same journey.

### Main risk

The page can become too long.

Control:
- do not solve length with a second truth-bearing view;
- shorten repeated warnings;
- keep necessary legal qualifications visible;
- use disclosure for detail, not for meaning-changing conditions;
- add jump navigation only if the content length earns it.

---

## 5. Representation C — Overview / Legal-detail split wireframe

This is the strongest cheap version of the sponsor-plan two-presentation idea.

### Shared persistent header

Both modes must show:

```text
Low Voltage Directive — Directive 2014/35/EU
IN FORCE
Legal view: 27 Sep 2026
Evidence verified: 27 Sep 2026
Consolidation used: 30 May 2026

[Overview] [Legal detail]
```

### Overview

```text
WHAT IT DOES
Plain-language purpose + voltage scope

IMPORTANT EXCLUSIONS
Short list / expandable full represented list

WHO IT REGULATES
Manufacturer | Representative | Importer | Distributor
One-sentence role orientation

KEY DATES
Only the consequential timeline, but still separate:
force ≠ application ≠ repeal

WHERE IT CAME FROM
73/23/EEC → 2006/95/EC → 2014/35/EU
typed labels remain visible

KEY CONNECTIONS
Legal basis
product-law framework
standardisation mechanism
current amendment

HOW STANDARDS MATTER
Article 12 explanation
Articles 13/14 existence
standard-status examples

WHAT THIS VIEW DOES NOT COVER
visible boundary
```

### Legal detail

```text
IDENTITY / VERSION
ELI, CELEX, authentic act, consolidation status

PURPOSE / SCOPE
Article 1 + exact locator
Annex II exclusions

ECONOMIC OPERATORS
Articles 2, 6–10
role-by-role evidence

TEMPORAL DETAIL
full event list
governing article for each date

LINEAGE
typed relation + evidence source for each edge

LEGAL CONTEXT
exact relation basis / recitals / provisions

CONFORMITY MECHANISMS
Articles 12–14
scope of each represented presumption route

CURRENT AMENDMENT
Directive 2024/2749
transposition/application dates

CLAIM PROVENANCE
source / version / verification / unresolved items
```

### Required anti-divergence rule

The Overview is not allowed to own a second summary truth.

It must be generated from or directly reference the same underlying claim set as Legal detail.

Meaning-changing caveats must appear in Overview too.

### Problem exposed by the wireframe

Even without implementation, the split creates duplicated presentation obligations for:
- purpose/scope;
- exclusions;
- actor roles;
- key dates;
- lineage;
- Article 12 limitation;
- freshness;
- coverage boundary.

The legal-detail mode then repeats those facts with source precision.

This may be justified later if real readers demonstrably have different depth/navigation needs. That evidence does not exist yet.

---

## 6. Task-by-task comparison

This is an internal design comparison, not a user study.

| Reader task | Source-linked note | Progressive page | Overview / Legal detail |
| --- | --- | --- | --- |
| T1 identity/current state | Direct and compact | Strong; persistent identity + fact blocks | Strong if shared header remains persistent |
| T2 purpose/scope/exclusions | Complete but prose-dense | Strong once #437 gaps are inserted near At a glance | Overview can simplify, but creates risk of omitted exclusions |
| T3 economic actors | Compact paragraph/list | Role cards/disclosure fit naturally | Attractive split, but duplicated role summaries/evidence |
| T4 distinguish dates | Correct list, requires scanning | Timeline materially separates event meanings | Overview risks compressing dates; detail can preserve them |
| T5 lineage | Correct prose/list | Typed visual/text lane gives stronger inspection structure | Same benefit possible, but duplicate representation |
| T6 selected context | Correct but heterogeneous list | Typed cards preserve relationship differences | Overview may flatten relations; detail repeats them |
| T7 Article 12 mechanism | Correct explanation | Integrates mechanism with actual standard-status examples | Could work, but context can be lost across view switch |
| T8 verification/boundary | Source block works | Claim-adjacent evidence + global boundary is stronger structurally | Detail mode is strong; Overview risks hiding provenance/limits |

### Interpretation

The concise note is a **credible endpoint**, not a straw baseline.

The progressive page's strongest internal advantage is not that it contains more facts. It is that:
- temporal events can be inspected as temporal events;
- genealogical/context relations can remain visibly different;
- standard-status examples can stay interactive;
- evidence can be adjacent without taking over the first reading layer.

The split-view wireframe does not currently solve a demonstrated problem that progressive disclosure cannot solve.

---

## 7. Maintenance comparison

### Source-linked note

Lowest technical maintenance burden.

Legal/content risk:
- prose edits can silently make internal cross-references inconsistent;
- no structural enforcement that a date, relationship or status example is updated everywhere it is described.

Still a legitimate public-information endpoint if maintained carefully.

### Progressive page

Moderate presentation maintenance.

Advantages:
- one displayed fact path;
- no mode synchronization;
- existing tests can protect critical status/date semantics;
- content categories map to existing Needle ownership distinctions.

Risk:
- page length and repeated warnings can grow.

### Overview / Legal detail

Highest maintenance risk of the three even if both read from one data source.

Why:
- two editorial compositions;
- every meaning-changing caveat needs a placement decision twice;
- labels can drift even when underlying fact values do not;
- browser/navigation state adds another class of usability/accessibility behavior;
- update review must verify that simplification did not alter meaning in Overview.

The maintenance penalty is real before any user benefit from the split has been demonstrated.

---

## 8. Adversarial checks

### “You chose the existing design because it already exists.”

Counter:
- the source-linked note was given full credit and remains a plausible endpoint;
- the progressive page is not adopted because it is richer, but because the split view fails to solve a currently evidenced problem;
- no new production UI was built in this comparison.

### “Sponsor enthusiasm is biasing the decision.”

Counter:
- sponsor feedback is evidence that the current integrated page can produce orientation value for one real reader;
- it is not being used as proof against the note or as external validation;
- the later human comparison remains required.

### “A professional obviously wants Legal detail.”

Not established.

Professional verification may be served by:
- visible source links;
- exact locators in disclosure;
- persistent freshness/version information.

A separate mode is only justified if those mechanisms prove inadequate.

### “The page will become endlessly long.”

Real risk.

Before adding a second view, test:
- better section order;
- concise copy;
- jump links;
- disclosure for secondary evidence;
- removal of repeated caveats.

If the content-complete page still becomes unwieldy, that is new evidence that can reopen the split-view option.

---

## 9. Decision

> **ADOPT_FOR_EXPERIMENT — SINGLE PROGRESSIVE-DISCLOSURE PAGE**

Keep:
- one page;
- one reading order;
- typed sections;
- text-first semantics;
- expandable secondary evidence;
- direct links into status examples.

Do **not** implement an Overview / Legal-detail toggle now.

Retain:
- the concise source-linked note as a strong comparator for later human evaluation;
- the split-view wireframe as a parked alternative, not as backlog work.

## 10. Next bounded build

Complete the LVD content contract on the existing page:

1. add Article-1-grounded purpose;
2. add major Annex-II exclusions;
3. add bounded actor-role orientation;
4. show legal-as-of / evidence-verified / source-version distinctly;
5. mention Articles 13/14 without expanding them into subproducts;
6. add compact correction / evidence-boundary information;
7. reduce repeated warnings where the new persistent context makes them unnecessary;
8. preserve the original known-standard lookup flow.

This is a content/IA completion pass, not a feature expansion.

After that:
- run P5 semantic/browser/accessibility checks;
- then P6 maintenance rehearsal;
- no second act before the P7 readiness decision.

## 11. P3 disposition

> **ADOPT_FOR_EXPERIMENT**

Reason:
- progressive disclosure supports all frozen reader tasks without a second navigation mode;
- source-linked note remains a credible strong baseline;
- split view adds maintenance/navigation cost before differentiated user need is evidenced;
- current uncertainty is whether the completed single page works for readers, not whether another presentation mode can be invented.

No external value claim is made.
