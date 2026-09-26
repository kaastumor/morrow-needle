# Issue #368 — owner license and citation decision package

Date: 2026-09-26  
Disposition: **OWNER_DECISION_READY**

> This is a project/release decision aid, not legal advice.

## Current repository state

Verified on current GitHub main before this review:

- repository is public;
- no root `LICENSE` / `COPYING`;
- no root `CITATION.cff`;
- `pyproject.toml` contains no license metadata;
- repository mixes executable/software material with research/reference data and
  documentation;
- Reference Pack v0.2 is project-authored derived metadata/navigation over linked evidence,
  not a bundled copy of the underlying legal-source estate;
- the pack already warns that public visibility is not a broad reuse grant.

GitHub's current licensing guidance states that, absent a license, default copyright rules
apply; public GitHub users may view/fork under GitHub's terms, but a public repository is not
thereby an open-source/open-data grant.

Source:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository

## Citation is separate from permission

GitHub supports a root `CITATION.cff` file as human- and machine-readable preferred
citation metadata and renders a **Cite this repository** control when it is present.

GitHub also supports `type: dataset` for dataset-oriented citation.

A citation file:

- tells users how the owner wants the work credited/cited;
- does not grant copyright/database reuse permission;
- does not substitute for a license.

Source:
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

## Material classes in Needle

For licensing clarity, Needle is not one homogeneous software package.

### Software / executable / integration material

Examples:

- `src/`;
- `scripts/`;
- `tests/`;
- `schemas/`;
- `.github/`;
- `pyproject.toml`;
- historical executable/tool surfaces under `mvp/` and `product/`.

### Research / corpus / reference material

Examples:

- `corpus/`;
- `data/`;
- `docs/`;
- `research/`;
- `release/`;
- structured research fixtures where they function as reference/test data;
- root orientation/project records such as `README.md`.

### Third-party / external evidence

Needle frequently **links to** official/legal/external evidence.

A project license can only license rights the project owner actually controls.

Linked or incorporated third-party material must remain subject to its original rights and
must not be described as relicensed merely because project-authored metadata around it is
licensed.

## Option A — remain inspectable-only

### Shape

- no license file;
- keep the current README rights warning;
- optionally add citation metadata later if owner authorship is supplied.

### Effect

- least maintenance;
- preserves all rights by default;
- users can inspect and use whatever independent legal exceptions/permissions apply;
- does **not** give a clear general permission to copy, adapt or redistribute
  project-authored corpus/reference material.

### Fit

Best if Needle is intended primarily as a public research record rather than a reusable
dataset/tool.

### Cost / risk

Low project complexity, but highest external reuse friction and greatest chance that a
careful consumer simply declines reuse because permission is unclear.

## Option B — one permissive repository-level license

A single software-oriented permissive license can create a simple repository-wide story.

### MIT

MIT is extremely short and permits use, copying, modification, publication, distribution,
sublicensing and sale subject principally to preservation of the copyright/license notice.

Reference:
https://spdx.org/licenses/MIT

### Apache-2.0

Apache-2.0 also permits broad reuse and redistribution and adds explicit contributor patent
terms.

Reference:
https://www.apache.org/licenses/LICENSE-2.0

### Advantages

- one root license;
- simple GitHub presentation/detection;
- low explanation burden;
- covers code cleanly.

### Weakness for Needle

Needle's primary surviving asset is increasingly a **corpus/reference dataset**, not
software.

A software license can cover copyrightable non-code work if the owner applies it, but it is
not the clearest expression of data/database reuse rights for a mixed research artifact.

Using one software license over everything also makes the distinction between:
- code;
- project-authored research metadata;
- third-party evidence

less legible than it should be.

### Assessment

Valid simple option, but **not the clearest default** for Needle's current mixed identity.

## Option C — split software + data/documentation licensing

### Structure

Use a software license for executable/code material and a content/data license for the
project-authored corpus/reference estate.

Creative Commons currently recommends **against** CC licenses for software and points users
toward software-specific licenses. It explicitly permits CC licenses for databases; CC 4.0
also addresses applicable sui-generis database rights.

Source:
https://creativecommons.org/faq/

### Suggested split if the owner wants open reuse

#### Code/software

**MIT** as the minimum-complexity default.

Alternative:

**Apache-2.0** if the owner specifically wants the additional explicit patent-license
structure.

#### Project-authored corpus / data / documentation

**CC BY 4.0** as the minimum-friction attribution-preserving candidate.

CC BY 4.0 permits sharing and adaptation, including commercial use, with attribution and
change indication.

Sources:
https://creativecommons.org/licenses/by/4.0/
https://creativecommons.org/licenses/by/4.0/legalcode

