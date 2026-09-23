# Discovery — REACH confirms the dynamic-set pattern is not about standards

**Date:** 2026-09-23  
**Issue:** #77  
**Status:** second orthogonal official case pinned

## Why this case was chosen

The toy-safety wave-roller case reopened Dependency Ripple v0.1, but one case
could still have been a standards-law oddity.

The next test therefore deliberately left harmonised standards entirely.

REACH supplies a stronger adversary.

## The unchanged rule

Article 33 of Regulation (EC) No 1907/2006 imposes communication duties for an
article containing a substance that:

- meets the Article 57 criteria;
- has been identified in accordance with Article 59(1);
- is present above 0.1% weight by weight.

Nothing in Article 33 needs to be amended when a new substance is identified.

## The moving set is legally explicit

Article 59 establishes the Candidate List.

Article 59(10) requires ECHA to publish and update that list **on its website**
without delay after a decision on inclusion.

ECHA's Candidate List adds two unusually useful source facts:

1. only the Candidate List published on the ECHA website is deemed authentic;
2. companies may have immediate legal obligations following inclusion,
   expressly including obligations under Articles 7, 31 and 33.

This is therefore not merely an informational mirror of a legal set elsewhere.

The website state itself is the authoritative publication surface designated by
the legal architecture.

## Concrete transition: n-hexane

The current authentic Candidate List records:

- **n-hexane**
- EC 203-777-6
- CAS 110-54-3
- inclusion date **4 February 2026**
- decision **D(2025)7771-DC**
- reason: specific target organ toxicity after repeated exposure under
  Article 57(f).

The chemical did not acquire a new identity.

Article 33 did not acquire new wording.

The authoritative set changed membership.

For articles satisfying the remaining Article 33 conditions, the governing duty
can therefore produce a different result after that membership event.

## Same deep shape, different machinery

Toy safety:

```
unchanged Article 13
      ↓
dynamic OJ standard-reference status
      ↓
same EN 71-1 identity, narrower presumption
```

REACH:

```
unchanged Article 33
      ↓
dynamic ECHA Candidate List membership
      ↓
same n-hexane identity, newly in scope of the conditional duty
```

The shared abstraction is not “harmonised-standard publication”.

It is:

> **an unchanged legal rule predicates its effect on membership or status in an
> authoritative dynamic set whose state is controlled outside that rule's own
> text.**

## What existing Needle contracts can and cannot do

### Source Observation

This survives.

`OTHER_OFFICIAL` can preserve immutable observations of an ECHA website
artifact.

That does not by itself establish the legal meaning of the list transition.

### Source Change v0.1

This does **not** fit.

It is explicitly a Cellar change-hint contract and requires Cellar/root IDs and
Cellar refresh scopes.

Inventing Cellar identity for an ECHA Candidate List would be false.

### Mutation Candidate v0.2

The generic INSERT/DELETE/REPLACE vocabulary looks tempting, but its evidence
contract is built around authentic acts, Cellar/consolidation evidence,
deterministic diffs and lineage.

There is no honest evidence character for an authentic agency register/list
whose legally designated publication surface is an agency website.

Calling the Candidate List an `AUTHENTIC_ACT` just to make the schema validate
would collapse source kind and legal authority.

### Change Atom v0.3

This case creates a more subtle pressure.

v0.3 defines a Change Atom as a semantic claim derived from one or more
**VERIFIED textual mutations**.

The Article 33 derived effect should not require a fake textual mutation merely
because the causal event is a legally operative set-membership transition.

That does not automatically mean Change Atom itself must broaden. It may mean
dynamic-set effects need a distinct canonical causal object underneath the
analytics.

The ownership question must be solved before changing that interface.

## Architectural conclusion after two cases

The toy case's provisional phrase
`DYNAMIC_PUBLICATION_GATEWAY`
is too narrow.

The smallest concept supported by both cases is:

**AUTHORITATIVE_DYNAMIC_SET_TRANSITION**

with a dependency character such as:

**DERIVED_FROM_AUTHORITATIVE_SET_STATE**

This is still a hypothesis about the correct contract name, not a frozen schema.

What is now demonstrated is the *need* for a canonical owner of:

- the authoritative set identity;
- the legal basis that makes set membership/status operative;
- member identity;
- membership/status transition;
- authoritative publication surface;
- effective time;
- exact evidence;
- and the separation between direct set-state evidence and derived local legal
  effect.

## Deliberate non-action

No generic graph.
No agency-registry framework.
No Change Atom v0.4.
No mutation-engine widening.

Two cases are enough to reject the standards-specific interpretation. They are
not enough to justify an all-purpose dependency architecture.

The next architecture move should model **only authoritative dynamic sets** and
then attempt to compose both cases through it.
