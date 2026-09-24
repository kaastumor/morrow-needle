# #220 result — executable compliance artifact failure family

Date: 2026-09-24  
Issue: #220

## Decision

# **ADMIT_DERIVATION_CLASS**

Canonical class:

`EXECUTABLE_COMPLIANCE_ARTIFACT`

Definition:

> A legal calculation, declaration or verification outcome depends on a
> prescribed, privileged or certified executable tool. The artifact identity,
> version or regulatory status is legally relevant evidence, so substituting
> another/current executable can change the accepted result or verification
> consequence without a parent-text amendment.

## Positive cases

The strongest two orthogonal cases are retained as public DERIVATION/regression
cases:

1. Regulation (EU) 2024/3110 — construction-product environmental calculation
   through Commission software, with explicit version reporting and an
   update-publication -> optional-use -> mandatory-use transition.
2. Regulation (EU) 2026/1030 — transport-emissions calculation tools, where
   Commission-tool use changes verification scope and external tools have a
   certification/status/evidence lifecycle.

Supporting third case:

- Implementing Regulation (EU) 2017/699 — mandatory Commission WEEE calculation
  tool as an integral part of the methodology.

## Negative control

Regulation (EU) No 649/2012 Article 25 requires ECHA-specified software packages
for submission of information.

That software is a procedural submission/format mechanism. Its executable
identity does not own the substantive legal calculation/evidence result.

Therefore:

> software in a regulatory workflow is not enough.

## Strong baseline

Rules-as-executed / computational-law version provenance is reused as the mature
control discipline.

The class claims no conceptual novelty. It gives the corpus a bounded owner for
real legal cases where executable artifact identity/version itself is part of
the legally consequential calculation/evidence chain.

## Corpus consequence

- +1 trap class;
- +2 public DERIVATION cases;
- corpus becomes **31 cases / 16 trap classes**;
- no software archive, calculation engine, monitor, schema or product follows.