Why CC BY rather than CC0 as the default candidate:

- provenance/attribution is unusually important to Needle's scientific/reference role;
- the project already treats evidence lineage and attribution as first-class;
- CC0 would intentionally waive the attribution condition as far as legally possible.

Why not recommend BY-SA/NC/ND by default:

- ShareAlike adds downstream licensing constraints not currently connected to a project
  requirement;
- NonCommercial/NoDerivatives reduce reuse and are not needed to preserve attribution or
  evidence lineage;
- Creative Commons itself advises against NC/ND for databases intended for scholarly or
  scientific use.

### Third-party boundary

The split must state clearly:

> licenses apply only to project-authored material and rights actually held by the
> licensor; linked or separately identified third-party material remains under its original
> terms.

CC's own guidance similarly distinguishes a licensor's own contribution from third-party
material included in a work.

### Advantages

- aligns license type with material type;
- CC BY 4.0 is clearer for corpus/database reuse, including applicable database rights;
- MIT is clear and lightweight for code;
- attribution aligns with Needle's provenance-centric role.

### Costs

- more explanation than one root license;
- GitHub may not present one simple license badge/detection result for a mixed-license
  repository;
- scope mapping must remain clear when new files/directories are added.

### Assessment

# **Recommended structure if the owner wants open reuse**

This is a structural recommendation, **not** an owner license choice.

## Option D — citation metadata only

Citation can be added regardless of whether the repository remains all-rights-reserved or
becomes openly licensed.

### Proposed CFF posture

Given the smaller project identity, the most natural top-level citation type is:

> `type: dataset`

Candidate metadata:

- title: `Morrow // Needle`;
- repository URL;
- current release/reference version as chosen by owner;
- preferred author/creator identity supplied by owner;
- optional ORCID(s);
- optional preferred citation/technical report later.

Do not invent authorship from account metadata, commit history or chat memory.

### Effect

- improves attribution/citation ergonomics;
- GitHub exposes Cite this repository;
- does **not** change reuse rights.

## Recommended decision structure

The owner only needs to decide two independent things.

### Choice 1 — reuse posture

Pick one:

**1A — Inspectable only**
> Keep no project license.

or

**1B — Open reuse**
> Grant explicit reuse rights.

If **1B**, the project recommendation is:

> **split licensing: MIT for software/code + CC BY 4.0 for project-authored
> corpus/data/documentation**

with Apache-2.0 as the code alternative if explicit patent terms are desired.

### Choice 2 — citation identity

Independently decide whether to add `CITATION.cff`.

If yes, the owner must explicitly provide/approve:

- preferred creator/author name(s) or organization;
- optional ORCID(s);
- preferred citation title if different from `Morrow // Needle`;
- whether the repository should cite the overall project/dataset or a future report as the
  preferred citation.

A DOI is **not required** for CFF.

## Exact repository changes after each choice

### If 1A — inspectable only

No licensing files added.

Keep current README limitation.

If citation is approved:
- add `CITATION.cff`;
- do not add license metadata to it that implies permission not granted elsewhere.

### If 1B — recommended split open reuse

Proposed implementation:

1. add `LICENSES/MIT.txt`;
2. add `LICENSES/CC-BY-4.0.txt`;
3. add root `LICENSES.md` defining scope, for example:
   - software/tooling paths -> MIT;
   - project-authored corpus/data/docs/reference release paths -> CC BY 4.0;
   - third-party/external evidence excluded except where separately stated;
4. update README reuse section;
5. add software-package MIT license metadata to `pyproject.toml`;
6. add `CITATION.cff` only after owner citation identity is approved;
7. add a small validation/sanitation check only if future edits demonstrate real scope-drift
   risk — not pre-emptively.

The exact path map should be reviewed during implementation rather than inferred from file
extensions alone.

### If one repository-wide license is chosen instead

1. add root `LICENSE` with owner-approved license;
2. update README;
3. update package metadata where applicable;
4. add explicit third-party/evidence exclusion language;
5. optionally add CFF.

## Reversibility

A licensing grant already made to recipients generally should not be treated as something
the project can simply claw back for existing copies.

Therefore:

> license selection deserves explicit owner approval even though the mechanical repository
> changes are small.

Citation metadata is much easier to revise prospectively.

## Owner gate

The research/technical part is complete.

The project should **not** infer the following owner choices:

- whether broad reuse should be granted at all;
- the identity of the copyright/licensing party;
- preferred citation authorship;
- whether explicit Apache patent terms are desired instead of MIT.

## Disposition

# **OWNER_DECISION_READY**

No license, citation identity or reuse permission has been selected or applied.
