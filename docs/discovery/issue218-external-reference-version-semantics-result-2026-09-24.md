# #218 result — external-reference version semantics

Date: 2026-09-24  
Issue: #218  
Parent operating correction: #217

## Decision

# **REJECT — no new Needle trap class**

The research found a real and consequential legal-reference distinction, but it
is already owned by mature legal drafting/reference semantics.

## Strong incumbent baseline

The 2023 Joint Handbook for acts subject to the ordinary legislative procedure
expressly distinguishes:

- **dynamic references** — including non-Union acts “as amended” or in the most
  up-to-date version applicable to the Union;
- **static references** — references to a particular version/date or specified
  amended state.

Source:
https://www.consilium.europa.eu/media/67390/joint_handbook_en_01-october-2023_clean_def_final.pdf

The Joint Practical Guide separately warns drafters to consider the consequences
of subsequent amendments to referenced acts.

Source:
https://eur-lex.europa.eu/content/techleg/KB0213228ENN.pdf

ELI subdivision specifications expose the same information problem at the
identifier layer: an abstract/dynamic legal reference needs additional
information to resolve it to a specific version.

Source:
https://eur-lex.europa.eu/content/eli-register/ELI-subdivisions-specifications-v2.pdf

## Static/version-specific example

Regulation (EU) 2024/1781 names specific external standard editions, including
ISO/IEC 15459 editions by year.

Source:
https://eur-lex.europa.eu/eli/reg/2024/1781/oj

A later edition is therefore not silently the same legal reference merely
because it is newer.

Commission Implementing Regulation (EU) 2025/2162 reinforces the legal
importance of version identity by requiring conformity-assessment schemes to
state the year and version number of applicable standards.

Source:
https://eur-lex.europa.eu/eli/reg_impl/2025/2162/oj/eng

## Dynamic/latest-version example

Commission Decision (EU) 2021/1870 requires use of the Detergent Ingredient
Database and directs the user to the **latest version** of the DID list.

Source:
https://eur-lex.europa.eu/eli/dec/2021/1870/oj/eng

That is a content-version update path under unchanged parent wording.

## Status-gated control

Harmonised standards form a third reference mode.

The Commission Blue Guide explains that presumption of conformity follows the
European harmonised standard whose reference is published in the Official
Journal. A current international ISO/IEC text does not automatically inherit
that legal status.

Source:
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=oj:JOC_2022_247_R

This remains the mechanism already owned by
`DYNAMIC_REFERENCE_STATUS` / #77.

## Existing-class first refusal

The three observed patterns are:

1. static external-version reference;
2. dynamic external-content reference;
3. status-gated external reference.

Only the third is the current `DYNAMIC_REFERENCE_STATUS` class.

Broadening that class to absorb static/dynamic version semantics would reduce
precision.

Creating a second Needle class is also unnecessary because the incumbent legal
rule is already sufficient:

> determine whether the parent reference is static, dynamic or status-gated,
> then resolve the legally operative external version/status at the relevant
> time.

That rule predicts the consequential error completely:

- substituting today's external edition for a legally pinned edition; or
- freezing an external artifact that the law expressly follows dynamically.

## Consequence

Do not:

- add a trap class;
- broaden `DYNAMIC_REFERENCE_STATUS`;
- add a version resolver/schema;
- build a standards database.

Keep the three-way reference-mode check as ordinary research discipline.

## Research value

This is a useful negative result.

It removes a tempting taxonomy extension while exposing a richer next research
question: what happens when the external artifact is not merely text/data but
**executable compliance software** whose versions acquire legal relevance over
time?

That question is now #219.

## Astra checkpoint

Not triggered.

The incumbent legal baseline cleanly resolves the candidate mechanism.
