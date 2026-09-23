# Morrow // Needle — Project charter

Status: **CANONICAL PROJECT NORTH STAR**

## Purpose

Needle exists to make consequential EU legal change inspectable without turning
source activity, model inference, legal interpretation, or uncertainty into
false certainty.

It should help a non-specialist answer:

- what changed;
- compared with what;
- why the change is visible now;
- when it matters legally;
- who or what is affected when evidence actually supports that claim;
- what official evidence supports the answer;
- what remains unknown.

Thread answers the complementary historical question: how did this rule become
what it is today?

## Current central question

Issue #49 falsified the assumption that Needle's current live-change feed
provides repeated material understanding advantage over a strong combination of
EUR-Lex, mature change tooling, direct official sources and a capable LLM.

The project is therefore **redirected from a presumed general legal-news product
toward legal-change audit and rule-history reconstruction**.

The remaining high-value question is:

> Does Needle's evidence-linked Thread / audit discipline make a complex rule
> history materially easier to reconstruct correctly than the strong simpler
> baseline?

Issue #59 is the active gate. It tests the already-frozen Article 3 Thread; it
does not authorize new architecture.

## North star

> A person can understand a legally meaningful change, non-change, or
> uncertainty state quickly, inspect the official evidence, and distinguish
> source activity, textual mutation, legal effect, interpretation, and unknowns
> without needing to understand Needle's internal ontology.

The north star is user/research value, not number of sources, schemas, commits,
analytical primitives, or processed documents.

## Strong simpler baseline

Needle must justify itself against the strongest practical combination of:

1. EUR-Lex / OEIL alerts and document relationships;
2. a mature legal version-comparison / regulatory-monitoring product;
3. direct reading of the official source;
4. ordinary search plus a capable LLM asked to summarize the change.

A feature does not earn permanent architecture merely because Needle can build
it. It must make a meaningful class of questions more accurate, more
inspectable, more temporally correct, or more usefully uncertain than this
simpler baseline.

emendrix is currently the strongest direct architectural adversary for the core
EU change-monitoring loop. Needle must not claim novelty for monitoring,
structural diffing, corroboration, grounded explanation, or preservation of
source disagreement alone.

## Success condition

The project succeeds if repeated real cases demonstrate that its evidence and
legal-state model reveals useful distinctions that the simpler baseline
regularly obscures, while keeping those distinctions understandable and
traceable.

Examples may include, if they continue to survive adversarial review:

- source update versus legal mutation;
- publication versus entry into force versus application;
- context-dependent applicability;
- language-scoped corrigenda;
- rule/proposition continuity versus provision identity;
- indirect dependency effects without local text change;
- positive non-impact and abstention.

These examples are hypotheses, not a guaranteed roadmap.

## Failure / redirect condition

The project should simplify, redirect, or stop if the extra machinery repeatedly
fails to improve decisions or understanding over the simpler baseline, or if its
maintenance and explanation cost exceeds the value of the distinctions it adds.

Failure of a novelty claim is evidence, not a reason to invent a narrower claim.

## Invariants

The Morrow Constitution in `docs/foundation-v0.1.md` remains binding unless
explicitly superseded by evidence-backed decision.

Especially:

- official evidence outranks models;
- evidence classes remain distinct;
- legal text, legal effect, procedure, source state and interpretation do not
  collapse into one status;
- uncertainty and abstention survive to public output;
- public views are derived projections, not competing truth stores;
- canonical claims remain traceable to official evidence;
- new complexity must be earned by a demonstrated failure of a simpler design.

## Explicit non-goals for the current horizon

- broad jurisdiction expansion;
- opaque importance/risk scoring;
- personalized recommendations;
- replacing lawyers or issuing legal advice;
- predicting political or judicial outcomes;
- a general-purpose legal knowledge graph;
- infrastructure for hypothetical future scale;
- custom model training;
- a polished product shell over hand-selected cases.

## Current horizon

Complete Issue #59: adversarially compare the existing Article 3 Thread and its
audit distinctions against EUR-Lex, emendrix, direct official sources, ordinary
search and a capable LLM.

No new schema, analytic primitive, product shell or infrastructure is authorized
during this gate.

At completion choose **continue / simplify / stop public-product expansion**.
If Thread does not show recurring material advantage, retain Needle as a
research/audit engine and regression corpus rather than inventing a new public
product thesis.
