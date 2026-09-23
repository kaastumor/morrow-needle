# Issue #97 — latent-detection candidate discovery

**Date:** 2026-09-23  
**Status:** CASE SELECTION + CUE AUDIT + SEAL COMPLETE / NO ARM RUNS  
**Gate:** `docs/evaluations/needle-latent-detection-v0.1.md`

## Firewall statement

No R or M investigator run was executed, simulated or previewed while selecting
these cases.

Candidates were assessed only for:

- fresh-case independence;
- official/public evidence sufficiency;
- a falsifiable consequential failure;
- plausible ordinary-task shape;
- latent-prompt cue risk;
- overlap with already exposed Needle cases.

No candidate was retained because a baseline was observed to fail it.

## Selected adversarial cases

### LD-A1 — EU–Chile parallel agreement lifecycle

**Trap class:** `PARALLEL_INSTRUMENT_LIFECYCLE`  
**Status:** ACCEPT  
**Freshness:** not present in the corpus or prior value-gate case packets.

Official evidence:

- Notice 2025/67: the EU–Chile Interim Agreement on Trade (ITA) entered into
  force on **1 February 2025**.
- The Council treaty record for the Advanced Framework Agreement (AFA) records
  partial provisional application between the EU and Chile from
  **1 June 2025** and shows Member-State ratifications still separately tracked.
- EU material describes the ITA and AFA as parallel legal instruments; the ITA
  expires when the AFA enters into force.

Decisive hidden distinction:

> “The modernised EU–Chile agreement” is not one legal identity with one
> lifecycle date. ITA entry into force on 1 February 2025 cannot be inherited as
> full AFA entry into force.

Consequential wrong answer:

- reporting 1 February 2025 as the entry-into-force date of the full AFA.

Ordinary task shape:

- update a short briefing giving the current legal status/date of the
  “modernised EU–Chile agreement” after finding a 1 February 2025 effective
  date.

Cue-risk audit:

- **PASS if** the final investigator question does not name ITA/AFA identity
  conflation, “parallel instruments,” provisional application, or replacement
  as the issue to watch.
- It may naturally contain the umbrella phrase used in ordinary briefings.

Sources:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22025X00067
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22024A02953
- https://www.consilium.europa.eu/en/documents/treaties-agreements/agreement/?docLanguage=en&id=2023027

---

### LD-A2 — EN 50434 garden shredder restriction

**Trap class:** `DYNAMIC_REFERENCE_STATUS`  
**Status:** ACCEPT  
**Freshness:** not present in the corpus or prior value-gate case packets.

Official evidence:

Commission Implementing Decision (EU) 2026/80 keeps EN 50434:2014 in the
harmonised-standard reference system but inserts a restriction for machines
where the shredding means can rotate above **300 r/min**. For that scope, the
standard does not confer a presumption of conformity with the specified
Machinery Directive essential health and safety requirements.

Decisive hidden distinction:

> A harmonised standard can remain listed while a product-specific or
> clause/requirement-specific restriction removes part of its presumption of
> conformity.

Consequential wrong answer:

- treating the mere presence of EN 50434:2014 in the OJ reference list as proof
  of the relevant presumption for a shredder above the restricted speed.

Ordinary task shape:

- review whether a mains-operated garden shredder using EN 50434:2014 and a
  specified rotor/shredding speed can rely on the standard for its conformity
  position.

Cue-risk audit:

- **PASS if** the final question gives the real product/standard/speed facts but
  does not use the words “restriction,” “restricted presumption,” or instruct
  the investigator to inspect row 622a.

Source:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202600080

---

### LD-A3 — Delegated Regulation 2026/305 historical source state

**Trap class:** `SOURCE_STATE_BACKPROJECTION`  
**Status:** ACCEPT  
**Freshness:** not present in the corpus or prior value-gate case packets.

Official evidence:

- Delegated Regulation (EU) 2026/305 was published on 6 February 2026.
- Corrigendum 2026/90289 was published on **21 April 2026** for a specified
  language set including English and Dutch.
- In English Table 2 it corrected, among other text, `PLN OTC ORD` to
  `PLN OTC IRD`.
- The currently served consolidation labelled
  `02026R0305-20260206` incorporates the corrected wording despite its nominal
  6 February version date.

Decisive hidden distinction:

> A present consolidated representation labelled with the original publication
> date is not proof of what the official source visibly contained on that date.

Consequential wrong answer:

- using today's 6-February-labelled consolidation to state that the original
  February English publication already said `PLN OTC IRD`.

Ordinary task shape:

- reconstruct the February 2026 Table 2 wording for an archive/audit after
  finding the current consolidated text labelled 6 February 2026.

Cue-risk audit:

- **PASS if** the final question asks for the historical wording in an ordinary
  archive/compliance context and mentions the document the user found, but does
  not mention the April corrigendum, back-projection, source-state terminology,
  or ask separately for “then” versus “now”.

Sources:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R0305R(01)
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:02026R0305-20260206

