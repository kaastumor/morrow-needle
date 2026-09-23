# Discovery — a crisis solidarity rule hidden inside an older permanent regulation

**Date:** 2026-09-23  
**Lane:** Discovery  
**Issue:** #75  
**Status:** High-value bounded finding; no new architecture required

## The question

Can a temporary emergency rule become permanent without living on in either its
emergency act **or** a clean new successor regime?

Yes.

The gas-solidarity rules introduced by Council Regulation (EU) 2022/2576 are a
particularly clean legal fossil because their permanent descendants are now
embedded inside **Regulation (EU) 2017/1938** — a legal instrument that predates
the 2022 crisis.

That means a reader looking only at today's consolidated permanent host can see
the rule while missing the historical reason it exists.

## 1. The temporary workaround

Regulation 2022/2576 explicitly established temporary measures for a gas
emergency.

Articles 27 and 28 supplied default solidarity machinery where Member States had
not concluded the bilateral technical, legal and financial arrangements
anticipated by Regulation 2017/1938.

The package supplied, among other things:

- a default trigger when no solidarity agreement exists;
- compensation categories;
- a day-ahead gas-price benchmark;
- refusal grounds;
- a standard request payload;
- request, response and confirmation timing.

Regulation 2023/2919 prolonged the temporary act through **31 December 2024**.

Official sources:

- https://eur-lex.europa.eu/eli/reg/2022/2576/oj
- https://eur-lex.europa.eu/eli/reg/2023/2919/oj

## 2. The legislature says the crisis measure is becoming permanent

Regulation 2024/1789 Recital 111 is unusually useful genealogy evidence.

It says that certain provisions build on the crisis measures introduced by
Regulation 2022/2576 and that the new Regulation aims to transform some of
those crisis measures into **permanent features**.

The recital specifically includes additional solidarity measures in a natural
gas emergency.

This is not ancestry inferred from similar wording.

It is ancestry stated by the legislature.

## 3. But the permanent destination is an older host

The permanent rule does not simply become “Article X of Regulation 2024/1789.”

Article 84(9) of Regulation 2024/1789 **amends Regulation 2017/1938** and inserts
new paragraphs into its Article 13.

So the identity chain is:

```
temporary source rule
Reg. 2022/2576 Arts 27-28
          │
          │ direct genealogy
          ▼
amending instrument
Reg. 2024/1789 Art. 84(9)
          │
          │ inserts / rewrites
          ▼
permanent canonical host
Reg. 2017/1938 Art. 13(8a)-(8c)
```

This is a different persistence shape from AggregateEU.

AggregateEU gave us a temporary regime transformed into a successor permanent
regime. Here, emergency logic is **grafted back into a pre-crisis framework**.

That distinction matters for provenance and identity:

- the 2024 act explains and performs the amendment;
- the resulting permanent rule belongs to the amended 2017 act;
- the 2022 crisis act is the genealogical ancestor.

## 4. This is not a copy-paste transplant

The resemblance between temporary Article 27/28 and permanent Article
13(8a)/(8b) is unmistakable.

The permanent text keeps the core machinery:

- the no-bilateral-agreement trigger;
- the same main compensation categories;
- the same core day-ahead market-price hierarchy;
- the same main solidarity-request information.

But it also changes the machinery.

### Request timing

Temporary Article 28:

- request at least **72 hours** before delivery;
- response within **24 hours**.

Permanent Article 13(8b):

- request at least **48 hours** before delivery;
- response effective within **18 hours**.

### Confirmation timing

The temporary package used a different confirmation formulation.

The permanent rule requires confirmation within **six hours of receipt of the
offer** and at least 24 hours before the indicated delivery time.

### Compensation controls

The temporary rule placed a default 100% gas-price cap on specified indirect
costs, with a Commission route for higher compensation.

The permanent paragraph 8a keeps indirect costs as a compensation category but
does not reproduce that default cap.

And permanent Article 13(8c) adds an **ex-post control** layer involving the
national regulatory authorities and, where needed, ACER.

So the correct relation is:

> **direct genealogy + substantive mutation**

not:

> same rule, copied permanently.

## 5. The handoff is calendar-contiguous

The temporal choreography is clean:

- temporary Regulation 2022/2576 applies through **31 December 2024**;
- Regulation 2024/1789 Article 89(2)(a) makes Article 84 apply from
  **1 January 2025**.

For this EU-level directly applicable handoff, there is no calendar gap between
the temporary solidarity package and the permanent amendment.

That is useful contrast with the renewables-permitting discovery in Issue #74,
where a Directive transposition deadline could not safely be promoted into a
Member-State application-start fact.

## 6. Why this is a real “legal fossil”

A present-day reader can open consolidated Regulation 2017/1938 and find
Article 13(8a)-(8c) as ordinary permanent security-of-supply law.

The text itself does not, by its current location alone, communicate:

1. that the default mechanism was trialled as temporary crisis law in 2022;
2. that the 2024 legislature explicitly described the solidarity measures as
   crisis measures being made permanent;
3. which parts survived;
4. which parts were rewritten during the transplant.

That history is distributed across three instruments and time.

This is exactly the kind of ancestry that a current-text-only legal information
view tends to flatten.

## Discovery result

We now have three genuinely different crisis-to-permanent patterns in the same
broad 2022 energy-crisis family:

| Pattern | Example | Shape |
|---|---|---|
| successor-regime metamorphosis | AggregateEU | temporary regime -> permanent successor, operational brand crosses boundary |
| selective proposition survival | renewables permitting | one emergency act -> different rule fates |
| permanent graft into older host | gas solidarity | temporary rules -> amended/mutated insertion into pre-crisis permanent framework |

The third pattern is especially valuable because “current legal location” and
“historical origin” point in opposite chronological directions: the permanent
host is older than the crisis ancestor of the inserted rule.

## Architectural disposition

**SURVIVES.**

No new schema is necessary if Needle keeps these separate:

- canonical current rule identity;
- amending instrument;
- rule genealogy;
- temporal application;
- substantive mutation.

The case is a regression against several attractive but false shortcuts:

- amendment act = canonical current rule identity;
- direct genealogy = verbatim copy;
- permanentisation = continued validity of the temporary act;
- current consolidated location = sufficient history.

## Pinned regression

- `fixtures/lineage/reg2022-2576-solidarity-to-reg2017-1938-art13-v0.1.json`
- `tests/test_gas_solidarity_permanent_graft.py`

## Follow-up deliberately not promoted

Regulation 2024/1789 Recital 111 also identifies LNG/storage measures as crisis
features being made permanent. That may contain yet another identity pattern,
but this run stops here rather than manufacturing a family of issues.
