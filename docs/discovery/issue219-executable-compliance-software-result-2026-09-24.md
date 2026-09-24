# #219 result — executable compliance software as legal input

Date: 2026-09-24  
Issue: #219

## Decision

# **ADOPT_FOR_DERIVATION**

Three orthogonal EU regimes show that executable tools can be legally
consequential inputs rather than mere implementation conveniences.

### Construction products — Regulation (EU) 2024/3110

Article 15(2) requires environmental sustainability performance to be calculated
using the latest Commission software. Updates may be used voluntarily from
publication and become mandatory one year later.

Annex V requires the declaration to identify the software version used.

Source:
https://eur-lex.europa.eu/eli/reg/2024/3110/oj

### WEEE — Implementing Regulation (EU) 2017/699

The Commission WEEE calculation tool is an integral part of the methodology and
Member States shall use it for specified calculations.

Source:
https://eur-lex.europa.eu/eli/reg_impl/2017/699/oj

### Transport emissions — Regulation (EU) 2026/1030

The Commission EU calculation tool is periodically updated and use of it removes
the normal need for verification to address correctness of the calculation.
External tools require certification and are identified in supporting evidence.

Source:
https://eur-lex.europa.eu/eli/reg/2026/1030/oj

## Existing-class first refusal

`STATUS_APPLICATION_SEPARATION`, `DYNAMIC_REFERENCE_STATUS`,
`AUTHORITATIVE_METRIC_TRIGGER` and `SOURCE_STATE_BACKPROJECTION` each own
important components.

None owns the residual causal fact:

> which executable artifact/version actually performed the legally relevant
> transformation?

That question moved to #220 for a bounded derivation/admission test.

## Adjacent baseline

Computational-law literature already requires executable-version and input
provenance for reproducibility.

Needle claims no novelty over that principle.

The research value is preserving real EU legal cases where execution-artifact
identity/version is part of the legal calculation/evidence chain.
