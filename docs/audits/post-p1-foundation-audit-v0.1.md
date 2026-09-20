# Post-P1 Foundation Audit v0.1

**Started:** 2026-09-20
**Completed:** 2026-09-20
**Issue:** #16
**Status:** COMPLETE AFTER NARROW REOPEN — P0/P1 ownership repaired; P2 unblocked

## Decision

The composed P0/P1 foundation survived the post-P1 red-team with **no schema/interface freeze requiring reopening**.

The audit did find implementation and evidence-handling defects. Those were repaired at the enforcing layer rather than by weakening canonical contracts.

The foundation is ready for controlled P2 expansion, provided P2 remains projection/analytics-first and does not duplicate canonical legal truth.

## What the audit changed

### Concrete implementation defect fixed

**Change Atom language evidence was under-enforced.**

Before the multilingual money adversary, a VERIFIED atom could claim additional languages even when its source spans evidenced only one expression.

The audit added deterministic enforcement in src/needle/semantic/adversary.py:

- every provision-ref language must be inside the atom language scope;
- every language claimed by a VERIFIED atom must have source-span evidence.

Permanent negative regression: the English-only Regulation 2742/90 ECU 225 → ECU 255 corrigendum cannot be globalised to DEU, FRA or all expressions.

This was an implementation gap in enforcement, not a representational failure of Change Atom v0.3. The freeze is retained.

### Source-route failure separated from legal absence

For CELEX:31990R2742R(01) the preferred Publications Office Cellar CELEX route was observed returning 404 while authoritative EUR-Lex HTML and OJ PDF remained available.

Needle now carries the explicit invariant:

ROUTE_UNAVAILABLE_NOT_SOURCE_ABSENT

Pinned legal evidence remains authoritative independently of current endpoint availability.

### Authentic source-internal conflict preserved

Directive 2008/7/EC contains a useful adversary inside one authentic act:

- Article 16 literally prints Directive 69/355/EEC;
- recital 1, Annex II and Annex III identify Directive 69/335/EEC.

Needle must not silently rewrite the authentic Article 16 text.

The adopted handling is:

PRESERVE_LITERAL_AND_RESOLVE_CANONICAL_SEPARATELY

Canonical predecessor resolution may use independent in-act evidence while the literal conflicting source text remains immutable evidence.

### Temporal inheritance across lineage rejected

Directive 69/335/EEC Article 7(2) structurally splits into Directive 2008/7/EC Articles 7 and 8.

The same authentic successor act separately establishes:

- a 31 December 2008 DEADLINE for transposition of Articles 7 and 8;
- predecessor repeal from 1 January 2009;
- an explicit 1 January 2009 APPLICATION set containing Articles 1, 2, 6, 9, 10 and 11 — not Articles 7 or 8.

Therefore Articles 7 and 8 remain APPLICATION = NOT_ASSERTED for that date in this evidence set. Structural succession, repeal chronology and a transposition deadline do not manufacture an application start.

## Discovery Lane result — Half-Life

The audit deliberately spent one cycle on a public-interest capability rather than another defensive fixture.

The temporary ePrivacy derogation history is now live-verified from official Cellar bytes:

- Regulation 2021/1232: application from 2 August 2021, originally planned through 3 August 2024;
- Regulation 2024/1307: extends the first regime through 3 April 2026;
- gap: 4 April through 30 July 2026 — **118 days**;
- Regulation 2026/1881: successor starts 31 July 2026 and currently runs through 3 April 2028.

Derived analytics:

- original planned duration: **1,098 days**;
- extension beyond original planned end: **+608 days**;
- first regime total: **1,706 days**;
- successor duration through current end: **613 days**;
- total applicable time through current successor end: **2,319 of 2,437 calendar days**.

The important architectural result is negative:

> Genealogical succession does not imply uninterrupted applicability.

Half-Life remains fact-first. “Temporary” is a source/legal characterization, not criticism, and proposition-level continuity is not inferred from regime genealogy.

