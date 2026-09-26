# Issue #395 — official EU legal-information representation sufficiency

Date: 2026-09-26  
Mode: **DISCOVER — OFFICIAL EU LEGAL-INFORMATION REPRESENTATION SUFFICIENCY**

## Result

# **OFFICIAL_STACK_PARTIAL_WITH_EXTERNAL_STATE_OWNERS**

The strongest current official EU information stack is materially more capable than Needle's earlier framing assumed.

The bounded audit finds:

- **0/7 MODEL_GAP_CONFIRMED**
- **3/7 OFFICIAL_MODEL_LINKED_OWNER**
- **4/7 LEGAL_INFERENCE_REQUIRED**
- **0/7 OFFICIAL_MODEL_DIRECT**
- **0/7 INDETERMINATE**

The seven #377 residuals therefore do not support a claim that the EU lacks a sufficiently expressive legal-information model and needs a separate Needle ontology.

What survives is narrower:

> **operative legal state is often distributed across legal-resource metadata, interpreted rule structure and domain-specific authoritative state owners; the final answer can still require cross-owner legal composition/inference.**

That is a research/evidence problem, not an established official-model gap.

---

## 1. Stronger official baseline discovered before classification

The original #395 issue named ELI v1.5, ELI-Impact, Cellar / Common Data Model, EUR-Lex metadata and national-transposition metadata.

Before classifying any residual, the audit found a material current incumbent omitted from that list:

> **LOMO 1.0 — Legal Obligation Metadata Ontology**

The correction was frozen in Issue #395 before scoring.

### LOMO matters

LOMO 1.0 was released 10 July 2026 and is maintained as a project of the European Institutions.

Its published contract models interpreted legal rules, prescriptive and constitutive rules, obligation / permission / prohibition / right, conditional requirements, specific agents and agent types, actions and action results, temporal specifications and triggers, rule-to-rule specification, references from legal rules to datasets/standards/software/services, and links from action results to concrete datasets.

LOMO explicitly distinguishes the legal interpretation of a rule from its literal textual expression and links interpreted rules back to ELI legal-source works.

This is highly relevant to Needle's historical concern that current text alone does not equal operative law.

LOMO therefore counts as strong anti-Needle incumbent evidence, not merely theoretical OWL extensibility.

Official documentation:
- https://drpm.pages.code.europa.eu/lomo/latest/
- https://op.europa.eu/en/web/eu-vocabularies/ontologies

---

## 2. What the broader official stack already owns

### ELI

ELI is a common data model for exchanging legislation metadata.

Current official diagrams expose, among other things: in-force state, entry-into-force and applicability dates, relevance, change/consolidation/commencement/repeal/correction/amendment relations, application and transposition relations, and implementation relations.

So the correct baseline is not 'documents plus dates'. It already contains a substantial legal-resource/effect graph.

Official source:
https://op.europa.eu/documents/3938058/11669184/eli-diagrams.pdf

### ELI-Impact

ELI-Impact extends ELI for impact analysis, text modifications, changes to consolidated versions, and impacts originating from sources such as court decisions.

This materially overlaps Needle's historical change/corrigendum/judicial-impact concerns.

Official overview:
https://op.europa.eu/en/web/eu-vocabularies/eli

### Cellar / CDM

Cellar is the Publications Office semantic repository underlying services including EUR-Lex. The Common Data Model describes official EU documents, legislative decision-making, related publications, agents, procedures/events and relationships among resources. Cellar metadata is available through Linked Open Data, SPARQL and REST services.

Official sources:
- https://op.europa.eu/en/web/cellar/cellar-data
- https://op.europa.eu/en/web/cellar/cellar-data/metadata
- https://op.europa.eu/en/web/cellar/cellar-data/metadata/knowledge-graph

### National transposition

EUR-Lex exposes national transposition measures, but its own contract states that Member States are responsible for submitted information and that the information does not prejudge Commission verification of completeness and correctness.

So notification metadata is not the same thing as verified operative transposition truth.

---

## 3. Frozen seven-residual mapping

### R1 — CBAM dynamic authoritative certificate price

#377 residual: an unchanged legal rule uses a periodically published authoritative value that changes the operative calculation.

Current official owner: Regulation (EU) 2023/956 and implementing methodology plus the Commission CBAM certificate-price publication. The Commission publishes quarterly prices in 2026 and weekly prices from 2027.

