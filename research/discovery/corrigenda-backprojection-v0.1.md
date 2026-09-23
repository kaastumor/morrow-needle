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


## Independent confirmation — Regulation 2025/905 corrigendum (2026)

A second, temporally distant case now confirms the same source-state trap.

For Regulation (EC) No 794/2004 Article 4(1):

1. authentic Implementing Regulation (EU) 2025/905, published 13 June 2025,
   printed “existing aid that is authorised…”;
2. corrigendum `32025R0905R(01)`, published 17 July 2026, explicitly replaces
   that wording with “existing aid scheme that is authorised…”;
3. the currently served EUR-Lex consolidation labelled
   `02004R0794-20250813` displays the corrected “aid scheme” wording and marks
   the sentence with correction marker C4.

The current consolidation is therefore a valid witness for an **ex-post
corrected historical text state**, but its 13 August 2025 label is not proof
that the corrected wording was available from official sources on that date.

This does not add a new semantic rule. It independently confirms the frozen
P0-F invariant established by the 2004/2005 back-projection case:

> consolidated text-state date, corrigendum publication/source-availability
> date, and observation date are separate clocks.

Pinned regression:
`fixtures/audit/reg794-2025-corrigendum-backprojection-v0.1.json`.

Official sources checked 2026-09-23:

- https://eur-lex.europa.eu/eli/reg_impl/2025/905/oj/eng
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R0905R(01)
- https://eur-lex.europa.eu/eli/reg/2004/794


## Language asymmetry follow-up — Dutch was not corrected by the 2026 event

The 17 July 2026 corrigendum to Implementing Regulation 2025/905 is officially
published for:

BG, ES, DA, DE, EL, EN, FR, GA, HR, IT, LV, MT, RO and SK.

Dutch is not listed.

The authentic Dutch 2025/905 publication nevertheless already replaces
Regulation 794/2004 Article 4(1) with wording containing
`bestaande steunregeling` (“existing aid scheme”), while the authentic English
2025 text used “existing aid” and the 2026 English corrigendum changes that to
“existing aid scheme”.

This produces a useful three-part distinction:

1. **ENG:** the 2026 corrigendum directly evidences a textual mutation.
2. **NLD:** the corrigendum contributes **NO_ASSERTION** because Dutch is not in
   its official expression scope.
3. **Independent NLD source state:** the authentic Dutch 2025 publication
   already evidences the scheme concept before the 2026 corrigendum.

The third fact does not convert the second into a Dutch corrigendum event, and it
does not establish unrestricted cross-language semantic equivalence.

This is a confirmation of the frozen P0-F expression-scope contract with a
stronger multilingual asymmetry: different expressions can arrive at similar
legal concepts through different textual histories.

Pinned regression:
`fixtures/audit/reg2025-905-corrigendum-nonlisted-nld-v0.1.json`.

Official sources checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/NL/ALL/?uri=OJ:L_202500905
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32025R0905R(01)
