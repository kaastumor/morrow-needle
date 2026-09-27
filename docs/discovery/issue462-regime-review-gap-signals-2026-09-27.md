# #462 — Typed regime review/gap signal discovery

Date: 2026-09-27  
Disposition: **ADOPT_FOR_EXPERIMENT — REVIEW QUEUE, NOT LEGAL-GAP DETECTOR**

## 1. Question

> Can the bounded typed medical-devices regime projection generate useful review/coverage signals that point a human toward work worth checking, without presenting graph-derived absence or staleness as a legal conclusion?

Yes, but only after narrowing the concept.

The defensible first product is not:
> “Needle detects gaps in EU law.”

It is:
> **“Needle can expose source-backed coverage omissions, transition triggers and review dependencies that tell a researcher what should be checked next.”**

That distinction is binding.

## 2. Signal contract

### A. COVERAGE_GAP

Meaning:
> An authoritative or strong official baseline identifies a directly relevant act/relation that the bounded projection intentionally does not represent.

Evidence required:
1. represented focal node/relationship;
2. official source naming the omitted item and its relation;
3. proof that the omitted item is outside the current bounded projection;
4. explicit coverage boundary.

Allowed wording:
> **Not represented in this slice — official source identifies an additional amending act.**

Forbidden:
> **Missing legislation**
> **Legal gap**

Public UI:
> **Allowed**, when the omitted item materially qualifies the represented object.

Maintainer/research UI:
> **Allowed**.

### B. REVIEW_GAP

Meaning:
> A represented upstream source/state changed after a dependent claim or projection was last substantively reviewed.

Evidence required:
1. typed dependency;
2. upstream change with verified effective/source timing;
3. dependent claim's last substantive review timestamp;
4. proof that the review timestamp predates the upstream change.

Allowed wording:
> **Review needed — upstream legal state changed after this dependent claim was last checked.**

Forbidden:
> **Downstream act is outdated**
> **This rule is invalid**

Public UI:
> normally **not yet**; a public page should instead show the affected claim as awaiting review/unavailable if its correctness is uncertain.

Maintainer/research UI:
> **Primary home**.

Current fixture result:
> **NO CURRENT LIVE EXAMPLE ASSERTED.**

The macro page has one global evidence checkpoint, not a sufficiently granular historical last-reviewed timestamp for each dependency. Manufacture of a REVIEW_GAP would therefore be unjustified.

### C. TEMPORAL_REVIEW_SIGNAL

Meaning:
> A source-backed event changes or activates a legal/operational transition state across represented branches, so dependent projections should be checked against the new state.

Evidence required:
1. explicit event/decision;
2. exact affected system/provision/branch context;
3. source-backed timing;
4. identified downstream projection class that could be affected.

Allowed wording:
> **Transition trigger — check dependent EUDAMED-related state against this event.**

This is not necessarily an open defect; it can be a completed/reviewed trigger.

Public UI:
> show the underlying legal event if useful;
> do not show a scary “review gap” badge unless a current unresolved dependent claim exists.

Maintainer/research UI:
> **Allowed**.

### D. STRUCTURAL_GAP_CANDIDATE

Meaning:
> An authoritative provision appears to require a downstream legal measure and a bounded, sufficiently complete official-source search has not identified the expected child.

Minimum evidence threshold:
1. provision uses sufficiently mandatory language / legal structure to create an expected downstream measure;
2. target measure/type is identifiable;
3. official-source search scope is documented and reasonably complete for that measure;
4. no child identified;
5. no evidence that the obligation was satisfied another way, repealed, superseded or not yet due.

Allowed wording:
> **Expected downstream measure not identified in the documented evidence search.**

Forbidden:
> **EU failed to legislate**
> **legal vacuum**
> **missing law**

Public UI:
> **NO** at prototype stage.

Maintainer/research UI:
> only after the full threshold is met.

Current fixture result:
> **NULL — NO STRUCTURAL_GAP_CANDIDATE EARNED.**

