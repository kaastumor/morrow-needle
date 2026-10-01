# #492 first diverse-law development tranche — 1 October 2026

Status: **TRANCHE_01_PASS — expectations were frozen before replay; the exact engine/projection replay passed on the review head. WP4 is next after this checkpoint is accepted.**

Canonical input: `0d876b4f66c3c4b5c8b5ada80adab6f6ad164acf` (merged #504).

This is the first actual structurally diverse tranche required by #492. Earlier search,
source-passage and multilingual experiments remain exposed mechanism/regression evidence;
they explicitly did not complete this campaign.

## Selection rule

The three cases were selected for the assumption they can falsify, not for sector count.
They deliberately mix an EU directive with later national implementation, an amended
regulation with provision-specific staged application, and an implementing decision whose
future operation must not be collapsed into its current legal state.

No case in this tranche becomes a maintained public act page or a frozen scientific-corpus
case by being tested here.

## Frozen cases and expected behavior

| Case | Structural pressure | Frozen expected behavior | Misleading / wrong result |
| --- | --- | --- | --- |
| D1 — NIS2 / Netherlands | Directive transposition; EU deadline vs national in-force state | Keep Directive (EU) 2022/2555 identity and its 17 Oct 2024 transposition deadline / 18 Oct 2024 EU measure-application requirement separate from the Dutch Cyberbeveiligingswet, which entered into force on 15 Aug 2026. A Netherlands-oriented answer must identify the national source/date rather than present the directive deadline as the Dutch effective date | “NIS2 became directly applicable in the Netherlands on 18 Oct 2024”; using an old Commission transposition-status snapshot as the current Dutch legal state |
| D2 — AI Act after Digital Omnibus | Regulation with staggered application; later act mutates the timetable | Resolve current Article 113 against Regulation (EU) 2026/1744 / the current consolidated state. Preserve multiple application dates and the amendment identity; do not silently reuse the original 2024 timetable | Showing the original high-risk dates as current after the 2026 amendment; flattening all provisions into one “effective from” date |
| D3 — LVD harmonised-standard withdrawal | Implementing decision already in force with a future operation on a dynamic OJ-reference set | For EN 60335-2-60:2003 at the frozen 26 Sep 2026 view: current OJ state remains **CITED** / presumption available within covered scope, while the already-fixed next event is withdrawal on 18 Jan 2027 | Treating adoption/publication of Decision (EU) 2025/1457 as immediate withdrawal; hiding the fixed future transition; saying loss of OJ reference means the underlying standard ceases to exist |

The expectations above were fixed before the repository product-path inspection below.

## Primary / official source observations

### D1 — NIS2 and Dutch implementation

- Directive (EU) 2022/2555 is the NIS2 Directive:
  <https://eur-lex.europa.eu/eli/dir/2022/2555/oj/eng>
- EUR-Lex records that the directive had to be transposed by **17 October 2024** and
  the measures were to apply from **18 October 2024**:
  <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=LEGISSUM:4637829>
- The Dutch government records that the **Cyberbeveiligingswet entered into force on
  15 August 2026**, implements NIS2 in the Netherlands and replaced the Wbni:
  <https://www.rijksoverheid.nl/actueel/nieuws/2026/08/15/cyberbeveiligingswet-en-wet-weerbaarheid-kritieke-entiteiten-vanaf-vandaag-van-kracht>
- NCSC independently states the same 15 August 2026 in-force date:
  <https://www.ncsc.nl/cyberbeveiligingswet-nis2>

**Pressure exposed:** a directive page cannot have one undifferentiated “applies from”
date when the user asks about a particular Member State. EU transposition duty, national
measure identity, national entry into force and user-specific applicability are distinct.

### D2 — AI Act current timetable after 2026 amendment

- Regulation (EU) 2026/1744 is an in-force amending regulation:
  <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744>
- Its amendment to Article 113 changes the staged application timetable, including
  **2 December 2027** for Article 6(2)/Annex III high-risk systems and
  **2 August 2028** for Article 6(1)/Annex I high-risk systems, and adds
  **27 July 2026** for Articles 102–110.
- The current consolidated AI Act is source/version sensitive:
  <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727>

**Pressure exposed:** “the AI Act applies from 2 August 2026” is insufficient as a
single product status. The current explanation needs provision-specific dates, amendment
lineage and the source version that owns the answer.

### D3 — LVD / EN 60335-2-60

- Commission Implementing Decision (EU) 2025/1457:
  <https://eur-lex.europa.eu/eli/dec_impl/2025/1457/oj/eng>
- Article 2 makes the Decision effective on publication while point (1) of the Annex
  applies from **18 January 2027**.
- The existing canonical Needle fixture
  `fixtures/dependency/lvd-en60335-2-60-scheduled-withdrawal-v0.1.json`
  represents the member as INCLUDED/ACTIVE before that date and NOT_INCLUDED/WITHDRAWN
  after it.

**Pressure exposed:** current status and already-fixed future state must be visible at the
same time without treating a future transition as current law.

## Available product-path inspection at `0d876b4f66c3c4b5c8b5ada80adab6f6ad164acf`

### Home captured-source search

The merged #504 search is intentionally a four-source English medical-guidance collection.

Repository inspection of:
- `mvp/product-home/search/index.json`
- `mvp/product-home/search/medical-engine.js`
- `mvp/product-home/search/app.js`

shows:

- the captured index contains neither `2022/2555` nor `2024/1689`;
- it contains no NIS2 or AI-Act source material;
- the product wrapper requires an explicit medical-device anchor before any lexical
  `RESULTS` response can be exposed.

Therefore D1 and D2 are **outside declared maintained coverage** on this revision. That is
a legitimate safety result, not evidence that Needle can explain them.

Disposition for D1/D2 on this slice:

> **SAFE_LIMIT at the repository contract layer; exact UI/runtime output NOT_TESTED here.**

A later executable replay must confirm that representative ordinary and exact-reference
queries do not substitute a medical-device result. It must not add these laws to the public
catalogue merely to make the test pass.

### Candidate-B known-standard path

The existing Candidate-B route already owns D3:

- `mvp/candidate-b/app.js` includes `EN 60335-2-60:2003`;
- its supported window includes the frozen 26 Sep 2026 view;
- the canonical fixture records one future `REMOVE_MEMBER` transition effective
  18 Jan 2027;
- the projection contract distinguishes current `CITED` state from the next fixed event.

Disposition for D3:

> **STRUCTURAL PASS on canonical fixture/projection inspection; rendered runtime replay NOT_EXECUTED in this slice.**

This preserves #416 as exposed regression evidence rather than pretending D3 is a fresh
independent validation case.

## What this tranche changes

The first diversity matrix establishes three reusable content/representation requirements
for the next M1 work:

1. **jurisdiction-specific implementation state cannot be inherited from an EU directive date;**
2. **temporal summaries must be version/amendment aware and may require multiple provision-specific dates;**
3. **current and already-fixed future state must coexist without collapsing into one status.**

These are constraints on WP4/WP5 design, not authorization to build a national-law engine,
a general temporal ontology or live monitoring.

## Remaining execution before WP4

Run a narrow exact-revision replay of the current product paths:

1. ordinary + exact-reference NIS2 query → no medical substitution; outside/no-result state
   is explicit;
2. ordinary + exact-reference AI Act query → no medical substitution; outside/no-result
   state is explicit;
3. Candidate-B `EN 60335-2-60:2003` at 26 Sep 2026 → current cited state plus
   18 Jan 2027 future withdrawal.

Record exact output/status and browser/runtime evidence if available. A failure is a
product-boundary defect and should be repaired minimally on the same WIP. A pass closes
this first WP2 tranche and unlocks WP4 substantive MDR/IVDR views under the three
requirements above.

The sponsor has separately accepted the remaining #504 200% zoom/no-script/remote-preview
limits; do not reopen those unrelated checks during this replay.

## Boundaries retained

- no public NIS2 or AI Act page from this test alone;
- no reserved #492 case consumed;
- no all-EU-law or all-language quality claim;
- no personalised applicability conclusion;
- no frozen-corpus change;
- no #493/#494/Candidate A/C activation;
- no outreach, recruitment, paid service, release or deployment.
