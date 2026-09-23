# Discovery — selective survival of emergency renewables permitting rules

**Date:** 2026-09-23  
**Lane:** Discovery  
**Issue:** #74  
**Status:** High-value bounded finding; no new architecture required

## The question

What happens when an emergency regulation does **not** have one clean successor?

Council Regulation (EU) 2022/2577 was explicitly temporary emergency law. Its
renewables-permitting rules were adopted to accelerate deployment during the
energy crisis.

The later handoff into the permanent RED III framework is not act-to-act
replacement. It is selective at rule level.

That makes this case more useful than another whole-regime
“temporary becomes permanent” example: **different propositions from the same
temporary instrument have different legal afterlives.**

## 1. The permanent framework arrives before the emergency instrument is gone

Directive (EU) 2023/2413 amends Directive 2018/2001 with a long-term permitting
framework, including new Articles 16a-16f.

For selected permitting provisions, Member States were required to transpose the
Directive by **1 July 2024**, immediately after the emergency Regulation's
original end on **30 June 2024**.

Regulation (EU) 2024/223 explains the architecture directly:

- some measures introduced by Regulation 2022/2577 were included in the
  permanent Directive 2018/2001 framework through Directive 2023/2413;
- some more exceptional emergency measures were **not** mirrored in the
  permanent framework, preserving their temporary character.

That is already enough to reject an act-level shortcut such as:

> Regulation 2022/2577 -> Directive 2023/2413 = one successor relation.

The correct unit of comparison is the rule/proposition.

Official sources:

- https://eur-lex.europa.eu/eli/reg/2022/2577/oj
- https://eur-lex.europa.eu/eli/dir/2023/2413/oj
- https://eur-lex.europa.eu/eli/reg/2024/223/oj

## 2. Fate A — explicit promotion into permanent law

The cleanest case is Regulation 2022/2577 Article 3(1).

The emergency rule establishes a presumption that renewable-energy plants,
their grid connections, the related grid and storage assets are of overriding
public interest and serve public health and safety for specified environmental
balancing tests.

Permanent RED III inserts Article 16f into Directive 2018/2001 with the same
core presumption.

The strongest evidence is not textual resemblance. The Commission's proposal
for the emergency extension, COM(2023) 763 final, says explicitly that it does
**not** propose prolonging Article 3(1) because the same presumption is contained
in Directive 2023/2413.

This is unusually strong rule-genealogy evidence:

```
temporary Article 3(1)
        │
        │ official statement: not prolonged because same presumption is now in RED III
        ▼
permanent Article 16f
```

Classification: **PROMOTED_TO_PERMANENT / DIRECT**.

Sources:

- COM(2023) 763 final
- Regulation (EU) 2024/223
- Directive (EU) 2023/2413, Article 16f as inserted into Directive 2018/2001

## 3. Fate B — emergency rule kept alive beside the permanent regime

Article 5(1), concerning repowering permitting, does not follow the same path.

Regulation 2024/223 prolongs the emergency rule in narrowed scope while the
permanent RED III permitting deadlines apply elsewhere.

That is not promotion. It is **bounded coexistence**:

```
permanent RED III regime  ─────────────────────────────►
                         ╲
emergency Article 5(1)    └── narrowed temporary tail ──●
```

The legal system is deliberately using two related rule families at once for
different scopes.

Classification:
**TEMPORARY_COEXISTENCE_WITH_PERMANENT_REGIME / DIRECT**.

## 4. Fate C — a temporary bridge while the permanent machinery is built

Article 6 is even more revealing.

The final extension Regulation says that the emergency Article 6 approach and
the permanent RED III renewables-acceleration-area framework **can and should
coexist for a limited period**.

The reason is temporal and administrative: setting up the permanent
acceleration areas takes longer, so the emergency mechanism remains available
during the handoff.

This is a legal bridge, not a permanent transplant.

Classification:
**TEMPORARY_BRIDGE_ALONGSIDE_PERMANENT_REGIME / DIRECT**.

This also demonstrates a useful distinction:

- genealogical relationship can be clear;
- semantic identity can still be false;
- temporal overlap can be intentional.

## 5. Fate D — plausible descendants that remain deliberately weaker claims

Emergency Article 4 (solar) and Article 7 (heat pumps) have close permanent
analogues in RED III Articles 16d and 16e.

The resemblance is substantial: the subject matter, accelerated permitting
logic and several time/capacity thresholds line up.

But this discovery did not find the provision-specific official statement that
makes Article 3(1) unusually strong.

So Needle should **not** launder textual similarity into direct genealogy.

Classification:
**TEXTUALLY_CLOSE_PERMANENT_ANALOGUE / DERIVED**.

That negative discipline is part of the result.

## 6. The temporal trap: 1 July 2024 is not a national application fact

The handoff is designed to look almost seamless at EU legislative level:

- emergency Regulation original end: 30 June 2024;
- selected RED III transposition deadline: 1 July 2024.

It is tempting to draw a continuous line.

Needle must not.

A directive's transposition deadline is not itself evidence that every Member
State had the permanent rule in force and applicable on that date. Establishing
domestic continuity would require Member-State implementation evidence.

So this discovery records:

**national application continuity = UNRESOLVED without national evidence.**

That preserves an existing Needle invariant exposed by earlier adversarial work:
a transposition deadline is not an application start.

## 7. The rule-fate map

| Emergency rule | Later state | Evidence strength | Fate |
|---|---|---|---|
| Art. 3(1) overriding-public-interest presumption | RED III Art. 16f | Direct official bridge | Promoted into permanent law |
| Art. 5(1) repowering | Emergency tail + permanent regime in other scopes | Direct final-regulation explanation | Temporary coexistence |
| Art. 6 designated-area/environmental mechanism | Emergency bridge beside acceleration areas | Direct final-regulation explanation | Temporary bridge |
| Art. 4 solar | RED III Art. 16d | Text comparison + general bridge context | Derived permanent analogue |
| Art. 7 heat pumps | RED III Art. 16e | Text comparison + general bridge context | Derived permanent analogue |

## Discovery result

The interesting object is not “Regulation 2022/2577 survived.”

It did not survive as one thing.

Instead, the crisis instrument behaved like an **incubator of rules** whose
individual propositions were sorted into different long-term states:

- promoted into ordinary permanent law;
- kept temporarily alive beside that law;
- used as a bridge until permanent machinery could operate;
- or left as only a plausible analogue unless stronger genealogy is found.

This is a materially different persistence pattern from AggregateEU, where a
temporary legal regime is explicitly transformed into a permanent successor
mechanism with a carefully engineered handoff.

## Why this matters for Needle

The current architecture survives if we keep lineage proposition-granular.

The case reinforces four existing rules:

1. legal genealogy does not imply legal identity;
2. whole-act succession can hide divergent rule fates;
3. similarity is candidate evidence, not sufficient proof of direct ancestry;
4. transposition deadlines do not become application dates by convenience.

No new schema is justified.

## Pinned regression

- `fixtures/lineage/reg2022-2577-to-dir2023-2413-rule-fates-v0.1.json`
- `tests/test_renewables_emergency_rule_fates.py`

## Follow-up deliberately not promoted

The same 2022 energy-crisis cluster contains other promising fossils. In
particular, default gas-solidarity rules from Regulation 2022/2576 appear to
have been inserted later into the permanent Security of Gas Supply framework.

That is a different persistence shape — an emergency workaround embedded into
an older standing regulation — and is worth remembering as a future discovery
candidate, but this run does not create a queue from it.
