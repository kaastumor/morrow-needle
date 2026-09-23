# Parallel international-agreement identity and lifecycle — discovery memo

**Issue:** #91  
**Research cutoff:** 2026-09-23  
**Status:** CONFIRMED TWO-CASE FAILURE FAMILY

## Research question

Can an umbrella political/negotiation label safely be represented as one legal
instrument with one lifecycle state when the negotiated outcome is implemented
through a comprehensive agreement plus a separate interim trade agreement?

The answer from the two fresh 2026 cases below is **no**.

The legally safe unit is the individual agreement, with signature, provisional
application, conclusion, entry into force and replacement/cessation attached to
that agreement rather than inherited from the umbrella label.

## Case A — EU–Mercosur

### Distinct instruments

Council Decision (EU) 2026/183 records that the negotiations produced two
parallel legal instruments:

1. the EU–Mercosur Partnership Agreement (EMPA), containing political,
   cooperation, trade and investment components;
2. the Interim Agreement on Trade (ITA), covering the trade/investment material
   that can proceed through the EU-only route.

The two texts have separate CELEX identities:

- ITA: `22026A00184`;
- EMPA: `22026A00186`.

They were both signed on 17 January 2026.

### ITA state

OJ Notice 2026/868 states that the EU, Argentina, Brazil, Paraguay and Uruguay
completed the procedures necessary for **provisional application** of the ITA.

The notice states that the ITA is provisionally applied from **1 May 2026**
between the EU and each of those four states respectively.

Commission and Council current explanatory material consistently describes the
ITA as applying provisionally from that date.

### EMPA state

The EMPA is a separate mixed agreement. Current EUR-Lex metadata for
`22026A00186` records:

> Date of entry into force unknown (pending notification) or not yet in force.

Council Decision (EU) 2026/185 authorises provisional application only of
specified EMPA provisions, pending full entry into force and subject to the
Agreement's notification conditions. Article 2(2) of that Decision requires the
date of any such provisional application to be published in the Official
Journal.

The decisive point here does not require proving whether any subset of EMPA has
subsequently begun provisional application. **Provisional application of the
separate ITA on 1 May cannot be turned into full entry into force of the EMPA.**

### Replacement relation

Current Commission/Council material states that the standalone ITA will cease
to have effect when the EMPA enters into force.

That replacement relation itself proves why the instruments cannot share a
single state: at one point the ITA may be applicable while the EMPA is not yet
fully in force, and later EMPA entry into force terminates the interim
instrument.

### Consequentially unsafe statement

> "The EU–Mercosur Partnership Agreement entered into force on 1 May 2026."

This is unsafe. The official 1 May event is provisional application of the
separate ITA. The EMPA is a distinct agreement and current EUR-Lex does not
record it as having entered into force.

## Case B — EU–Mexico

### Distinct instruments

The Commission and Council likewise identify two parallel legal instruments:

1. the Political, Economic and Cooperation Strategic Partnership Agreement,
   commonly called the Modernised Global Agreement (MGA);
2. the EU–Mexico Interim Agreement on Trade (ITA).

Separate CELEX identities:

- ITA: `22026A01528`;
- MGA: `22026A01509`.

Both were signed on 22 May 2026.

### EU ITA conclusion is not entry into force

The European Parliament consented to the ITA in July 2026. On 14 July the
Council adopted the decision formally concluding the ITA for the EU and stated
that this completed the **EU's internal process**.

The same Council notice then states the remaining treaty condition:

- the ITA enters into force on the first day of the second month after the EU
  and Mexico notify each other that their respective internal procedures are
  complete.

Current EUR-Lex metadata for `22026A01528` still records:

> Date of entry into force unknown (pending notification) or not yet in force.

So a Council conclusion decision is not itself proof that the agreement has
entered into force internationally.

### MGA remains a different lifecycle

Current EUR-Lex metadata for `22026A01509` likewise records entry into force
as unknown/pending notification or not yet in force.

The comprehensive MGA requires the broader mixed-agreement ratification path.
The ITA functions as a standalone interim agreement and will cease to apply
when the full MGA enters into force.

### Consequentially unsafe statement

> "The Council formally concluded the modernised EU–Mexico agreement in July
> 2026, so the full modernised agreement is now in force."

This collapses at least three distinct facts:

- EU internal conclusion of the ITA;
- international entry into force of the ITA;
- entry into force of the separate MGA.

## Cross-case failure mechanism

Both cases support a common failure family:

### PARALLEL_INSTRUMENT_LIFECYCLE

An umbrella negotiation or political label is implemented through legally
distinct interim and comprehensive agreements. Lifecycle facts — signature,
provisional application, conclusion, entry into force and
replacement/cessation — belong to the specific instrument.

Unsafe inferences include:

- trade preferences started -> the comprehensive agreement entered into force;
- Council conclusion -> international entry into force;
- state of the interim agreement -> state of the comprehensive agreement;
- umbrella label -> one canonical legal identity;
- future replacement relation -> present identity equivalence.

This family is related to but distinct from
`STATUS_APPLICATION_SEPARATION`. That older class concerns different temporal
states/effects inside or downstream of a legal status. Here the additional
failure is **identity substitution between separate legal instruments**.

Two counterparties with different current states support treating this as a
corpus class rather than a one-off observation.

## Source-role notes

The decisive sources are official:

### Mercosur

- Council Decision (EU) 2026/183 — signing/provisional application of ITA;
- Council Decision (EU) 2026/185 — signing/provisional application authority
  for specified EMPA provisions;
- OJ Notice 2026/868 — ITA provisional application from 1 May 2026;
- EUR-Lex `22026A00184` — ITA identity;
- EUR-Lex `22026A00186` — EMPA identity/current entry-into-force metadata;
- Council, *EU-Mercosur agreements explained* — standalone/replacement
  relationship.

### Mexico

- Council, 14 July 2026, *EU-Mexico: Council gives final approval to modernised
  trade agreement* — EU internal conclusion and remaining reciprocal
  notification condition;
- EUR-Lex `22026A01528` — ITA identity/current entry-into-force metadata;
- EUR-Lex `22026A01509` — MGA identity/current entry-into-force metadata;
- Council Decision (EU) 2026/1742 — EU conclusion of ITA;
- Commission, *EU trade relations with Mexico* — parallel-instrument and
  replacement relationship.

## URLs

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026D0183
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026D0185
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026X00868
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026A00184
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026A00186
- https://www.consilium.europa.eu/en/policies/eu-mercosur-agreements-explained/
- https://www.consilium.europa.eu/en/press/press-releases/2026/07/14/eu-mexico-council-gives-final-approval-to-modernised-trade-agreement/
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026A01528
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:22026A01509
- https://eur-lex.europa.eu/eli/dec/2026/1742/oj
- https://policy.trade.ec.europa.eu/eu-trade-relationships-country-and-region/countries-and-regions/mexico_en

## Architectural conclusion

No new legal-state schema is earned.

The project is now a corpus/protocol project, and the existing finding can be
preserved directly as two corpus adversaries with one shared trap class.

If a future concrete task needs machine persistence of treaty lifecycle state,
that task must independently earn it.
