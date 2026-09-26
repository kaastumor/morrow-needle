# Issue #362 — paired temporal-oracle test of Needle incremental value

Date: 2026-09-26  
Disposition: **CONDITIONAL_HYPOTHESIS_NOT_SUPPORTED**  
Discipline delta: **NO**  
Artifact delta: **NO**  
Reference Pack v0.2 navigation: **NOT_NEEDED**

## Question

Can a predeclared external changed-law condition separate cases where Needle adds material
incremental evaluator/oracle-maintenance value from cases where excellent ordinary
professional practice is sufficient?

The purpose was to make the recent "conditional complexity" interpretation falsifiable
rather than labelling positive cases complex after the result.

## External benchmark and frozen pair

Source:

> **ChronoLex-TW** — public temporal legal benchmark for Taiwanese bar/judicial exam
> questions.

The benchmark independently labels items:

- `Shifted` — the gold article text changed between the benchmark legal date and today;
- `Stable` — the gold article text did not change.

The benchmark also warns that its August-1 legal date is a proxy and that the gold article
is not necessarily sufficient to answer every question.

The pair was mechanically frozen before substantive source analysis.

### Shifted

- ID: `CLTW-2012-criminal-41`
- year: 2012
- law: Criminal Code
- gold article: 122
- benchmark legal date: 2012-08-01
- gold version date: 2011-11-30
- official answer: D

### Stable control

Using the precommitted same-statute rule:

- ID: `CLTW-2020-criminal-19`
- year: 2020
- law: Criminal Code
- gold article: 168
- benchmark legal date: 2020-08-01
- gold version date: 2020-01-15
- official answer: B

No row was replaced.

## Stage A — excellent ordinary evaluator-maintainer baseline

Needle corpus/classes/Reference Pack were not consulted.

### Shifted item

The actual official exam date was **2012-08-11**, rather than the benchmark's August-1
proxy.

The question combines:

- suspected bribery in breach of duty under Criminal Code Article 122(2);
- direct prosecutor arrest without prior summons;
- post-questioning bail rather than detention.

The key maintenance finding is that ChronoLex's `Shifted` label is true at the
**gold-article text** level but misleading as a proxy for oracle complexity.

Article 122 was later amended, but the answer-determinative minimum custodial threshold in
Article 122(2) used by the direct-arrest analysis remained materially stable.

The arrest and bail conclusions also depend on criminal-procedure rules rather than merely
the changed portions of Article 122.

Ordinary maintenance can therefore preserve:

- actual target/exam date;
- historical Article 122(2) penalty state;
- the procedural direct-arrest route;
- prosecutor bail authority;
- official answer D;
- a regression check pinned to the answer-determinative historical state rather than a
  generic current-vs-historical article comparison.

Stage-A disposition:

> **SHIFTED_BUT_ORACLE_RELEVANT_STATE_STABLE**

### Stable control

The actual official exam date was **2020-08-08**.

Article 168 itself is stable for the relevant period, but answer B requires more than
reading the article.

The evaluator must preserve the relationship among:

- Article 168's sworn false-statement elements;
- the witness's right to refuse testimony;
- the authority's duty to advise that right before administering the oath;
- Supreme Court treatment under which a materially defective advisement/oath procedure can
  prevent the false statement from satisfying perjury;
- the separate rule that perjury does not require the judgment itself to be affected.

Ordinary maintenance can already preserve:

- actual target date;
- stable Article 168 text;
- the procedural refusal-right/oath dependency;
- the controlling treatment;
- the no-result-required boundary;
- official answer B;
- a two-sided regression check.

Stage-A disposition:

> **STABLE_BUT_RELATIONSHIP_COMPLEX**

## Pre-Needle falsifier result

The external temporal label did **not** order the legally consequential reconstruction
burden in the predicted direction.

Observed:

- `Shifted` — textual amendment exists but is not materially answer-determinative for
  the selected question;
- `Stable` — no gold-article text shift, but a richer substantive/procedural/case-law
  relationship must be reconstructed.

Therefore:

> **changed gold-article text is not a reliable proxy for residual evaluator/oracle
> complexity.**

This result was preserved rather than replacing the pair.

## Stage B — Needle discipline / artifact test

Reference Pack v0.2 was consulted only after Stage A.

### Existing-class first refusal

No current class causally owns either benchmark-maintenance problem.

Both receive:

> **NO_EXISTING_CLASS_MATCH**

Apparent temporal/status/judicial classes concern different causal mechanisms and were not
forced onto the pair.

No new class follows.

### Shifted item

The conditional Needle discipline asks for historical source state, target date, boundary
and regression reuse where they matter.

The excellent ordinary baseline already preserved all consequential elements:

- real target date;
- historical penalty state;
- procedural dependencies;
- distinction between article-text change and oracle change;
- reusable regression logic.

Needle adds no consequential legal or evaluator distinction.

### Stable control

The excellent baseline already preserved:

- target date;
- substantive/procedural/case-law relationship;
- opposite-error boundaries;
- regression PASS/FAIL logic.

Again, Needle adds no consequential distinction.

Scientific/exposure labelling would be appropriate if the public benchmark rows were reused
as regression examples, but it does not change the maintenance outcome.

## Artifact-specific test

Everything useful for both rows can be represented in ordinary benchmark-maintenance state:

- target date;
- authoritative source/version;
- related procedural/judicial authorities;
- correction/maintenance rationale;
- expected answer/oracle;
- regression test.

Neither the frozen corpus nor Reference Pack v0.2 is operationally required.

Result:

> **ARTIFACT_DELTA = NO**

The deliberately strong Stage-A practice also absorbed the proposed method-level
discipline.

Result:

> **DISCIPLINE_DELTA = NO**

Because packet work was not earned, Reference Pack navigation was substantively unnecessary:

> **V0.2_NAVIGATION = NOT_NEEDED**

## Primary disposition

# **CONDITIONAL_HYPOTHESIS_NOT_SUPPORTED**

This is intentionally narrower than saying all prior positive evidence was wrong.

It establishes:

1. the tested external `Shifted` vs `Stable` condition does not predict the residual
   structure that previously appeared to earn Needle;
2. excellent ordinary evaluator-maintenance practice fully absorbed the useful discipline
   on both mechanically selected items;
3. the project cannot use "complexity" as an operational value selector without a stronger
   pre-result definition;
4. a full Needle artifact dependency remains unproven.

## Effect on prior evidence

Unchanged:

- #214 hard null;
- #327 generic legal-research-use null;
- #339 bounded positive packet-use observation;
- #349 postmortem-baseline null + v0.2 navigation success;
- #353 bounded conditional-use positive;
- #357 strong-postmortem-first rule;
- #359/#361 conclusion that external discipline value is credible but full-artifact value
  is unproven.

What changes:

> confidence falls in the stronger interpretation that a readily observable "legal
> complexity" condition can tell us in advance when Needle provides incremental value.

The safer current interpretation is:

> some prior cases benefited from disciplined legal failure analysis, but the incremental
> contribution is not yet separated from excellent ordinary professional practice by a
> reliable predeclared selector.

## Next decision

Do not search for a friendlier temporal pair.

The next allocation should reconsider the external-value line itself:

- either devise a genuinely discriminating test of **operational incremental value**
  independent of case selection;
- or consolidate the useful discipline into ordinary project practice and redirect
  discovery away from trying to prove a separate external Needle artifact/job.
