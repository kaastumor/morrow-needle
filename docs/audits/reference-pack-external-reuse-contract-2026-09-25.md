# Issue #307 — external reuse rights and citation contract

Date: 2026-09-25  
Disposition: **OWNER_LICENSE_DECISION_REQUIRED**

## Question

What minimum rights/citation/distribution metadata is required before Needle Reference
Pack can honestly be called externally reusable, and which parts are mechanical versus
owner/legal decisions?

## Actual repository state

At the start of #307:

- repository visibility: **public**;
- GitHub detected license: **none**;
- no root `LICENSE`, `LICENSE.txt`, `COPYING` or equivalent;
- no `CITATION.cff` or other root citation file;
- `pyproject.toml` declares no license metadata.

GitHub's own documentation states that public/open-source reuse requires an explicit
license and that without a license default copyright rules apply. GitHub separately
supports `CITATION.cff` as machine-readable citation metadata.

References:

- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository
- https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files

This is a project-governance finding, not legal advice.

## Public visibility is not the same as project-granted reuse

The current public repository makes Needle inspectable and gives GitHub users the
platform capabilities GitHub provides for public repositories.

It does **not** currently contain a project-authored license granting general permission
to reproduce, redistribute, modify or create derivatives outside whatever rights already
exist under applicable law or GitHub's own terms.

Therefore the current Reference Pack can accurately be described as:

> publicly inspectable reference material

but not yet as:

> openly licensed reusable data/software/documentation

unless an owner chooses and grants terms.

## What the Reference Pack actually contains

Inspection of the released pack shows that its case records contain only:

- stable ID;
- title;
- domain;
- jurisdiction;
- trap-class membership;
- provenance;
- exposure state;
- decisive-trap description;
- evaluation metadata where applicable;
- `issue:` / `path:` evidence references.

There are no raw-source-text, quotation, excerpt or full-content fields in
`cases.jsonl`.

The remaining pack files are generated project metadata/navigation/documentation:

- class definitions and membership;
- evidence-owner navigation;
- manifest/build metadata;
- human catalog;
- safe-use README;
- checksums.

This substantially reduces the licensing complication: the Reference Pack does not
attempt to bundle the underlying legal-source evidence.

However, a project license could only grant permissions in material the project owner is
entitled to license. It cannot grant rights in independently owned third-party material
merely because Needle links to or describes it.

## Options matrix

| Option | Solves reuse permission? | Solves citation? | Complexity | Decision |
| --- | --- | --- | --- | --- |
| No license, no notice | No | No | Lowest | Too ambiguous for an external-use surface |
| Explicit unlicensed/all-rights-reserved notice | Honest limitation, not open reuse | No | Very low | Safe interim state |
| `CITATION.cff` only | **No** | Yes | Low | Useful later, but does not solve permission |
| One repository-level license | Yes for covered project-authored material | Partly | Low | Strong boring option **if owner chooses terms** |
| Separate code/data/docs licenses | Yes, granular | Partly | Higher | Not earned unless owner wants different terms |
| Bespoke Reference Pack license | Potentially | Partly | Highest/legal overhead | No evidence this complexity is needed |

## Why citation metadata is not the blocker

GitHub's `CITATION.cff` is a useful machine-readable way to state how a repository,
software artifact or dataset should be cited.

But citation metadata answers:

> How should this work be attributed?

A license answers a different question:

> What permission is granted to copy, modify or redistribute it?

Adding `CITATION.cff` while leaving the repository unlicensed would improve
attribution ergonomics but would not make the Reference Pack openly reusable.

Citation metadata also requires an authorship/attribution decision. The repository owner
and the project identity are known, but #307 does not assume whether the preferred
citation author should be the individual owner, a project/contributor collective, or
another form.

## Strongest boring solution

If the owner wants broad external reuse, the simplest maintainable architecture is likely:

1. one standard repository-level license for project-authored material;
2. an explicit statement that linked/third-party material remains under its own rights;
3. one root `CITATION.cff` describing the project/release once preferred authorship is
   decided;
4. optional package license metadata aligned with the repository license.

There is currently no evidence that split licensing or a bespoke Reference Pack license
is worth the additional ambiguity and maintenance.

But selecting a license changes legal permissions. That is an owner decision and is not
made autonomously by #307.

## Bounded repair applied

The root README is updated to state the current status explicitly:

- the repository is public but currently has no project license;
- public visibility must not be read as a general project grant to
  reproduce/redistribute/modify;
- linked or third-party legal evidence is not relicensed by Needle;
- license and citation metadata require an explicit owner decision.

The already frozen Reference Pack v0.1 bytes are not changed.

## Disposition

**OWNER_LICENSE_DECISION_REQUIRED**

Reason:

- there is a real external-reuse ambiguity;
- citation metadata alone does not cure it;
- the released pack architecture itself is relatively clean because it does not bundle raw
  underlying legal evidence;
- a standard license is likely the strongest boring solution if open reuse is intended;
- choosing that license and preferred citation authorship is a genuine owner/legal
  decision, not a mechanical repository task.

Until that decision exists, describe Needle and the Reference Pack as publicly
inspectable/reference material, not openly licensed reusable material.
