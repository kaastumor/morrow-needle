# Post-P1 Foundation Audit v0.1

**Started:** 2026-09-20  
**Issue:** #16  
**Status:** ACTIVE — broad P2 remains blocked

## Purpose

This audit red-teams the composed P0/P1 system after the first complete Thread and structured retrieval slice.

It is not a documentation review. A frozen interface is retained only when:

1. its schema distinction survives executable composition;
2. implementation actually enforces the distinction;
3. another subsystem does not silently re-collapse it;
4. negative / unresolved states survive downstream projection;
5. authoritative-source quirks do not require duplicating legal truth.

A freeze is reopened only when evidence demonstrates representational or implementation failure.

## First adversary cohort

The first cohort deliberately avoids relying only on Regulation 794/2004 Article 3:

- **Directive 69/335/EEC → Directive 2008/7/EC** — official one-to-many provision correlation.
- **Regulation 2021/1232 → Regulation 2026/1881** — genealogical continuity across a real applicability gap.
- **Digital Services Act, Regulation 2022/2065** — provision overrides plus provider/event-relative applicability.
- **Regulation 2742/90 English corrigendum** — language-specific operative money correction, ECU 225 → ECU 255.
- **Regulation 794/2004 corrigenda** — disjoint language groups, correction-of-correction and consolidation back-projection.
- **ESRS Delegated Regulation 2023/2772** — adopted while scrutiny remains open and publication remains pending.
- **1958 Regulation 1 + modern EU identifiers** — awkward official ELI and strict WEMI/equivalence boundaries.
- **Cellar ingestion/update adversaries** — feed action versus re-observed source hashes.

The Article 3 Thread remains an integration anchor, not the sole adversary.

## Cross-contract executable gate

tests/test_post_p1_foundation_audit.py

Initial run: **GREEN**.

The gate currently checks:

- structural genealogy does not erase temporal gaps;
- one-to-many structural lineage does not become whole-rule semantic identity;
- language scope survives correction chains;
- a language-specific monetary correction is not globalised;
- current consolidation does not rewrite historical source availability;
- identifier equivalence stops at identity-level boundaries;
- procedure adoption, scrutiny and publication stay orthogonal;
- Cellar feed action remains a hint rather than source-change truth;
- zero unexplained AST text does not imply full structural fidelity;
- superseded provenance remains historical but disappears from the current view;
- every Change Atom temporal reference resolves to a canonical temporal assertion;
- the Thread reference graph resolves and Source Mode closes;
- every Thread Gold machine expectation retains a human assertion.

## Integration defects already exposed before / during this audit

These are evidence that the post-P1 review is necessary.

| Finding | Contract pressure | Resolution |
| --- | --- | --- |
| inclusive=false existed in temporal schema but was ignored by the resolver | P0-E | Implementation fixed; exclusive start/end + mixed-inclusivity conflict regressions added. Freeze retained. |
| Old Thread fixture duplicated semantic/temporal truth and drifted | P1-E / P1-A / P0-E | Duplicate fixture removed; Thread persistence is reference-only. |
| Live source endpoint/interstitial state could be confused with legal truth | P0-B / P1-B / P1-E | Pinned legal evidence separated from availability observations. |
| 2025 Article 3(4) text unchanged while referenced paragraph changed | P0-I / P1-A / P1-E | No textual mutation; derived cross-reference ripple modeled separately. |
| Thread Gold machine IDs initially lacked v0.2 human assertion links | P0-C / P1-E | Fixture aligned to frozen Gold contract; validator not weakened. |
| Search originally lacked complete PKI/SANI temporal lifecycle | P0-E / P1-D | Canonical temporal data repaired first; retrieval then followed canonical refs. |
| Historical source-as-of retrieval lacked official publication assertions | P0-E / P1-D | 2008 and 2025 publication points modeled and provenance-backed. |
| 2025 Formex repeats identical publication metadata in multiple streams | P0-B / P0-D | Consistent duplicate metadata treated as representation duplication; deterministic canonical locator retained. |
| Retrieval support count alone could hide a supersession with equal cardinality | P1-C / P1-D | Active support record IDs added to projection/fingerprint. |
| Broad lexical discovery could be mistaken for exact legal-status retrieval | P1-D | Exact canonical entity selectors separated from broad discovery. |

## Audit matrix

Legend:

- **RETAIN** — current freeze survives composed adversaries.
- **RETAIN / ATTACK NEXT** — no reason to reopen, but a targeted adversary is still high-value.
- **REOPEN** — evidence demonstrates a foundation defect requiring contract change.
- **PENDING** — insufficient audit evidence.

