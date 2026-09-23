# Needle Relay pilot audit — Issue #87

**Date:** 2026-09-23  
**Status:** PILOT COMPLETE / FULL CONFIRMATION PENDING

## Integrity

The sealed Stage-A, Stage-B and answer-key artifacts matched their pre-execution
SHA-256 commitments exactly before evaluation.

The first three Arm-C attempts returned `CORE ACCESS MISSING`. They are
preflight failures, not experimental runs. Before any valid Core run, Arm C was
moved to one frozen Core reference pack without changing any case, hidden
follow-up, answer key, or completed R/M artifact.

## Result

All 9 independent Stage-B answers were substantively correct.

The pilot therefore found no raw correctness advantage. The signal is handoff
degradation and reconstruction burden.

### EUDR

All arms reconstructed the 15 August 2025 legal state correctly.

- R preserved the double-postponement date pairs but required amendment-force
  timing to be re-established.
- M preserved the amendment chronology/force timing but required one exact
  historical Article 38(3) scope detail to be reconstructed.
- C preserved the three application-date states and historic scoped override,
  but B still reopened sources to establish amendment-force timing.

No clear Core-over-Method advantage appeared.

### DMA

All arms correctly separated gatekeeper designation from the later Articles
5–7 compliance boundary.

- R already contained the decisive facts, but B nevertheless reopened official
  sources and searched for corroboration.
- M answered entirely from the handoff.
- C answered entirely from the handoff.

Method and Core were parity.

### GDPR control

- R preserved the application date and distinction but omitted the exact
  entry-into-force date, so B reopened EUR-Lex.
- M preserved publication, force and application dates; B reopened nothing.
- C correctly chose PERSISTENCE_NOT_JUSTIFIED, but its Method dossier omitted
  the exact force date, so B reopened official material.

Core cannot rescue information that the handoff dossier never preserved.

## Provisional interpretation

H-12 (Method improves handoff reproducibility) receives provisional support:
Method showed the lowest reconstruction burden in this pilot.

H-13 (Core materially improves handoff beyond Method) is not supported by the
pilot.

Do not promote or shrink the project yet. One run per arm per case is weak
evidence, and two pre-sealed confirmation cases remain.

## Full confirmation

Proceed only with the two cases sealed before execution:

1. battery due-diligence postponement;
2. RoHS 7(a) scope split.

No new cases, criteria or architecture are added.

If Method remains materially as good as or better than Core, activate the Issue
#87 shrink rule toward Method + corpus/protocol, with Core becoming
individually-earned optional persistence rather than part of the default
identity.

If Core materially wins on the remaining state/scope cases, retain Method +
Core and define exactly which problem classes earn persistence.
