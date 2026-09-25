# Issue #317 — negative/null evidence discoverability audit

Date: 2026-09-25  
Disposition: **CURRENT_OWNERS_SUFFICIENT**

## Question

Do Needle's current orientation and evidence owners make material negative, null, parity,
REJECT and PARK findings discoverable enough to prevent future claim resurrection, or does
the polished corpus/reference surface require a new negative-evidence navigation layer?

## Materiality rule

This audit considers a negative result material only when it constrains at least one of:

- current project identity;
- a live project-level value claim;
- interpretation of an evaluation;
- reuse of exposed corpus evidence;
- taxonomy/method rules used by later research.

It does not attempt to index every rejected candidate or dead end.

## Existing navigation architecture

The current repository already has a deliberate chain:

1. root `README.md` says negative/parity findings are part of the asset;
2. the README identifies `docs/value-evidence.md` as the **project-thesis evidence** owner;
3. `docs/value-evidence.md` is explicitly the **CANONICAL PROJECT-THESIS EVIDENCE INDEX**;
4. the ledger links each material result to the owning issue/audit/fixture;
5. `docs/assumptions.md` records live/rejected assumptions whose status still affects
   decisions;
6. charter and Way of Working define how stopped/rejected claims may or may not reopen.

That is already the correct shape for negative-evidence navigation.

## Fixed sample

### #214 — hard null: PASS

Discoverability:

- root README explicitly names #214;
- project charter explicitly names #214 and its 0-rescue result;
- Reference Pack README explicitly names #214 and states what the null does and does not
  prove;
- value-evidence ledger records it as project-thesis evidence;
- assumptions register rejects the corresponding live claim;
- Issue #214 contains the full frozen counts, interpretation and rejected escape routes.

A competent reader cannot reasonably miss that the corpus-assisted latent-diagnostic claim
failed unless they ignore the named project-thesis owner.

No repair needed.

### #88 + #95 — surfaced-trap parity / construct correction: PASS

`docs/value-evidence.md` separately records:

- #88 as PARITY for surfaced-trap adjudication;
- #95 as CONTRADICTION of the overbroad interpretation that #88 established latent
  detection.

The exact issue/audit chain preserves why the construct was narrowed rather than merely
recording "6/6 parity."

This is important: the correction is discoverable as a correction, not just as another
negative result.

### #97 — latent-detection parity: PASS

The value-evidence ledger records:

- explicit LATENT_TRAP_DETECTION construct;
- four fresh adversarial R/M pairs;
- all R-pass/M-pass;
- zero Method rescues;
- the execution-provenance limitation.

The root README's broader statement that the strongest gates did not demonstrate general
correctness/latent-diagnostic advantage is therefore traceable to a canonical evidence
entry.

### #207 / #209 — taxonomy baseline-challenge REJECTs: PASS

The value ledger records the two baseline challenges together as CONTRADICTION:

- registry-absence candidate rejected because mature predicate/local completeness
  semantics fully predict the failure;
- soft-law-effect candidate rejected because mature EU soft-law doctrine/source-role
  analysis owns the mechanism without residual Needle-specific state.

The exact issues preserve their kill rules and the instruction not to build the rejected
classes/tooling.

These are good examples of negative evidence that constrains future taxonomy expansion.

### #245 — scoped third-country recognition REJECT: PASS

The issue preserves a useful current rejection pattern:

- ordinary scope analysis owns what the recognition instrument covers;
- existing `DYNAMIC_REFERENCE_STATUS` owns current qualifying membership/status;
- no residual class remains.

This is the stronger current model for a lossless REJECT: incumbent + existing classes
fully express the consequential distinction.

### #218 — historical REJECT with superseded rationale: PASS

#218 remains a historical REJECT.

However, #282 explicitly records that its **incumbent-as-sufficiency rationale is not a
reusable rejection rule**. The later governance rule is stricter:

> incumbent doctrine/competitor existence is a baseline, not automatic rejection;
> REJECT requires lossless prediction/expression of the pre-specified consequential
> regression distinction.

This proves why a flat negative-results registry would be dangerous. A new index that
listed "#218 — REJECT" without the #282 methodological correction could make stale
rationale look current.

The existing ownership hierarchy handles this correctly: historical issue result remains
history; later canonical governance owns the reusable rule.

## Reference Pack boundary

Reference Pack v0.1 is intentionally case-centric, not a project-history archive.

It already includes the two negative protections most important to safe external use:

- all cases are exposed / `REGRESSION_ONLY`;
- #214 is stated explicitly as a frozen hard null against corpus-assisted diagnostic
  superiority.

The pack also preserves evaluation role/mode/result for the ten revealed evaluation cases.

It does **not** enumerate every project-level REJECT/PARK result. That is acceptable because:

- the pack declares itself a derived reference/navigation layer;
- it does not claim to be a full project-evidence bundle;
- repository access is already required for underlying evidence owners;
- root repository orientation points to the canonical value-evidence ledger.

Copying the entire negative ledger into the pack would create a second project-thesis
truth store and new staleness risk.

## Discoverability failure tested

A real failure would look like:

- root orientation celebrates accepted cases but does not name the negative-evidence owner;
- current project identity relies on a null that cannot be found without knowing an issue
  number;
- the evidence ledger omits a binding contradiction;
- a superseded REJECT rationale is presented as current;
- the Reference Pack makes an affirmative claim that conflicts with a hidden null.

The fixed sample found none of those failures.

## Why no new negative-evidence index

A standalone registry would duplicate `docs/value-evidence.md`.

It would also create hard problems that the current architecture already solves:

- deciding which ordinary REJECTs are "important enough";
- keeping project-level claim status synchronized;
- distinguishing binding current negatives from superseded historical rationale;
- avoiding repeated copies of exact result language;
- preserving later methodological corrections.

The strongest boring solution is the existing one:

> one canonical project-thesis evidence ledger, with exact linked owners.

## Disposition

**CURRENT_OWNERS_SUFFICIENT**

No new negative-evidence map, Reference Pack file or registry is warranted.

Durable interpretation:

- `docs/value-evidence.md` remains the canonical project-level evidence index for both
  positive and negative thesis evidence;
- `docs/assumptions.md` owns material live/rejected beliefs;
- historical issues remain evidence, not reusable policy unless current governance adopts
  their rationale;
- the Reference Pack remains a corpus/reference surface, not a duplicate project-history
  ledger.

The audit found no claim-resurrection gap requiring implementation.
