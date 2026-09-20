# Decision — Freeze Typed Identifier / Equivalence Semantics v0.1

**Date:** 2026-09-20  
**Status:** ADOPTED  
**Issue:** #7

## Decision

Freeze the identifier foundation around:

- `schemas/identifier-graph-v0.1.schema.json`
- `schemas/identifier-resolution-query-v0.1.schema.json`
- `src/needle/identity/resolver.py`

The core rule is:

> **There is no generic "same document" relation.**

Identifiers are equivalent only at a named identity level. Relationships across levels remain typed hierarchy or legal/procedural relations.

## Identity levels

v0.1 distinguishes:

- `LEGAL_RESOURCE`
- `TEXT_STATE`
- `EXPRESSION`
- `MANIFESTATION`
- `ITEM`
- `SUBDIVISION`
- `PROCEDURE`
- `PUBLICATION_CITATION`

## Equivalence relations

Only same-level identities may participate in equivalence:

- `SAME_LEGAL_RESOURCE`
- `SAME_TEXT_STATE`
- `SAME_EXPRESSION`
- `SAME_MANIFESTATION`

Everything else is a typed relation:

- `EXPRESSION_OF`
- `MANIFESTATION_OF`
- `ITEM_OF`
- `TEXT_STATE_OF`
- `SUBDIVISION_OF`
- `CORRIGENDUM_OF`
- `DOCUMENT_IN_PROCEDURE`
- `RESULT_OF_PROCEDURE`
- `PUBLISHED_AS`

The resolver rejects cross-level equivalence edges.

## Resolution API

Callers must explicitly request:

1. **equivalents** at the current identity level; or
2. a named typed relation and direction.

There is deliberately no “resolve everything that is the same document” operation.

Unknown identifiers return `NOT_FOUND`; the resolver does not synthesize a plausible identifier.

## Adversaries passed

### Modern act
Regulation 794/2004:
- CELEX, ELI and Cellar Work are identifiers of the same legal resource.
- English Cellar Expression is not the Work.
- FMX4 Manifestation is not the Expression.
- a Cellar Item is not the Manifestation.

### Consolidated state
`02004R0794-20250813` and its ELI represent the same consolidated text state but are not equivalent to the authentic base act.

A language-specific consolidated ELI is an Expression of that text state.

### Corrigendum
`32004R0794R(02)` and its ELI identify the corrigendum resource. The corrigendum is related to the base act through `CORRIGENDUM_OF`; it is not an alias of the base act.

### Historical identifier
Regulation No 1 (1958) resolves to the official ELI:

`http://data.europa.eu/eli/reg/1958/1(1)/oj`

Needle must preserve the authoritative `(1)`; it must not manufacture a simpler ELI from the visible act number.

### Procedure graph
For the Digital Services Act:
- proposal CELEX `52020PC0825` and `COM/2020/825 final` identify the same proposal resource;
- procedure `2020/0361/COD` is a distinct procedure identity;
- adopted act `32022R2065` is a distinct legal resource;
- proposal is `DOCUMENT_IN_PROCEDURE`;
- adopted act is `RESULT_OF_PROCEDURE`;
- Official Journal citation is publication metadata, not an alias of the act.

### Subdivision
An Article-level ELI is a `SUBDIVISION` related through `SUBDIVISION_OF`, never an alias of the whole act.

## Durable invariants

1. Never manufacture an authoritative identifier when it can be resolved.
2. Equivalence is identity-level specific.
3. Work, Expression, Manifestation and Item are different identities.
4. Consolidated states are not the authentic base resource.
5. Corrigenda are their own legal resources.
6. Proposal, procedure and adopted act are distinct nodes.
7. OJ citations are publication references, not legal-resource aliases.
8. Subdivision identifiers do not collapse into act identity.
9. A resolver must abstain on an unknown identifier rather than guessing.
10. New identifier systems should normally add a typed scheme/relation, not weaken these distinctions.

## Post-freeze rule

P0-G freezes the **identity semantics and resolver contract**, not a complete registry.

Live source adapters may add identifiers and evidence edges continuously. Reopen the core contract only if an authoritative identifier system demonstrates a relationship that cannot be represented without collapsing identity levels.
