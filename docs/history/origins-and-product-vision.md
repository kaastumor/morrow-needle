# Origins and original product vision

Status: **HISTORICAL CONTEXT — recovered from early chats and accepted foundation artifacts**

## 1. Naming and roles

Early project framing was explicit:

- **Morrow** = the builder/operator.
- **Needle** = the thing being built.
- **Thread** = the historical view that follows a rule/change through ancestry and descendants.

The metaphor was functional rather than decorative: Needle finds the legally meaningful change;
Thread lets the user follow how that rule became what it is.

## 2. Original ambition

The earliest product thesis was substantially broader than the current corpus identity.

The project was **not** intended to be a document summarizer or a generic 'ask legal PDF' tool.
It was conceived as public legal-change intelligence / public infrastructure for making rules
observable through time.

Recovered early formulation:

> **Make legal change observable.**

A second recurring promise was:

> Tell me what changed, who it affects, when it matters, and show me exactly where you got that from.

The desired chain was:

> **decision -> change -> consequence -> evidence -> public understanding**

The canonical object was initially not a document but a **change in rules**:

- compared with what;
- what textual/legal state changed;
- who or what the rule concerns;
- when the change becomes relevant/applicable;
- which official evidence proves each part.

## 3. Intended user experience

The original user experience had layered explanation rather than one long legal answer:

- **3 seconds** — a factual headline;
- **30 seconds** — what changed / who must do what / when / exceptions;
- **3 minutes** — chronological explanation retaining qualifications and uncertainty;
- **Source Mode** — exact evidence and provenance behind every consequential claim.

One early product image was an explainable public feed roughly equivalent to:

> Europe changed in 17 places yesterday.

But unlike a news feed, the system was supposed to distinguish:

- authentic legal mutation;
- procedural movement;
- representation/source refresh;
- non-impact;
- unresolved state;
- change in application/effect without local text mutation.

## 4. Three histories

Foundation v0.1 described three linked histories:

1. **Document graph** — what EU institutions published.
2. **Rule graph** — what rules/concepts exist at a given time.
3. **Mutation graph** — how one state became another.

This is important historical context: Needle was originally trying to solve a hard longitudinal
legal-information problem, not merely collect interesting edge cases.

## 5. Why EU legislation was the original domain

EU law supplied exactly the adversarial substrate the thesis needed:

- authentic multilingual expressions;
- amending acts and corrigenda;
- consolidation that is useful but not legally canonical;
- entry-into-force versus application distinctions;
- delegated/implementing measures;
- national options/transposition;
- institutional procedure state;
- official Cellar/WEMI infrastructure;
- versioned and machine-readable sources with surprising edge cases.

Regulation 794/2004 was selected early because it was 'boring administrative law' with unusually
rich machine-readable history — ideal for testing whether the architecture could reconstruct
real legal change rather than only famous headline legislation.

## 6. Early success definition

Technical success initially meant:

- reconstruct a rule state from authentic official material;
- never let a consolidated/current view overwrite historical truth;
- represent renumbering/split/merge without fake persistent article identity;
- separate text change from legal effect;
- preserve language-scoped corrections;
- keep multidimensional legal time separate;
- show every consequential claim's evidence chain;
- abstain rather than invent missing continuity;
- operationally detect a new official event and turn it into an understandable card.

Product success meant more:

- a normal person could understand a trustworthy card quickly;
- Thread made historical reconstruction materially easier;
- live change detection created useful public awareness;
- Needle's additional structure repeatedly beat the strongest practical alternative enough
  to change user behavior.

The engineering largely achieved the first group. Later value gates did **not** establish the
second group strongly enough.

## 7. Original architecture ambition versus actual implementation

Very early architecture sketches considered a scaled product stack — database, storage, queue,
frontend and richer delivery infrastructure.

Evidence-driven implementation quickly became much leaner:

- Python and small dependencies;
- Git/versioned JSON fixtures as the evidence backbone;
- GitHub Actions for deterministic/live contracts;
- static projections instead of an application platform;
- no database/vector store/custom model unless a concrete need earned it.

This lean implementation choice is a recurring Needle pattern: large conceptual ambition, but
architecture only when adversarial evidence requires it.

## 8. Built versus merely imagined product layers

Historical memory must distinguish shipped/proven prototypes from roadmap ideas.

### Actually built/frozen

- Thread v0.1;
- structured Retrieval v0.1;
- Half-Life v0.1;
- Source Anomaly v0.1;
- Legislative X-Ray / Dependency Ripple v0.1;
- operational update monitoring/re-observation/classification;
- CHANGE_FEED / AUDIT_FEED / ABSTENTION_FEED routing and feed-card contracts;
- an early thin product checkpoint;
- later Corpus Explorer v0.1.

### Identified as possible future directions but deliberately not earned/built as full product layers

- richer affected-entity intelligence;
- public-interest/importance ranking as a product system;
- broad public UI/application platform;
- general API/platform layer;
- subscription/large-scale delivery machinery;
- additional analytics merely to create product breadth.

Affected-entity intelligence was at one point identified as the strongest information gap after the
first live feed cards, but later adversarial/product-value gates intervened before a new canonical
layer was justified.

Likewise, early architecture sketches mentioned larger database/queue/frontend infrastructure, but
the project deliberately stayed with a much leaner evidence-backed implementation.

## 9. What the original vision still contributes

The public-feed thesis is not current, but several original ideas remain highly relevant:

- legal state is not equivalent to current consolidated text;
- every material conclusion has an evidence owner;
- source observation time and legal effect time differ;
- lineage and continuity are claims, not identities;
- negative/non-impact evidence matters;
- a user-facing explanation should never hide uncertainty;
- longitudinal change can be more important than static retrieval.

These are not abandoned principles. They became the scientific/evaluation discipline that survived
after the product thesis contracted.