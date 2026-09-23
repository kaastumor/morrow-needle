# Discovery — a private notified body can change certificate state

**Date:** 2026-09-23  
**Issue:** #85  
**Status:** second orthogonal private-origin proof pinned

## Why this is a better second case

The first Issue #85 specimen uses a private credit-rating agency.

That could still be dismissed as a peculiar financial-regulation mapping.

Medical-device conformity assessment removes nearly every domain-specific
feature of the first case.

## Concrete event

A field safety notice hosted by Swissmedic records that **SZUTEST Uygunluk
Değerlendirme A.Ş., Notified Body 2195** informed BIOTRH s.r.o. on
**23 March 2023** that its CE certificate had been suspended.

The same notice records that SZUTEST sent the manufacturer a decision on
**2 May 2023** withdrawing the certificates.

The manufacturer expressly disputed the grounds and appealed.

That disagreement is useful:

> legal relevance of the certificate-status decision does not depend on the
> manufacturer agreeing with the private assessor.

## Public-law recognition

At the relevant time, Directive 93/42/EEC Article 16 provided the legal role.

Member States designate bodies for specified conformity-assessment tasks.

The Directive also required notified bodies to communicate certificate
suspension/withdrawal and, where relevant requirements were no longer met, to
suspend or withdraw the certificate unless corrective measures restored
compliance.

The direct determination therefore originates with a private conformity
assessment company but matters because EU law has placed that body inside a
bounded recognition/delegation framework.

## Downstream events remain separate

The notice also records:

- no European sales since the suspension date, according to the notified body's
  requirements;
- a later competent-authority call for corrective action;
- a manufacturer recall/withdrawal of remaining supply.

Those are not one event.

Needle must not compress:

```
private certificate suspension/withdrawal
          |
          +--> manufacturer market behavior
          |
          +--> later competent-authority action
          |
          +--> field safety corrective action
```

into a single generic enforcement status.

## Cross-domain result

The S&P/Capri and SZUTEST/BIOTRH cases now share a real architectural pattern.

### S&P

```
private rating agency
        ↓
private ordinal determination
        ↓
EU ECAI recognition + mapping
        ↓
conditional prudential input
```

### SZUTEST

```
private notified body
        ↓
private certificate-status decision
        ↓
EU notified-body recognition/delegation
        ↓
conformity/market consequences
```

The commonality is not the determination payload.

It is the **recognition relationship**.

## Architecture direction

Do not merely add:

`LEGALLY_RECOGNIZED_PRIVATE_ACTOR`

to every authority enum.

That would still mix:

- source origin;
- public-law recognition;
- determination semantics.

The repair should keep those separate.

The likely minimum is:

1. make source observation capable of preserving non-official primary sources
   without pretending they are official;
2. add one bounded recognition-basis object that explains why a non-public
   actor/output is legally eligible to matter;
3. add a narrow private/external determination owner only if necessary to
   preserve the direct semantic state.

Do not build a universal actor graph, accreditation platform or conformity
engine.