Why:
- many MDR/IVDR provisions empower or require implementing/delegated measures;
- the bounded prototype does not provide exhaustive downstream coverage;
- “power to adopt” is not the same as “must adopt”;
- proving absence would require a stronger bounded completeness argument than this experiment currently has.

This null is a success condition, not a missing feature.

## 3. Concrete control 1 — omitted amendment to represented child

### Represented item

Implementing Regulation (EU) 2022/2346 is displayed in the constellation as:
> common specifications · Annex XVI products

### Official external fact

The Commission's medical-devices overview states that Implementing Regulation 2022/2346 is amended by Implementing Regulation (EU) 2023/1194.

EUR-Lex confirms that 2023/1194:
> amends Implementing Regulation 2022/2346 as regards transitional provisions for certain Annex XVI products under MDR.

Sources:
- https://health.ec.europa.eu/medical-devices-new-regulations/overview_en
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32023R1194

### Projection state

2023/1194 is intentionally outside the representative child slice.

### Signal

> **COVERAGE_GAP — represented child has an official amending act outside this slice.**

This is high-value and low-risk because:
- the relation is positively evidenced;
- the omitted node is known;
- no absence inference is required.

Suggested public wording:
> **Additional amendment not expanded here:** Implementing Regulation (EU) 2023/1194 amends this act's transitional provisions. Open official source.

This is better than silently showing 2022/2346 as if the representative node were self-contained.

## 4. Concrete control 2 — IVDR delegated-family branch coverage

### Current representative slice

The displayed delegated children are MDR-side:
- 2023/2197 / 2025/788;
- 2023/502;
- 2026/1451.

### Official external fact

The Commission overview also lists Delegated Regulation (EU) 2023/503.

EUR-Lex confirms:
> 2023/503 amends Regulation (EU) 2017/746 (IVDR) as regards the frequency of complete re-assessments of notified bodies.

It is the IVDR-side counterpart to the MDR-side 2023/502 relation.

Sources:
- https://health.ec.europa.eu/medical-devices-new-regulations/overview_en
- https://eur-lex.europa.eu/eli/reg_del/2023/503/oj/eng
- https://eur-lex.europa.eu/eli/reg_del/2023/502/oj/eng

### Signal

> **COVERAGE_GAP — delegated family is cross-regime, but the representative expanded sample currently contains no IVDR delegated child.**

Important:
this does **not** mean:
- IVDR has no other delegated acts;
- the macro family is wrong;
- the graph discovered missing legislation.

Suggested UI:
> **Representative sample:** MDR examples shown here. The official overview also contains IVDR delegated acts; this slice does not expand them.

A direct link to 2023/503 is appropriate because it is the evidenced control demonstrating that omission.

## 5. Concrete control 3 — EUDAMED transition trigger

Decision (EU) 2025/2371 confirms functionality of four EUDAMED electronic systems.

The decision expressly links those systems to provisions in both:
- Regulation 2017/745 (MDR);
- Regulation 2017/746 (IVDR).

It also states that relevant transition periods start from publication of the functionality notice.

The Commission's EUDAMED page states that the first four modules became mandatory to use from 28 May 2026.

Sources:
- https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32025D2371
- https://health.ec.europa.eu/medical-devices-eudamed/overview_en

### Signal

> **TEMPORAL_REVIEW_SIGNAL — cross-branch operational trigger.**

Correct interpretation:
- a source-backed event changes the operational/transition state of parts of the regime;
- downstream EUDAMED-dependent explanations should be checked against that event.

Incorrect interpretation:
- EUDAMED was previously legally absent;
- all MDR/IVDR obligations change on the same day;
- a graph edge alone determines applicability.

Current prototype state:
- the decision is already represented in the system lane;
- the global evidence check is after the 2026 mandatory-use transition.

Therefore this is a **represented/resolved transition signal**, not an open review defect.

## 6. REVIEW_GAP control — why no current signal is asserted

A tempting inference would be:

> “2025/2371 changed EUDAMED, therefore every older EUDAMED-related child is stale.”

That is unsupported.

To assert REVIEW_GAP, Needle would need:
- the exact dependent claim;
- its last substantive review time;
- evidence that the upstream event occurred after that review;
- a reason the upstream event could affect the claim.

