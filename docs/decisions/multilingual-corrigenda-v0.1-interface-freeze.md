# Decision — Freeze Multilingual Corrigendum Semantics v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #6

## Decision

Freeze the language-scoped mutation foundation around:

- `schemas/language-scoped-mutation-v0.1.schema.json`
- `src/needle/multilingual/mutations.py`

Mutation history is expression-scoped. A legal act does not have one universal textual mutation stream that can be applied blindly to every language expression.

## Stable v0.1 rules

### Language scope is explicit
Every language-scoped mutation event carries the official expression/language scope supplied by the source.

A language not listed by the event means:

`NO_ASSERTION`

It does **not** mean:
- the expression was definitely correct;
- the expression was unaffected by every other correction;
- or the correction should be globalized.

### Corrigenda are first-class mutation events
They are not metadata notes attached to an otherwise language-neutral act.

### Corrigenda may correct corrigenda
Correction chains are preserved explicitly. A correction-of-corrigendum can target the prior correction instruction while still changing the resulting text-state reconstruction.

### Source time and text-state time are separate
Corrigendum publication date is a source-availability date.

It must not be reused as the legal text-state/checkpoint date.

Current EUR-Lex consolidations demonstrate that later corrigenda may be back-projected into an earlier labelled consolidated text state.

### Change Atoms inherit expression scope
A mutation derived only from a language-scoped correction may not become a language-neutral semantic change unless independent evidence establishes the same legal change across the other expressions.

## Adversaries passed in CI

### Regulation 794/2004 — split language groups
On 28 January 2005 two distinct corrigenda cover different language groups:

- `32004R0794R(02)`: DA, DE, EN, IT, NL, PT, SV.
- `32004R0794R(03)`: ES, EL, FR, FI.

The correction sets differ materially.

The second group includes corrections absent from the first group, including:
- the act number in the title;
- Annex I introductory text;
- Annex III C heading.

Both groups also include fisheries-related corrections.

A language-neutral mutation stream would therefore produce false expression states.

### Corrigendum of corrigenda
`32004R0794R(04)`, 25 May 2005, corrects the January placement instruction across the combined language set.

The correction chain remains explicit rather than being flattened.

### Consolidation backprojection
Current consolidated expressions labelled `02004R0794-20040520` already contain correction markers/content sourced from 2005 corrigenda.

Therefore:
- text-state/checkpoint date;
- source-publication date;
- and Needle observation date

are three different clocks.

This is compatible with the frozen temporal query perspectives:
- `EX_POST_LEGAL_EFFECT`
- `OFFICIAL_SOURCE_STATE_AS_OF`

### English-only operative monetary correction
Corrigendum `31990R2742R(01)` is officially scoped to English and changes Article 4(1) from ECU 225 to ECU 255.

This proves that globalizing a language-specific corrigendum can alter an operative monetary rule, not merely headings or annex formatting.

## Durable invariants

1. Every source text state is language-expression scoped.
2. Corrigendum language scope is evidence and must survive the pipeline.
3. Non-listed language = no assertion from that corrigendum.
4. Corrigendum chains remain explicit.
5. Source availability time and corrected text-state time are separate.
6. Consolidated checkpoints are expression-specific documentary witnesses.
7. Language-specific legal mutations cannot silently become universal Change Atoms.
8. Cross-language equivalence is something to establish, never assume.

## Post-freeze rule

A new language/source case should normally extend:
- fixtures;
- expression adapters;
- correction-chain handling;
- or cross-language alignment.

Reopen the core contract only if an official source demonstrates a mutation-scope phenomenon that cannot be represented through explicit expression scope and correction ancestry.

P0-F no longer blocks downstream work.
