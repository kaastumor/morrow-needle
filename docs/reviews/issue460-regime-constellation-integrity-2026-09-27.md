# #460 — Regime constellation compression and relation-integrity review

Date: 2026-09-27  
Disposition: **PASS_TO_NEXT_EXPERIMENT — AFTER REPAIR**

## Question

> Does the compressed medical-devices regime view preserve legal meaning, or does aggregation create false impressions even when individual labels look plausible?

The answer before repair was **not reliably**. The review found a real compression defect at child-branch level. The bounded repair was implemented in PR #461 and passed the Vercel gate.

## 1. Strong baseline retained

The European Commission medical-devices overview remains the strongest public baseline for this fixture.

At the evidence checkpoint it exposes:
- MDR and IVDR;
- predecessor transition;
- later transition amendments;
- implementing measures;
- delegated acts;
- EUDAMED-related acts;
- corrigenda;
- guidance;
- the 2025 Commission revision proposal.

The constellation earns no value merely by repeating this inventory.

Its narrower hypothesis remains:
> typed branch structure + temporal/legal-state separation + progressive drill-down + explicit bounded coverage/review semantics can make the regime easier to inspect.

Official baseline:
https://health.ec.europa.eu/medical-devices-new-regulations/overview_en

## 2. Verified relation table

This table records the relation needed by the bounded prototype, not every legal effect of each act.

| Represented item | Verified branch / role | Source basis used in review | UI implication |
| --- | --- | --- | --- |
| Directive 90/385/EEC | MDR predecessor | Commission overview / MDR repeal lineage | predecessor -> MDR |
| Directive 93/42/EEC | MDR predecessor | Commission overview / MDR repeal lineage | predecessor -> MDR |
| Directive 98/79/EC | IVDR predecessor | Commission overview / IVDR repeal lineage | predecessor -> IVDR |
| Regulation 2020/561 | MDR only | act title: amends Regulation 2017/745 re dates of application | MDR child |
| Regulation 2022/112 | IVDR only | act title: amends Regulation 2017/746 re transition | IVDR child |
| Regulation 2023/607 | MDR + IVDR | act title expressly amends both regulations | both branches |
| Regulation 2024/1860 | MDR + IVDR | act title expressly amends both regulations | both branches |
| Implementing Regulation 2021/2078 | MDR legal basis; EUDAMED system also serves IVDR | Regulation 2017/745 Article 33(8); recitals note IVDR uses EUDAMED under MDR arrangements | label MDR legal basis; cross-system context |
| Implementing Regulation 2022/1107 | IVDR | class-D IVD common specifications; IVDR Article 9(1) | IVDR child |
| Implementing Regulation 2022/2346 | MDR | Annex XVI products under MDR | MDR child |
| Implementing Regulation 2023/2713 | IVDR | EU reference laboratories under IVDR Article 100 | IVDR child |
| Implementing Regulation 2026/977 | MDR + IVDR | MDR Article 36(3) and IVDR Article 32(3) | both branches |
| Implementing Decision 2019/1396 | MDR implementing basis; expert-panel tasks include IVDR | MDR Article 106; decision Article 1 also references IVDR Article 48(6) | both-context with basis nuance |
| Implementing Decision 2025/1324 | amends 2019/1396; MDR Article 106 basis; adds/changes expert panels including IVD | official amending decision | both-context with basis nuance |
| Delegated Regulation 2023/2197 | MDR | amends MDR re UDI assignment for contact lenses | MDR child |
| Delegated Regulation 2025/788 | MDR | amends 2023/2197 application date; MDR Article 27(10)(b) basis | MDR amendment |
| Delegated Regulation 2023/502 | MDR | amends MDR re notified-body reassessment frequency | MDR child |
| Delegated Regulation 2026/1451 | MDR | amends MDR re clinical-investigation exemption list | MDR child |
| Decision 2025/2371 | MDR + IVDR operational effect | EUDAMED modules correspond to provisions in both MDR and IVDR; transition periods start from publication of functionality notice | cross-branch operational trigger |
| MDCG 2021-25 rev.1 | MDR guidance, non-binding | Commission guidance page; guidance concerns MDR legacy devices | MDR non-binding child |
| COM(2025) 1023 | proposal affecting MDR + IVDR | Commission / EUR-Lex proposal; submitted to Parliament and Council | proposal lane only |

Core official sources:
- https://health.ec.europa.eu/medical-devices-new-regulations/overview_en
- https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en
- https://eur-lex.europa.eu/eli/reg_impl/2021/2078/oj/eng
- https://eur-lex.europa.eu/eli/dec_impl/2019/1396/2025-07-28/eng
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R0788
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R1451
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202600977
- https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32025D2371
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC1023

## 3. Defect — branch ownership hidden inside shared families

### Before repair

