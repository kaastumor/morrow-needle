# Needle Reference Pack v0.2

Needle Reference Pack v0.2 is a **derived failure-analysis navigation layer** over the same frozen Morrow // Needle known-failure reference corpus used by v0.1.

It keeps the frozen corpus/data semantics unchanged and adds one new navigation surface:

- `failure-analysis-guide.md` — how to use Needle for legal failure analysis, evaluation design, debugging and regression-fixture derivation without forcing taxonomy or creating a second legal truth store.

The pack is **publicly inspectable/reference material**. The repository currently has no project license, so public visibility must **not** be read as a grant making this openly licensed reusable material. Linked or third-party legal evidence remains under its own rights.

## Frozen source

This pack is derived from exactly the same frozen scientific source as v0.1:

- reference name: `NEEDLE_CORPUS_REFERENCE_2026-09-25`;
- reference commit: `c3416514e054e8c3c61ca4d42c4534eca21e1cc5`;
- canonical index: `corpus/index-v0.1.json`;
- canonical index blob: `ecaab3f59fe118b71d2cafa19f05363a65ae49a1`;
- corpus shape: **81 cases / 26 trap classes**;
- all cases remain exposed with `blind_reuse=false` and `future_use=REGRESSION_ONLY`.

v0.2 does not add a scientific case, class, evaluation result or external-failure dataset.

## File map

| File | Purpose |
| --- | --- |
| `manifest.json` | Pack identity, frozen-source identity, counts, exposure policy and failure-analysis navigation metadata. |
| `cases.jsonl` | The same complete frozen canonical case records, sorted by stable case ID. |
| `classes.json` | The same trap-class definitions, counts and member case IDs. |
| `evidence-map.json` | The same navigation from case evidence refs to repository issue/path owners. |
| `catalog.md` | Human-readable v0.2 class/case catalog over the frozen source. |
| `failure-analysis-guide.md` | Supported failure-analysis workflow, truth-ownership rules and worked navigation to accepted #339 evidence. |
| `checksums.sha256` | Deterministic payload checksums. |
| `README.md` | This safe-use and rebuild guide. |

## Failure-analysis use

Start with `failure-analysis-guide.md` when the job is to analyze a known legal-AI or legal-research failure.

The guide makes these rules explicit:

- an existing trap class is used only when it causally fits;
- **`NO_EXISTING_CLASS_MATCH` is a valid result**;
- exposed/known failures do not become fresh validation;
- historical/source-state distinctions must remain attached to their exact owners;
- boundary/opposite-error evidence is preserved only when an accepted owner supports it;
- regression PASS/FAIL criteria are used only when an evidence/result owner supports them;
- the pack navigates to truth owners rather than becoming one.

The first accepted worked-use owner is:

- Issue #339;
- `docs/uses/issue339-external-failure-packet-use-2026-09-26.md`.

That external failure is **not** copied into the canonical corpus.

## Evaluation and exposure

The frozen corpus still distinguishes `DERIVATION` from `EVALUATION`.

Evaluation modes remain:

- `SURFACED_TRAP_ADJUDICATION`;
- `LATENT_TRAP_DETECTION`.

Every frozen case remains exposed and `REGRESSION_ONLY`. Fresh blind validation still requires a new independently selected and sealed case under the canonical evaluation protocol.

## What v0.2 does not prove

v0.2 does not prove:

- representative legal-AI performance;
- model, workflow or product superiority;
- generic value while answering ordinary legal questions;
- that every external failure has a Needle class;
- that every known failure should become a regression fixture;
- that one positive #339 use observation generalizes to a population;
- that concise pack text is legal authority.

Issue #214 remains the hard null for corpus-assisted latent diagnostic/correctness advantage. Issue #327 remains `BASELINE_SUFFICIENT` for its generic post-answer legal-research use. Issue #339 is one positive observed failure-analysis packet use and one demonstrated v0.1 surface gap.

## Rebuild and validation

From a clean checkout:

```bash
python3 scripts/build_reference_pack_v02.py
python3 scripts/validate_reference_pack_v02.py --write-checksums
python3 scripts/validate_reference_pack_v02.py
```

The v0.2 validator validates v0.1 first, so a successful v0.2 validation also checks that the historical v0.1 release still matches its frozen source and checksums.

The builder uses only the Python standard library and the proven v0.1 derivation functions. It requires no network access.

## Safe interpretation rule

Use v0.2 to **analyze and preserve known legal-information failures**, not to manufacture a class match or a fresh-validation claim.

The pack is a compact method/navigation surface over accepted evidence. Legal facts, boundaries and executable regression criteria remain owned by the exact referenced evidence/result chains.