LOMO can represent the legal rule, temporal trigger/effective period, a reference to an external dataset/resource, and an action result manifested in a dataset. The decisive numeric value is not legislation metadata in ELI.

Classification: **OFFICIAL_MODEL_LINKED_OWNER**

The model can describe the rule/resource relationship; the current value lives in a specialised authoritative owner.

Official source:
https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en

### R2 — CER Member-State critical-entity identification

#377 residual: a concrete entity becomes subject to the CER framework because the Member State identifies it as critical.

The Commission describes the Directive as requiring Member States to identify critical entities based on national risk assessments.

LOMO can model the identification rule, Member State/entity agents, the identification action/result and temporal conditions. But the actual entity-identification state is owned by the Member State process, not by ELI publication metadata.

Classification: **OFFICIAL_MODEL_LINKED_OWNER**

This is a distributed-state owner, not a confirmed ontology gap.

Official source:
https://home-affairs.ec.europa.eu/policies/internal-security/counter-terrorism-and-radicalisation/protection/critical-infrastructure-resilience-eu-level_en

### R3 — CSRD permitted Member-State exemption / divergence

#377 residual: Union law permits a bounded national option, so the operative result can differ by Member State for the same cohort/time window.

ELI and EUR-Lex can represent/link EU amending law, national transposition measures and effect/application dates. LOMO can represent permission, conditions, Member State as relevant agent and temporal window.

But determining whether a particular national legal order exercised the option, and whether a concrete undertaking falls within that national exemption, requires reading/interpreting national law and facts.

Classification: **LEGAL_INFERENCE_REQUIRED**

The official stack provides source/relationship primitives; the final applicability state is not simply metadata lookup.

### R4 — MDR transition eligibility

#377 residual: current marketability can depend on historic device class/certificate state and transition actions/conditions.

The official ecosystem now includes EUDAMED. From 28 May 2026 its first four modules became mandatory, including actor registration, device registration, notified bodies and certificates, and market surveillance. The certificate module records status including issued, amended/supplemented, suspended, reinstated, withdrawn, refused and other restrictions.

However transition eligibility can also depend on historic classification, significant-change rules, QMS state, timely application, notified-body agreement and other transition predicates. Those must be composed with the legal rule.

Classification: **LEGAL_INFERENCE_REQUIRED**

The data-owner problem is substantially addressed by EUDAMED; the legal eligibility result still requires rule/fact composition.

Official sources:
- https://health.ec.europa.eu/medical-devices-eudamed/overview_en
- https://health.ec.europa.eu/medical-devices-eudamed/notified-bodies-and-certificates-module_en

### R5 — IVDR transition eligibility

The same EUDAMED architecture applies to IVDR devices and certificates. The database provides major concrete state owners, but transition eligibility depends on class/cohort and legally specified process conditions.

Classification: **LEGAL_INFERENCE_REQUIRED**

Again: not a missing official state system; a cross-owner legal inference problem.

### R6 — Construction Products Regulation product-family migration

#377 residual: CPR-2011 and CPR-2024 coexist; product families migrate individually when the relevant new harmonised technical specification reaches its legal boundary.

The Commission explicitly publishes the transition rule and harmonised-technical-specification ecosystem. The official environment can separately own old/new Regulations, implementing acts, standard references/citations, product-family information and effective dates. LOMO can reference external standards and model temporal/conditional rules.

But the practical proposition 'this product family is now under CPR-2024 rather than CPR-2011' is derived by combining the cited specification, its legal status/date and the product family.

Classification: **LEGAL_INFERENCE_REQUIRED**

Official sources:
- https://single-market-economy.ec.europa.eu/sectors/construction/construction-products-regulation-cpr/cpr-2024-revision_en
- https://single-market-economy.ec.europa.eu/sectors/construction/construction-products-regulation-cpr/harmonised-standards_en

### R7 — Gas Appliances / EN 497:2022 citation status

#377 residual: the private standard exists independently, but EU legal recognition/presumption depends on Commission/OJ citation state.

The Commission has a dedicated formal-objections surface linking Commission Implementing Decision, relevant EU legislation, affected EN reference and decision date. LOMO can explicitly reference standards, while ELI/CDM can represent the Commission legal decision itself and its legal-resource state.

Classification: **OFFICIAL_MODEL_LINKED_OWNER**

No missing generic official ontology is needed to say that a separate standards-status owner controls the outcome.

