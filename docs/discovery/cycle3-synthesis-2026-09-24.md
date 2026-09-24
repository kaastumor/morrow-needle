# Cycle 3 synthesis — source-role and evidence-state map

Issue: #183  
Parent: #177  
Date: 2026-09-24  
Cycle decision: **CONTINUE**

## Executive decision

Cycle 3 produced three evidence-backed candidates and one useful negative result:

- Run 3A — `OFFICIAL_SOFT_LAW_EFFECT_COLLAPSE` → **PARK / RESERVE**
- Run 3B — `OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM` → **PARK / RESERVE**
- Run 3C — machine-readable derivative drift → **PARK / NO DISTINCT FAMILY**
- Run 3D — `OFFICIAL_AUTHORITY_HANDOFF` → **ADOPT_FOR_EXPERIMENT**

Select exactly one next experiment:

> **test whether #171 `TECHNICAL_STANDARD_AUTHORITY_HANDOFF` is one instance
> of a broader `OFFICIAL_AUTHORITY_HANDOFF` family.**

No product implementation is authorised.

## Why active discovery earned continuation

Cycle 3 changed the map in four different ways.

1. Run A found that official non-legislative artifacts cannot safely be reduced
   to one BINDING/NONBINDING bit.
2. Run B found a distinct negative-inference mechanism based on registry
   coverage rather than staleness.
3. Run C killed an attractive machine-readable-specific class: automation scale
   did not create a new legal-information mechanism.
4. Run D showed that the newly earned RTS handoff class may itself be too narrow.

This is evidence of useful active discovery rather than opportunity-count
production.

## Run 3A — official soft-law effect collapse

Candidate:

`OFFICIAL_SOFT_LAW_EFFECT_COLLAPSE`

Independent evidence spans materially different official effect profiles:

- EBA Q&A:
  - no binding force;
  - no comply-or-explain;
  - practical/supervisory significance;
- ESA Article 16 guidelines:
  - no binding legal effect as such;
  - make-every-effort architecture;
  - competent-authority comply-or-explain;
- Commission competition guidelines:
  - not legislation;
  - can constrain Commission discretion through equal-treatment and
    legitimate-expectation principles.

Boundary:

- ordinary ECHA website information can genuinely remain low-effect
  informational material.

### Synthesis disposition: PARK / EVIDENCE-BACKED RESERVE

Why not select now:

- the mechanism is plausible and new;
- but a generalised "effect profile" risks importing doctrine-specific
  complexity into the corpus taxonomy;
- the fresh experiment would primarily add another failure family;
- a positive result may pressure the project toward an effect ontology that has
  not independently earned itself.

Reopen after the selected authority-handoff experiment or when a concrete
soft-law error becomes independently consequential.

## Run 3B — registry coverage overclaim

Candidate:

`OFFICIAL_REGISTRY_COVERAGE_OVERCLAIM`

Independent evidence:

- Union Register absence cannot establish absence of all EU/national medicinal
  marketing authorisation because the register is centralised-procedure scoped;
- Safety Gate absence cannot establish product safety/compliance because the
  system is notification/event/sector scoped;
- ECHA Candidate List supplies a narrow authentic-set control and demonstrates
  that even valid negative inference still depends on identity/group
  resolution.

The mechanism is:

> negative observation from a current official register is widened beyond the
> registry's declared coverage predicate.

This is orthogonal to update lag.

### Synthesis disposition: PARK / EVIDENCE-BACKED RESERVE

Why not select now:

- target evidence is strong;
- the mechanism is clean and likely testable;
- but success would mainly add one new corpus class;
- it changes project understanding less than testing whether a class admitted
  only hours earlier is itself over-specific.

This is the strongest reserve after the selected experiment.

## Run 3C — machine-readable derivative drift

Proposed mechanism:

`MACHINE_READABLE_OFFICIAL_DERIVATIVE_DRIFT`

Result:

**PARK / NOT DISTINCT**

The Union Register BETA dataset showed a real older observation horizon than
human-facing pages.

But the causal error was still:

> derived snapshot state != newer official state.

CELLAR feeds and ECHA version/delta packages also demonstrate mature incumbent
freshness/version controls.

Machine-readability increases blast radius but did not create a new
legal-information failure mechanism.

### Synthesis consequence

Do not create a class merely because automation scales an existing error.

Re-entry requires a same-time semantic/transformation mismatch not explained by:

- freshness;
- update horizon;
- representation-local identity.

## Run 3D — authority handoff generalisation

Candidate:

`OFFICIAL_AUTHORITY_HANDOFF`

Run D has the strongest taxonomy-level information gain.

### RTS anchor

#171 already established:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

An ESA final draft RTS can be final within the upstream technical-authority role
while the Commission still owns amendment/adoption of the binding delegated
regulation.

### Medicines pipeline

CHMP performs the scientific assessment and recommends whether a centrally
authorised medicine should be authorised.

The Commission owns the legally binding marketing-authorisation decision.

The distinction is not merely formal.

Orphacol supplies direct material evidence:

- CHMP positive opinion: 16 December 2010;
- Commission refusal: 25 May 2012;
- General Court annulled that refusal in Case T-301/12;
- marketing authorisation ultimately issued: 12 September 2013.

So:

> positive specialist recommendation != final legal authorisation.

