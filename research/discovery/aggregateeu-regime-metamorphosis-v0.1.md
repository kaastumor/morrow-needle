# Discovery — AggregateEU: emergency instrument to permanent market mechanism

**Date:** 2026-09-23  
**Lane:** Discovery  
**Status:** High-value research finding; no new architecture required

## The question

Can an emergency legal mechanism become permanent while its operational service
name survives the change of legal basis?

**Yes. AggregateEU is a clean official-source example.**

The case is useful because four different continuities overlap:

1. legal-regime genealogy;
2. legal applicability;
3. service/brand operation;
4. platform/product-shell implementation.

Treating those as one identity produces a false history.

## 1. Temporary emergency origin

Council Regulation (EU) 2022/2576 was adopted during the gas-supply crisis.

Article 1 expressly says it establishes **temporary rules**, including expedited
demand aggregation and joint gas purchasing.

Article 31 originally limited the Regulation to one year.

Council Regulation (EU) 2023/2919 then prolonged it, but remained equally
explicit that the regime was temporary. It changed Article 31 so that
Regulation 2022/2576 applied only until **31 December 2024**.

Official sources:

- https://eur-lex.europa.eu/eli/reg/2022/2576/oj
- https://eur-lex.europa.eu/eli/reg/2023/2919/oj

## 2. The legislature explicitly turns crisis machinery into permanence

Regulation (EU) 2024/1789 is unusually explicit about genealogy.

Recital 111 says that some measures introduced by Regulation 2022/2576 as
crisis measures are to be transformed into **permanent features of the natural
gas market**.

It specifically includes:

- demand aggregation and joint purchasing;
- measures concerning LNG facilities and gas storage;
- additional solidarity measures.

For demand aggregation, Articles 42–51 create the permanent mechanism.

This is not an inferred resemblance. The successor act itself identifies the
temporary predecessor and states the transformation.

Official source:

- https://eur-lex.europa.eu/eli/reg/2024/1789/oj

## 3. The transition deliberately separates preparation from substantive use

The timing is more interesting than a simple replacement.

Regulation 2024/1789 Article 89 provides:

- preparatory Articles 42, 43 and 44 apply from **4 August 2024**;
- the rest of Section 5 applies from **1 January 2025**.

Recital 111 explains why:

- preparatory work, including service-provider tendering, needed to begin before
  the emergency instrument expired;
- the substantive permanent provisions were delayed to avoid overlap with the
  temporary 2022/2576 regime;
- the permanent mechanism was intended to be operational when the temporary
  Regulation expired.

So the temporal shape is:

```
temporary substantive regime
───────────────────────────────● 31 Dec 2024
             permanent preparation starts
             ● 4 Aug 2024 ────────────────┐
                                           │
permanent substantive regime               ● 1 Jan 2025 ─────────────►
```

This produces:

- **preparatory overlap**;
- **no substantive calendar gap**.

The current Temporal + Regime Lineage contracts represent this directly:
genealogy references the relevant boundaries but does not own them.

## 4. AggregateEU the service survives the legal-basis change

This is the best identity adversary in the case.

AggregateEU continued to operate visibly in March 2025.

PRISMA's Terms and Conditions dated 7 March 2025 state that:

- PRISMA offers the **AggregateEU** service on behalf of DG ENER;
- PRISMA is the service provider selected pursuant to Article 43 of
  Regulation 2024/1789;
- “AggregateEU” means services implementing Articles 42–51 of Regulation
  2024/1789;
- legacy declarations referring to Regulation 2022/2576 are to be read as
  references to corresponding provisions of Regulation 2024/1789.

The Commission then ran another AggregateEU mid-term matching round in March
2025 under this successor environment.

Sources:

- https://www.prisma-capacity.eu/aggregateeu-gtcs
- https://energy.ec.europa.eu/news/joint-gas-purchasing-very-good-results-2nd-mid-term-demand-aggregation-round-natural-gas-2025-03-26_en

Therefore:

> **The visible service identity “AggregateEU” crossed the legal-regime
> boundary.**

A source history that groups by service name would wrongly imply one continuous
legal basis.

## 5. The later platform shell is another identity again

The Commission launched the **EU Energy and Raw Materials Platform** in July
2025.

It explicitly says the platform builds on experience from AggregateEU, and
hosts a broader family of mechanisms spanning energy and raw materials.

That makes it genealogically related at implementation/platform level, but it
is not simply the same legal object as:

- Regulation 2022/2576;
- the permanent Articles 42–51 regime;
- or the AggregateEU service brand.

Official source:

- https://energy.ec.europa.eu/topics/energy-security/eu-energy-and-raw-materials-platform_en

## Discovery result

The case establishes four independent questions:

| Layer | Finding |
|---|---|
| Legal genealogy | Temporary crisis demand aggregation is directly superseded by a permanent demand-aggregation regime |
| Substantive applicability | Continuous: temporary regime ends 31 Dec 2024; permanent substantive regime starts 1 Jan 2025 |
| Transition/preparation | Overlapping: permanent setup provisions begin 4 Aug 2024 |
| Service identity | AggregateEU brand/service survives into the permanent legal basis |
| Platform identity | Later EU Energy & Raw Materials Platform is a broader successor shell, not the same legal identity |

## Why this matters for Needle

This falsifies a very tempting shortcut:

> **same operational name = same legal regime**

It also shows the reverse shortcut is unsafe:

> **new legal instrument = operational discontinuity**

Neither is true here.

The case supports the existing separation between:

- legal identity;
- genealogy;
- legal time;
- operational/source identity.

It does **not** require a new Regime Lineage schema.

## Architectural disposition

**SURVIVES.**

Regime Lineage v0.2 + Temporal v0.1 can represent the legal transition without
owning duplicate dates.

The operational history belongs in discovery/audit evidence rather than being
promoted into canonical legal-regime identity.

This is a stronger validation of Regime Lineage than the earlier ePrivacy case:
the legislature itself states that temporary crisis measures are being
transformed into permanent features, and deliberately engineers the handoff.

## Pinned regressions

- `fixtures/temporal/aggregateeu-regime-transition-v0.1.json`
- `fixtures/lineage/reg2022-2576-to-reg2024-1789-aggregateeu-v0.1.json`
- `fixtures/discovery/aggregateeu-operational-afterlife-v0.1.json`
- `tests/test_aggregateeu_regime_metamorphosis.py`

## Follow-up question deliberately not promoted

The same Regulation says other emergency-era measures — LNG/storage access and
solidarity measures — were also transformed into permanent market features.

That may be worth a later comparative discovery run, but this run does not
manufacture a queue from it.
