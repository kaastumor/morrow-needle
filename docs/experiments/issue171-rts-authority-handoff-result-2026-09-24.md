# #171 result — technical-standard authority handoff

Date: 2026-09-24  
Issue: #171  
Disposition: **SUPPORT — NEW DERIVATION FAILURE FAMILY**

New class:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

Evidence role:

`DERIVATION / PUBLIC_EXPOSED / REGRESSION_ONLY`

No model/evaluation claim is made.

## Claim tested

An ESA "final draft RTS" may be final only within the upstream authority's
drafting stage.

Where the European Commission has formal amendment/adoption power, the final
binding legal rule may differ materially.

A legal researcher must therefore keep:

- upstream technical-authority draft status;
- downstream Commission amendment/adoption authority;
- final binding delegated act

attached to their exact document roles rather than inheriting legal effect from
the word "final".

## Chain A — investment-firm fixed overheads

### Upstream state

EBA submitted its final draft RTS on fixed-overheads requirements on
16 December 2020.

EBA's own history page and press release identify the document as a **final
draft RTS**, not the Commission's adopted binding regulation.

Official EBA sources:

- https://www.eba.europa.eu/publications-and-media/press-releases/eba-publish-final-draft-technical-standards-prudential
- https://eba.europa.eu/activities/single-rulebook/regulatory-activities/investment-firms/regulatory-technical-standards-prudential-requirements-investment-firms?version=2020

### Frozen proposition delta

The Commission's 29 November 2021 amendment letter states that the EBA draft's
existing trading-fee deduction applied only where fees were directly passed on
and charged to customers.

The Commission explained that market makers therefore could not benefit from
that deduction when acting as market makers.

It proposed an **additional deduction** for market-maker trading fees, subject
to retaining the amount corresponding to liquidation of the relevant inventory.

Official Commission/EBA-hosted letter:

- https://www.eba.europa.eu/sites/default/files/document_library/About%20Us/Missions%20and%20tasks/Correspondence%20with%20EU%20institutions/2021/Art%2010%20RTS%20FOR/1026843/Art%2010%20letter%20RTS%20FOR%20v7%20%281%29.pdf

EBA's 11 February 2022 opinion describes this as a **substantive change** to its
December 2020 final draft.

Official EBA source:

- https://eba.europa.eu/publications-and-media/press-releases/eba-issues-opinion-european-commissions-proposed-amendments-0

### Adopted state

Commission Delegated Regulation (EU) 2022/1455 includes the additional
market-maker deduction in Article 1.

It permits market makers to deduct an amount based on trading fees paid for
market-making transactions, less the defined inventory-liquidation component.

EUR-Lex:

- https://eur-lex.europa.eu/eli/reg_del/2022/1455/oj/eng

EUR-Lex identifies the act as a Commission Delegated Regulation, in force and
binding in its entirety/directly applicable.

### Realistic conclusion changed

Question:

> May an investment firm acting as a market maker deduct qualifying trading fees
> that were not directly passed on and charged to customers when calculating the
> fixed-overheads requirement?

Using the EBA final draft as if it were the binding final rule can produce:

> **No / not under the ordinary trading-fee deduction.**

The adopted Commission rule adds a dedicated market-maker deduction.

That is a material calculation/input difference.

### Chain A result

**PASS.**

The authority handoff changes a realistic legal-compliance answer.

---

## Chain B — crowdfunding credit-risk documentation

### Upstream state

EBA submitted its final draft RTS under Article 19(7) of Regulation (EU)
2020/1503 on 10 May 2022.

Official EBA source:

- https://www.eba.europa.eu/publications-and-media/press-releases/eba-publishes-final-technical-standards-crowdfunding-service

### Frozen proposition delta

EBA's 7 June 2023 Opinion records the original final-draft rule:

> creditworthiness-assessment documentation was to be retained for **at least**
> five years after repayment of the final loan instalment.

The Commission proposed a substantive amendment following EDPS comments:

- documentation may still have the minimum record-keeping rule;
- **personal data** in that documentation must be kept for **no longer than**
  five years after repayment of the final instalment.

EBA explicitly classified this as the one substantive Commission amendment and
accepted it.

Official EBA sources:

- https://eba.europa.eu/sites/default/files/document_library/Publications/Opinions/2023/1056402/EBA%20Opinion%20RTS%20Crowdfunding.pdf
- https://eba.europa.eu/publications-and-media/press-releases/eba-issues-opinion-response-european-commissions-proposed

