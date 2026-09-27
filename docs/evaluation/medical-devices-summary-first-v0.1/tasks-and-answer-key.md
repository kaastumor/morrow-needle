# #477 — Summary-first medical-devices landing page: frozen task set

Date: 2026-09-27  
Status: **FROZEN BEFORE BUILD**

Purpose:
> test whether the public entry page answers ordinary legal-orientation questions before relationship exploration.

These tasks are not an external user test yet. They freeze what the build must support.

## T1 — purpose

Prompt:

> In one or two sentences, what do the MDR/IVDR rules broadly do?

Expected boundary:
- regulate placing/making available/putting into service of medical devices / IVDs in the Union;
- include clinical investigations (MDR) / performance studies (IVDR);
- support safety/performance/market oversight;
- no claim that the page is a complete compliance guide.

Failure examples:
- answer only describes predecessor lineage;
- answer only says “medical-device law”;
- answer implies the regime is merely a database/graph.

## T2 — MDR vs IVDR

Prompt:

> You have an ordinary medical device and an in-vitro diagnostic device. Which core Regulation should you inspect first for each?

Expected:
- ordinary medical device -> MDR, Regulation (EU) 2017/745;
- IVD -> IVDR, Regulation (EU) 2017/746;
- borderline classification can require checking definitions/intended purpose.

Failure:
- presents MDR/IVDR as interchangeable;
- product-category label is treated as a final legal determination.

## T3 — importer / distributor relevance

Prompt:

> A business does not manufacture devices. It imports them from outside the EU and distributes them. Is there a reason to inspect these rules?

Expected:
- yes;
- importers and distributors are expressly regulated economic-operator roles;
- obligations differ by role;
- the page should route to the relevant provisions / official operator guidance;
- no personalised conclusion about every duty.

Failure:
- only manufacturers are described;
- being a non-manufacturer is treated as exclusion.

## T4 — laboratory / research-use boundary

Prompt:

> A product is used in a laboratory or for research. Is that label alone enough to decide whether IVDR is relevant?

Expected:
- no;
- IVDR excludes general laboratory/research-use products unless, in view of their characteristics, the manufacturer specifically intends them for in-vitro diagnostic examination;
- intended purpose therefore matters;
- individual classification is not decided by the landing page.

Failure:
- “lab use = outside IVDR”;
- “used on human specimens = automatically IVDR”.

## T5 — application dates and transition

Prompt:

> What do 26 May 2021 and 26 May 2022 mean, and why are those dates not enough to decide every legacy-device transition question?

Expected:
- MDR generally applies / replaced its predecessor directives from 26 May 2021;
- IVDR generally applies / replaced Directive 98/79/EC from 26 May 2022;
- later transition measures preserve routes/effects for some legacy devices subject to conditions;
- a device-specific transition conclusion needs more facts.

Failure:
- those dates are called the adoption or entry-into-force dates;
- every predecessor route is said to have ended on that date.

## T6 — source verification and proposal status

Prompt:

> Where should you verify a consequential statement from this page, and is COM(2025) 1023 current binding law?

Expected:
- official EUR-Lex act/current consolidated text and relevant Commission material;
- claim-adjacent source links should be available;
- COM(2025) 1023 is a Commission proposal submitted to Parliament/Council at the evidence checkpoint and is not enacted binding law;
- do not confuse Commission working consolidations of proposed changes with operative legislation.

Failure:
- source verification requires entering Needle's expert/research view;
- proposal is styled as future-fixed or current law.

## Integrity rule

The build fails if any task can only be answered by:
- opening the relationship browser first;
- reading an internal research/maintenance explanation;
- inferring from an icon or colour;
- relying on an unsourced sentence.

## Later comparison

When sponsor/external testing is appropriate, compare:
1. summary-first page;
2. current /regime-v2/;
3. strong official-source workflow.

Do not compare only against raw legislation.
