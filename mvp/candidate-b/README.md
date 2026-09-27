# Candidate B — harmonised-standard status + act-context product experiment

Status: **PRODUCT EXPERIMENT — EXTERNAL VALUE UNPROVEN**

This static surface provides a known-standard lookup over five frozen official EU harmonised-standard legal-status records and one bounded act-centric context view for Directive 2014/35/EU.

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

External-user recruitment remains deferred. #434 is an internal product experiment, not external-value evidence.

## Act-centric lifecycle experiment

The first governing-act view is deliberately bounded to **Directive 2014/35/EU — Low Voltage Directive**.

It is text-first and source-linked. It shows:

- Article-1-grounded purpose and voltage scope;
- a first-class **Who / what does this concern?** view that separates formal addressee, economic actors, market activity, product scope, territory/time context and Annex-II exclusions;
- bounded manufacturer / authorised-representative / importer / distributor orientation;
- the displayed 73/23/EEC -> 2006/95/EC -> 2014/35/EU lineage;
- adoption, publication, entry-into-force, transposition/application and repeal-transition dates as distinct events;
- separate legal-as-of, evidence-verified and source-version dates;
- the current consolidated text date and Directive (EU) 2024/2749 amendment;
- Article 114 TFEU as the legal basis;
- selected framework context from Regulation (EC) No 765/2008, Decision No 768/2008/EC and Regulation (EU) No 1025/2012;
- first-class **operative legal dependencies**, including the imported harmonised-standard definition and Regulation 1025/2012 OJ-reference/formal-objection machinery;
- Article 12's harmonised-standard/OJ-reference mechanism plus the represented Articles 13/14 fallback presumption routes;
- links back to the two frozen LVD standard-status examples;
- an explicit correction and evidence-coverage route.

The view explicitly does **not** claim complete legal context. It excludes national transposition, a general case-law graph, applicable-standard discovery, all amendments/standards and recursive relationship traversal.

“Operative dependency” is narrower than “related legislation”: the page shows an external provision only where it materially supplies a definition, procedure, condition or other legal mechanism needed to understand the focal act. Displaying such a dependency does not imply that the entire external act is imported into every LVD question.

The visual treatment is secondary to semantic HTML: every displayed legal relationship remains readable without relying on arrows, layout or colour.

Design research:
`docs/mvp/candidate-b-lifecycle-information-design-research-2026-09-27.md`

Red-team boundary:
`docs/discovery/issue432-act-centric-lifecycle-red-team-2026-09-27.md`

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

The generated bundle has been successfully deployed through Vercel from the canonical GitHub repository.
Deployment URLs are environment-specific and are not treated as canonical project identifiers.

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