The macro cards for:
- implementing measures;
- delegated acts;
- EUDAMED;
- guidance;

can legitimately span both core branches at family level.

But branch focus only dimmed top-level macro objects.

If a user focused MDR and expanded “Implementing measures”, an IVDR-only act such as 2022/1107 or 2023/2713 remained at full weight.

That created a false visual implication:
> shared family == every displayed child belongs to the focused branch.

### Repair

PR #461:
- assigns every represented child a branch tag;
- shows human-readable MDR / IVDR / MDR + IVDR labels;
- propagates focus into expanded children;
- keeps non-focused children visible as **sibling context** instead of hiding them.

This preserves the sponsor's desired connectedness while keeping child ownership explicit.

## 4. Defect — cross-list reuse looked like a second instrument

Implementing Regulation 2021/2078 is useful in two conceptual views:
- implementing-measures inventory;
- EUDAMED system lane.

Showing it twice without qualification can imply two instruments or distort family counts.

Repair:
- EUDAMED lane is explicitly a **cross-cutting lens**;
- repeated items are navigation cross-references;
- 2021/2078 is marked as already counted in the implementing family.

General rule:
> one legal resource may appear in more than one useful projection, but projection reuse must never imply duplicate legal resources.

## 5. Family-count audit

### Implementing measures

The Commission overview lists 17 unique implementing regulations/decisions in its implementing-measures section at the 2026-09-27 evidence checkpoint.

### Delegated acts

The same overview names 7 unique delegated/delegated-amending regulations when:
- 2025/788 is counted as the separate amending regulation it is;
- the 2022 Commission delegated-powers **report** is not counted as a delegated regulation.

Repair:
- UI now says **17 unique acts** / **7 unique acts**;
- source-check date is visible;
- counts are explicitly frozen navigation summaries;
- counts are not completeness or legal-importance claims.

## 6. Transition compression audit

The original family title “joint transition/change layer” is acceptable only because its explanatory text says **one or both** core regulations.

Child ownership now removes the remaining ambiguity:

- 2020/561 — MDR;
- 2022/112 — IVDR;
- 2023/607 — both;
- 2024/1860 — both.

Therefore:
> a family can be cross-regime even when individual members are branch-specific.

That distinction is now visible rather than inferred.

## 7. Guidance / proposal separation

### Guidance

The Commission states that MDCG guidance documents are **not legally binding** and present a common understanding of MDR/IVDR application in practice.

The represented MDCG 2021-25 rev.1 item is MDR-specific legacy-device guidance.

The dashed/non-binding lane plus textual label is therefore supported.

### Proposal

COM(2025) 1023 is a Commission proposal submitted to the European Parliament and Council.

The Commission overview expressly says it must be adopted through the ordinary legislative procedure to become binding Union law.

The prototype now says:
> proposal/procedure item, not enacted law.

No future-fixed/enacted styling is used.

## 8. Graph-spaghetti result

The first-render cap of nine macro objects survives this review.

Why:
- the default view exposes the regime shape without enumerating ~30 child acts;
- individual acts remain in native disclosure;
- branch focus keeps sibling context;
- relation meaning is readable without a legend.

The grouped Commission page remains a credible alternative.

The constellation should be narrowed to a ledger/tree if later expansion forces:
- dozens of visible nodes;
- crossing edge lines;
- a large legend;
- or hidden legal qualifications.

No evidence currently requires that narrowing.

## 9. Gap semantics result

The abstract taxonomy remains safe only if it stays evidence-bounded.

Accepted:
- COVERAGE_GAP
- EVIDENCE_GAP
- REVIEW_GAP
- STRUCTURAL_GAP_CANDIDATE

But **STRUCTURAL_GAP_CANDIDATE** is not yet instantiated as a concrete medical-device claim.

That is intentional.

No missing node is currently displayed as evidence that EU law lacks a required measure.

Successor #462 owns the question of whether useful source-backed review/gap signals can be derived at all.

## 10. Maintenance result

Family counts can stale.

Minimum current control:
- evidence-check date is shown adjacent to the count;
- count semantics are regression-tested;
- prototype remains explicitly non-live.

Do not build automated ingestion merely to keep two prototype counters fresh.

If this surface survives later value testing or becomes multi-act, count/source ownership must move out of hand-authored presentation.

## 11. Disposition

> **PASS_TO_NEXT_EXPERIMENT — AFTER REPAIR**

Why:
- compression did create a real semantic defect;
- the defect was repaired without data expansion or a graph-engine redesign;
- binding/non-binding/proposal distinctions survived;
- family counts are now explicit dated summaries;
- the first-render structure remains bounded;
- the next high-information question is not “add more nodes”, but whether typed structure can support safe review/gap signals.

Successor:
> **#462 — Typed regime review/gap signals from the medical-devices slice**

No user-value or market claim follows from this internal pass.
