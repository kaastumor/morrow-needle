# Candidate B — disposable harmonised-standard status MVP

Status: **USABILITY PROTOTYPE — VALUE UNPROVEN**

This static surface projects five frozen official EU harmonised-standard legal-status cases.

It exists to test one narrow user question:

> Can a lean product/compliance user understand the operative OJ-reference state and its timing
> more easily than by reconstructing the same state from fragmented official pages?

It is **not** a live monitoring service and must not be used as a current compliance database.

## Local launch

From repository root:

```sh
python -m http.server 8000
```

Then open:

`http://localhost:8000/mvp/candidate-b/`

## Frozen cases

1. GAR — EN 497:2022 — formal non-publication;
2. Machinery — EN 50434:2014 — citation maintained with restriction;
3. Toy Safety — EN 71-1:2014+A1:2018 — restricted citation;
4. LVD — EN 60335-2-14:2006 — formal non-publication;
5. LVD — EN 60335-2-60:2003 — current citation with future withdrawal on 18 January 2027.

The surface reads the canonical fixtures under `fixtures/dependency/`.

It does not copy a second legal-state database into the MVP directory.

## Safety boundary

The prototype deliberately does **not** determine full product conformity.

It does not provide:

- the standard text;
- technical-requirement interpretation;
- applicable-legislation discovery;
- testing/lab evidence;
- notified-body decisions;
- supplier evidence validation;
- CE-marking advice;
- live updates.

Each case has an explicit frozen evidence window. Queries outside that window fail instead of
inventing historical/future state.

## Relationship to competitors

#411 already established that accessible products offer substantial standards-monitoring/status
capability.

This MVP is not a novelty demonstration.

A positive usability result against free official sources would only show that the compact
decision-ready rendering deserves further comparison against real incumbent product views.