The current macro page has:
- evidence check date for the projection as a whole;
- no canonical per-claim reviewed-through field for every macro relationship.

Therefore:
> **no live REVIEW_GAP badge is earned.**

If this research line survives, per-claim review state may become justified later. It is not justified merely to make the diagnostics richer.

## 7. False-positive adversaries

### FP1 — bounded sample omission

Graph:
> no IVDR child expanded in delegated family

Wrong conclusion:
> no IVDR delegated acts exist

Correct:
> representative slice omits them; 2023/503 is an official positive control.

### FP2 — enabling power

Provision:
> Commission is empowered to adopt delegated acts

Wrong conclusion:
> no child node means an expected act is missing

Correct:
> an empowerment may never require exercise; no structural-gap signal without stronger obligation evidence.

### FP3 — outdated source wording

Official overview says:
> act A amended by act B

Projection does not show B.

Wrong:
> A is invalid or stale

Correct:
> projection coverage is incomplete around A.

### FP4 — upstream event

EUDAMED functionality decision exists.

Wrong:
> every EUDAMED-related explanation written before it is now wrong

Correct:
> identify concrete dependent claims and compare last-reviewed state first.

### FP5 — source list completeness

Commission overview is strong but not automatically complete for every conceivable legal relation.

Wrong:
> absence from Commission overview proves non-existence

Correct:
> use the overview as the bounded baseline for the declared family/count task only.

## 8. Signal placement

| Signal | Public Navigator | Maintainer/research view | Rationale |
| --- | --- | --- | --- |
| COVERAGE_GAP | yes, softly and locally | yes | known omitted relation improves transparency |
| REVIEW_GAP | usually no; affected public claim should fail closed | yes | internal quality-control state |
| TEMPORAL_REVIEW_SIGNAL | show underlying event, not alarm language | yes | legal event can be useful context |
| STRUCTURAL_GAP_CANDIDATE | no | research-only after strict threshold | high false-positive/legal-implication risk |

## 9. Smallest earned demonstration

A full graph-analytics system is not earned.

A small **Research diagnostics / coverage** panel on the existing `/regime/` page is earned if it shows only:

1. **Known coverage omission**
   - 2022/2346 -> amended by 2023/1194 outside represented child slice.

2. **Branch sample omission**
   - IVDR delegated counterpart 2023/503 exists but is not expanded in the representative delegated sample.

3. **Transition trigger**
   - Decision 2025/2371 -> EUDAMED functionality / cross-branch transition context;
   - status: represented at current evidence checkpoint, not an unresolved gap.

4. **Structural gap**
   - **none asserted**;
   - explain that missing nodes cannot support this signal on incomplete coverage.

This panel should be explicitly labelled:
> **Research diagnostics — evidence/coverage signals, not findings that EU law is defective.**

It is a static demonstration over verified controls, not an automated detector.

## 10. Research implication

The promising capability is not “find holes”.

It is closer to:

> **turn a dense legal web into a review queue whose reasons are inspectable.**

That can later support questions such as:
- which represented children have known unrepresented amendments?
- which branch lacks representative coverage?
- which transition events should trigger a downstream review?
- which claims were last reviewed before an upstream change?

Only the first three are currently testable in this fixture.

## 11. Disposition

> **ADOPT_FOR_EXPERIMENT — REVIEW QUEUE, NOT LEGAL-GAP DETECTOR**

Why:
- two useful coverage signals are positively evidenced without needing completeness;
- one temporal trigger is strongly evidenced and demonstrates cross-branch propagation;
- REVIEW_GAP correctly abstains because per-claim review timestamps are insufficient;
- STRUCTURAL_GAP_CANDIDATE correctly returns a null under the current coverage model;
- the result can be demonstrated without a crawler, graph database or automatic legal conclusion.

Next bounded build:
> add the four-state static research-diagnostics panel to the existing medical-devices constellation and test whether the language keeps “coverage/review signal” distinct from “law is missing/wrong”.

Do not add more medical-device acts merely to populate the panel.
