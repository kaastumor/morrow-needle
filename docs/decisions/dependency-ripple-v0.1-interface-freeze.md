# Decision — Freeze Legislative X-Ray / Dependency Ripple v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #20

## Decision

Freeze Dependency Ripple v0.1 as a **derived public-intelligence projection** over existing canonical mutation and Change Atom truth.

Canonical implementation:
- `schemas/dependency-ripple-composition-v0.1.schema.json`
- `schemas/dependency-ripple-view-v0.1.schema.json`
- `src/needle/analytics/dependency_ripple.py`
- `fixtures/analytics/dependency-ripple-first-cohort-v0.1.json`
- `fixtures/gold/dependency-ripple-first-cohort-v0.1.json`
- `tests/test_reach_dependency_ripple.py`
- `tests/test_dependency_ripple_view.py`
- `tests/test_gold_dependency_ripple.py`
- `.github/workflows/dependency-ripple-view.yml`

## Proven shape

A Dependency Ripple requires all of:

1. the local provision's canonical subtree is identical before/after;
2. no local textual mutation is emitted;
3. a different referenced provision/annex/rule has a VERIFIED upstream mutation;
4. an EVIDENCED + DERIVED Change Atom explicitly carries CROSS_REFERENCE scope;
5. the Change Atom references the selected upstream mutation;
6. public output preserves the direct-vs-derived distinction.

## First frozen cases

### Regulation 794/2004 Article 3(4)

Article 3(4) remains textually unchanged through the 2025 Article 3(3) replacement.

Its operative references to channels described in paragraph 3 therefore experience a derived dependency ripple without a paragraph-4 textual mutation.

### REACH Regulation 1907/2006 Article 67(1)

Article 67(1) remains canonically identical across the 2023 transition.

Its operative reference to Annex XVII means the VERIFIED insertion of Annex XVII entry 78 by Regulation 2023/2055 changes the referenced restriction set.

The local effect is EVIDENCED + DERIVED, not a textual mutation of Article 67(1).

## Ownership rule

Legislative X-Ray owns presentation only.

It does not own:
- mutation truth;
- local text-state truth;
- semantic Change Atoms;
- temporal state;
- dependency identity beyond what the referenced semantic evidence supports.

The persisted composition contains only references.

## Stable v0.1 guardrails

- unchanged local subtree means no local textual mutation;
- upstream mutation must be VERIFIED;
- local ripple must remain EVIDENCED + DERIVED;
- CROSS_REFERENCE scope is mandatory;
- local target must differ from upstream mutation target;
- cross-language equivalence is not assumed;
- X-Ray may not infer additional practical effects beyond the referenced Change Atom.

## Gold contract

The Gold case permanently rejects:
- manufactured local textual mutations;
- reclassification of a derived ripple as DIRECT evidence.

## Reopen rule

Reopen only when an official case cannot be represented without either:
- manufacturing local mutation truth;
- introducing a new dependency relation that existing semantic evidence cannot carry;
- or collapsing direct upstream evidence into derived local effect.


## Reopen trigger — Issue #77 (2026-09-23)

The v0.1 contract is **reopened narrowly** by the official toy-safety
harmonised-standard case captured in
`fixtures/discovery/toy-wave-roller-dynamic-standard-gateway-v0.1.json`.

Directive 2009/48/EC Article 13 is textually unchanged and does not statically
cite EN 71-1. Instead it confers a presumption of conformity through a moving
set of harmonised standards or parts whose references are published in the
Official Journal.

Implementing Decision (EU) 2025/1785 keeps the same
`EN 71-1:2014+A1:2018` identifier while restricting the presumption for
specified clauses as regards wave rollers.

Representing that relation as
`DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM` would be schema-compatible but
semantically false. The honest case requires a distinct dynamic-publication
gateway relation.

This directly satisfies the existing reopen rule: an official case requires a
new dependency relation that v0.1 cannot carry.

Disposition at this commit:
- v0.1 remains valid for its frozen cross-reference cases;
- no v0.2 schema is invented until this representational failure is preserved
  by regression;
- Issue #77 is the sole evidence-backed architecture reopen;
- public-product expansion remains stopped.


## Cross-domain confirmation — REACH Candidate List (Issue #77)

The first reopen trigger is **not standards-specific**.

REACH Article 33 conditions communication duties on substances identified under
Article 59. Article 59(10) requires ECHA to publish and update the Candidate List
on its website, and ECHA states that only that website list is authentic and that
inclusion may trigger immediate obligations including Article 33.

The n-hexane inclusion on 4 February 2026
(D(2025)7771-DC) supplies an orthogonal case:

- Article 33 is not textually amended by the inclusion;
- n-hexane identity does not change;
- authoritative Candidate List membership does change;
- the local legal duty can therefore produce a different result for articles
  meeting the remaining statutory conditions.

This shows that `DYNAMIC_PUBLICATION_GATEWAY` is too narrow.

The smallest evidenced abstraction is currently:

`AUTHORITATIVE_DYNAMIC_SET_TRANSITION`

with a derived dependency character conceptually equivalent to:

`DERIVED_FROM_AUTHORITATIVE_SET_STATE`

No v0.2 schema is frozen yet. The ownership problem must be solved before
implementation because:

- Cellar Source Change v0.1 is source-system-specific and cannot own ECHA list
  membership;
- Mutation Candidate v0.2 lacks an honest evidence character for an authentic
  agency register/list;
- Change Atom v0.3 requires a textual-mutation cause and must not be fed a fake
  mutation solely to preserve schema compatibility.

The next architecture move must model only this demonstrated dynamic-set causal
shape. A generic dependency graph remains unjustified.
