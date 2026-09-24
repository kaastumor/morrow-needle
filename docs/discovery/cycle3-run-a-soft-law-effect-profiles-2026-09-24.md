# Cycle 3 Run 3A — official soft-law effect profiles

Issue: #178  
Parent: #177  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven anchors

- #135 judicial-document-role confusion;
- #171 `TECHNICAL_STANDARD_AUTHORITY_HANDOFF`;
- corpus source-role / authority discipline.

The search question was not:

> Is guidance legally binding?

That binary is itself too coarse.

The stronger question is:

> Do different official guidance/Q&A/soft-law artifacts carry materially
> different bounded legal/practical effects that are lost when a research system
> labels all of them simply BINDING or NONBINDING?

## Target 1 — EBA Single Rulebook Q&A

The EBA Single Rulebook Q&A process handles practical application and
implementation questions across banking/payment/AML legislation and associated
delegated acts, RTS/ITS, guidelines and recommendations.

EBA's current official page states:

- Article 16b(2) answers have **no binding force in law**;
- Q&As are **not** subject to comply-or-explain;
- nevertheless their application is scrutinised by EBA and competent
  authorities because of their practical significance for a level playing field.

It also warns that:

- Q&As refer to the provisions in force on their publication date;
- EBA does not systematically review all Q&As after legislative amendment;
- users must check whether the referenced provisions remain unchanged.

Official sources:

- https://www.eba.europa.eu/single-rulebook-qa
- https://eba.europa.eu/single-rule-book-qa/search

### Effect profile

```text
BINDING LEGAL FORCE            = NO
COMPLY-OR-EXPLAIN              = NO
OFFICIAL PRACTICAL GUIDANCE    = YES
SUPERVISORY SCRUTINY/RELEVANCE = YES
TIME-BOUNDED INTERPRETIVE USE  = YES
```

Calling the Q&A "binding law" overstates it.

Calling it "legally irrelevant because nonbinding" understates its actual
supervisory/practical role.

## Target 2 — ESA Article 16 Guidelines

Regulation (EU) No 1095/2010 Article 16 provides a different profile for ESMA
guidelines/recommendations.

The current regulation requires:

- competent authorities and financial-market participants to **make every
  effort to comply**;
- competent authorities to notify whether they comply/intend to comply;
- non-compliance to be reported with reasons;
- ESMA to publish non-compliance status.

ESMA guidelines themselves repeat this compliance architecture.

Official sources:

- https://eur-lex.europa.eu/eli/reg/2010/1095/2025-11-10/eng
- https://www.esma.europa.eu/sites/default/files/2023-04/ESMA35-43-3565_Guidelines_on_certain_aspects_of_the_MiFID_II_remuneration_requirements.pdf

CJEU Case C-911/19 held that EBA Article 16 guidelines do **not**, as such,
produce binding legal effects vis-à-vis competent authorities or financial
institutions.

But the Court also distinguished this Article 16 "power to exhort and persuade"
from binding technical standards.

Official judgment:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:62019CJ0911

### Effect profile

```text
BINDING LEGAL EFFECT AS SUCH   = NO
MAKE-EVERY-EFFORT DUTY         = YES
NCA COMPLY-OR-EXPLAIN          = YES
PUBLIC NONCOMPLIANCE SIGNAL    = YES
SUPERVISORY INCORPORATION      = YES / CONTEXTUAL
```

This is materially stronger than the Q&A profile while still not equivalent to
a binding regulation.

## Target 3 — Commission competition Guidelines

EU competition-law case law supplies a different soft-law profile again.

The Court/General Court repeatedly states that Commission fining Guidelines:

- are not rules of law that the administration is always bound to observe;
- are nevertheless rules of practice;
- constrain Commission discretion after publication;
- departure without compatible reasons can engage equal-treatment and
  legitimate-expectation principles.

Examples:

- Dansk Rørindustri line, summarised in Case C-167/04 P:
  https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62004CJ0167
- Panasonic / General Court:
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=ecli:ECLI:EU:T:2015:612
- Quinn Barlo:
  https://eur-lex.europa.eu/legal-content/IT/ALL/?uri=ecli:ECLI:EU:C:2013:351

### Effect profile

```text
RULE OF LAW / LEGISLATION      = NO
SELF-IMPOSED PRACTICE RULE     = YES
LIMIT ON ADMIN DISCRETION      = YES
EQUAL-TREATMENT EFFECT         = YES
LEGITIMATE-EXPECTATION EFFECT  = POSSIBLE / CONTEXTUAL
BINDS EU COURT IN SAME WAY     = NO
```