### Adopted state

Commission Delegated Regulation (EU) 2024/358 Article 5 now contains both
boundaries:

- Article 5(2): credit-risk-assessment documentation retained for at least five
  years after final repayment;
- Article 5(3): personal data within that documentation retained for no longer
  than five years after final repayment.

EUR-Lex:

- https://eur-lex.europa.eu/eli/reg_del/2024/358/oj

EUR-Lex records the act as in force and identifies the Commission as author.

### Realistic conclusion changed

Question:

> What retention boundary applies to personal data contained in a crowdfunding
> provider's creditworthiness-assessment documentation after the final loan
> instalment is repaid?

Treating only the EBA final draft as the binding final rule can collapse the
answer into a minimum five-year record-retention requirement.

The adopted rule adds a specific maximum five-year boundary for personal data.

That is a material compliance distinction.

### Chain B result

**PASS.**

The authority handoff changes the legally relevant retention answer.

---

## Existing taxonomy first-refusal result

### 1. PARALLEL_INSTRUMENT_LIFECYCLE — does not own

That class protects separate legally distinct interim/comprehensive agreements
under a shared negotiation/deal identity.

The RTS cases are not parallel instruments carrying independent lifecycle states.

They are successive institutional artifacts in one delegated rulemaking chain,
where the downstream institution can change the text before the binding act
exists.

**REJECT AS OWNER.**

### 2. STATUS_APPLICATION_SEPARATION — does not own

No decisive error depends on confusing:

- status date;
- application date;
- entry into effect.

The wrong proposition exists even if all dates are understood correctly.

The error is assigning binding authority to the wrong institutional artifact.

**REJECT AS OWNER.**

### 3. DYNAMIC_REFERENCE_STATUS — does not own

Neither case turns on a parent rule referring to an external item whose
authoritative status later changes.

The operative text itself is modified during institutional handoff.

**REJECT AS OWNER.**

### 4. SOURCE_STATE_BACKPROJECTION — does not own

A researcher could make the error **before** the delegated regulation is adopted
by treating the ESA "final draft" as binding law.

No later source state needs to be projected backward for the failure to occur.

Backprojection can be a secondary historical error, but it is not the core
mechanism.

**REJECT AS OWNER.**

## New family earned

# `TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

Definition:

> A document may be final within an upstream technical-standard-setting
> authority's drafting stage without owning the downstream binding legal rule.
> Where a later institution has formal amendment/adoption power, authority and
> legal effect must remain attached to the exact institutional stage and adopted
> artifact rather than inherited from the upstream "final draft".

## Why this is not generic draft/final hygiene

The upstream artifact is not an informal working draft.

It is:

- produced by a legally mandated specialist authority;
- formally submitted to the Commission;
- labelled **final draft RTS**;
- substantively authoritative for the authority's completed technical position.

The trap arises because "final" is true **within one institutional stage** while
false as a statement about final binding EU law.

The downstream actor's formal amendment power is the consequential missing
dimension.

## Generality result

Both frozen chains satisfy the preregistered success conditions:

| Condition | Fixed overheads | Crowdfunding |
|---|---|---|
| ESA final draft exists | PASS | PASS |
| Commission amendment/adoption authority exercised | PASS | PASS |
| substantive operative delta | PASS | PASS |
| adopted rule differs materially | PASS | PASS |
| realistic legal answer changes/narrows | PASS | PASS |
| existing taxonomy cleanly owns mechanism | NO | NO |

Disposition:

# **SUPPORT**

## Evidence limitation

This is **DERIVATION** evidence.

The two chains were exposed before #171.

They cannot establish that a baseline/model would miss this trap when latent.

Any future evaluation claim about detection requires independently selected,
sealed fresh cases.

## Corpus consequence

Admit exactly two regression-only derivation cases under the new trap class.

No schema or product change is justified.

## Project consequence

H-20 survives as a bounded legal-information failure family.

This strengthens the corpus by one orthogonal source/authority-role mechanism.

It does not change the essential project identity:

> adversarial legal-research corpus + evaluation protocol.

The next already-earned active-discovery reserve is Run C:

> test `OFFICIAL_DERIVED_VIEW_LAG` generality.

No Cycle 3 brainstorming is required before using that reserve.
