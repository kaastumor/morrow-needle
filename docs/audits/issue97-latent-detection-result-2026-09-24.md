# Issue #97 — latent-trap detection result

**Date:** 2026-09-24  
**Status:** COMPLETE — STOPPED ON FULL PARITY  
**Evaluation mode:** LATENT_TRAP_DETECTION  
**Stage:** v0.3 manual 8-chat closure test

## Executive result

All eight submitted outputs passed the frozen per-case rubric **before arm
mapping was used**.

After reveal, all four R/M pairs were:

> **R PASS / M PASS**

Therefore the exact v0.3 stop rule fires.

No matched controls, replications, reserve cases or further Method experiments
are required.

## Blind grades

| Result file | Blind grade | SHA-256 |
|---|---|---|
| RESULT-01.txt | PASS | `ebb20807346770cd2961daf28256431c6603544ec0a191f61dcaebd53c823e46` |
| RESULT-02.txt | PASS | `24e3d1d9cdae355b78c3ed581fbd7e36be329b91df99b292d7e93e9ee7820431` |
| RESULT-03.txt | PASS | `1b294dbf075b49cf4eee3c503fe6065f55291498bafd8cd8f59d87b80b046d09` |
| RESULT-04.txt | PASS | `dae7c2f8464a2cab40fa0777e5c9f7ff5fcb5ff7f9fd4e02257478b648312cfa` |
| RESULT-05.txt | PASS | `d858427515af7ac56e07136297369f30d4aae400ee6e73853ddc0533be380e58` |
| RESULT-06.txt | PASS | `f4de596fd54cce4abbef23ce1783f696e13c4dbf7e3478574b3672067b33f479` |
| RESULT-07.txt | PASS | `9052d00d4d0dbba4b31c9cafacb36a08fd7dc11707536d90eaa5acf3a7107b58` |
| RESULT-08.txt | PASS | `5a2045169933c260df90efae97c472a436b9a0d0c3faf4cdb99486224cbf3544` |

Style, answer length and citation count were not scoring criteria.

## Arm reveal

| Case | R result | M result | Pair |
|---|---|---|---|
| EU–Chile parallel instrument lifecycle | RESULT-01 PASS | RESULT-07 PASS | R_PASS_M_PASS |
| Haringvliet / Leenheerenpolder judicial invalidity | RESULT-05 PASS | RESULT-03 PASS | R_PASS_M_PASS |
| EN 50434:2014 at 320 r/min | RESULT-04 PASS | RESULT-08 PASS | R_PASS_M_PASS |
| Temu on 15 June 2024 | RESULT-02 PASS | RESULT-06 PASS | R_PASS_M_PASS |

## Why each case passed

### EU–Chile

Both outputs detected that the umbrella “modernised agreement” contains two
separate legal instruments. Both attached 1 February 2025 to the ITA, not the
AFA, and both identified partial AFA provisional application from 1 June 2025.

### Haringvliet

Both outputs detected the later CJEU invalidity holding and separated the 2015
list state from the later validity judgment. Neither treated Decision 2015/72
alone as a complete 2026 legal-history answer.

### EN 50434:2014 / 320 r/min

Both outputs found the restricted OJ reference status, applied the >300 r/min
threshold, and rejected the claimed presumption of conformity for Annex I
points 1.1.2(a) and 1.3.3.

### Temu / 15 June 2024

Both outputs distinguished Temu's already-existing VLOP designation and general
DSA duties from the later application point for the additional VLOP-specific
Section 5 obligations.

## Stop rule

The pre-registered rule was:

> If all four adversarial pairs are R-pass/M-pass, stop after 8 chats and
> conclude latent-detection value is not demonstrated in this stage.

That condition is met exactly.

Do not run:

- matched near-miss controls;
- confirmation pairs;
- v0.1/v0.2 runners;
- harder post-result Method cases.

Doing so would move the goalposts after a clean null/parity result.

## Scientific interpretation

### H-15 — reject for the tested workflow

The bounded Needle Method checklist did **not** demonstrate improved latent-trap
detection over the strong baseline on these four fresh adversarial classes.

This is stronger than #88 for the detection construct because these v0.3
questions did not explicitly name the decisive trap.

It is still bounded evidence:

- four adversarial cases;
- one response per arm/case;
- manual consumer-ChatGPT execution;
- no matched controls were needed because the stop rule fired on full parity.

The correct conclusion is **no demonstrated Method advantage**, not a universal
claim that checklists can never help.

### Execution-provenance limitation

The eight submitted result files prove the answer text and are preserved by
hash.

They do not contain machine-verifiable metadata proving that each UI run used:

- Temporary Chat;
- Unpersonalized mode;
- GPT-5.6 Sol;
- High reasoning.

Those settings were frozen in the sponsor execution protocol and are treated as
sponsor-executed conditions rather than independently machine-verified run
metadata.

This limitation should stay visible in any external claim.

## Project consequence

The project no longer has an unresolved Method-correctness value question worth
chasing.

Evidence now separates cleanly:

- #87: bounded handoff/reporting packaging benefit;
- #88/#95: no demonstrated Method advantage on surfaced-trap adjudication;
- #97: no demonstrated Method advantage on latent-trap detection in the tested
  workflow;
- #87: no default Core-over-Method persistence win.

Therefore:

> **Needle Method remains an optional handoff/reporting convention, not a
> project-specific correctness layer.**

Core and Full Needle remain parked.

The canonical project identity stays:

> **adversarial legal-research corpus + evaluation protocol**

## Next direction

Do not create another Method value gate.

The next research value should come from the corpus itself:

- better failure-mode coverage;
- stronger source-system/jurisdiction diversity;
- metamorphic legal-state pairs where one legally material variable changes and
  the expected answer changes in a precise, falsifiable way;
- fresh sealed challenges only when a concrete evaluation claim justifies them.

Issue #97 should close as a successful negative/parity result.
