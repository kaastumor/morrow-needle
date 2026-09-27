# #447 — Navigator P6 maintenance and correction rehearsal

Date: 2026-09-27  
Disposition: **PASS_TO_P7 — PROTOTYPE-SCALE MAINTENANCE ONLY**

## 1. Question

> If a consequential legal fact or relationship changes, how much of the Low Voltage Directive Navigator must be found, reviewed and repaired, and can stale or contradictory information survive across the page?

P6 used synthetic in-memory mutations to rehearse change. No fictional legal fact was committed to the product.

## 2. Rehearsal A — temporal/current-state correction

### Pre-repair observation

The rendered act page contained the visible date **30 May 2026** six times.

That initially looked like one repeated fact.

It is not.

The six occurrences belong to two separate legal/information concepts that currently happen to share a value:

1. **Directive (EU) 2024/2749 application date**
2. **EUR-Lex consolidation/source-version date**

Collapsing those into one generic “last updated” value would be semantically wrong.

### Actual pre-repair blast radius

The amendment-application date appeared in three user-facing places:
- At a glance;
- applicability/time context;
- lifecycle timeline.

The consolidation/source-version date appeared in three user-facing places:
- freshness block;
- current-consolidated-text fact;
- evidence metadata.

The consolidation version also appeared in versioned source identifiers/links:
- four dated LVD ELI links used by actor evidence;
- three consolidated CELEX identifier/link occurrences.

### Failure reproduced

A synthetic mutation changed only one visible amendment-application date.

The old regression suite still had another “30 May 2026” elsewhere, so a global string-presence assertion could remain green.

Therefore:

> **string presence did not protect temporal consistency.**

### Minimum repair

PR #449 introduced typed presentation fact markers:

- `lvd-2024-2749-application`
- `lvd-consolidation-version`

The two concepts remain separate even though their current values match.

Maintenance tests now verify:
- every copy within a fact ID has one machine date;
- every copy within a fact ID has one visible date;
- visible text agrees with the machine date;
- dated LVD ELI links agree with the consolidation-version fact;
- consolidated CELEX versions agree with the consolidation-version fact.

### Adversarial retest

In-memory mutation after the repair showed:

- changing only one visible application-date copy -> **detected**;
- changing one copy's visible text and machine date together -> **detected**.

The sentry therefore catches the partial-update class it was built for.

## 3. Freshness semantics rehearsal

P6 then found the same accidental-equality risk in:

- **legal view / legal as-of**
- **evidence verified**

Both are currently 27 September 2026, but they represent different questions.

PR #451 therefore added separate typed facts:

- `lvd-legal-view-date`
- `lvd-evidence-verified-date`

The legal-view date appears in two page locations and is checked for consistency.

The evidence-verification date remains independently typed even though it currently appears once.

This preserves the distinction:

> legal state described != evidence checked != source version.

No automation is allowed to merge those concepts merely because the values happen to match.

## 4. Rehearsal B — operative-dependency correction

### Pre-repair observation

The Article-12 -> Regulation 1025/2012 dependency repeated the external locator in multiple presentation layers:

- hidden/accessible path label;
- visible external-provision node;
- explanatory prose;
- source-link wording;
- broad global tests.

### Failure reproduced

A synthetic change to only the visible external-provision locator could leave the old combined locator in the hidden label while a broad global assertion still passed.

Therefore:

> **global relationship-string presence did not protect a route from internal disagreement.**

### Minimum repair

PR #449:

- removed unnecessary hidden duplication of the exact locator;
- added stable route IDs:
  - `lvd-art2-9-reg1025-definition`
  - `lvd-art12-reg1025-oj-procedure`
- scoped regression checks to the individual operative route;
- checks focal provision;
- checks human-readable relation;
- checks exact external provision;
- checks relevant-rule explanation;
- checks source-link locator.

### Adversarial retest

After repair:
- the exact combined Article 10(6)/11 locator occurs once as the route's visible external-provision label;
- there are no hidden `dependency-path` aria-label copies;
- a synthetic one-place visible locator mutation fails the scoped route expectation.

## 5. What the maintenance sentries do

They protect against:

- partial edits of repeated current dates;
- accidental conflation of distinct temporal concepts;
- source-version links lagging behind displayed consolidation state;
- one presentation layer of an operative dependency drifting from the others.

They do **not**:

- discover that EU law changed;
- decide what the new legal interpretation is;
- replace source verification;
- automatically update the page;
- turn the page into a legal database.

This is intentional.

## 6. Maintenance cost after repair

The page still contains hand-authored legal explanation.

For a genuine update, a maintainer must still:

1. inspect the new official source;
2. identify which typed claim(s) changed;
3. edit every affected user-facing location;
4. update source/version links where required;
5. update scoped tests;
6. review neighboring prose for consequential implications;
7. advance the evidence-verification date only after that review.

The important improvement is that several high-risk partial edits now fail visibly.

### Historical research documents

Documents such as #437's discovery result retain the evidence/reasoning state of that checkpoint.

They are not co-equal current legal truth and should not be silently rewritten merely because the product page later changes.

### Standard-status fixtures

The existing Candidate-B dynamic-set fixtures remain separate canonical owners for their standard/OJ states.

An act-page content correction must not mutate those fixtures unless the underlying standard-state evidence itself changed.

## 7. Remaining architecture risk

The current one-act page is still primarily hand-authored HTML.

That is acceptable for:
- one bounded prototype;
- a human test;
- a maintenance rehearsal.

It is **not yet an earned architecture for dozens or hundreds of acts**.

Before broad multi-act scale, the project will likely need a clearer claim/projection ownership strategy so that:
- source-backed claims have one maintained owner;
- multiple presentations derive from that owner;
- temporal/lineage/dependency semantics remain typed;
- rendering does not become the truth store.

P6 does **not** authorise building that system now.

A second act should be treated as evidence for what must generalise, not as permission to design a universal ontology in advance.

## 8. Evidence from the repair loop

- PR #449 exact final head passed Vercel before merge.
- Synthetic post-repair mutations demonstrated detection of the targeted drift classes.
- PR #451 exact head passed Vercel before merge.
- No hypothetical legal state was shipped.

## 9. Disposition

> **PASS_TO_P7 — PROTOTYPE-SCALE MAINTENANCE ONLY**

Why:
- P6 reproduced actual internal-consistency failure modes rather than reasoning about them abstractly;
- the most immediate high-risk temporal and dependency drift classes now have sentries;
- no broad backend or second truth store was required;
- the remaining maintenance limitations are acceptable for a one-act formative test;
- those limitations are **not** acceptable evidence of scaling readiness.

Successor:

> **#450 — Navigator P7 readiness gate**

P7 must decide whether this artifact has earned a bounded human test.

P6 grants no second-act, market, commercial or scale claim.
