# #207 result — registry absence vs completeness semantics

Date: 2026-09-24  
Issue: #207  
Claim type: `CORRECTNESS_VALIDITY / FAILURE_FAMILY_DISTINCTIVENESS`

## Decision

# **REJECT**

The parked Cycle-3 candidate:

> `OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM`

does not earn a Needle-specific failure family.

## Strong baseline

The wide-lens review surfaced mature adjacent-discipline machinery for exactly
this inference problem:

- closed-world versus open-world reasoning;
- local / partial closed-world semantics;
- predicate-scoped completeness;
- completeness assertions for query answering.

Representative sources:

- W3C Closed World Assumption:
  https://www.w3.org/wiki/ClosedWorldAssumption
- Darari, Razniewski & Nutt, *Bridging the Semantic Gap between RDF and SPARQL
  using Completeness Statements*:
  https://arxiv.org/abs/1408.6395
- Darari et al., *Enabling Fine-grained RDF Data Completeness Assessment*:
  https://arxiv.org/abs/1604.08377
- Razniewski et al., *Completeness, Recall, and Negation in Open-World Knowledge
  Bases: A Survey*:
  https://arxiv.org/abs/2305.05403

The baseline rule is already precise:

> absence supports a negative conclusion only when completeness is established
> for the relevant predicate/domain; otherwise non-observation remains unknown.

## Mapping the #179 derivation

### Union Register medicinal products

The Commission states that the Union Register lists all medicinal products
authorised by the Commission through the centralised procedure, while separate
national/mutual-recognition routes exist.

Source:
https://health.ec.europa.eu/medicinal-products/union-register_en

So the register can close the narrow predicate:

> Commission-authorised through the centralised procedure.

It does not close the broader predicate:

> has any EU / Member-State marketing authorisation.

That is predicate-scoped completeness.

### Safety Gate

Safety Gate is a rapid alert system for dangerous non-food products
found/notified by authorities.

Source:
https://commission.europa.eu/topics/business-and-industry/product-safety_en

Absence therefore does not close the universe:

> safe / compliant product.

That is an incomplete/open relation, not a new legal inference mechanism.

### ECHA Candidate List control

ECHA says the Candidate List published on its website is authentic and inclusion
can trigger immediate legal obligations.

Source:
https://echa.europa.eu/candidate-list-table

For the narrow predicate:

> included in the current Candidate List

the official list supplies the closure condition, subject to correct
substance/group identity resolution.

This is the hard counterexample required by #207: registry absence can
legitimately support a negative conclusion when the legal source establishes a
complete predicate.

### EUDAMED rollout

The existing voluntary→mandatory transition is a time-indexed completeness
boundary. Completeness can vary by predicate, domain and time without requiring a
separate legal inference rule.

## Residual legal work

Legal research still has to establish:

- the universe owned by the register;
- whether inclusion is constitutive, declaratory, event-based or informational;
- the relevant time;
- entity/group identity.

Those facts determine whether a completeness assertion is justified.

They do not change the underlying inference rule.

Identity ambiguity should also remain with existing identity/scope disciplines
rather than be folded into a registry class to preserve the candidate.

## Kill rule

#207 asked whether the strong baseline can express:

- when absence is valid;
- when absence is unknown;
- why the predicate boundary matters;
- the consequential #179 error.

Answer:

> **yes on all four.**

The Needle-specific family is therefore rejected before fresh validation.

## Consequence

Do not create:

- `OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM`;
- a completeness metadata schema;
- registry ontology/tooling;
- fresh registry validation merely to reconfirm the generic rule.

The #179 examples remain useful explanatory legal examples of a general
completeness mistake.

## Astra decision

Not triggered.

The normal red team resolved the structural question. Escalating merely to find a
way to save the candidate would violate the selective-reasoning rule.
