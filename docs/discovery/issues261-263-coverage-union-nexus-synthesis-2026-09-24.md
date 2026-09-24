# #261/#263 coverage + Union-nexus synthesis

Date: 2026-09-24  
Operating rule: #217

## Result

# **CONTINUE — 66 cases / 22 classes**

The batch started from:

> **64 cases / 21 classes**

It used a wide-lens coverage audit to choose one under-covered causal dimension,
then tested that dimension against a strong ordinary territorial-scope baseline.

## #261 — coverage map

No case or class was added in #261.

The audit found that the corpus is already heavily covered across:

- temporal/procedural state;
- jurisdiction and Member-State participation;
- source/authority/representation;
- judicial validity/interpretation/norm conflict.

Several apparent gaps were deliberately excluded because earlier research had
already rejected Needle-specific abstractions:

- proof/evidentiary scope (#228);
- threshold/presumption state (#236);
- generic ownership/control graph scope (#240);
- notification-vs-publication timing (#232);
- generic scoped recognition/equivalence (#245).

The highest-information uncovered dimension was:

> **relational / extraterritorial applicability nexus**

The missing state was not country membership or territorial incorporation, but
the legally defined relationship that connects an external actor/conduct to the
Union.

## #263 — Union-nexus applicability

New class:

`UNION_NEXUS_APPLICABILITY`

Definition:

> EU-law applicability can attach to an actor or conduct outside the Union
> because the governing rule defines scope through a legally specified Union
> nexus, such as targeted persons/recipients, a regulated Union market or
> instrument, or output/use in the Union.

Two DERIVATION cases were added:

1. GDPR Article 3(2) — third-country controller/processor targeting or
   monitoring people in the Union;
2. Market Abuse Regulation Article 2(4) — third-country conduct concerning
   financial instruments within the Regulation's scope.

Supporting generality/boundary evidence:
- DSA: provider establishment is not determinative, but mere technical
  accessibility from the Union is insufficient;
- AI Act: third-country scope can follow Union-market placement or output used
  in the Union.

The class does not replace ordinary territorial/extraterritorial doctrine.

Its bounded representation rule is:

> actor establishment or physical location is not always a sufficient
> jurisdiction key; preserve the legally required Union nexus.

## Corpus consequence

Before batch:
- 64 cases
- 21 classes

After batch:
- **66 cases**
- **22 classes**

No jurisdiction engine, targeting detector, monitor, schema, compliance product
or runtime dependency was earned.

## Next WIP

#264 tests a different under-covered dimension:

> whether a legally effective party/person choice can change the **applicable
> law** despite forum, location, nationality or default connecting factors.

Primary candidates are Rome I Article 3 and Succession Regulation Article 22,
with mandatory-protection/default-law controls.

Substantive #264 research starts only after this batch is reconciled to
canonical main.
