# Comparative value audit — 2026-09-23

Status: **COMPLETE — Issue #49 verdict: REDIRECT**

Parent: #49

## Question

Does Needle's evidence/legal-state discipline produce materially more correct,
inspectable or usefully uncertain understanding of difficult EU legal change
than the strong simpler baseline defined in `docs/project-charter.md`?

The baseline is deliberately strong:

1. EUR-Lex / other official EU relationships and metadata;
2. a mature change/version product, with emendrix as the closest direct
   architectural adversary currently found;
3. direct reading of the official source;
4. ordinary search plus a capable LLM asked to explain the result.

Needle does not receive credit for facts or distinctions that this combination
can recover straightforwardly.

## Evaluation rule

A case is:

- **WIN** only when Needle materially changes the answer or reliably exposes a
  relevant state the baseline normally hides;
- **PARITY** when Needle formalises or automates a distinction the baseline can
  recover without unusual effort;
- **LOSS** when the baseline exposes a material fact Needle omits or gets wrong;
- **PLAUSIBLE ADVANTAGE** when Needle improves systematic discovery or
  inspectability but the final reasoning remains straightforward once the right
  sources are retrieved.

A repair after a LOSS is valuable engineering evidence, but it is not converted
retroactively into a product WIN.

## Case 1 — Regulation (EU) 2026/2104 legal timing

### Needle before comparison

The real operational path correctly established:

- authentic Annex V / XIV mutation;
- official publication on 18 September 2026;
- publication as the reason the event was current;
- no pre-event consolidated comparator;
- no invented application date.

The Evidence view closed over the supplied provenance.

### Strong baseline

EUR-Lex also exposes an official **date of effect / entry into force:
19 September 2026**, tied to Article 2, which says the Regulation enters into
force the day after publication.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32026R2104
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32026R2104

Cellar's official CDM vocabulary exposes the corresponding
`resource_legal_date_entry-into-force` property.

### Result

**Initial result: LOSS.**

Needle was epistemically conservative but incomplete. The official baseline
answered a material part of “when does this matter legally?” that Needle did
not surface.

Issue #57 repaired the integration without adding temporal ontology:

- explicit Cellar entry-into-force metadata now projects to existing P0-E
  `LEGAL_FORCE / START`;
- publication remains the independent operational recency reason;
- the live Evidence view closes publication 2026-09-18 and legal force
  2026-09-19 separately;
- legal force is not silently converted into a separate application date.

Repair merged as `93339ce`.

**Post-repair result: PARITY / SEMANTIC CLARITY, not a WIN.**

The case validates Needle's temporal separation but also proves that caution is
not product value when official facts are simply being under-consumed.

## Case 2 — English-only ECU 225 → 255 corrigendum

### Needle

Canonical evidence establishes:

- target act `CELEX:31990R2742`;
- corrigendum `CELEX:31990R2742R(01)`;
- Article 4(1) changes ECU 225 → ECU 255;
- official expression scope = ENG;
- non-listed language = `NO_ASSERTION`;
- the mutation and downstream semantic claim must not become language-neutral.

### Strong baseline

EUR-Lex exposes the base act's `Corrected by` relationship. The corrigendum
page is itself an EN Official Journal publication and explicitly prints both
the old and corrected amounts.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31990R2742R(01)
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:31990R2742

A careful reader or capable LLM supplied these pages can recover the same core
answer: the evidenced corrigendum is English-scoped and changes 225 to 255.

Current other-language displays may independently contain 255; that does not
prove this English corrigendum caused a mutation in every expression. Needle's
`NO_ASSERTION` invariant protects automation from making that leap.

### Result

**PARITY on user understanding; WIN only as machine-safety discipline.**

The invariant is worth retaining in the foundation. It does not demonstrate a
material comprehension advantage over the strong baseline.

## Case 3 — REACH Article 67(1) dependency ripple

### Needle

Official before/after checkpoints establish that Article 67(1) is textually
unchanged. Its operative text says that substances for which Annex XVII
contains a restriction may not be manufactured, placed on the market or used
unless the restriction conditions are met.

Regulation (EU) 2023/2055 adds Annex XVII entry 78 on synthetic polymer
microparticles.

Needle therefore emits:

- no local Article 67(1) textual mutation;
- a VERIFIED upstream Annex XVII mutation;
- an EVIDENCED + DERIVED cross-reference effect on Article 67(1).

### Strong baseline