Official source:
https://single-market-economy.ec.europa.eu/single-market/goods/european-standards/harmonised-standards/formal-objections_en

---

## 4. Result table

| #377 residual | Classification |
| --- | --- |
| CBAM dynamic price/input | **OFFICIAL_MODEL_LINKED_OWNER** |
| CER critical-entity identification | **OFFICIAL_MODEL_LINKED_OWNER** |
| CSRD national option/exemption | **LEGAL_INFERENCE_REQUIRED** |
| MDR transition eligibility | **LEGAL_INFERENCE_REQUIRED** |
| IVDR transition eligibility | **LEGAL_INFERENCE_REQUIRED** |
| CPR product-family migration | **LEGAL_INFERENCE_REQUIRED** |
| Gas Appliances / EN 497 citation state | **OFFICIAL_MODEL_LINKED_OWNER** |

Totals: **3 linked-owner, 4 legal-inference, 0 direct, 0 confirmed model gap, 0 indeterminate.**

---

## 5. Strongest red team

### Objection: LOMO can model almost anything, so this proves nothing

Partly correct. The audit does not treat generic OWL extensibility as evidence. LOMO receives weight because its current stable public contract specifically defines interpreted legal rules, legal agents, actions/results, conditions, temporal triggers, external digital resources/standards and dataset manifestation.

However, the audit does not claim that EUR-Lex is fully populated with LOMO instances for all seven cases. Representational sufficiency and population/coverage are different.

### Objection: if a human still has to join several sources, Needle remains unique

Not established. Cross-source legal inference is ordinary legal work unless Needle demonstrates a recurring failure, material reconstruction burden, product/system omission or relative workflow advantage. #214/#327 block casual promotion from 'structure exists' to 'Needle helps find it'.

### Objection: external owners mean the official stack is insufficient

Too strong. A legal-information model should not automatically duplicate EUDAMED certificate state, Member-State security designation records, dynamic CBAM price publication or private technical standards. A clean semantic link plus a specialised authoritative owner can be the correct architecture.

Needle's prior implicit preference for one integrated state model must therefore not be treated as the baseline.

### Objection: the actual cross-owner contract may still be poor

Yes. That is now an external/product/workflow question. Public specifications can show expressive capacity and owner boundaries, but they cannot establish whether users can query the composed state easily, whether commercial products do it correctly, how much qualified work composition takes or how often missing joins cause errors.

Those are the external gates preserved by #392/#394.

---

## 6. What #395 changes about Needle

Before, a plausible reading was that Needle preserves legal-state distinctions ordinary official legal-information models do not represent.

After this audit, the stronger reading is:

> **official EU information infrastructure already contains substantial legal-resource, impact, obligation, agent, action, temporal and external-resource semantics; domain state is often intentionally owned by specialised registries/systems, while operative legal conclusions still require cross-owner composition and legal inference.**

That is a substantial narrowing.

Needle may still be useful as adversarial failure memory, a regression reference, an evaluation-discipline source and a catalogue of dangerous cross-owner inference boundaries.

It has not demonstrated that a new integrated EU legal-state ontology is needed.

---

## 7. EU exhaustion rerun

After #395, the remaining EU-specific uncertainty is no longer a public specification gap.

Publicly tested to current boundary:
- legal-state existence/boundary;
- generic implementation prevalence;
- matter-specific dispute prevalence;
- official EU information-model sufficiency;
- core legal-resource/change/effect representation;
- major external-owner patterns.

External evidence required:
- actual regulatory-intelligence product behavior;
- real practitioner reconstruction burden;
- real production failure/incident prevalence;
- maintained oracle/evaluation estate;
- qualified adjudication;
- buyer/customer value.

Therefore the #394 matrix changes from **EU_PUBLIC_RESEARCH_NOT_EXHAUSTED** to:

# **EU_ONLY_EXTERNAL_GATES_REMAIN**

This does not mean EU research is permanently finished. It means no further internally selected public EU-source experiment currently has enough discriminating information value to justify itself. A genuinely new public EU model/dataset/incident can reopen a bounded question.

---

## Final disposition

# **OFFICIAL_STACK_PARTIAL_WITH_EXTERNAL_STATE_OWNERS**

and, for the broader EU exhaustion programme:

# **EU_ONLY_EXTERNAL_GATES_REMAIN**

No new schema, ontology, corpus class, Reference Pack release, product or commercial claim is earned.
