# Cycle 3 Run 3D — expert opinion/recommendation to final decision

Issue: #181  
Parent: #177  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven anchors

- #171 `TECHNICAL_STANDARD_AUTHORITY_HANDOFF`;
- #135 judicial-document-role confusion;
- #85 public/private recognition boundaries.

The discovery question is:

> Is the #171 RTS class a genuinely technical-standard-specific mechanism, or is
> it one instance of a broader official authority-handoff failure family?

## Pipeline 1 — EMA/CHMP opinion → Commission marketing authorisation

The Commission's official centralised-authorisation page describes a split
decision chain.

### Upstream role

EMA validates and scientifically evaluates the application.

CHMP:

- performs the scientific assessment;
- gives a **recommendation** on whether the medicine should be authorised;
- if favourable, supplies draft product information.

EMA forwards the opinion to the Commission.

### Downstream role

The European Commission then starts its separate decision-making phase.

The Commission:

- prepares a draft implementing decision;
- obtains Member-State scrutiny through the Standing Committee;
- adopts the decision;
- notifies the marketing-authorisation holder;
- publishes the decision in the Union Register.

The official page states directly:

> marketing authorisation is granted by the European Commission following EMA
> scientific assessment.

Source:

- https://health.ec.europa.eu/medicinal-products/legal-framework-governing-medicinal-products-human-use-eu/authorisation-procedures-centralised-procedure_en

### Material role difference

A favourable CHMP opinion changes the probability/trajectory of authorisation.

It does **not** itself grant the EU marketing authorisation.

Current EMA pages make this state visible in practice: September 2026 CHMP
recommendations such as Pepaxti are explicitly labelled **pending EC decision**.

The distinction is also historically outcome-consequential, not merely a formal
waiting period.

#### Orphacol

CHMP adopted a positive opinion for Orphacol on 16 December 2010 recommending a
marketing authorisation.

The European Commission nevertheless adopted Implementing Decision C(2012) 3306
final on 25 May 2012 **refusing** that marketing authorisation.

The General Court later annulled the refusal in Case T-301/12. EMA records the
marketing authorisation as issued only on 12 September 2013.

Sources:

- https://www.ema.europa.eu/en/documents/smop-initial/chmp-summary-positive-opinion-orphacol_en.pdf
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex:62012TJ0301
- https://www.ema.europa.eu/en/medicines/human/EPAR/orphacol
- https://www.ema.europa.eu/en/news/meeting-highlights-committee-medicinal-products-human-use-chmp-14-17-september-2026

Therefore the two propositions are genuinely independent:

- "Has CHMP recommended authorisation?" can be YES;
- "Has the Commission granted the marketing authorisation?" can still be NO.

This is direct evidence that legal effect cannot be inherited from the upstream
scientific recommendation.

## Pipeline 2 — ECHA RAC/SEAC opinions → Commission REACH restriction

ECHA's official REACH restriction process likewise separates expert assessment
from binding restriction.

### Upstream role

RAC:

- adopts an opinion on whether the proposed restriction appropriately reduces
  risk.

SEAC:

- develops and adopts the socio-economic opinion.

ECHA then sends the RAC/SEAC opinions and background material to the Commission.

### Downstream role

The Commission:

- prepares a draft amendment to Annex XVII;
- proceeds through the relevant committee/scrutiny process;
- adopts the restriction if not opposed;
- publishes the binding restriction in the Official Journal.

Only after adoption does ECHA state that industry needs to comply with the
restriction.

Sources:

- https://echa.europa.eu/regulations/reach/restrictions/restriction-procedure/restrictions-process/steps
- https://echa.europa.eu/restriction-process-phase-3

ECHA's Registry of Restriction Intentions also keeps separate states for:

- RAC/SEAC opinion;
- final opinion/background document;
- adopted restriction/Commission communication.

Example pages visibly distinguish "Opinions adopted" from "Commission decided."

### Material role difference

At:

```text
RAC/SEAC final opinion
    ↓
Commission restriction not yet adopted
```

the answers differ:

- "Have ECHA committees recommended/assessed the restriction?" → YES
- "Is the proposed Annex XVII restriction already binding on industry?" → NO

