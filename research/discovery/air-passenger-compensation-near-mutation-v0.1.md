# Discovery — the near-mutation: when a legal number survives while everything around it moves

**Date:** 2026-09-23  
**Lane:** Discovery  
**Issue:** #76  
**Status:** Bounded finding; no new architecture required

## Why I chose this detour

The previous three discoveries all asked what happens when emergency rules
**survive by changing legal form**.

This one asks the inverse question:

> What if the legal number does not change, but almost everything else does?

Regulation (EC) No 261/2004 gives us an unusually clean example.

Its Article 7 compensation schedule is the familiar:

- EUR 250;
- EUR 400;
- EUR 600.

Those nominal amounts survived more than two decades of inflation, a thirteen-year
legislative reform process, multiple institutional attempts to rewrite the
schedule, conciliation, and final adoption of a wider reform.

The result is not “nothing happened”.

It is a **near-mutation**.

## 1. Baseline: the 2004 amount schedule

Article 7(1) of Regulation 261/2004 fixed compensation at EUR 250 / 400 / 600,
using three distance categories.

Official source:

- CELEX 32004R0261

For this discovery the object under examination is deliberately narrow:
**the nominal amount component**.

The surrounding compensation regime is not assumed to be unchanged.

## 2. By 2018, the text was stable but its economic meaning had drifted

The European Court of Auditors' Special Report 30/2018 made a useful observation.

It recorded that the air-passenger compensation amounts had not been adjusted
for inflation since the Regulation came into force.

Its own inflation comparison gave theoretical equivalents of approximately:

| nominal rule | ECA 2018 inflation equivalent |
|---:|---:|
| EUR 250 | EUR 313 |
| EUR 400 | EUR 500 |
| EUR 600 | EUR 751 |

That is not a legal mutation.

Article 7 did not silently become EUR 313 / 500 / 751.

It is an **external contextual change** that alters the economic weight of an
unchanged legal number.

This is the first boundary the case tests:

```
legal state:       250 / 400 / 600 ───────────────►
economic context:  purchasing power drifts ──────►

                    no legal mutation
```

## 3. The reform procedure creates real alternative rule states

Procedure 2013/0072(COD) then becomes interesting.

The procedure began in 2013 and ultimately ran for more than thirteen years.

Intermediate institutional positions did not merely discuss wording around the
edges. They contained different compensation architectures.

### Parliament first reading — 2014

Parliament's 2014 first-reading position proposed:

- EUR 300 for journeys up to 2 500 km;
- EUR 400 for 2 500–6 000 km;
- EUR 600 for longer journeys.

This is a real legislative rule variant.

It is not a legal mutation.

### Council first reading — 2025

The Council position went in a different direction.

It proposed two compensation bands:

- EUR 300;
- EUR 500;

with compensation for delay triggered only after four or six hours depending on
distance.

Again: procedurally real, legally non-canonical.

### Parliament second reading — January 2026

Parliament rejected the Council architecture and adopted another variant:

- EUR 300;
- EUR 400;
- EUR 600;

with a three-hour delay threshold irrespective of distance.

The Council did not approve Parliament's amendments, sending the file into
conciliation.

At this point Needle could easily make a disastrous mistake if it treated the
latest institutional text as “the law changed”.

It had not.

## 4. Conciliation returns the nominal amounts to the old baseline

On 15 June 2026 the Conciliation Committee approved a joint text.

The agreement restored/maintained the familiar nominal schedule:

- EUR 250;
- EUR 400;
- EUR 600.

Parliament approved the joint text at third reading on 7 July 2026.

The Council gave final clearance on 13 July 2026.

So at the narrow component we are tracking:

```
2004 applicable rule
250 / 400 / 600
       │
       ├─ 2014 EP position:       300 / 400 / 600
       │
       ├─ 2025 Council position:  300 / 500
       │
       ├─ 2026 EP position:       300 / 400 / 600
       │
       ▼
2026 adopted compromise
250 / 400 / 600
```

The final amount component equals the starting amount component.

That equality does **not** make the intermediate history imaginary.

## 5. Nor does it mean the whole rule stayed unchanged

This is the second trap.

The 2026 reform changes and clarifies other parts of the passenger-rights
framework. The final agreement preserves a three-hour compensation trigger for
delay and introduces other procedural and substantive changes.

Therefore:

> **amount schedule unchanged != compensation rule unchanged**

A legal-information system that hashes only the EUR values would miss the
surrounding reform.

A system that says “Article 7 changed, therefore the compensation amounts
changed” would make the opposite error.

Non-change is proposition-component-specific.

## 6. Three different truths occupy the same history

This case needs three layers and no more:

### Legal rule state

What is actually adopted/applicable at the relevant legal time?

The applicable baseline amounts remain EUR 250 / 400 / 600, and the adopted 2026
reform preserves those same nominal values.

### Procedure-stage rule state

What did an institution formally propose or adopt as its position?

These can contain EUR 300 / 500 or EUR 300 / 400 / 600 without becoming the
legal rule.

### External context

What happened to the real-world significance of the rule?

Inflation eroded the purchasing power of fixed compensation.

That is important information, but it does not mutate Article 7.

## 7. Why the near-mutation matters

Ordinary legal change tracking tends to privilege positive events:

- replacement;
- insertion;
- repeal;
- new amount.

This case shows a different kind of history:

> **a rule survives a serious attempt to change it.**

That survival can itself be informative.

It tells us that:

- alternative institutional rule states existed;
- the final legislature did not adopt them;
- the nominal component returned to its old value;
- external conditions had nevertheless moved substantially.

A diff of 2004 versus the final 2026 amount schedule says:

> no change.

That answer is technically correct and historically impoverished.

Needle can do better without inventing a new legal-change type.

## 8. Architectural disposition

**SURVIVES_WITH_STRICT_LAYER_SEPARATION.**

The existing Procedure State contract already prevents Council and Parliament
positions from being laundered into adopted law.

The canonical legal mutation engine should continue to emit **no amount mutation**
where the adopted amount schedule remains EUR 250 / 400 / 600.

The Court of Auditors inflation observation remains contextual research evidence,
not a Change Atom.

No “near mutation” schema is justified.

The useful object is a discovery/audit projection over things Needle already
knows how to keep separate:

- canonical legal state;
- procedure state;
- external context.

## 9. The stronger lesson

The earlier energy cases taught us that one apparent continuity can conceal
multiple legal identities.

This case teaches the mirror image:

> **one apparent legal non-change can conceal a great deal of history.**

The most interesting answer to “what changed?” may occasionally be:

> The number didn't.  
> The world did.  
> The legislature tried.  
> And then the number survived.

## Pinned regressions

- `fixtures/discovery/air-passenger-compensation-near-mutation-v0.1.json`
- `fixtures/procedure/air-passenger-rights-2013-0072-near-mutation-v0.1.json`
- `tests/test_air_passenger_compensation_near_mutation.py`

## No follow-up queue

There are many other nominal thresholds that could be examined this way.

That is exactly why this run stops here.

The finding is the pattern, not a mandate to manufacture twenty threshold issues.