---

### LD-A4 — Dutch food-information Article 25(2) corrigendum

**Trap class:** `LANGUAGE_SCOPE_ASYMMETRY`  
**Status:** ACCEPT  
**Freshness:** not present in the corpus or prior value-gate case packets.

Official evidence:

A Dutch-only corrigendum to Regulation (EU) 1169/2011, published on
**21 July 2026**, corrects Article 25(2):

- old Dutch: `uiterste consumptiedatum`;
- corrected Dutch: `consumptietermijn`.

The English authentic expression uses “time limit for consumption.”

The corrigendum metadata is scoped to **NL**; it is not a correction of the
English expression.

Decisive hidden distinction:

> A historical Dutch wording that appears substantively narrower/different
> cannot be generalised into a Union-wide rule or reconciled by silently
> substituting another authentic language; the later Dutch-only correction is a
> language-expression event.

Consequential wrong answer:

- treating the old Dutch phrase as proof that Article 25(2) imposed a
  Netherlands/Dutch-expression “use-by date” requirement that the Union rule in
  other authentic languages also contained.

Ordinary task shape:

- answer a food-label compliance question where a Dutch team quotes the older
  Dutch wording and an English team quotes “time limit for consumption,” asking
  which wording to use in a current policy.

Cue-risk audit:

- **PASS if** the question presents the two pieces of source text as ordinary
  conflicting material but does not reveal that a Dutch-only corrigendum exists
  or instruct the investigator to compare corrigendum language scope.

Sources:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32011R1169R(26)
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32011R1169

---

### LD-A5 — Haringvliet / Leenheerenpolder judicial invalidity

**Trap class:** `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`  
**Status:** ACCEPT WITH HISTORICAL-FRAMING GUARD  
**Freshness:** not present in the corpus or prior Issue #86/#88 gate packets.

Official evidence:

- Commission Implementing Decision (EU) 2015/72's eighth Atlantic-region list
  omitted the Leenheerenpolder from the Haringvliet site.
- In C-281/16, judgment of 19 October 2017, the Court of Justice held Decision
  2015/72 **invalid insofar as** Haringvliet (NL1000015) was placed on that list
  without inclusion of the Leenheerenpolder.

Decisive hidden distinction:

> Reconstructing the legal significance of a historical Commission list from
> the list text alone can miss a later judicial invalidity holding directed at
> exactly that listing.

Consequential wrong answer:

- a 2026 legal-history memo presenting the 2015 exclusion as an unqualified
  valid EU-law position without identifying the later CJEU invalidity.

Ordinary task shape:

- prepare a 2026 legal-history note on what the 2015 Haringvliet listing did
  with the Leenheerenpolder, using Decision 2015/72 as the starting source.

Cue-risk audit:

- **PASS if** the final question does not mention litigation, validity,
  C-281/16, or ask whether a court later changed the result.
- The answer key must avoid requiring a broader claim about every retrospective
  consequence not necessary to identify the invalidity.

Sources:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015D0072
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:62016CJ0281

---

### LD-A6 — Temu VLOP designation versus additional-obligation start

**Trap class:** `STATUS_APPLICATION_SEPARATION`  
**Status:** ACCEPT  
**Freshness:** Temu is not an exposed Needle case; the class itself is already
known from other services.

Official evidence:

- Commission designated Temu as a VLOP on **31 May 2024**.
- The designation notice says Temu had four months after notification to comply
  with the most stringent VLOP rules.
- Later Commission material states the VLOP-specific risk-assessment obligation
  applied to Temu as of **3 October 2024**.
- DSA Article 33(6) states that Section 5 obligations apply four months after
  notification to the provider.

Decisive hidden distinction:

> designation status and the start of the additional VLOP obligations are
> separate legal states.

Consequential wrong answer:

- saying that Temu's Section 5/VLOP-specific obligations all began on
  31 May 2024 merely because that was the designation date.

Ordinary task shape:

- complete a compliance timeline for Temu around summer 2024 and identify which
  DSA obligations applied at a specified date shortly after designation.

Cue-risk audit:

- **PASS if** the final question does not say “distinguish designation from
  applicability,” does not mention the four-month rule, and does not supply the
  October answer.
- It may naturally state the known designation date.

Sources:

- https://digital-strategy.ec.europa.eu/en/news/commission-designates-temu-very-large-online-platform-under-digital-services-act
- https://digital-strategy.ec.europa.eu/en/news/commission-requests-information-under-digital-services-act-temu-traders-selling-illegal-products
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2065

## Selected negative controls

### LD-N1 — NIS2 transposition deadline

**Status:** ACCEPT CONTROL

Straightforward source proposition:

Directive (EU) 2022/2555 Article 41(1) requires Member States to adopt and
publish transposition measures by **17 October 2024** and apply them from
**18 October 2024**.

Ordinary task shape:

- answer what deadline Article 41 set for adoption/publication and when those
  measures were to apply.

Why control rather than adversary:

