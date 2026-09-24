# #245–#252 sponsored discovery synthesis

Date: 2026-09-24  
Operating rule: #217

## Result

# **CONTINUE — 57 cases / 19 classes**

This batch started from the post-#244 compressed baseline:

> **50 cases / 18 classes**

It produced one bounded new mechanism, several cross-domain generality results,
and one clean rejection.

## #245 — REJECT scoped third-country recognition

EU-US DPF adequacy and financial-services equivalence show that recognition
scope can be organisation-, sector-, purpose-, time- or condition-specific.

No new class was admitted.

Ordinary decision-scope analysis owns the recognition boundary, while dynamic
organisation-list status remains under `DYNAMIC_REFERENCE_STATUS`.

## #247 — generalise cohorted transitional applicability

DPF exit supplies a non-product cohort case.

Removal from the DPF List ends reliance on the adequacy decision for new
transfers, while personal data received during the earlier participation cohort
continues to carry residual Principles obligations unless another lawful
protection mechanism is supplied or the data are returned/deleted.

This broadened `COHORTED_TRANSITIONAL_APPLICABILITY` from products/systems to
regulated subjects, assets and data sets whose current treatment depends on a
historical cohort event.

One DERIVATION case was added and cross-tagged with
`DYNAMIC_REFERENCE_STATUS`.

## #248 — generalise procedural silence

Article 290 TFEU and Regulation (EU) 2024/1781 show that institutional
non-objection can itself be legally causal.

`PROCEDURAL_SILENCE_LEGAL_EFFECT` was broadened from affirmative
administrative-decision absence to legally consequential absence of a decision,
objection or other required institutional act.

One delegated-act DERIVATION case was added.

## #249 — generalise judicial operative-state divergence

QS v Commission supplies an interim-relief case.

The source Commission decision remained publicly visible while the General Court
temporarily suspended part of its operation pending the main action.

`JUDICIAL_VALIDITY_TEXT_DIVERGENCE` already covered validity **or operative
legal state**, so no rename was required.

One DERIVATION case was added.

## #250 — admit Member-State option divergence

New class:

`MEMBER_STATE_OPTION_DIVERGENCE`

Definition:

> A Union act that otherwise binds or applies across the relevant Member States
> expressly delegates a bounded legal choice or parameter to national law; the
> operative result depends on whether/how the relevant Member State exercised
> that option.

Orthogonal cases:

1. GDPR Article 8 child-consent age — 16-year Union baseline, Member States may
   lower to not below 13;
2. MiCA Article 143(3) — Member States may disapply or shorten the CASP
   grandfathering period.

The MiCA case is also cross-tagged with
`COHORTED_TRANSITIONAL_APPLICABILITY`.

## #251 — authority handoff generality

September 2026 CHMP positive opinions are explicitly labelled by EMA as
**pending EC decision**.

Regulation 726/2004 Article 10 assigns the final marketing-authorisation
decision to the Commission.

This strengthens `OFFICIAL_AUTHORITY_HANDOFF` outside financial technical
standards.

ECHA Candidate List inclusion remains the negative boundary where specialist
agency action itself can trigger legal obligations.

One medicines DERIVATION case was added.

## #252 — cross-order incorporation generality

Swiss Schengen association validates `CROSS_ORDER_INCORPORATION_STATE`
outside the EEA.

EU Schengen developments are notified to Switzerland, which separately accepts
and implements them under its own procedures.

The class definition was broadened from a specifically separate
“incorporation instrument” to the linked legal order's required
**acceptance or incorporation mechanism**.

Regulation (EU) 2024/1717 and the Swiss 12 June 2026 implementation supply the
DERIVATION case.

## Corpus consequence

Before batch:

- 50 cases
- 18 classes

After batch:

- **57 cases**
- **19 classes**

One class was added.

No product, schema, monitor, ingestion system or runtime dependency was earned.

## Research-discipline result

The batch continues the #217 pattern:

- one attractive candidate was rejected;
- several existing classes were generalised instead of duplicated;
- the only new class has two orthogonal examples plus a same-act negative
  control;
- source/legal doctrine remains the owner of the law;
- Needle classes remain representation-failure labels, not claims of doctrinal
  novelty.

## Next WIP

#253 tests the exception boundary of
`JUDICIAL_INTERPRETATION_TEMPORAL_EFFECT` using an actual CJEU limitation of
temporal effects.

No new-mechanism hunt starts until that bounded question is resolved.
