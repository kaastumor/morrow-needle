# #165 result — scholarly-status protocol transfer

Date: 2026-09-24  
Issue: #165  
Disposition: **INDETERMINATE / TRANSPORT_BLOCKED**

## Result

The scientific claims were not executed.

No model answer was produced and no four-case validation sample was frozen.

The experiment therefore provides **no evidence for or against**:

- P165-A — protocol transfer outside legal research;
- P165-B — latent versus surfaced scholarly-status detection.

Do not interpret this as a failed transfer.

## What happened

The pre-registration deliberately separated scientific claims from candidate
enumeration transport.

Three transports were attempted in sequence, each recorded before candidate
selection:

1. Crossref / Retraction Watch production metadata;
2. PubMed indexed status notices;
3. Scite editorial-notice metadata;
4. final fixed public-web PubMed-domain search fallback.

The final fallback was explicitly declared the hard stop.

### Crossref / Retraction Watch

The runtime could not retrieve the needed Crossref REST payload and the
Retraction Watch dataset was not practically retrievable through the available
web layer.

No candidate was selected.

### PubMed direct transport

NCBI ESearch/EFetch endpoints and PubMed search pages were not accessible through
the available web/runtime interface.

No candidate was selected.

### Scite transport

The connected Scite MCP account returned a hard monthly-usage-limit error before
returning any candidate result.

No candidate DOI/title/status was exposed from Scite.

### Final fixed web-search fallback

The six pre-registered fixed searches were issued together.

The web layer returned a merged, non-query-attributable result set rather than
six preservable search-result sets.

Visible results were overwhelmingly/only expression-of-concern notices.

That means the experiment could not reconstruct the separate frozen:

- RETRACTED_CURRENT pool;
- MATERIAL_CORRECTION_HISTORICAL pool;
- CONCERN_CURRENT pool

as required by the pre-registration.

Running the six queries again separately would violate the final fallback's hard
stop:

> use the first returned result set; no extra search query because transport or
> candidates are inconvenient.

Therefore candidate enumeration stops here.

## Evidence-preservation consequence

The returned public-search results are classified only as:

`POOL_METADATA_PREVIEW_EXPOSURE`

They are not validation cases and receive zero experiment credit.

No DOI from the merged result set is promoted.

No control article is selected.

No L/S prompt is written.

No model run is executed.

## Why this is not REJECT

The kill rule for P165-A/P165-B concerns:

- legal-specific protocol machinery;
- existing scientific methods already owning the construct;
- absence of consequential latent status cases;
- retrieval-only value.

None of those claims was tested.

The runtime failed earlier, at deterministic sample construction.

Therefore:

> **transport failure ≠ scientific/protocol failure**

## Why transport is not repaired again

The pre-registration intentionally converted repeated transport repair into a
bounded failure state.

A fourth post-exposure redesign would make the sample increasingly analyst-shaped
and reward persistence until a runnable experiment appears.

That would be worse evidence than an indeterminate result.

## Project-level interpretation

H-19 remains scientifically unresolved.

The scholarly-status target remains conceptually credible, but it is not the
current best use of this runtime.

Because the sponsor has explicitly authorised continued active discovery, the
project should now move to an already-earned Cycle 2 reserve rather than idle or
keep repairing #165.

## Next-direction recommendation

Choose Run A's parked candidate:

> `TECHNICAL_STANDARD_AUTHORITY_HANDOFF`

before Run C's `OFFICIAL_DERIVED_VIEW_LAG`.

Reason:

- Run A tests a potentially **new failure family**;
- it has two completed official EU regulatory chains already identified;
- it can be evaluated directly from authoritative documents without another
  external execution transport;
- success or failure changes corpus taxonomy/coverage;
- Run C mostly tests whether an existing #93 family deserves a broader label.

Run C remains a strong reserve.

## Final disposition

# **INDETERMINATE / TRANSPORT_BLOCKED**

No project-identity conclusion is allowed from #165.

Proceed to a fresh bounded experiment rather than repairing transport after the
hard stop.
