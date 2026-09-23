# Discovery — EU law can make a private rating legally relevant

**Date:** 2026-09-23  
**Issue:** #85  
**Status:** first private-origin failure pinned; no architecture change

## The uncomfortable assumption

Needle's non-textual causal contracts mostly assume that direct legally relevant
truth originates in:

- an EU institution;
- an EU agency;
- a Member State authority;
- another official authority/control system.

Credit ratings show that this is too narrow.

EU law can deliberately make a private actor's determination an input to a
regulatory calculation without transforming that actor into a public authority.

## Concrete event

On **20 February 2025**, S&P Global Ratings lowered the issuer credit rating of
**Capri Holdings Ltd.** from **BBB-** to **BB**.

This is direct private-source truth.

It is not an EU act and it does not mutate EU legal text.

## Recognition chain

The CRR does not accept arbitrary internet ratings.

Article 135 limits standardized-approach use to assessments issued or endorsed
by an ECAI under the EU credit-rating framework.

Implementing Regulation (EU) 2016/1799 maps the S&P long-term scale:

- BBB band -> credit quality step 3;
- BB band -> credit quality step 4.

The current CRR corporate-exposure table maps:

- CQS 3 -> 75% risk weight;
- CQS 4 -> 100% risk weight.

So the abstract legal chain is:

```
private S&P determination
BBB- -> BB
        |
        v
EU recognition as usable ECAI assessment
        |
        v
EU mapping
CQS 3 -> CQS 4
        |
        v
conditional CRR output
75% -> 100%
```

## The conditionality is essential

This fixture does **not** assert that a particular bank's Capri exposure changed
risk weight.

CRR use depends on institution-specific conditions, including nomination/use of
the relevant ECAI and applicability of the assessment to the exposure.

The only safe derived statement is:

> if the CRR use conditions are satisfied for a corporate exposure, this rating
> transition crosses the CQS 3/4 boundary that maps to 75%/100%.

That distinction is a useful adversary in its own right.

## Existing contracts

### Source Observation v0.1 — fails vocabulary

The direct source is S&P itself.

Source Observation only accepts official/public systems.

Calling the S&P page `OTHER_OFFICIAL` would erase the exact provenance fact we
need to preserve.

### Authoritative Finding v0.1 — semantically close, authority model wrong

A credit rating is plausibly a categorical determination.

But the schema permits only public/official authority types and source
characters.

Adding `OTHER_OFFICIAL_AUTHORITY` would be false.

### Authoritative Metric Observation — wrong value type

BBB- and BB are ordinal classifications, not numeric metrics.

### Authoritative Dynamic Set — wrong causal shape

The issuer is not being added to or removed from an authoritative set.

## What may actually be missing

The temptation is to invent:

`PRIVATE_AUTHORITATIVE_FINDING`.

That may be the wrong layer.

The deeper issue appears to be that Needle currently collapses two different
questions:

1. **who originated the determination?**
2. **why is that determination legally eligible to matter?**

For S&P:

- originator = private rating agency;
- legal-recognition basis = EU ECAI framework + CRR mapping.

Those should remain separate.

Before changing any schema, Issue #85 requires an orthogonal second domain such
as notified-body conformity assessment, accredited verification or another
recognized private-control regime.

If the second case has the same structure, the repair should probably address
recognition/authority provenance rather than invent another domain object.
