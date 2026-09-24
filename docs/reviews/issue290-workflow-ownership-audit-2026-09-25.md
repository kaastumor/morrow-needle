# #290 workflow ownership audit — active vs passive GitHub Actions

Date: 2026-09-25  
Mode: **MAINTAIN**  
Baseline: main after #288 / commit `32d5bf49a65a58f784f8ecf7fa8cda9009001087`

## Decision

# **SIMPLIFY — keep 2 automatic workflows; make 23 workflows manual-only**

The repository contains 25 workflow files.

No workflow has a scheduled/cron trigger.

Before this run:
- 2 workflows were already manual-only;
- 21 specialist workflows still reacted automatically to path changes;
- 2 shared workflows owned the current automatic repository gates.

After this run:

> **2 KEEP_AUTO / 23 MANUAL_ONLY / 0 RETIRE_WORKFLOW**

No historical workflow is deleted.

## Current automatic owners

### `repository-sanitation.yml` — KEEP_AUTO

Current owner:
- repository integrity;
- secret/local-path/generated-file sanitation boundary.

Automatic PR + main execution remains appropriate because this safety property applies to
the whole repository rather than one historical subsystem.

### `unit-tests.yml` — KEEP_AUTO

Current owner:
- shared executable regression suite;
- current adversarial-corpus validation;
- current MVP JavaScript regression.

It runs:
- full `python -m pytest -q`;
- `scripts/validate_adversarial_corpus.py`;
- Node MVP tests.

This is the default shared regression owner. Specialist workflows do not need to rerun
subsets automatically merely because their old paths change.

## Workflow dispositions

| Workflow | Previous automatic role | Current owner analysis | Disposition |
| --- | --- | --- | --- |
| `repository-sanitation.yml` | repo sanitation on PR/main | unique current repository-integrity owner | **KEEP_AUTO** |
| `unit-tests.yml` | full Python/current-corpus/MVP tests | unique current shared executable regression owner | **KEEP_AUTO** |
| `cellar-feed-discovery.yml` | none; dispatch only | historical Cellar anchor discovery | **MANUAL_ONLY — unchanged** |
| `operational-monitor.yml` | none; dispatch only | frozen operational pilot diagnostic | **MANUAL_ONLY — unchanged** |
| `authentic-amendment.yml` | authentic amendment subset test on path push | deterministic test is inside full pytest; live probe is historical/diagnostic | **MANUAL_ONLY** |
| `cellar-feed.yml` | Cellar update subset test on path push | subset test is inside full pytest; live endpoint probe remains useful only on demand | **MANUAL_ONLY** |
| `cellar-probe.yml` | source-adapter subset test on path push | subset test is inside full pytest; live Cellar representation probe is historical | **MANUAL_ONLY** |
| `dependency-ripple-view.yml` | X-Ray tests/build on path push | stopped derived product surface; tests remain in shared suite | **MANUAL_ONLY** |
| `foundation-audit.yml` | broad subset audit on push/PR | all deterministic pytest coverage is already exercised by full shared suite; no unique current release gate | **MANUAL_ONLY** |
| `gold-corpus.yml` | legacy Gold Corpus tests + validator on push/PR | old Gold Corpus is not the current adversarial corpus owner; validator remains reproducible on demand | **MANUAL_ONLY** |
| `half-life-discovery.yml` | Half-Life regressions on path push | stopped derived surface; live probe remains historical evidence | **MANUAL_ONLY** |
| `half-life-view.yml` | Half-Life view test/build on path push | stopped projection; build remains reproducible manually | **MANUAL_ONLY** |
| `live-ast.yml` | AST parser subset tests on path push | full pytest owns deterministic regressions; live fixture build is diagnostic | **MANUAL_ONLY** |
| `money-corrigendum-audit.yml` | case-specific tests on path push | tests remain in shared suite; live legal-source probe is historical | **MANUAL_ONLY** |
| `operational-pilot.yml` | operational subset + live sample on path push | public-product operational horizon is stopped | **MANUAL_ONLY** |
| `operational-replay-discovery.yml` | replay discovery on path push | historical discovery helper, not a current gate | **MANUAL_ONLY** |
| `reach-dependency-ripple.yml` | REACH live probe on path push | historical X-Ray discovery evidence | **MANUAL_ONLY** |
| `recent-create-amendment-discovery.yml` | discovery search on path push | automatic discovery is not a current standing mode | **MANUAL_ONLY** |
| `recent-legislation-update-discovery.yml` | discovery search on path push | automatic discovery is not a current standing mode | **MANUAL_ONLY** |
| `reg2104-live-case.yml` | live case replay/card build on path push | valuable historical end-to-end case, but no current product/release owner | **MANUAL_ONLY** |
| `retrieval.yml` | retrieval test/demo on push/PR | Retrieval is a passive historical projection; test remains in full suite | **MANUAL_ONLY** |
| `semantic-source.yml` | Change Atom test + live source on path push | Change Atom machinery is conditional/historical under #288; tests remain shared | **MANUAL_ONLY** |
| `source-anomaly-view.yml` | Source Anomaly test/build on path push | stopped derived projection | **MANUAL_ONLY** |
| `split-temporal-audit.yml` | case-specific temporal audit on path push | deterministic test remains in shared suite; probe is historical | **MANUAL_ONLY** |
| `thread-article3.yml` | Thread tests/build/live probes on path push | Thread is a passive historical projection; tests remain in shared suite | **MANUAL_ONLY** |

## Why manual-only instead of deletion

The workflows still encode reproducible:

- official-source probes;
- historical case replays;
- artifact builders;
- subsystem-specific deterministic commands.

Deleting them would save little runtime beyond what trigger removal already saves and would
discard convenient historical execution evidence.

Manual dispatch preserves that evidence while removing the assumption that the subsystem
is under active continuous maintenance.

## Safety check

The change intentionally does **not** remove specialist tests from the repository.

The full shared test workflow still runs the complete Python test suite when its current
path trigger fires. The maintenance change removes duplicate/specialist workflow
invocation, not the underlying regression tests.

The current adversarial corpus also remains explicitly validated by the shared unit
workflow.

## Cost interpretation

This change should reduce future Actions event volume when passive historical paths are
edited.

No invoice saving is claimed:
- there are no cron schedules to eliminate;
- future event frequency is unknown;
- manual dispatch remains available.

The measured structural result is narrower:

> **automatic workflow ownership falls from 23 event-triggered workflows to 2 shared
> current gates.**

## Complexity outcome

- workflow files: still **25**;
- automatic current gates: **2**;
- manual historical/research workflows: **23**;
- deleted workflows: **0**;
- replacement workflows/dashboards/services: **0**.

This makes the active maintenance surface smaller without rewriting history.

## Successor allocation

The maintenance objective is complete when the trigger edits pass repository sanitation
and the shared regression gate.

The next purposeful mode should **not** revert automatically to taxonomy discovery.

The strongest bounded successor is:

> **REVIEW / RELEASE — assess whether the current 81-case / 26-class corpus can be frozen
> as a coherent reference release checkpoint without adding cases/classes or product
> scope.**

Why this mode:
- two consecutive structural simplification passes (#288 and #290) have reduced
  governance/maintenance debt;
- accepted scientific state is now large enough that a stable reference checkpoint is
  more useful than immediately extending classification breadth;
- release review can expose inconsistency in corpus metadata/docs/validation without
  creating another legal research experiment.

This is a successor allocation, not permission to create new taxonomy or product work.

## Final

# **SIMPLIFY**

Retain automatic execution only for:
1. repository sanitation;
2. shared unit/current-corpus validation.

Preserve every other workflow as manual historical/research evidence.