## Adversary cohort

The audit is intentionally not an Article-3-only confidence exercise. Executable evidence now spans:

- Regulation 794/2004 Article 3 — integrated mutation/semantic/temporal/Thread/retrieval anchor;
- Directive 69/335/EEC → Directive 2008/7/EC — one-to-many split plus temporal non-inheritance and source-internal identifier conflict;
- Regulation 2021/1232 → 2024/1307 → 2026/1881 — temporary-regime extension, expiry, gap and reenactment;
- Regulation 2742/90 corrigendum — English-only operative money correction through VERIFIED mutation and Change Atom;
- Digital Services Act — default, provision override and entity-relative application;
- Regulation 794/2004 multilingual corrigenda — disjoint language groups, correction-of-correction and back-projection;
- ESRS delegated act — adoption, scrutiny and publication remain orthogonal;
- 1958 Regulation 1 + modern identifiers — awkward official identity and strict WEMI boundaries;
- Cellar update/feed fixtures — event hints separated from re-observed source truth.

## Audit matrix — final disposition

| Contract | Composed risk tested | Evidence/result | Decision |
| --- | --- | --- | --- |
| **P0-A Provision / rule identity** | branching, genealogy vs semantics/time | one-to-many 69/335 Article 7(2) split; ePrivacy gap; proposition decomposition | **RETAIN** |
| **P0-B Cellar ingestion backbone** | endpoint/representation state mistaken for legal truth | live feed drift; duplicate Formex metadata; historic Cellar 404 with authoritative EUR-Lex fallback | **RETAIN** |
| **P0-C Gold Corpus v0.2** | machine regressions detached from human assertions | Thread Gold linkage plus non-Article-3 money corrigendum Gold case | **RETAIN** |
| **P0-D Canonical AST v0.1** | text accounting mistaken for structural completeness; representation duplication | historical HTML, modern/consolidated Formex, duplicate metadata semantics | **RETAIN** |
| **P0-E Temporal v0.1** | force/application/text/deadline/source-time collapse | DSA context, retroactivity, exclusive boundaries, Half-Life gap, split deadline vs application | **RETAIN** |
| **P0-F Multilingual corrigenda v0.1** | language-scoped corrections globalised downstream | split 2005 groups; correction chain; back-projection; English-only money correction end-to-end | **RETAIN** |
| **P0-G Identifier graph v0.1** | generic same-document reasoning or silent identifier cleanup | WEMI boundaries, historic ELI quirks, 69/355 literal vs 69/335 canonical resolution | **RETAIN** |
| **P0-H Procedure state v0.1** | agreement/adoption/scrutiny/publication/application collapsed | DSA, withdrawn proposal, ESRS delegated act, implementing act | **RETAIN** |
| **P0-I Mutation engine v0.2** | diff/similarity promoted into legal/semantic truth | authentic replacement, authentic corrigendum for/read parser, evidence-backed SPLIT, conflict quarantine | **RETAIN** |
| **P1-A Change Atom v0.3** | language/time/exception scope lost | Article 3 graph plus money-corrigendum language-boundary adversary; enforcement gap fixed | **RETAIN** |
| **P1-B Cellar update detection v0.1** | feed UPDATE treated as legal mutation | RSS/Atom drift, canonical event keys, hash-based source-change classification | **RETAIN** |
| **P1-C Provenance ledger v0.1** | corrections erase history or stale support stays current | append-only supersession plus active-support projection regressions | **RETAIN** |
| **P1-D Structured retrieval v0.1** | index becomes truth; discovery/date/identity collapse | exact-vs-discovery, bitemporal source-as-of, typed aliases, explicit unknowns | **RETAIN** |
| **P1-E Thread v0.1** | chronology duplicates domain truth or hides non-impact/unknowns | reference-only Article 3 Thread, Source Mode closure, Gold chronology | **RETAIN** |

## Durable audit gates

The audit is executable, not just this document.

Core gates:

