# #492 / #511 — M2 development campaign, D1-D8

Date: 1 October 2026  
Programme: WP6 / M2  
Canonical input: `b443f770d90a30dd412b4bab0cf82b1543e1e1f1`

Status: **DEVELOPMENT_SET_EXECUTED — contrast candidate earned; held-back WP7 cases untouched**

## Method

Eight development cases are used to pressure different assumptions. D1-D3 were already
frozen and accepted in tranche 01. D4-D5 are ordinary positive controls from the accepted
medical journey. D6-D8 are new source-backed structures selected before replay.

Search safety and detail-contract generalisation are scored separately. Safe abstention is
not evidence that Needle can explain an out-of-coverage act.

## Development matrix

| Case | Pressure | Current-path result | Detail-contract result | Disposition |
| --- | --- | --- | --- | --- |
| D1 NIS2 -> Dutch Cyberbeveiligingswet | EU directive vs national implementation date | PASS / safe boundary | constraint retained | accepted regression |
| D2 AI Act after 2026/1744 | amended provision-specific dates | PASS / safe boundary | constraint retained | accepted regression |
| D3 LVD future OJ-reference withdrawal | current vs fixed future state | PASS | represented temporal control PASS | accepted regression |
| D4 exact IVDR `2017/746` | positive exact-identity control | `REFERENCE_MENTIONS_ONLY` + IVDR internal route | represented act detail available | PASS |
| D5 ordinary EUDAMED timing | positive ordinary-query control | `RESULTS`, 5 cards, bounded overview continuation | represented medical journey available | PASS |
| D6 Implementing Decision 2026/1323 | explicit addressees + limited authentic languages | `REFERENCE_NOT_IN_SNAPSHOT`; no internal route | **CONTRACT_BREAK if medical template reused** | SAFE_LIMIT + explicit narrowing |
| D7 Delegated Regulation 2026/1022 | subordinate/amending act, EUR 150 threshold, split dates, voluntary early use | exact ref `REFERENCE_NOT_IN_SNAPSHOT`; ordinary query `NO_SUPPORTED_TERMS` | **PARTIAL_FIT**; time/relationship model useful, medical role template not reusable verbatim | contrast candidate |
| D8 Corrigendum 2025/90725 to 2024/2956 | correction/version event, table/code corrections | `REFERENCE_NOT_IN_SNAPSHOT`; no internal route | **CONTRACT_BREAK if treated as standalone core act** | SAFE_LIMIT + explicit correction-event narrowing |

## D4-D8 exact replay on canonical input

- D4 `2017/746` -> `REFERENCE_MENTIONS_ONLY`, two source locator cards,
  deterministic `/medical-devices/ivdr/` continuation.
- D5 “EUDAMED is mandatory now: does that include all six modules?” -> `RESULTS`,
  five source cards and bounded `/medical-devices/` continuation.
- D6 `2026/1323` and ordinary addressee wording -> `REFERENCE_NOT_IN_SNAPSHOT`.
- D7 `2026/1022` -> `REFERENCE_NOT_IN_SNAPSHOT`; ordinary customs/timing wording ->
  `NO_SUPPORTED_TERMS`.
- D8 `2025/90725` and ordinary corrigendum wording -> `REFERENCE_NOT_IN_SNAPSHOT`.

No D6-D8 output substitutes medical evidence or invents a nearby represented act.

## Source-backed pressure findings

### D6 — Implementing Decision (EU) 2026/1323

Official source:
<https://eur-lex.europa.eu/eli/dec_impl/2026/1323/oj/eng>

The decision excludes specified EAGF/EAFRD expenditure from Union financing. Article 2
addresses it only to Bulgaria, Denmark, Greece, France, Italy, Latvia, Hungary, Poland,
Portugal, Romania and Slovakia. EUR-Lex also states that only the Bulgarian, Danish,
French, Greek, Hungarian, Italian, Latvian, Polish, Portuguese, Romanian and Slovak texts
are authentic.

**Break:** the current medical act renderer presents an “Economic-operator orientation”
role section and a general-application field. Reusing that template here would invent the
wrong audience model and obscure authentic-language status.

**Scope decision:** `mvp/medical-act-detail/` remains a medical core-regulation contract,
not a universal EU-instrument template. D6 does not earn a public page in WP6.

### D7 — Delegated Regulation (EU) 2026/1022

Official source:
<https://eur-lex.europa.eu/eli/reg_del/2026/1022/oj/eng>

The act amends Delegated Regulation (EU) 2015/2446 for the temporary EUR 3 customs duty on
distance sales of imported consignments with intrinsic value not exceeding EUR 150.
Article 2 applies the regulation from 1 July 2026, while point (2)(a)-(b) of the Annex
applies from 1 November 2026; operators may voluntarily provide those data from 1 July.

