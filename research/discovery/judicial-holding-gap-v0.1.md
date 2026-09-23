# Discovery — a judgment can change legal state while the text stays put

**Date:** 2026-09-23  
**Issue:** #83  
**Status:** direct judicial-holding ownership gap pinned

## Test-Achats: text survives, derogation does not

In **C-236/09 Test-Achats**, judgment of 1 March 2011, the Grand Chamber held
that Article 5(2) of Directive 2004/113/EC is invalid with effect from
21 December 2012.

The current 2026 consolidated Directive still prints Article 5(2).

That is not a contradiction.

It is a separation Needle must preserve:

```
TEXT_STATE
Article 5(2) wording remains present
        ≠
OPERATIVE DEROGATION STATE
Article 5(2) unavailable from 21 Dec 2012
```

Commission guidance published after the judgment states that from that date the
Article 5(1) unisex rule applies without the Article 5(2) exception.

Temporal v0.2 can therefore own a bounded functional consequence:

- dimension: DEROGATION;
- boundary: END;
- date: 2012-12-21;
- exclusive.

What Temporal does not own is the direct legal proposition that the Court
declared the provision invalid.

## Planet49: interpretation is not a judgment-date mutation

In **C-673/17 Planet49**, judgment of 1 October 2019, the Grand Chamber
interpreted Article 5(3) of Directive 2002/58 read with the data-protection
consent rules.

One operative holding is that consent is not validly constituted by a
pre-checked checkbox which the user must deselect to refuse cookie
storage/access.

That is an authoritative legal interpretation.

It is not:

- a textual amendment to Article 5(3);
- an Authoritative Finding about a real-world subject;
- evidence that Article 5(3) suddenly acquired an application start on
  1 October 2019.

The judgment date is safely a judgment/source date.

Its relationship to the interpreted rule's valid-time meaning must not be
invented as a generic prospective change boundary.

## Existing contract probe

### Change Atom v0.3 — fails as owner

Change Atom explicitly requires one or more VERIFIED textual mutations.

Neither case supplies one.

Fabricating a mutation would erase the exact distinction this run is testing.

### Authoritative Finding v0.1 — wrong semantic owner

That contract was created for direct categorical determinations about concrete
subjects:

- disease confirmed at a holding;
- detainable deficiencies found on a ship.

A Court deciding what a legal provision means or whether it is valid is not a
real-world factual finding.

Reusing the contract because both involve an 'official determination' would
collapse law into fact.

### Temporal v0.2 — partial and healthy

Temporal can own an explicitly evidenced consequence such as the Test-Achats
derogation end.

It should **not** own the holding itself.

Planet49 is the stronger guardrail: a holding may have no safely asserted new
valid-time boundary at all.

### Source Observation — artifact only

Judgment bytes and identifiers can be observed like other official sources.

The binding proposition decided by the Court still needs semantic ownership.

## Missing layer

The smallest common object supported by both cases is:

**JUDICIAL_HOLDING**

It should own:

- court/case identity;
- judgment date;
- holding type;
- target legal provision(s);
- bounded holding proposition;
- direct official judgment evidence;
- optional references to separate temporal consequences.

It should not own:

- textual mutation;
- generic case-law citation graphs;
- national follow-on proceedings;
- temporal effects not stated or otherwise evidenced;
- factual findings about regulated entities.

No schema is added in this failure commit.
