# Discovery — Corrigenda are expression-scoped and can be back-projected

## Case

Regulation (EC) No 794/2004 provides two independent traps for a document-centric legal-history model.

### 1. Same act, different language mutation histories

On 28 January 2005 EUR-Lex records two distinct corrigenda:

- `32004R0794R(02)`: DA, DE, EN, IT, NL, PT, SV.
- `32004R0794R(03)`: ES, EL, FR, FI.

They do not contain the same correction set.

The second group includes additional corrections such as the act-number title correction, an Annex I introductory-text correction and an Annex III C heading correction.

A language-neutral mutation stream would therefore falsely apply mutations to expressions for which that corrigendum was not published.

### 2. Corrigenda can be back-projected into an earlier consolidated text state

Current EUR-Lex consolidated expressions labelled `02004R0794-20040520` display correction markers and fisheries content sourced from corrigenda published in 2005.

Therefore three clocks must remain distinct:

1. **text-state/checkpoint date** — e.g. 20 May 2004;
2. **corrigendum source/publication date** — e.g. 28 January / 25 May 2005;
3. **observation date** — when Needle retrieved the current generated consolidation.

This is exactly the distinction preserved by the frozen temporal query perspectives.

## Architectural consequences

- Mutation graphs are expression-scoped.
- A Corrigendum Event carries an explicit official language list.
- A non-listed language means `NO_ASSERTION`, not “confirmed unaffected”.
- A corrigendum-of-corrigendum keeps its correction chain.
- Source availability filtering and ex-post text-state reconstruction are different operations.
- Consolidated version labels must never be used as historical source-availability timestamps.

## Current implementation

- `schemas/language-scoped-mutation-v0.1.schema.json`
- `src/needle/multilingual/mutations.py`
- `fixtures/multilingual/reg794-2004-corrigenda-language-scope-v0.1.json`
- `fixtures/multilingual/reg794-2004-consolidation-backprojection-v0.1.json`
- `tests/test_multilingual_corrigenda.py`
