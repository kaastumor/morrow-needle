# Step-back review — 2026-09-20

## Question

After the first provision-lineage, Cellar, Gold Corpus, and Legal AST foundation work: are we still solving the right problem with the simplest defensible architecture?

## What still earns its cost

1. **Immutable observations and text states.** Raw publication bytes, expression state, legal text state, and legal applicability are genuinely different things. Collapsing them would recreate errors already observed in live Cellar/Formex evidence.
2. **Flat-with-links Legal AST.** Nodes + ordered segments + references + annotations remains simpler than source-shaped trees downstream, while preserving source anchors.
3. **Evidence-backed lineage rather than persistent provision identity.** This has survived recasts, renumbering, same-act moves, and no-official-mapping adversaries.
4. **Gold Corpus as negative as well as positive contract.** Forbidden inferences are as important as expected outputs.
5. **Source-assisted mutation detection.** Embedded consolidation provenance is useful evidence, but authentic modifying/correcting acts remain authoritative legal cause.

## Complexity to resist

- Do not create a universal ontology for every Formex tag. Normalize only legally useful structure and explicitly account for the rest.
- Do not let parser coverage percentages become a proxy for correctness. A parser can map many characters incorrectly.
- Do not fuse AST completeness with legal applicability, lineage confidence, or source authority. These are separate dimensions.
- Do not implement the mutation engine while AST source accounting can still report unexplained or multiply-owned text.
- Do not promote Discovery Lane product concepts into foundation dependencies.

## Architectural correction: fidelity must fail closed

The source-text ledger exposed a subtle contradiction: the parser could previously return `FULL_STRUCTURAL` while also declaring unexplained source text or duplicate accounting ownership. That makes the fidelity label stronger than the evidence.

New invariant:

> `FULL_STRUCTURAL` requires zero unexplained normalized source-text characters and zero duplicate source-text ownership claims, in addition to no unassembled fragments or unknown native structural kinds.

Unexplained text is not automatically legal text, but until it is classified the parser cannot honestly claim full structural fidelity. Duplicate ownership is a parser ambiguity, not a harmless warning.

This is intentionally stricter than a coverage threshold. There is no acceptable percentage below which unknown text becomes invisible.

## Priority decision

Keep P0-D ahead of temporal/status work until the live modern, historical, and consolidated fixtures satisfy this fail-closed fidelity contract. P0-B AST integration should then close almost immediately because its remaining work is the same normalization path, not a separate ingestion architecture.

P0-C should remain open until actual reconstruction outputs, not only fixture syntax, are matched in CI.

## Deletion/simplification candidates

No major subsystem should be deleted yet. The main simplification is conceptual: **source accounting is part of parser correctness, not a separate analytics feature.** Treat it as an invariant of every structured-source adapter rather than growing a parallel completeness subsystem.
