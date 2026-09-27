# Candidate B — harmonised-standard status product-readiness prototype

Status: **PRODUCT-READINESS PROTOTYPE — EXTERNAL VALUE UNPROVEN**

This static surface provides a known-standard lookup over five frozen official EU harmonised-standard legal-status records.

It exists to test one narrow user question:

> Does a compact projection of operative OJ-reference state and timing provide useful workflow
> value versus the strongest free official-source process for a real product-compliance user?

It is **not** a live monitoring service and must not be used as a current compliance database.

## Current product shape

The primary interaction is now deliberately product-like but still narrow:

1. enter a harmonised-standard reference already known to be relevant;
2. select a supported status date;
3. read a human-facing OJ citation state and presumption consequence;
4. inspect a restriction or already-fixed future transition;
5. open the attached official EUR-Lex evidence.

The interface no longer exposes an internal fixture/case selector as its primary task.

Visible freshness language makes clear that the data is frozen demonstration evidence, not live monitoring.

External-user recruitment remains deferred under #425.

## Static deployment bundle

A hosting bundle can be generated from canonical repository files without committing a second
hand-maintained copy of the legal-state data:

```sh
node mvp/candidate-b/build-static-demo.js
```

This creates ignored `dist/` output containing only:

- the Candidate-B HTML/CSS/JavaScript surface;
- the five frozen canonical fixtures required by the prototype;
- a small build manifest recording that the artifact is not live monitoring and that external
  value remains unproven.

`vercel.json` points a static deployment at this generated `dist/` directory.

The repository currently has no connected Vercel team/project in this ChatGPT environment, so this
is **deployment-ready, not deployed**.

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

#416 found that the Commission Formal Objections page is already a strong centralized discovery
surface for the frozen workload. The remaining test is therefore narrower: whether the maintained
state projection itself has useful workflow value.

A positive usability result against free official sources would only show that the compact
decision-ready rendering deserves further comparison against real incumbent product views.