**Pressure:** one “applies from” badge would be materially incomplete. The act is also
subordinate/amending rather than a standalone core regime, and the EUR 150 threshold is a
scope condition.

**Disposition:** this is the strongest candidate for WP6's at-most-one public contrast.
It can reuse the accepted product shell, evidence/version/date discipline and typed
relationships without pretending the medical role contract is universal.

### D8 — Corrigendum 2025/90725

Official source:
<https://eur-lex.europa.eu/eli/reg_impl/2024/2956/corrigendum/2025-09-19/oj/eng>

The corrigendum repairs specific table/code content in Implementing Regulation (EU)
2024/2956, including B_05.01.0020 code instructions, a B_05.01.0090 cross-reference and a
B_06.01.0060 code reference.

**Break:** treating this as a standalone “core act” with its own purpose/roles/application
page would be false. It is a correction event attached to another legal resource/version.

**Scope decision:** corrigenda belong in source/version/change history where supported.
D8 does not earn a standalone public page in WP6.

## Generalisation result after D1-D8

What generalises:
- exact identity must precede internal routing;
- evidence/source/version boundaries;
- typed temporal events rather than one status date;
- typed legal relationships;
- current vs fixed-future distinction;
- explicit unsupported/outside-coverage state.

What does **not** generalise from the medical template:
- economic-operator roles as a universal audience model;
- a required single general-application field;
- treating every legal resource as a standalone core act;
- assuming all language versions share the same authenticity status.

## Repair / narrowing decision

No search repair is justified by D6-D8: current fail-closed behavior is correct for the
declared medical source set.

The proportional representation repair is **narrowing**, not a universal schema:
`mvp/medical-act-detail/` is medical-core-regulation-specific.

WP6 may now implement **one** separate bounded contrast for D7. It should reuse only the
parts actually shown to generalise: product shell, evidence/version panel, typed dates,
typed relationships, explicit scope/thresholds and official handoffs. It must not create a
generic legal-instrument framework.

## Held-back cases

WP7's four reserved cases remain unselected and unexposed. No repair decision in this note
uses them.


## D7 bounded public contrast — implemented

WP6 earned exactly one maintained contrast route:

> `/customs-low-value-imports/`

The page is intentionally separate from `mvp/medical-act-detail/`. It reuses only the
conventions that survived D1-D8:

- source/version identity;
- explicit scope/threshold limits;
- typed temporal events;
- typed legal relationships;
- language-scoped correction visibility;
- nearby official-source handoffs;
- explicit non-applicability/non-compliance boundaries.

It does **not** introduce a universal act renderer or generic EU-law ontology.

### D7 temporal representation

The public contrast preserves the following distinct events:

- 30 Apr 2026 — adoption;
- 1 Jul 2026 — Official Journal publication and the date Article 2 states the Regulation
  applies from;
- 2 Jul 2026 — entry into force, as the day following publication;
- from 1 Jul 2026 — voluntary early provision of the data in Annex point (2)(a)-(b);
- 4 Aug 2026 — later corrigendum affecting German and Dutch, explicitly not English;
- 1 Nov 2026 — Annex point (2)(a)-(b) application.

The ordering is left explicit rather than normalized into a single “effective date”.

### Product placement

The home route links this as **M2 contrast example**, separately from the medical overview
and known-standard tool. Copy states that it is one bounded example, not comprehensive
customs coverage.

The page does not calculate customs owed, determine a user's declaration route, or imply
that the delegated amendment is the whole Union customs regime.

### Verification

Final review candidate head:
`485e0be0af564b5f754316fca908667cf968dba5`.

- D1-D8 development results preserved.
- D6-D8 exact/ordinary search controls remain fail-closed.
- D4/D5 positive controls remain in the existing suite.
- Customs contrast focused tests are included in the normal Node workflow.
- Unit tests run `36881125338`: **SUCCESS**.
- Repository sanitation run `36881125392`: **SUCCESS**.
- Vercel deployment `dpl_Au4Mm3QrMnkcT1GTWuJZvSyfsSJW`: **READY**.
- A rendered `/customs-low-value-imports/` route was observed on the immediately preceding
  page-identical preview; later branch changes touched only test source.
- Normal CI static-build step completed successfully on the final head.

The four WP7 held-back cases remain unselected and unexposed.

## WP6 disposition

**READY_FOR_SPONSOR_REVIEW.**

The development campaign supports a bounded generalisation claim:

> Needle's evidence/version/typed-time/typed-relationship discipline transfers beyond the
> medical example, but instrument-specific audience/scope/change semantics must remain
> instrument-specific.

It does not support a universal EU-instrument template, general customs coverage, complete
EU-law search, all-language quality or external/user value.