EUR-Lex accurately records the 2023 change as an addition to Annex XVII entry
78; it does not call Article 67 text amended.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32006R1907
- https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32023R2055
- https://eur-lex.europa.eu/eli/reg/2006/1907/2024-12-18/eng

emendrix likewise records the Annex XVII change, while its Article 67 provision
history contains no 2023 Article 67 event:

- https://emendrix.eu/acts/32006R1907/an-xvii/
- https://emendrix.eu/acts/32006R1907/ar-67/

Once Article 67 and the Annex XVII amendment are both supplied, the dependency
reasoning is one hop and a capable LLM can derive it.

### Result

**PLAUSIBLE ADVANTAGE — proactive dependency discovery and inspectability.**

This is the strongest #49 result:

- a provision-centric text/version view says Article 67 did not change;
- Needle can proactively surface that its referenced rule set changed;
- Needle preserves the distinction between DIRECT upstream mutation and DERIVED
  local effect.

But the final legal inference is not inaccessible to the baseline. The product
advantage is systematic discovery, not exclusive reasoning.

One plausible case does not satisfy the charter's requirement for repeated
material advantage.

## Case 4 — DSA context-dependent application

### Needle

The canonical temporal fixture separates:

- general application from 17 February 2024;
- enumerated provisions applicable from 16 November 2022;
- VLOP/VLOSE anticipated application four months after the provider-specific
  Article 33(6) notification where earlier than the general date.

Without the relevant provider notification event, Needle returns
`CONTEXT_REQUIRED` rather than inventing one universal date.

### Strong baseline

Article 92 and Article 93 state those rules explicitly. Commission guidance
also explains that designated VLOPs/VLOSEs become subject to the relevant DSA
rules four months after notification/designation.

Sources checked 2026-09-23:

- https://eur-lex.europa.eu/eli/reg/2022/2065/oj
- https://digital-strategy.ec.europa.eu/en/policies/dsa-enforcement
- https://digital-strategy.ec.europa.eu/en/policies/dsa-vlops

A capable official-source + LLM baseline can therefore answer the same
contextual question and withhold an exact provider date when notification
context is absent.

### Result

**PARITY on user understanding; strong machine-safe representation.**

Again, Needle's temporal model is correct and valuable internally, but the
distinction itself is not difficult to recover from the official baseline.

## Cross-case verdict

| Case | Before any repair | Final comparative result | What Needle actually earned |
|---|---|---|---|
| 2026/2104 timing | LOSS | PARITY / semantic clarity | Better integration test for orthogonal legal time |
| English money corrigendum | PARITY | PARITY | Machine-safe language scope / provenance |
| REACH Article 67 ripple | PLAUSIBLE ADVANTAGE | PLAUSIBLE ADVANTAGE | Automatic discovery of indirect dependency effect |
| DSA contextual application | PARITY | PARITY | Machine-safe context-required temporal resolution |

The success condition from the charter was **repeated real cases** where the
extra machinery reveals useful distinctions the strong simpler baseline
regularly obscures.

That threshold is **not met**.

The evidence does support a narrower conclusion:

> Needle is stronger as a legal-change audit/research engine that systematically
> tests evidence ownership, temporal state and dependency consequences than as a
> general public “what changed?” feed competing with EUR-Lex, emendrix and a
> capable LLM.

## What survives

1. **Evidence / Why this is shown** survives as trust/read-side infrastructure.
   It closed the real 2026/2104 case without a new truth store.
2. **P0/P1 foundation survives.** Comparative failures were mostly consumption
   or product-position failures, not reasons to collapse the legal-state model.
3. **Dependency Ripple survives as a research/audit detector**, not proof of a
   broad public-product moat.
4. **Thread remains untested against the strong simpler baseline.** It answers
   the second core question (“how did this rule become what it is today?”), not
   the live-feed question #49 just tested.
5. The operational monitor survives as an evidence generator and adversarial
   test rig. It is no longer presumed to be the product.

## What is rejected

- a broad general-interest legal-change feed as the next product horizon;
- “more cautious” as a value proposition;
- formalising an official distinction as sufficient evidence of product value;
- adding affected-entity models, ranking, subscriptions, more analytics or
  infrastructure to compensate for a weak comparative result.

## Direction

**REDIRECT.**

The next gate should test the remaining core Thread/audit proposition with no
new architecture:

> Does Needle's evidence-linked rule history and audit discipline make a complex
> rule history materially easier to reconstruct correctly than EUR-Lex,
> emendrix and a capable LLM?

If Thread also fails that test, public-product expansion should stop. The
existing system can remain a research/audit toolkit and regression corpus
without inventing another product thesis.
