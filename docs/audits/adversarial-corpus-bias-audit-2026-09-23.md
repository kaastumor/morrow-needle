# Adversarial corpus v0.1 — coverage and bias audit

**Date:** 2026-09-23  
**Status:** INITIAL CORPUS AUDIT  
**Scope:** the 19 public cases indexed in `corpus/index-v0.1.json`.

## Why this audit exists

After Issue #88, Needle's durable identity is the adversarial corpus and its
evaluation protocol. That makes corpus bias a project-level risk.

The wrong optimisation target is "make the cases harder until the baseline
fails." That would recreate the exact post-result tuning problem #88 was built
to avoid.

The useful question is instead:

> What kinds of legal-information failure are represented, which have genuinely
> independent evaluation evidence, and where is the corpus structurally blind?

## Current composition

The v0.1 seed contains:

- **19 total public cases**;
- **13 DERIVATION cases** — cases that discovered or shaped a failure mechanism;
- **6 EVALUATION cases** — fresh sealed #88 cases later revealed;
- **0 cases eligible for fresh blind reuse**;
- **15 named legal domains**;
- **12 trap classes**.

Jurisdiction labels:

- 16 EU-only;
- 2 EU + Netherlands;
- 1 EU + Sweden.

The jurisdiction count understates language diversity in the source material,
but it accurately shows that Member-State legal implementation and national
case-law are not yet a meaningful corpus axis.

## Evaluation coverage is only half the taxonomy

Issue #88 independently evaluated six trap classes:

- source-state back-projection;
- language-scope asymmetry;
- status/application separation;
- dynamic reference status;
- private-origin legal recognition;
- sub-day temporal boundaries.

All six #88 pairs were R-pass/M-pass. Those cases are now regression-only.

Six other trap classes currently have **derivation evidence but no fresh sealed
evaluation counterpart**:

1. representation-local marker identity;
2. authoritative metric trigger;
3. authoritative finding -> spatial effect;
4. vertical spatial extent;
5. judicial validity / printed-text divergence;
6. judicial interpretation / temporal overclaim.

This is not a queue to test Needle Method again. It is a map of where the corpus
currently has only "we found this phenomenon" evidence rather than an
independently selected counterpart.

## Trap-class balance

The largest classes are:

- language-scope asymmetry — 3 cases;
- private-origin legal recognition — 3 cases.

Four classes have two cases each:

- source-state back-projection;
- dynamic reference status;
- status/application separation;
- sub-day temporal boundary.

Six classes have only one indexed derivation case each.

A one-case class is useful as a preserved adversary but weak support for
generalising the failure family.

## Domain diversity is better than source-system diversity

The 19 cases cover state aid, digital services, emissions trading, animal
health, aviation/UAS, fisheries, judicial interpretation, privacy, prudential
banking, medical devices, visas, cybersecurity and product-safety regimes.

But the underlying research history is strongly centred on EUR-Lex, Commission
material and a small number of Member-State official sources.

That creates several likely blind spots:

- national transposition and implementation of EU directives;
- national courts applying or misapplying EU-law temporal/state distinctions;
- legislative-procedure state before OJ publication;
- international agreements with signing/provisional-application/entry-into-force
  separation;
- agency registers or datasets whose version semantics differ from EUR-Lex;
- older digitised legal sources where metadata quality is materially worse.

These are discovery opportunities, not assumptions that failures exist.

## The corpus is not a difficulty benchmark

The public v0.1 corpus must not be described as "19 hard questions."

Many cases were admitted because they reveal a real failure mechanism, not
because a strong current model is likely to answer incorrectly.

#88 is direct evidence of that distinction: all six fresh adversarial cases were
solved correctly by the strong baseline.

The corpus therefore measures and preserves **failure-mode coverage**, not model
difficulty.

If a future model solves every public regression case, that is not evidence that
the corpus is worthless. It means the revealed cases are functioning as
regressions. New performance claims require new sealed cases.

## Next discovery preference

When choosing fresh research, prefer **orthogonal coverage** over greater
difficulty.

A useful next case would ideally add at least one of:

1. a source system not already dominant in the corpus;
2. a Member-State implementation layer rather than EU-level law alone;
3. a second independent instance of a one-case trap family;
4. a genuinely new failure class discovered from evidence rather than invented
   from architecture.

Do not require a baseline failure for admission.

## Current decision

Corpus v0.1 is diverse enough to be a useful seed, but not broad enough to claim
coverage of EU legal-information failure modes generally.

Its strongest immediate value is that it now makes those limits visible and
prevents us from confusing a collection of interesting fixtures with a
scientifically independent benchmark.


## Post-audit addition — Issue #91

The first discovery selected from this audit's blind-spot map produced two
independent international-agreement cases rather than a harder version of an
existing benchmark.

EU–Mercosur and EU–Mexico both implement an umbrella negotiated outcome through
a legally distinct interim trade agreement plus a comprehensive mixed
agreement. Their current lifecycle states differ, but both demonstrate that
agreement identity, provisional application, internal conclusion, entry into
force and later replacement cannot safely be collapsed into one umbrella
status.

The corpus therefore now contains:

- **21 public cases**;
- **13 trap classes**;
- a new two-case `PARALLEL_INSTRUMENT_LIFECYCLE` family;
- one newly represented source/lifecycle domain: international agreements and
  treaty entry-into-force mechanics.

Both new cases are public DERIVATION evidence and regression-only. They do not
count as fresh validation of the new class.

This is the desired discovery pattern after #88: orthogonal source/lifecycle
coverage can expand while the architecture stays still.


## Post-audit addition — Issue #93

The national-implementation blind spot produced a second orthogonal two-case
family.

The Netherlands and Sweden both have newer national official NIS2 implementing
law in force while the Commission's currently accessible country pages still
display the 7 May 2025 reasoned-opinion state. The Sweden page additionally
shows a 7 July 2025 last-update marker; the Netherlands page explicitly says
content is updated progressively as information becomes available.

This supports a new `OFFICIAL_TRACKER_UPDATE_LAG` class:

- official source origin does not imply current factual coverage;
- current URL accessibility does not imply current observation time;
- an official summary/status tracker may be superseded for a narrow current-law
  proposition by newer primary national legal publication;
- that does not make the historical tracker state false or decide Commission
  compliance/infringement assessment.

The corpus therefore now contains:

- **23 public cases**;
- **14 trap classes**;
- the first dedicated **national transposition / implementation** cases;
- direct primary legal evidence from Dutch Staatsblad and Swedish SFS in the
  same failure family.

Both cases are public DERIVATION evidence and regression-only.

This partially addresses the source-system and Member-State bias identified in
the initial v0.1 audit without requiring monitoring or ingestion architecture.
