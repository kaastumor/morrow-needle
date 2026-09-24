# #195 result — official authority-handoff generality

Date: 2026-09-24  
Issue: #195  
Disposition: **SUPPORT — GENERALISE / RENAME IN PLACE**

Canonical class:

`OFFICIAL_AUTHORITY_HANDOFF`

Evidence mode:

`CORRECTNESS_VALIDITY / FAILURE_FAMILY_GENERALITY`

No model-performance, prevalence or product-value claim is made.

## Decision

Generalise the #171 class formerly named
`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`.

One definition cleanly owns the two #171 RTS derivation cases plus fresh EMA and
REACH-restriction validation while excluding a procedure where the agency act
itself owns the tested legal effect.

The trap-class count therefore stays at 15.

## Frozen protocol and transport failure

The exact pre-registration is preserved in Issue #195.

Before candidate selection, a metadata-only search smoke test was attempted with
a unique sentinel. The search backend still returned substantive ECHA
restriction identities. That guard therefore **failed**: those identities were
recorded as contaminated and excluded rather than silently reused.

The replacement selection rule was frozen before the validation searches:
non-enumerative, first eligible official result under declared primary/fallback
queries. This supports existence/generality only, not population frequency.

## Fresh positive A — Balversa / EMA → Commission

Selected from the frozen EMA 2024 fallback as the first eligible product-specific
official EMA record.

Official sources:

- https://www.ema.europa.eu/en/medicines/human/EPAR/balversa
- https://www.ema.europa.eu/en/human-regulatory-overview/marketing-authorisation/obtaining-eu-marketing-authorisation-step-step

Observed chain:

- CHMP opinion adopted: **27 June 2024**;
- EU marketing authorisation issued: **22 August 2024**;
- frozen midpoint question date: **25 July 2024**.

EMA's centralised-procedure guidance states that CHMP issues the scientific
opinion and sends it to the European Commission; the Commission is the
authorising body and takes the legally binding marketing-authorisation decision.

Frozen materiality question:

> Has EU marketing authorisation already been granted for Balversa on
> 25 July 2024?

Answer:

> **No.** The positive CHMP opinion existed; the Commission marketing
> authorisation did not yet exist.

Promoting the upstream specialist opinion to final legal state changes the
answer.

**PASS.**

## Fresh positive B — N,N-dimethylformamide / RAC-SEAC → Commission

Selected as the first eligible fresh result from the frozen ECHA primary search.

Official sources:

- https://echa.europa.eu/registry-of-restriction-intentions/-/dislist/details/0b0236e18213ec9e
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32021R2030
- https://echa.europa.eu/de/-/echa-s-committees-conclude-on-two-restrictions-and-15-harmonised-classification-and-labelling-opinions

Observed chain:

- RAC opinion adopted: **20 September 2019**;
- SEAC opinion adopted: **5 December 2019**;
- ECHA submitted the RAC/SEAC opinions to the Commission: **1 April 2020**;
- Commission Regulation (EU) 2021/2030 adopted: **19 November 2021**;
- frozen midpoint between completed SEAC opinion and Commission adoption:
  **26 November 2020**.

The final Commission Regulation records the RAC/SEAC opinions as inputs and then
states the Commission's own assessment before amending Annex XVII.

Frozen materiality question:

> Is the proposed Annex XVII DMF restriction already the adopted binding
> restriction on 26 November 2020?

Answer:

> **No.** RAC/SEAC had completed their opinions and ECHA had submitted them, but
> the Commission had not yet adopted Regulation (EU) 2021/2030.

Promoting the completed ECHA committee stage to the binding restriction changes
the answer.

**PASS.**

## Fresh boundary control — Candidate List inclusion

Selected from the frozen 2024 control fallback:

**Bis(α,α-dimethylbenzyl) peroxide**, added to the Candidate List on
**27 June 2024**.

Official sources:

- https://echa.europa.eu/-/echa-adds-one-hazardous-chemical-to-the-candidate-list
- https://echa.europa.eu/en-GB/web/guest/candidate-list-obligations
- https://echa.europa.eu/candidate-list-table
- https://euon.echa.europa.eu/documents/10162/733088cd-8dd7-aa78-b278-ad3f5b79e942

ECHA states that legal obligations resulting from Candidate List inclusion are
effective from the date of inclusion. Its inclusion decision for this substance
takes effect on 27 June 2024.

Frozen control question:

> Can the relevant Candidate List obligations arise from ECHA inclusion itself,
> without waiting for a separate Commission adoption of the tested effect?

Answer:

> **Yes.**

So the valid rule is not:

> agency or expert output is merely advisory until the Commission acts.

The boundary follows the exact legal procedure and the actor/artifact that owns
the tested effect.

**CONTROL PASS.**

## Strongest rival

The strongest rival is ordinary domain-specific source-role reading:

> "recommendation is not decision."

That is sufficient to solve the EMA example, and a careful official-source
researcher needs no Needle-specific machinery to answer any of these cases.

But it does not cleanly explain the whole failure family:

- the #171 EBA artifacts are formal **final draft RTS**, not merely
  recommendations;
- RAC/SEAC opinions and CHMP opinions differ in doctrine and procedure;
- Candidate List inclusion shows that an agency act can itself own legal effect.

The reusable predictive question is narrower and cross-domain:

> Which institution and artifact own the **tested legal effect** at this exact
> procedural stage?

The error occurs when binding effect is inherited across that ownership boundary
because the upstream official artifact is final, complete, authoritative or
practically important within its own role.

## Generalised class

# `OFFICIAL_AUTHORITY_HANDOFF`

Definition:

> An official specialist artifact may be complete or final within its upstream
> role while a different institution owns the downstream binding decision.
> Legal effect must remain attached to the procedure's actual decision owner and
> binding act rather than inherited from upstream authority, finality or
> practical importance.

Boundary:

> The class applies only when a distinct downstream actor/act is legally
> necessary for the **tested effect**. If the upstream agency act itself creates
> that effect, there is no authority handoff for that proposition.

This remains falsifiable and does not classify every multi-stage administrative
procedure as a failure. A procedure is only in scope when the research answer
actually crosses the wrong legal-effect owner.

## Frozen success / kill criteria

| Criterion | Result |
|---|---|
| Fresh EMA chain reproduces consequential handoff | PASS |
| Fresh ECHA restriction chain reproduces consequential handoff | PASS |
| One definition fits both #171 RTS cases | PASS |
| Fresh direct-effect agency control is excluded cleanly | PASS |
| Material as-of answer changes in both positives | PASS |
| No doctrine-specific sibling class needed | PASS |
| Generalisation collapses into generic administration/recommendation hygiene | NO |

Disposition:

# **SUPPORT — GENERALISE / RENAME IN PLACE**

## Corpus consequence

Rename the existing class in `corpus/index-v0.1.json` and relabel exactly the
two #171 RTS cases.

Do **not** add Balversa or DMF merely to increase case count. Their role here is
fresh documentary validation and the result record preserves them.

Corpus remains:

- **29 cases**;
- **15 trap classes**.

## Inference limit

This experiment establishes a supported documentary generalisation under a
non-enumerative exposed sample.

It does **not** establish:

- how common the failure is;
- that a strong researcher or model will miss it;
- Method advantage;
- a need for an authority ontology, lifecycle graph or monitor;
- external/user product value.

## Next action

Run the horizon health check, reconcile canonical state, then give #200 the next
bounded decision.

Do not open Cycle 4 automatically.