| Contract | Core risk under composition | Current executable evidence | Disposition | Next attack |
| --- | --- | --- | --- | --- |
| **P0-A Provision / rule identity** | Structural succession mistaken for semantic identity; branching lost | 69/335 Article 7(2) one-to-many split; 2021/1232→2026/1881 gap; proposition-decomposition fixtures | **RETAIN** | Compose split/merge with mutation + temporal transition in one case. |
| **P0-B Cellar ingestion backbone** | Representation/availability quirks mutate legal truth | Live feed drift, live Cellar Thread probes, duplicate 2025 Formex metadata | **RETAIN / ATTACK NEXT** | Expression available in one language/representation but unavailable in another. |
| **P0-C Gold Corpus v0.2** | Machine regression becomes detached from human legal assertion | Thread Gold linkage audit + canonical Gold workflow | **RETAIN** | Add one non-Article-3 cross-contract Gold case. |
| **P0-D Canonical AST v0.1** | Zero text loss mistaken for structural completeness; multi-stream duplication double-owned | source-accounting audit + live Formex/HTML contracts | **RETAIN / ATTACK NEXT** | Multi-stream repeated legally relevant content vs harmless repeated metadata. |
| **P0-E Temporal v0.1** | force/application/text state/source time collapse; exclusivity ignored | DSA context, real gap, retroactivity, Article 3 boundary, bitemporal retrieval | **RETAIN** | Temporary regime repeatedly extended/re-enacted: Half-Life Discovery. |
| **P0-F Multilingual corrigenda v0.1** | correction globalised across expressions; later correction back-projected as historical source | English-only ECU 225→255; split 2005 groups; correction chain; back-projection | **RETAIN / ATTACK NEXT** | Carry a language-scoped operative correction through mutation → Change Atom. |
| **P0-G Identifier graph v0.1** | same-document reasoning absorbs expression/manifestation/consolidation/corrigendum | WEMI boundary audit + typed retrieval aliases | **RETAIN** | Test a language-scoped corrigendum identifier through retrieval enrichment. |
| **P0-H Procedure state v0.1** | adoption/agreement/publication/application collapsed | ESRS delegated act, DSA political agreement, withdrawn proposal | **RETAIN** | Compose procedure state with temporal legal effect without adding a catch-all status. |
| **P0-I Mutation engine v0.2** | textual diff promoted to semantics; structural mutation inferred from similarity | verified Article 3, structural lineage reclassification tests, representation-noise tests | **RETAIN / ATTACK NEXT** | Official split/merge plus different application dates. |
| **P1-A Change Atom v0.3** | semantic claim loses language/time/exception scope | Article 3 atom graph; temporal-ref integrity audit | **RETAIN / ATTACK NEXT** | First language-scoped monetary Change Atom from a corrigendum. |
| **P1-B Cellar update detection v0.1** | feed UPDATE treated as legal change; malformed IDs break idempotency | live RSS/Atom drift + source-change hash classification audit | **RETAIN** | Update event where only one expression/manifestation branch changes. |
| **P1-C Provenance ledger v0.1** | correction deletes history or stale support survives projections | ledger validation + supersession/current-view + retrieval active support IDs | **RETAIN** | Retraction/correction propagation into Thread/public rendering. |
| **P1-D Structured retrieval v0.1** | index becomes legal truth; date/discovery/identity scope collapsed | exact-vs-discovery, bitemporal, typed identity, unknowns, active support regressions | **RETAIN** | Multi-Thread retrieval after the audit; no production backend yet. |
| **P1-E Thread v0.1** | chronology duplicates domain truth or hides unknown/non-impact evidence | zero-gap Article 3 Thread + Gold + public renderer + audit dependency checks | **RETAIN / ATTACK NEXT** | Build second Thread from a different legal shape only after audit adversaries clarify reusable gaps. |

## Current reopening decisions

**No frozen schema/interface is reopened by the first composed audit cohort.**

This is a positive result, but not a declaration that P0/P1 is complete. Three high-risk attacks remain before broad P2 work:

1. **language-scoped operative correction → verified mutation → Change Atom**, to prove expression scope survives the whole semantic pipeline;
2. **split/merge + different temporal transition**, to force identity/mutation/time composition outside Article 3;
3. **Discovery Lane: temporary-law Half-Life**, using the 2021/1232 → 2024/1307 → 2026/1881 derogation history to test whether Needle can expose legal gaps/extensions without converting genealogy into uninterrupted validity.

## Creative hypothesis: silent dependency ripple

Article 3 already demonstrated one important class of change:

> A provision can remain textually identical while its practical semantic operation changes because a referenced provision changes.

This should become a candidate public-intelligence primitive, but **not yet a new canonical contract**.

During the audit we will look for a second official-source case. If repeated, open a dedicated P2 issue for a dependency-ripple view backed by explicit reference edges, textual non-mutation evidence and derived semantic character.

## Exit criteria for Issue #16

The audit may close only when:

- every P0/P1 row has an explicit retain/reopen decision;
- at least three non-Article-3 adversary shapes have executable evidence;
- at least one new cross-contract defect or useful negative result is recorded;
- the Discovery Lane produces a durable artifact/issue;
- stale duplicate truth found during the pass is removed;
- the P2 backlog is re-ranked from evidence rather than enthusiasm.
