# Cycle 3 Run 3C — machine-readable official derivative drift

Issue: #180  
Parent: #177  
Date: 2026-09-24  
Disposition: **PARK**

## Proven anchors

- #67 representation-local identity;
- #93 source observation horizon;
- #150 reproducibility/provenance;
- #174 official-derived-view hypothesis.

The run searched for a specifically **machine-readable** legal-information
failure that could not already be explained by existing source-state/freshness
mechanisms.

## Target evidence — Commission Union Register BETA dataset

The Commission Union Register currently offers a BETA machine-readable medicinal
products dataset.

At the time of this scan:

- downloadable dataset date: **21 September 2026**;
- active-substance / brand / company indices: updated **22 September 2026**;
- adopted Commission decisions page: updated **23 September 2026**.

Official sources:

- https://ec.europa.eu/health/documents/community-register/html/
- https://ec.europa.eu/health/documents/community-register/html/reg_index_inn.htm
- https://ec.europa.eu/health/documents/community-register/html/reg_last.htm

### Observation

An automated consumer using only the 21 September dataset on 24 September can
observe a different update horizon from the human-facing register pages.

This is real and potentially consequential.

### Why it does not earn a machine-readable-specific class

The causal mechanism is:

```text
derived snapshot timestamp
    <
newer official register state
```

Nothing about CSV/JSON/XML semantics is required for the error.

The same error could occur with a PDF export or cached HTML snapshot.

This is already structurally owned by the project's observation/update-horizon
discipline and is close to `OFFICIAL_TRACKER_UPDATE_LAG`.

Machine-readability changes scale and automation risk, not the underlying legal
failure mechanism.

## Strong baseline / safeguards

### CELLAR notification feeds

The EU Publications Office CELLAR exposes RSS/ATOM feeds specifically for:

- document ingestion;
- metadata changes;
- SPARQL loading;
- ontology changes.

The feed documentation says modified publications and/or metadata are exposed.

Source:

- https://op.europa.eu/en/web/cellar/cellar-data/rss-and-atom-feeds

This is a mature incumbent mechanism for automated consumers to track official
repository state rather than treating a local extract as timeless/current.

### ECHA versioned machine-readable packages

ECHA's Candidate List package provides:

- versioned packages;
- change logs;
- delta packages containing only new/updated reference substances;
- lists of package contents.

Source:

- https://echa.europa.eu/en/candidate-list-package

ECHA also distinguishes the authentic published Candidate List from derived
datasets and is transitioning data into ECHA CHEM with explicit availability /
transition status.

Sources:

- https://echa.europa.eu/candidate-list-table
- https://echa.europa.eu/en-GB/echa-chem

These controls show that machine-readable official data can be managed with
explicit provenance/version semantics.

## Existing taxonomy

### OFFICIAL_TRACKER_UPDATE_LAG

Near owner.

The label "tracker" is surface-specific, but the underlying rule already says
current access time cannot substitute for a derived view's observation/update
horizon.

### SOURCE_STATE_BACKPROJECTION

Also relevant when a newer machine-readable representation is used to infer an
older source state.

### REPRESENTATION_LOCAL_MARKER_IDENTITY

Would own a format-local identifier/marker mismatch, not simple freshness.

No evidence in this run required another machine-readable-specific family.

## Boundary

Machine-readable data can itself be an authoritative publication surface if the
governing legal regime says so.

The fact that data is XML/JSON/CSV does not make it derivative or inferior.

The role must come from the legal/publication contract, not format.

That boundary blocks a generic:

> machine-readable = secondary

assumption.

## One falsifiable hypothesis considered

`MACHINE_READABLE_OFFICIAL_DERIVATIVE_DRIFT`

> Official machine-readable legal datasets create a distinct failure mechanism
> beyond ordinary derived-view freshness because their automated consumers can
> observe materially different state.

## Result of hypothesis attack

**Not supported as distinct.**

Automation increases blast radius but the evidence found here reduces to known
update-horizon/version-state mechanics.

No semantically distinct machine-readable transformation error was found.

## Re-entry trigger

Reopen only if target evidence shows a machine-readable official artifact where:

- the same observation time is used;
- freshness/version difference is not the explanation;
- machine representation/transformation semantics themselves change legal
  meaning or identity;
- the mismatch is not already owned by
  `REPRESENTATION_LOCAL_MARKER_IDENTITY`.

## Run 3C disposition

# **PARK**

Do not create a new class or experiment now.

Do not build:

- official-data ingestion;
- freshness diff service;
- CELLAR listener;
- Union Register downloader;
- schema/version platform.

The useful result is subtraction:

> machine-readable scale is not a new legal-information mechanism by itself.
