# Issue #319 — frozen trap-class boundary / negative-control audit

Date: 2026-09-25  
Disposition: **BOUNDARIES_ADEQUATE**

## Question

Do the frozen 26 trap classes have source-backed limiting evidence, or are some merely
well-populated positive-example families whose definitions outrun their tested boundary?

## Method

This audit uses only:

- the frozen 26 class definitions;
- accepted corpus provenance;
- already-completed discovery/evaluation issues and result documents.

No new legal research, cases, classes or model runs were introduced.

A class can carry more than one support type:

- **EXPLICIT_NEGATIVE_CONTROL** — accepted evidence shows a nearby case/mechanism where
  the class must not apply;
- **EXPLICIT_BOUNDARY_RULE** — accepted source-backed limiting condition narrows the class;
- **COMPOSITION_ANTI_MERGE** — accepted evidence shows adjacent classes can coexist while
  remaining legally distinct;
- **POSITIVE_ONLY** — no accepted explicit boundary found;
- **UNKNOWN** — existing owner state is insufficient to decide.

## Frozen result

All **26/26 classes** have an explicit source-backed boundary rule.

Within that set:

- **14/26** also have a clean explicit negative/opposite control;
- **5/26** have composition evidence that directly resists an adjacent-class merge;
- **0/26** are `POSITIVE_ONLY`;
- **0/26** are `UNKNOWN`.

This does **not** mean all classes have independent evaluation evidence. #309 remains
binding: only 8/26 classes have any EVALUATION case. Boundary evidence and comparative
validation answer different questions.

## Class-by-class boundary profile

| Class | Boundary support | Accepted owner / limiting evidence |
| --- | --- | --- |
| `AUTHORITATIVE_EXTERNAL_INPUT_TRIGGER` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #222 excludes an official database that is merely informational; #226 shows official confirmation can still fall under a statutory derogation rather than mechanically create ordinary geography. |
| `CHOICE_OF_FORUM_STATE` | EXPLICIT_BOUNDARY_RULE; COMPOSITION_ANTI_MERGE | #276 preserves protected-party and Article 24 exclusive-jurisdiction limits; #279 shows forum choice can coexist with separate law choice and participation state. |
| `CHOICE_OF_LAW_STATE` | EXPLICIT_BOUNDARY_RULE; COMPOSITION_ANTI_MERGE | #264 preserves default-law, mandatory-protection and public-policy limits; #279 shows applicable-law choice remains separate from forum choice and participation. |
| `COHORTED_TRANSITIONAL_APPLICABILITY` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #239 contrasts object-specific legacy/cohort rules with ordinary uniform calendar application; qualifying historical state, not date alone, is required. |
| `CROSS_BORDER_RECOGNITION_ACTIVATION_STATE` | EXPLICIT_BOUNDARY_RULE | #270 gives the symmetric limits: home entitlement alone is insufficient, while a completed Union passport route can remove the need for duplicate host authorisation; the actual route/scope must be preserved. |
| `CROSS_ORDER_INCORPORATION_STATE` | EXPLICIT_BOUNDARY_RULE | #242 establishes that EEA relevance is not EEA applicability and that incorporation/JCD effect belongs to the target legal order; #252 generalises the separate acceptance route to Switzerland/Schengen. |
| `DIFFERENTIATED_MEMBER_STATE_PARTICIPATION` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE; COMPOSITION_ANTI_MERGE | #243 uses an ordinary EU-wide regulation as control; #273 excludes separate agreement/incorporation routes from direct participation; #279 composes participation with law/forum choice. |
| `DIRECTIVE_INVOCABILITY_STATE` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE; COMPOSITION_ANTI_MERGE | #266 uses Faccini Dori / private-party horizontal effect as the refusal boundary and Popławski as a primacy limit; #274 shows invocability and later disapplication are separate state owners. |
| `DYNAMIC_REFERENCE_STATUS` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #218 rejects static/dynamic incorporated-version semantics as a new instance of this class; the class remains narrow to authoritative status-gated changes such as publication/restriction/withdrawal. |
| `EU_PRIMACY_DISAPPLICATION_STATE` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE; COMPOSITION_ANTI_MERGE | #259 uses Popławski to show conflict alone is insufficient when the EU norm lacks direct effect; #274 shows disapplication can be owned by another directly effective norm without making a Directive horizontally invocable. |
| `EXPRESSION_LOCAL_REPRESENTATION_ASYMMETRY` | EXPLICIT_BOUNDARY_RULE | #64 preserves `NO_ASSERTION` for a non-listed authentic language even where independent wording evidence exists; #67 proves correction labels/ordinals are expression-local rather than cross-language identities. |
| `JUDICIAL_INTERPRETATION_TEMPORAL_EFFECT` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #230 preserves the normal declaratory/ex-tunc rule; #253 deliberately adds a genuine temporal-limit exception and requires a refused-limit request as control. |
| `JUDICIAL_VALIDITY_TEXT_DIVERGENCE` | EXPLICIT_BOUNDARY_RULE | #83/#249/#234 cover invalidity, interim suspension and partial annulment; #259 explicitly separates formal validity change from primacy-based disapplication where the national rule remains valid. |
| `MACHINE_COMPLIANCE_ARTIFACT` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #225 uses the voluntary ELI machine-readable ontology/schema as the negative control: machine readability + versioning alone is insufficient; the artifact must participate in a legally consequential compliance/acceptance path. |
| `MEMBER_STATE_PERMITTED_DIVERGENCE` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #272 uses Directive (EU) 2019/771 full harmonisation as the opposite control: national divergence is not presumed merely because a Directive/national implementation exists. |
| `OFFICIAL_AUTHORITY_HANDOFF` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #195 preregistered and satisfied the control where upstream agency action itself owns the tested legal effect (ECHA Candidate List), excluding it from the downstream-decision handoff family. |
| `PARALLEL_INSTRUMENT_LIFECYCLE` | EXPLICIT_BOUNDARY_RULE | #91 limits the mechanism to legally distinct instruments behind an umbrella deal and expressly distinguishes it from delayed application of obligations inside one instrument. |
| `PRIVATE_ORIGIN_LEGAL_RECOGNITION` | EXPLICIT_BOUNDARY_RULE | #85 requires a bounded public-law recognition basis and rejects downstream consequences not established by that basis; private origin is neither disqualifying nor converted into public authority. |
| `PROCEDURAL_CLOCK_SUSPENSION` | EXPLICIT_BOUNDARY_RULE | #241 states that not every request, delay or late response pauses a clock; only an event to which the governing procedure assigns suspension effect qualifies. |
| `PROCEDURAL_SILENCE_LEGAL_EFFECT` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #238 uses Prospectus Regulation Article 20 as the opposite control: missing a deadline expressly does **not** mean deemed approval there. |
| `SOURCE_VIEW_TEMPORAL_DIVERGENCE` | EXPLICIT_BOUNDARY_RULE | #61 distinguishes ex-post corrected/consolidated view from contemporaneous source availability; #93 preserves the converse boundary that a stale tracker does not erase the historical truth of its earlier enforcement state or decide later Commission compliance. |
| `STATUS_APPLICATION_SEPARATION` | EXPLICIT_BOUNDARY_RULE | #78 preserves divergence in both directions: designated-but-not-yet-applicable and no-longer-designated-but-still-applicable. Membership/status therefore cannot stand in for application state. |
| `SUBDAY_TEMPORAL_BOUNDARY` | EXPLICIT_BOUNDARY_RULE | #88's exact 12:59/13:01 licence pair and #81's offset-aware closure interval prove that a finer-than-date boundary is required only when it changes the legal result. |
| `SUBSTATE_TERRITORIAL_REGIME` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #255 uses mainland territory as the control and expressly excludes ordinary subnational divisions absent a legally distinct territorial regime. |
| `UNION_NEXUS_APPLICABILITY` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #263 uses mere passive/technical EU accessibility as a negative boundary; an external actor/conduct plus the act's legally specified Union nexus is required. |
| `VERTICAL_SPATIAL_EXTENT` | EXPLICIT_NEGATIVE_CONTROL; EXPLICIT_BOUNDARY_RULE | #286 retains #227 deep-sea fisheries as the negative control: a vertical measurement that can be losslessly projected to a horizontal eligibility mask does not qualify; independently meaningful vertical legal differentiation must survive. |

