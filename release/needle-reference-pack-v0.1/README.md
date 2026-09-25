# Needle Reference Pack v0.1

Needle Reference Pack v0.1 is a **derived reference layer** over the frozen Morrow // Needle adversarial legal-research corpus.

It is intended for researchers, evaluators and developers who need a compact, reproducible way to inspect the corpus, navigate its existing evidence owners, or use exposed cases for regression/reference work without reconstructing the project's issue history.

It is **not** a standalone copy of the underlying legal evidence, a current-law service, a complete legal benchmark, or evidence that a model or workflow using Needle outperforms an ordinary source-grounded baseline.

## Frozen source

This pack is derived from:

- reference name: `NEEDLE_CORPUS_REFERENCE_2026-09-25`;
- reference commit: `c3416514e054e8c3c61ca4d42c4534eca21e1cc5`;
- canonical index: `corpus/index-v0.1.json`;
- canonical index blob: `ecaab3f59fe118b71d2cafa19f05363a65ae49a1`;
- corpus shape: **81 cases / 26 trap classes**.

Generated files are views over that canonical index. Do not edit generated pack files as legal truth.

## File map

| File | Purpose |
| --- | --- |
| `manifest.json` | Pack identity, frozen-source identity, counts, exposure policy and generation contract. |
| `cases.jsonl` | One complete canonical case record per line, sorted by stable case ID. |
| `classes.json` | Trap-class definitions with derived case counts and member case IDs. |
| `evidence-map.json` | De-duplicated navigation from case evidence refs to repository issue/path owners. |
| `catalog.md` | Human-readable class and case catalog with stable internal anchors. |
| `README.md` | This quickstart and safe-use guide. |
| `checksums.sha256` | Deterministic payload checksums, produced by the validation/release step. |

The builder is `scripts/build_reference_pack.py`. Validation is owned by `scripts/validate_reference_pack.py`.

## Human use

For a human inspection:

1. start with `catalog.md`;
2. follow a stable case ID or trap-class anchor;
3. read the case's decisive trap and exposure state;
4. use the listed `issue:` / `path:` identifiers to locate the existing evidence owner through `evidence-map.json`;
5. inspect the underlying evidence chain before making or updating a legal claim.

The catalog is a navigation aid. Its short trap text is not a substitute for the evidence owner.

## Machine use

Read cases line-by-line without reverse-engineering the canonical index:

```python
import json
from pathlib import Path

pack = Path("release/needle-reference-pack-v0.1")

with (pack / "cases.jsonl").open(encoding="utf-8") as handle:
    cases = [json.loads(line) for line in handle if line.strip()]

classes = json.loads((pack / "classes.json").read_text(encoding="utf-8"))

print(len(cases))
print(len(classes["classes"]))
```

A consumer should treat stable IDs and source-preserved fields as data. Do not infer new class memberships, legal outcomes or freshness from the packaging layer.

## Evidence refs and access

Case records preserve their original `evidence_refs` exactly.

- `issue:<number>` refers to a repository issue that owns or records the relevant evidence chain.
- `path:<repository/path>` refers to a repository-relative evidence artifact.
- `evidence-map.json` converts these refs into stable navigation records and pins repository-path URLs to the frozen reference commit.

Repository-hosted owners require access to the repository in the environment where the pack is distributed. If an owner is inaccessible because repository access is unavailable, treat that as **missing access**, not as evidence that the underlying source or claim does not exist.

The pack intentionally does not copy the legal-source contents behind these refs. Public legal sources remain owned by their existing evidence chains.

## DERIVATION and EVALUATION cases

`provenance.role` distinguishes why a case is present.

**DERIVATION** cases were admitted from bounded research/discovery because they helped define or generalise a failure mechanism represented by a trap class. They are reference/regression examples; their presence is not a quality score or a claim of benchmark completeness.

**EVALUATION** cases entered through predeclared evaluation work. Evaluation provenance does not make a case permanently blind: once revealed into this public/reference corpus, it is exposed and becomes regression-only.

The frozen corpus contains both roles. Consumers should preserve the role rather than flattening evaluation cases into ordinary derivation examples.

## Surfaced vs latent evaluation modes

Evaluation cases can carry `evaluation_mode`.

**SURFACED_TRAP_ADJUDICATION** means the task prompt explicitly surfaced or strongly cued the dangerous distinction. It tests whether the distinction is adjudicated correctly once attention has been directed to it; it does not test unprompted discovery of the trap.

**LATENT_TRAP_DETECTION** means the evaluation is designed around detecting the relevant failure mechanism without that mechanism being surfaced in the same way.

Do not combine these modes into one undifferentiated performance claim. They test different things.

## Exposure and reuse

Every case in this pack is scientifically exposed.

The required reuse state is:

- `blind_reuse = false`;
- `future_use = REGRESSION_ONLY`.

These cases may be used for regression checks, worked examples, reference, debugging and method inspection. They must **not** be represented as fresh blind validation.

Fresh blind validation requires a new, independently selected and sealed case under an appropriate predeclared protocol.

## Historical state, current law and source drift

This pack is a frozen reference snapshot, not a promise of current legal state.

A case may intentionally concern:

- a historical legal state;
- an earlier source view;
- a later correction or consolidation;
- a tracker or derived view that lagged primary law;
- a status or applicability boundary that changed after the case's target date.

For a current-law question, re-open the evidence chain and verify the relevant authoritative source, version, jurisdiction and date. Do not treat a currently accessible source page, current consolidation or this pack's freeze date as interchangeable with the legal/source state the case was designed to test.

## What this pack does not prove

The pack does **not** prove:

- completeness across EU law, jurisdictions or failure mechanisms;
- representative population performance;
- model superiority;
- workflow superiority;
- that any trap class is equally important or equally frequent;
- that exposed cases remain valid as fresh blind tests;
- that a concise catalog statement is sufficient legal authority;
- that historical evidence automatically describes current law.

A particularly important frozen null is Issue #214. In its pre-frozen challenge-set pilot, supplying the frozen adversarial index plus its adversarial framing produced **0 diagnostic rescues**, **0 correctness-only treatment advantages**, and parity on the three adversarial R/C pairs. The pre-registered conclusion was **NO DIAGNOSTIC VALUE DEMONSTRATED / SIMPLIFY**.

That result does not prove the corpus is useless or establish population equivalence. It does mean this pack must not be marketed or interpreted as demonstrated evidence that giving Needle to an equally capable researcher/model improves decision-level or detection-level outcomes.

## Rebuild and validation

From a clean checkout at a compatible Python 3 version, the release path is:

```bash
python3 scripts/build_reference_pack.py
python3 scripts/validate_reference_pack.py
```

The builder requires no network access and uses only the Python standard library. It fails closed if the canonical source blob, reference status or frozen 81/26 shape changes.

The validation step owns pack membership, cross-file consistency, referential integrity, source identity, exposure policy, deterministic rebuild checks and `checksums.sha256`.

To verify a frozen released pack after checksums exist:

```bash
sha256sum -c release/needle-reference-pack-v0.1/checksums.sha256
```

If your platform does not provide `sha256sum`, use any SHA-256 implementation and compare the recorded digest for each listed file.

## Safe interpretation rule

Use this pack to **find and test known adversarial legal-research failure patterns**. Follow the evidence chain before making a legal claim, preserve the target date and source state, and keep exposed cases in regression/reference use.

The pack is a compact map of accepted project evidence. It is not the evidence itself.