- the primary provision states both dates directly;
- no competing instrument, corrigendum, hidden external state or later
  determination is needed to answer the task as scoped.

Source:

- https://eur-lex.europa.eu/eli/dir/2022/2555/oj

### LD-N2 — GDPR general application date

**Status:** ACCEPT CONTROL

Straightforward source proposition:

GDPR Article 99(2) states that the Regulation applies from
**25 May 2018**. Article 99(1) separately provides entry into force on the
twentieth day after OJ publication.

Ordinary task shape:

- answer when the GDPR started applying.

Why control rather than adversary:

- the task asks the application date directly;
- the primary provision states that date expressly;
- noting the distinct entry-into-force date is permissible but not necessary to
  rescue a hidden trap.

Source:

- https://eur-lex.europa.eu/eli/reg/2016/679/

## Rejected / deferred candidates

### Schrems II / Decision 2016/1250 — REJECT: prior gate exposure

The case is legally suitable for `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`, but
Issue #86 already used `schrems-ii-transfer-mechanisms` as a fixed value-gate
case packet.

It is therefore not fresh enough for #97 even though it is not currently a
public corpus entry.

### Booking.com May-2024 designation — REJECT: wrong legal regime candidate

A preliminary candidate conflated Booking's 13 May 2024 **DMA gatekeeper**
designation with DSA VLOP designation. Booking.com had already been designated
under the DSA in April 2023.

The candidate is rejected rather than repaired into a different task.

### Romania NIS2 tracker lag — REJECT: no observed lag

The current Commission Romania NIS2 country page says **Transposed**. It does
not instantiate the tracker-lag mechanism seen in the Netherlands/Sweden cases.

### Organic control-body certificate — DEFER: insufficiently concrete

EU organic rules clearly recognise legally relevant certificates issued through
control-authority/control-body machinery, but discovery did not yet pin a
specific fresh private-origin determination whose exact legal consequence would
support an objective #97 answer key.

Do not promote an abstract architecture-shaped example into the gate merely to
fill a class.

### Maritime recognised organisation — DEFER: insufficient concrete event

Directive 2009/15/EC establishes a legal framework for organisations entrusted
with ship inspection/survey/certification, but no sufficiently clean fresh
determination/event was pinned during this discovery pass.

## Selection summary

Selected:

- 6 adversarial cases;
- 6 distinct trap classes;
- 2 negative controls;
- 8 total cases;
- 0 arm runs.

Adversarial class coverage:

1. `PARALLEL_INSTRUMENT_LIFECYCLE`
2. `DYNAMIC_REFERENCE_STATUS`
3. `SOURCE_STATE_BACKPROJECTION`
4. `LANGUAGE_SCOPE_ASYMMETRY`
5. `JUDICIAL_VALIDITY_TEXT_DIVERGENCE`
6. `STATUS_APPLICATION_SEPARATION`

The selection intentionally includes cases that may be easy for a strong
baseline. Difficulty was not an admission criterion.

## Next gate step

Before sealing:

1. write exact eight investigator questions **outside investigator context**;
2. write exact answer keys;
3. perform a cue audit against the exact six adversarial questions;
4. reject/rewrite any question that names its hidden distinction;
5. freeze R and M instructions;
6. commit only cryptographic commitments + execution manifest.

No investigator run is permitted before those steps complete.


## Sealing completed

The exact eight question packet and exact answer-key packet were frozen after
the cue audit and before any R/M investigator request.

Public commitments:

- prompt packet SHA-256:
  `1956a2a99d0fedbcede162d7763a881f7b9af9e490b9def68c59f5804a54df17`;
- answer-key packet SHA-256:
  `dee28d2c9f3f77342923f09afc34e04f5cacb5ea3a3ac2aadbdda1b17cbaae61`;
- public manifest:
  `fixtures/value-gates/issue97-sealed-manifest-v0.1.json`.

The manifest also pins:

- exact case/run order;
- per-question commitments;
- per-answer-key-fragment commitments;
- R/M base-instruction commitments;
- all 16 full prompt commitments;
- `gpt-5.6-sol` / high reasoning / web search / `store=false` /
  stateless execution;
- the six adversarial cue-audit verdicts.

### Pre-execution manifest bookkeeping repair

The first public-manifest commit
(`5dad65fad23e0865d0a650c15e3e49eb6d686ca4`) contained an incorrect manual
transcription of 12 derived per-run prompt hashes.

The whole prompt-packet and answer-key commitments were already correct.

Before any investigator response existed, commit
`43f95b5bcf6da5b4b8795abd540ab30c9c63c1fd` replaced only that derived hash
table with hashes recomputed from the unchanged sealed prompt packet and added
an explicit repair record.

This does not constitute a re-seal: no scientific input bytes changed.

## Execution readiness

The gate is now ready for the external execution boundary.

Do not alter prompts, keys, arm instructions, case order or scientific settings.
Any scientific-input change requires a new gate version and new commitments.