So "nonbinding" does not mean "no legal effects."

## Boundary / control — ECHA website information

ECHA's current Legal Notice provides a useful hard boundary.

It states that information/documents/data on its website are generally not legal
advice and that, without prejudice to specifically identified authentic
information, only Official Journal text or specified authentic information is
capable of producing legal effects.

Source:

- https://echa.europa.eu/legal-notice

This shows that some official information artifacts genuinely should remain
low-effect documentary aids.

The proposed mechanism must therefore not promote every official guidance page
into soft law with bounded legal consequences.

## Existing baseline

The strongest baseline is already good:

- identify the exact legal basis for the artifact;
- read the issuing body's bindingness/status disclaimer;
- inspect any governing regulation;
- inspect relevant CJEU case law;
- distinguish legislation, technical standards, guidelines/recommendations,
  Q&A, opinions and documentation tools.

A capable EU lawyer can solve this without Needle.

Therefore this is not a product/value claim.

The candidate contribution is a reusable **failure classification** and later
evaluation construct.

## Structural correspondence

The recurring error is not simply:

`GUIDANCE -> LAW`

It is:

```text
official interpretive artifact
    ↓
research system assigns one coarse EFFECT value
    ↓
artifact's bounded legal/practical effect profile is lost
    ↓
research conclusion either:
  - over-promotes the artifact; or
  - wrongly discards its legally relevant effect
```

Examples of different effect dimensions include:

- binding legal force;
- comply-or-explain;
- make-every-effort obligation;
- supervisory incorporation;
- self-binding administrative practice;
- equal-treatment constraints;
- legitimate expectations;
- practical supervisory significance;
- no legal effect at all.

## Existing taxonomy check

### TECHNICAL_STANDARD_AUTHORITY_HANDOFF

Does not own.

That class concerns authority moving from an upstream final technical draft to
a downstream institution that amends/adopts binding law.

Soft-law artifacts may remain the relevant artifact; their problem is their
**bounded effect profile**, not later handoff to a final act.

### PRIVATE_ORIGIN_LEGAL_RECOGNITION

Does not own.

The current targets are public-origin official artifacts. The issue is not legal
recognition of a private determination.

### JUDICIAL_INTERPRETATION_TEMPORAL_OVERCLAIM

Does not own.

The issue is not judgment-date application timing.

No current trap class captures the effect-profile distinction cleanly.

## One falsifiable hypothesis

Working label:

`OFFICIAL_SOFT_LAW_EFFECT_COLLAPSE`

Hypothesis:

> EU legal research systems can produce materially wrong conclusions by
> collapsing official non-legislative artifacts into a binary
> BINDING/NONBINDING classification, because different artifact types possess
> materially different bounded effect profiles.

## Smallest discriminating experiment

If Cycle 3 synthesis selects this candidate:

1. perform a transport-free, source-fixed preregistration;
2. select three fresh official artifacts from materially different effect
   profiles:
   - Q&A / no binding force, no comply-or-explain;
   - ESA guideline / Article 16 make-every-effort + comply-or-explain;
   - Commission self-imposed guideline / discretion + legitimate-expectation
     effects;
3. exclude all artifacts used in this Run 3A derivation;
4. freeze governing legal basis and binding-effect evidence;
5. construct realistic research questions where a binary label changes the
   answer;
6. test whether the existing corpus structure can represent the distinction
   without a new ontology;
7. include one low-effect official-document control.

### Success

- at least two fresh profiles produce materially different legal consequences;
- a BINDING/NONBINDING-only answer is materially wrong or incomplete;
- one shared mechanism explains them;
- no existing trap class owns the distinction cleanly.

### Kill

Reject if:

- every consequential answer is resolved simply by "not legally binding";
- effect differences do not alter realistic legal advice/research conclusions;
- the profiles require unrelated doctrines with no reusable failure mechanism;
- or the result is only generic EU source-hierarchy instruction.

## Run 3A disposition

# **ADOPT_FOR_EXPERIMENT**

Retain:

`OFFICIAL_SOFT_LAW_EFFECT_COLLAPSE`

This candidate is interesting because it attacks an overly simple **effect
model**, not because guidance exists.

Do not add a trap class yet.

Do not build:

- guidance monitor;
- soft-law database;
- legal-effect ontology;
- Q&A ingestion;
- compliance product.

Only a bounded fresh-artifact generality test may be considered at #183.