## What this means

The final taxonomy is not merely a set of labels supported by repeated positives.

Every class has at least one accepted rule describing where it stops, and more than half
have a concrete opposite/nearby control where the mechanism does not apply.

That matters because it makes the classes falsifiable enough for regression/reference
use:

> a future case can fail a class not only because it looks different, but because it
> crosses an already-preserved causal or doctrinal boundary.

## What this does not mean

This audit does **not** establish:

- representative coverage;
- prevalence of any class;
- independent experimental validation for all classes;
- model-detection difficulty;
- that every boundary has been tested in every domain;
- that 26 is the uniquely correct taxonomy size.

In particular, the following remain distinct:

- **positive support** — multiple accepted examples;
- **boundary support** — evidence defining where the class stops;
- **evaluation support** — a case admitted through a predeclared evaluation design;
- **population support** — not established.

A class can be well bounded and still lack independent evaluation evidence.

## Packaging implication

No new maintained boundary registry is warranted.

The evidence is distributed across the owning discovery/evaluation records because those
records preserve the legal and methodological context needed to understand the boundary.
A separate 26-row machine artifact would add another truth surface with little new use.

This audit is a frozen retrospective description, not a new canonical taxonomy owner.

## Disposition

**BOUNDARIES_ADEQUATE**

The frozen 26-class taxonomy has adequate accepted boundary evidence for its current role
as a regression/reference classification.

No class definition repair, corpus mutation or new control research is required by #319.

The next useful audit should therefore not ask whether classes have *some* boundary. A
higher-information question is whether their 3–5 supporting cases provide genuinely
independent generality evidence or merely multiple examples from the same doctrinal/source
chain.
