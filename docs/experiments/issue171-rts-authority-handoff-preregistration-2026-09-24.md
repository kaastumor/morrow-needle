# #171 pre-registration — technical-standard authority handoff generality

Date: 2026-09-24  
Issue: #171  
Claim type: `CORRECTNESS_VALIDITY / FAILURE_FAMILY_GENERALITY`  
Evidence role: `DERIVATION / PUBLIC_EXPOSED`

## Question

Does one reusable legal-information failure mechanism explain two independent
ESA → European Commission delegated-technical-standard chains where an ESA
publishes a **final draft RTS**, the Commission substantively changes the draft,
and the later Commission Delegated Regulation owns binding legal effect?

Working label:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

The label is provisional and may be rejected.

## Exposure boundary

Both target chains were already used in Cycle 2 Run A.

Therefore #171 cannot establish:

- fresh latent detection;
- model correctness advantage;
- independent blind validation;
- product value.

It tests only whether the exposed evidence earns a distinct DERIVATION failure
family and corpus representation.

## Frozen chains

Exactly two chains:

### Chain A — investment-firm fixed overheads

- ESA: European Banking Authority;
- upstream stage: EBA final draft RTS submitted in December 2020;
- Commission amendment stage: modified Commission version communicated in 2021;
- EBA response/opinion: 2022;
- binding downstream act: Commission Delegated Regulation (EU) 2022/1455.

### Chain B — crowdfunding

- ESA: European Banking Authority;
- upstream stage: EBA final draft RTS under Article 19(7) of Regulation
  (EU) 2020/1503, submitted in May 2022;
- Commission amendment stage: Commission intention to endorse with amendments in
  2023;
- EBA response/opinion: 2023;
- binding downstream act: Commission Delegated Regulation (EU) 2024/358.

No chain replacement is allowed because a comparison is inconvenient or
immaterial.

If a required official artifact cannot be retrieved, record the chain as
`EVIDENCE_INCOMPLETE`.

## Required artifact set per chain

Retrieve, where publicly available:

1. ESA final draft / final report or official submission record;
2. Commission amendment notification or ESA opinion quoting/describing the
   Commission modification;
3. ESA response to the modification;
4. adopted delegated regulation on EUR-Lex / Official Journal;
5. legal-effect/adoption metadata sufficient to distinguish draft from binding
   act.

The ESA opinion may serve as evidence for both (2) and (3) when it reproduces or
describes the Commission amendment precisely enough to compare the proposition.

## Proposition test

For each chain, identify at most **one** clearest substantive proposition changed
between upstream final draft and adopted binding act.

Freeze it as:

- upstream proposition;
- Commission modification;
- adopted proposition;
- realistic legal-research question whose answer changes or becomes materially
  incomplete if the ESA final draft is treated as current binding law.

Do not select a second proposition merely because the first does not look
dramatic enough.

## Materiality

A proposition delta is material only if using the ESA final draft as the binding
final rule could cause at least one of:

- wrong legal requirement;
- wrong permission/prohibition;
- wrong calculation/input;
- wrong scope/person/entity coverage;
- materially incomplete compliance/research advice.

Pure drafting style, numbering, recital language or non-operative wording does
not qualify.

## Strong baseline

The strongest boring baseline is full official-source lifecycle research:

- ESA draft/submission;
- Commission modification stage;
- ESA response;
- EUR-Lex/OJ adopted delegated regulation.

A careful researcher can solve the lifecycle without Needle.

Needle gets no product-value credit for that.

The experiment asks whether preserving this failure mechanism as a reusable
adversarial corpus class is warranted.

## Existing taxonomy gets first refusal

Before creating a new class, test these existing classes in this order:

1. `PARALLEL_INSTRUMENT_LIFECYCLE`
2. `STATUS_APPLICATION_SEPARATION`
3. `DYNAMIC_REFERENCE_STATUS`
4. `SOURCE_STATE_BACKPROJECTION`

A current class **owns** the case only if its existing mechanism can explain both
chains without losing a consequential distinction.

A class does not own the case merely because its wording can be stretched.

### Specific boundaries

`PARALLEL_INSTRUMENT_LIFECYCLE`

Owns only if the core error is inheriting lifecycle state between separate legal
instruments under a shared umbrella identity.

`STATUS_APPLICATION_SEPARATION`

Owns only if the core error is confusing an instrument's status with its
application/start-of-effect state.

`DYNAMIC_REFERENCE_STATUS`

Owns only if the core error concerns current status of an externally referenced
document/set.

`SOURCE_STATE_BACKPROJECTION`

Owns only if the core error is later source state being projected backward into
an earlier observation horizon.

If none owns the mechanism cleanly, test the provisional new class.

## Provisional class definition

Only if earned:

`TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

> A document may be final within an upstream technical-standard-setting
> authority's drafting stage without owning the downstream binding legal rule.
> Where a later institution has formal amendment/adoption power, authority and
> legal effect must remain attached to the exact institutional stage and adopted
> artifact rather than inherited from the upstream "final draft".

This wording may be narrowed by the evidence but not broadened beyond the two
chains.

## Success

Support a distinct failure family only if **both** chains show:

1. an upstream ESA final draft;
2. formal downstream Commission modification/adoption authority;
3. a material operative proposition delta;
4. adopted binding text that resolves differently from the upstream draft;
5. a realistic legal-research conclusion that changes or materially narrows;
6. no existing trap class owns the mechanism without semantic distortion.

## REVISE

Use `REVISE` if the mechanism is real but:

- only one chain has a material proposition delta; or
- an existing class can be cleanly generalized with a small label/definition
  change.

## REJECT

Reject the distinct class if:

- the changes are not legally material;
- the mechanism reduces to ordinary draft-versus-final hygiene;
- both chains are already cleanly owned by an existing class;
- or the only distinction is that the final regulation has a later date.

## Corpus consequence

If supported:

- add both chains as `DERIVATION` cases;
- mark them `PUBLIC_EXPOSED` / regression-only;
- add exactly one new trap class;
- do not increase evaluation claims.

If revised into an existing class:

- update cases only if they add orthogonal useful coverage;
- do not create an alias class.

If rejected:

- add nothing merely because the research was completed.

## No implementation

No:

- RTS tracker;
- EBA/ESMA/EIOPA ingestion;
- delegated-act lifecycle graph;
- monitoring;
- Explorer feature;
- schema expansion beyond the minimal corpus class/cases if earned.

## Evidence closure

Preserve:

- this preregistration;
- exact official sources;
- one proposition comparison per chain;
- taxonomy comparator analysis;
- final disposition;
- any corpus diff.

No model execution occurs in #171.