Current EMA pages also explicitly label post-opinion medicines as
`pending EC decision`.

### REACH restriction pipeline

RAC/SEAC opinions are formal expert inputs.

The Commission and Member States own the downstream restriction decision and
binding Annex XVII amendment.

The Commission may also terminate a restriction procedure without an Annex XVII
amendment.

### Boundary

ECHA Candidate List inclusion prevents an over-general rule.

ECHA states that inclusion itself may trigger immediate legal obligations.

Therefore:

> specialist/agency artifact -> always merely advisory

is false.

The mechanism must follow the exact procedural owner of legal effect.

## Existing-class first refusal

The selected experiment is not allowed to spawn a second handoff class by
default.

Question:

> Can one falsifiable definition own RTS draft→adoption, CHMP
> opinion→authorisation and RAC/SEAC opinion→restriction while excluding
> procedures where the upstream agency action itself owns legal effect?

If yes:

- rename/generalise #171;
- keep one class;
- preserve subtypes/examples in case metadata/prose only if needed.

If no:

- keep #171 narrow;
- park the Run-D generalisation;
- do not automatically create a second opinion→decision class.

## Candidate ranking by information gain

### 1. Run D — authority handoff

Highest.

A positive result simplifies taxonomy.

A negative result protects #171 from an over-broad abstraction.

Both outcomes change how Needle represents mechanism families.

### 2. Run B — registry coverage

Strongest new-family reserve.

A positive result adds an orthogonal negative-inference failure class.

### 3. Run A — soft-law effect profiles

Strong evidence, but highest risk of doctrine/ontology creep.

### 4. Run C — machine-readable derivative

Already produced its useful negative result; no experiment currently earned.

## Transport lesson

Cycle 3 inherited the #165/#174 metadata-only transport guard.

None of the discovery conclusions above depends on claiming that external
transport itself proves the mechanism.

Any selected experiment requiring deterministic external enumeration must:

1. smoke-test transport shape before full preregistration;
2. observe schema/count/pagination only;
3. retain no candidate identity/content from the smoke test;
4. then freeze the real selection rule.

## Relative-value check

Cycle 3 did not produce a delivery-ready product/workflow claim.

A/B/D are correctness/validity/taxonomy hypotheses.

Therefore none may be preserved after a failed correctness experiment by
relabeling it as convenience or workflow value.

No Explorer/product work is authorised from this cycle.

## H-22 / active-discovery check

Cycle 3 supports the sponsor-directed active-discovery model.

Evidence:

- three genuinely different source-role/evidence-state mechanisms emerged;
- one proposed mechanism was explicitly rejected as non-distinct;
- strong official/incumbent safeguards narrowed every retained claim;
- no feature was built;
- one candidate is selected because it may **subtract** taxonomy, not because it
  is easiest to make positive.

The active-discovery claim therefore survives with the same guards:

- WIP=1;
- strong alternatives;
- explicit boundaries;
- no opportunity-count target;
- hard synthesis gate;
- at most one experiment.

## Selected experiment

Working title:

> **OFFICIAL AUTHORITY HANDOFF GENERALITY**

Claim type:

`CORRECTNESS_VALIDITY / FAILURE_FAMILY_GENERALITY`

### Claim

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF` is a specific instance of the broader:

`OFFICIAL_AUTHORITY_HANDOFF`

mechanism:

> an official specialist body can complete a draft, opinion, recommendation or
> assessment within its assigned role while a different institution owns the
> downstream binding decision; legal effect must remain attached to the
> procedure's actual decision owner rather than inherited from upstream
> authority/finality.

### Fresh evidence requirement

Pre-register:

1. one fresh completed EMA/CHMP → Commission marketing-authorisation chain;
2. one fresh completed ECHA RAC/SEAC → Commission restriction chain;
3. one control where the upstream agency action itself owns the relevant legal
   effect.

Exclude from positive validation:

- Orphacol;
- any specific examples used in Run 3D;
- #171 fixed-overheads/crowdfunding RTS chains.

These remain DERIVATION.

### Materiality

Each positive must support a realistic as-of research question where promoting
the upstream artifact to final legal state changes the answer.

Mere procedural sequencing is insufficient.

### Success

Generalise/rename #171 only if:

- both fresh pipelines reproduce the same authority/effect ownership error;
- the common definition also fits the two RTS cases without semantic strain;
- the control is cleanly excluded;
- the broader class remains specific enough to predict failure and boundary;
- no separate doctrine-specific class is required.

A pure rename/generalisation keeps trap-class count unchanged.

### Kill

Keep #171 narrow if:

- fresh examples reduce to generic "recommendation != decision";
- no realistic legal answer changes;
- the shared abstraction fits almost every administrative procedure;
- EMA and ECHA require materially different mechanisms;
- the control cannot be excluded without ad hoc wording.

Do not create a second class merely because the broad generalisation fails.

## Cycle 3 direction

# **CONTINUE**

Meaning:

- run exactly one authority-handoff generality experiment;
- keep Run B as first reserve;
- keep Run A as second reserve;
- keep Run C parked;
- no product implementation;
- no new cycle until the selected experiment is synthesised.

## Final position

The strongest Cycle-3 question is not:

> how many new source-role traps can Needle name?

It is:

> **can Needle's newest trap family become smaller and more general without
> becoming vague?**

That receives the next bounded experiment.