Again, legal effect belongs to the downstream adopted act.

## Boundary — expert-agency action can itself own legal effect

ECHA's Candidate List prevents an over-broad rule.

ECHA says:

- only the Candidate List published on its website is deemed authentic;
- companies may have immediate legal obligations following **inclusion** of a
  substance in that list.

Sources:

- https://echa.europa.eu/candidate-list-table
- https://echa.europa.eu/candidate-list-obligations

So the correct rule is not:

> agency/expert body output is never binding until Commission acts.

The actual question is:

> Which institution/artifact owns legal effect for this exact procedure?

## Comparison with #171 RTS class

### Shared mechanism

All three pipelines have:

```text
upstream official specialist artifact
    ↓
artifact is final/complete for upstream role
    ↓
different institution owns downstream binding act
    ↓
research system inherits legal effect across the role boundary
    ↓
current legal state is overstated
```

#171 RTS:

- EBA final draft RTS;
- Commission can amend and adopt delegated regulation.

EMA:

- CHMP scientific opinion/recommendation;
- Commission grants marketing authorisation.

REACH restriction:

- RAC/SEAC opinions;
- Commission adopts Annex XVII amendment.

### Important differences

RTS includes direct text-development/amendment of a future legal rule.

EMA/ECHA opinion pipelines are more clearly recommendation/input-to-decision
models.

Therefore the current class wording:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

is too implementation-specific to own EMA/ECHA cleanly.

But creating a second separate class may duplicate the same underlying
authority/effect error.

## One falsifiable hypothesis

Working generalisation:

`OFFICIAL_AUTHORITY_HANDOFF`

Provisional definition:

> An official specialist body may complete a draft, opinion, recommendation or
> assessment within its own legally assigned role while another institution owns
> the downstream binding decision. Legal effect must remain attached to the
> procedure's actual decision owner and final act rather than being inherited
> from the upstream artifact's authority, finality or practical importance.

Hypothesis:

> `TECHNICAL_STANDARD_AUTHORITY_HANDOFF` is a subtype/example of this broader
> reusable mechanism and should be generalised rather than accompanied by a
> second opinion-to-decision trap class.

## Strong baseline

Official procedures already make the ownership chain explicit:

- Commission centralised-authorisation process;
- ECHA restriction process diagrams/registry;
- adopted decisions in Union Register/OJ.

A careful domain expert can resolve the distinction.

No product value is claimed.

## Smallest discriminating experiment

If #183 selects this:

1. freeze one fresh completed EMA authorisation chain;
2. freeze one fresh completed ECHA restriction chain;
3. exclude any cases/artifacts cited in this derivation run;
4. preserve:
   - upstream specialist artifact;
   - explicit procedural legal basis;
   - downstream binding act;
   - dates/status;
5. formulate one realistic current-state question per chain;
6. test whether the existing #171 definition can be generalised without losing
   the RTS-specific distinction;
7. include one control where the upstream agency action itself owns legal effect.

### Success

Generalise/rename #171 only if:

- both fresh chains exhibit the same consequential authority-effect handoff;
- a common definition predicts all RTS + EMA + ECHA cases;
- the broader class remains falsifiable;
- the control is correctly excluded;
- no separate doctrine is needed to make the common mechanism true.

### Kill

Keep #171 narrow if:

- EMA/ECHA failures reduce only to generic "recommendation ≠ decision";
- the shared wording becomes so abstract that almost any administrative
  procedure fits;
- downstream legal-effect ownership is not consequential in fresh cases;
- the control cannot be stated cleanly.

## Run 3D disposition

# **ADOPT_FOR_EXPERIMENT**

Retain:

`OFFICIAL_AUTHORITY_HANDOFF`

as a **generalisation hypothesis**, not a new class.

This candidate has high information gain because success would make the corpus
taxonomy **smaller/more general**, not larger:

- rename/generalise one existing class;
- avoid spawning parallel classes for RTS, medicines, chemicals, etc.

Do not add EMA/ECHA corpus cases yet.

Do not build:

- authorisation tracker;
- ECHA restriction monitor;
- EMA integration;
- cross-agency lifecycle graph;
- authority ontology.

Only the bounded generalisation experiment may be considered at #183.
