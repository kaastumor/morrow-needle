"use strict";

const SHARED = Object.freeze({
  evidenceChecked: "2026-10-01",
  eudamedUrl: "https://health.ec.europa.eu/medical-devices-eudamed/overview_en",
  amendment2024Url: "https://eur-lex.europa.eu/eli/reg/2024/1860/oj/eng",
  eudamedDecisionUrl: "https://eur-lex.europa.eu/eli/dec/2025/2371/oj/eng"
});

const ACTS = Object.freeze({
  mdr: Object.freeze({
    slug: "mdr",
    code: "MDR",
    title: "Medical Device Regulation",
    citation: "Regulation (EU) 2017/745",
    legalStatus: "In force",
    originalSource: "https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng",
    consolidatedSource: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0745-20260719",
    consolidationDate: "2026-07-19",
    generalApplicationDate: "2021-05-26",
    purpose: "EU rules for placing on the market, making available or putting into service medical devices for human use and accessories, plus clinical investigations in the Union.",
    scope: [
      "Medical devices for human use and accessories are the core material scope.",
      "Selected Annex XVI products without an intended medical purpose enter the MDR when the Regulation's Article 1 conditions and applicable common specifications are met.",
      "In-vitro diagnostic devices belong to the IVDR branch; this page does not infer a reader's product classification."
    ],
    roles: [
      ["Manufacturer", "Article 10", "Primary design/manufacture, conformity-system, documentation and post-market responsibilities."],
      ["Authorised representative", "Article 11", "Mandated Union tasks for a manufacturer established outside the Union; the mandate is bounded."],
      ["Importer", "Article 13", "Specified checks and traceability duties before placing a third-country device on the Union market."],
      ["Distributor", "Article 14", "Due-care and specified checks when making devices available in the supply chain."]
    ],
    timeline: [
      ["ADOPTION", "2017-04-05", "Adopted", "Regulation adopted; this is not the same as its general application date."],
      ["ENTRY_INTO_FORCE", "2017-05-25", "Entered into force", "Twenty days after Official Journal publication."],
      ["GENERAL_APPLICATION", "2021-05-26", "Generally applies", "The general MDR application date; Article 123 contains provision-specific derogations."],
      ["AMENDMENT_APPLICATION", "2025-01-10", "Supply-interruption duty applies", "Regulation (EU) 2024/1860 inserted Article 10a; the relevant amendment applies from 10 January 2025."],
      ["OPERATIONAL_TRIGGER", "2026-05-28", "First four EUDAMED modules mandatory", "An operational milestone triggered under the gradual-roll-out rules; it does not mean all six modules are mandatory."],
      ["FUTURE_TRANSITION", "2027-12-31", "Selected legacy transition", "Eligible class III and certain class IIb implantable legacy devices may use the amended transition route through this date, subject to Article 120 conditions."],
      ["FUTURE_TRANSITION", "2028-12-31", "Selected legacy transition", "Other eligible class IIb, class IIa and specified class I legacy devices may use the amended transition route through this date, subject to conditions."]
    ],
    relationships: [
      ["REPLACES", "Directives 90/385/EEC and 93/42/EEC", "Replaced from the MDR regime subject to transition provisions."],
      ["AMENDED_BY", "Regulation (EU) 2023/607", "Changed selected MDR transition provisions and removed the former sell-off deadline."],
      ["AMENDED_BY", "Regulation (EU) 2024/1860", "Added supply-interruption duties and gradual EUDAMED roll-out changes; also amended IVDR."],
      ["OPERATIONAL_TRIGGER", "Decision (EU) 2025/2371", "Declared the first four represented EUDAMED systems functional, leading to mandatory use from 28 May 2026."]
    ],
    transitionSource: "https://eur-lex.europa.eu/eli/reg/2023/607/oj/eng",
    articlesUrl: "https://eur-lex.europa.eu/eli/reg/2017/745/2026-07-19/eng"
  }),
  ivdr: Object.freeze({
    slug: "ivdr",
    code: "IVDR",
    title: "In Vitro Diagnostic Medical Device Regulation",
    citation: "Regulation (EU) 2017/746",
    legalStatus: "In force",
    originalSource: "https://eur-lex.europa.eu/eli/reg/2017/746/oj/eng",
    consolidatedSource: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02017R0746-20250110",
    consolidationDate: "2025-01-10",
    generalApplicationDate: "2022-05-26",
    purpose: "EU rules for placing on the market, making available or putting into service in-vitro diagnostic medical devices for human use and accessories, plus performance studies in the Union.",
    scope: [
      "In-vitro diagnostic medical devices for human use, their accessories and performance studies are the core material scope.",
      "General laboratory-use and research-use-only products are outside Article 1 unless, in view of their characteristics, the manufacturer specifically intends them for in-vitro diagnostic examination.",
      "Where a product incorporates an MDR medical device as an integral part, Article 1 keeps the MDR/IVDR parts distinct; this page does not infer a reader's classification."
    ],
    roles: [
      ["Manufacturer", "Article 10", "Primary design/manufacture, performance-evaluation, documentation and post-market responsibilities."],
      ["Authorised representative", "Article 11", "Mandated Union tasks for a manufacturer established outside the Union; the mandate is bounded."],
      ["Importer", "Article 13", "Specified checks and traceability duties before placing a third-country IVD on the Union market."],
      ["Distributor", "Article 14", "Due-care and specified checks when making IVDs available in the supply chain."]
    ],
    timeline: [
      ["ADOPTION", "2017-04-05", "Adopted", "Regulation adopted; this is not the same as its general application date."],
      ["ENTRY_INTO_FORCE", "2017-05-25", "Entered into force", "Twenty days after Official Journal publication."],
      ["GENERAL_APPLICATION", "2022-05-26", "Generally applies", "The general IVDR application date; Article 113 contains provision-specific derogations."],
      ["AMENDMENT_APPLICATION", "2025-01-10", "2024/1860 amendments apply", "Supply-interruption duties and the amended IVDR transition framework apply from this date."],
      ["OPERATIONAL_TRIGGER", "2026-05-28", "First four EUDAMED modules mandatory", "An operational milestone; the two remaining modules were still under development at the evidence check."],
      ["FUTURE_TRANSITION", "2027-12-31", "Class D legacy transition", "Eligible legacy class D devices may use the amended route through this date, subject to Article 110 conditions."],
      ["FUTURE_TRANSITION", "2028-12-31", "Class C legacy transition", "Eligible legacy class C devices may use the amended route through this date, subject to conditions."],
      ["FUTURE_TRANSITION", "2029-12-31", "Class B / sterile A legacy transition", "Eligible class B and class A sterile legacy devices may use the amended route through this date, subject to conditions."]
    ],
    relationships: [
      ["REPLACES", "Directive 98/79/EC", "Replaced from the IVDR regime subject to transition provisions."],
      ["AMENDED_BY", "Regulation (EU) 2022/112", "Introduced an earlier staggered transition for selected legacy IVDs."],
      ["AMENDED_BY", "Regulation (EU) 2024/1860", "Further extended selected IVDR transitions and added supply-interruption/EUDAMED changes; also amended MDR."],
      ["OPERATIONAL_TRIGGER", "Decision (EU) 2025/2371", "Declared the first four represented EUDAMED systems functional, leading to mandatory use from 28 May 2026."]
    ],
    transitionSource: "https://eur-lex.europa.eu/eli/reg/2024/1860/oj/eng",
    articlesUrl: "https://eur-lex.europa.eu/eli/reg/2017/746/2025-01-10/eng"
  })
});

module.exports = {ACTS, SHARED};
