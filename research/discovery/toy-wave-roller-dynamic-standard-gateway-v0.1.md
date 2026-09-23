# Discovery — the legal switch hidden in a standards reference

**Date:** 2026-09-23  
**Lane:** Discovery  
**Issue:** #77  
**Status:** Official case pinned; Dependency Ripple v0.1 reopen criterion triggered

## The finding

Directive 2009/48/EC Article 13 creates a dynamic gateway: conformity with a harmonised standard or part whose reference is published in the Official Journal yields a presumption of conformity for the covered essential requirements.

Commission Implementing Decision (EU) 2023/740 originally listed **EN 71-1:2014+A1:2018** without the later wave-roller restriction.

Commission Implementing Decision (EU) 2025/1785 replaced that same row, kept the same standard identifier, and added a restriction for clauses 3.19 and 4.15.1 as regards wave rollers. For that specified scope, the standard no longer confers the presumption of conformity for the identified essential safety requirement. The Decision entered into force on publication, 10 September 2025.

So the parent Article 13 text is unchanged and the standard identifier is unchanged, while the legal effect produced by the Article 13 gateway narrows.

## Why Dependency Ripple v0.1 cannot honestly encode it

The frozen v0.1 cases are conventional operative references: one unchanged provision points to another legal location whose content mutates.

Article 13 does not statically cite EN 71-1. It defines a condition over a moving publication set: harmonised standards or parts **whose references have been published in the Official Journal**.

The honest dependency relation is therefore publication-status-driven.

v0.1 permits only:

`DERIVED_FROM_EVIDENCED_CROSS_REFERENCE_ATOM`

This case requires a distinct relation character such as:

`DERIVED_FROM_DYNAMIC_PUBLICATION_GATEWAY`

The exact future vocabulary is not decided here. Calling the case a normal cross-reference merely to satisfy the schema would make the representation less accurate.

## Court context

The Grand Chamber judgment of 5 March 2024 in **C-588/21 P, Public.Resource.Org and Right to Know v Commission** held that there was an overriding public interest in disclosure of the harmonised standards at issue and described harmonised standards as forming part of EU law owing to their legal effects.

The bounded relevance here is simple: harmonised-standard reference state is not safely treated as inert catalogue metadata.

## Architectural result

Dependency Ripple v0.1's own reopen rule is triggered.

The old cases remain valid. What fails is the assumption that all unchanged-local-text dependency effects can be represented as ordinary cross-reference ripples.

This commit deliberately preserves the failure before any v0.2 design is introduced.

No family of standards work is created from this one case.