- tests/test_post_p1_foundation_audit.py
- tests/test_half_life_discovery.py
- tests/test_money_corrigendum_fixture.py
- tests/test_money_corrigendum_semantics.py
- tests/test_gold_money_corrigendum.py
- tests/test_split_temporal_audit.py
- .github/workflows/foundation-audit.yml

Live inspection contracts are kept separate from canonical regression truth:

- .github/workflows/half-life-discovery.yml
- .github/workflows/money-corrigendum-audit.yml
- .github/workflows/split-temporal-audit.yml

Where endpoint state is volatile, push CI validates pinned evidence and deterministic contracts; live endpoint inspection is manual/explicit. Endpoint availability cannot rewrite pinned legal truth.

## Exit criteria

- [x] Every P0/P1 row has an explicit retain/reopen decision.
- [x] More than three non-Article-3 adversary shapes have executable evidence.
- [x] A real cross-contract enforcement defect was found and fixed.
- [x] Useful negative results were retained: genealogy ≠ application continuity; deadline ≠ application; route unavailable ≠ source absent.
- [x] Discovery Lane produced a durable live-evidenced Half-Life fixture and Issue #10.
- [x] Stale duplicate truth exposed during integration was removed or replaced by reference-only composition.
- [x] Gold Corpus gained a non-Article-3 multilingual semantic case.
- [x] P2 is re-ranked from audit evidence.

## P2 risk ordering after the audit

The recommended next sequence is:

1. **Half-Life / Issue #10** — first P2 analytic. It is already backed by live evidence and exercises temporal/regime genealogy without requiring new canonical truth.
2. **Source Anomaly / Issue #17** — provenance-driven view of fallback, source-internal conflict and representation duplication. Keep it read-only over existing truth/provenance.
3. **Legislative X-Ray / dependency ripple** — high upside, but first find a second official case where unchanged text changes practical operation through a changed reference before promoting silent dependency ripple into a reusable public primitive.
4. **Daily/weekly change feed** — update detection and retrieval are now stable enough for a factual feed.
5. **Impact / affected-entity intelligence** — intentionally later because inference risk is materially higher than for the first four slices.
6. Ranking, plain-language evaluation, subscriptions and saved monitors after direct-vs-derived presentation semantics are exercised in public views.

## New P2 discovery

Issue #17 captures a source-layer capability revealed by the audit:

**Source Anomaly** — expose authoritative-source conflicts, unavailable preferred routes, duplicated representations and fallbacks without treating source infrastructure oddities as legal change.

## Final foundation conclusion

P0/P1 is not finished forever; freezes remain reopenable when official evidence demonstrates failure.

But the current baseline has now survived isolated contract tests, one complete Thread, structured retrieval pressure, and a deliberately heterogeneous post-P1 red-team.

**Decision: retain all frozen P0/P1 interfaces and proceed to P2, starting with Half-Life.**


## Addendum — first P2 slice reopened temporal ownership

The first Half-Life implementation pass immediately found one omission in the audit itself: discovery-era regime-lineage v0.1 still persisted application start/end dates, derived gap dates and an applicability-continuity verdict.

That contradicted P0-E's later ownership rule that Temporal Assertions are canonical legal-time truth.

Issue #18 reopened the foundation narrowly.

Resolution:
- regime-lineage v0.1 remains historical discovery provenance only;
- regime-lineage v0.2 is genealogy-only and reference-based;
- canonical ePrivacy dates now live in fixtures/temporal/eprivacy-temporary-regime-v0.1.json;
- the v0.2 genealogy edge references temporal assertion IDs and stores no dates/gap verdict;
- Half-Life regressions derive all metrics from Temporal Assertions;
- changing a temporal assertion changes the derived gap without modifying lineage.

Decision record:
- docs/decisions/regime-lineage-v0.2-temporal-ownership.md

This addendum strengthens, rather than weakens, the audit conclusion:

**Genealogy owns ancestry. P0-E owns legal time. Product analytics own neither; they derive.**
