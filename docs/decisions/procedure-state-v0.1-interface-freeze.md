# Decision — Freeze Legal / Procedural State v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #8

## Decision

Freeze the P0-H procedural-state foundation around:

- `schemas/procedure-state-event-v0.1.schema.json`
- `src/needle/procedure/resolver.py`
- `fixtures/procedure/procedure-state-adversaries-v0.1.json`
- `tests/test_procedure_state.py`

The core model is an **orthogonal state vector driven by evidence-backed events**, not one lifecycle/status enum.

Legal force and application are deliberately excluded from this subsystem and remain owned by the frozen temporal model.

## Stable dimensions

- PROCEDURE_ACTIVITY
- PROCEDURE_OUTCOME
- FORMAL_ACT_ADOPTION
- FINAL_ACT_PUBLICATION
- PARLIAMENT_POSITION
- COUNCIL_POSITION
- NEGOTIATION_STATE
- DELEGATED_SCRUTINY

Each dimension has a typed value vocabulary. Cross-dimension values and legal-effect dimensions are rejected by schema.

## Adversaries passed

### GDPR — ordinary legislative procedure
Parliament and Council positions can exist while the final act remains not formally adopted and not published. Signature/adoption and OJ publication are separate later events.

### European Private Company proposal — withdrawn terminal path
A real proposal may terminate as WITHDRAWN with no adopted act. WITHDRAWN is not equivalent to “still pending” or “not yet adopted”.

### ESRS delegated regulation
Commission adoption can coexist with:
- procedure still open;
- objection scrutiny open;
- no final OJ publication yet.

Delegated scrutiny is not modelled as fake Parliament/Council legislative readings.

### Implementing Regulation 2023/2773
A Commission implementing act can be formally adopted and later published without any invented Parliament/Council legislative position. Entry into force and retroactive application remain separate temporal assertions.

### Digital Services Act — provisional political agreement
A provisional political agreement is a negotiation state, not formal adoption. The official Council source explicitly stated that the April 2022 agreement was still subject to approval; final adoption occurred later.

## Durable invariants

1. There is no single canonical “procedure status” field.
2. Proposal/document roles, institutional positions, negotiation state, formal adoption and publication are different facts.
3. Political agreement does not equal formal adoption.
4. Formal adoption does not equal publication.
5. Publication does not equal entry into force or application.
6. WITHDRAWN / REJECTED / LAPSED are terminal outcomes, not pending states.
7. Delegated and implementing acts are not forced through ordinary legislative stages.
8. A delegated act may be adopted while scrutiny remains open.
9. Procedure family is explicit and stable across events; conflicting families fail closed.
10. Legal-effect state belongs to the temporal subsystem.

## Post-freeze rule

Extend adapters/events/fixtures for new procedure families. Reopen the core state model only if an official procedure requires a legally meaningful state dimension that cannot be represented without distortion.
