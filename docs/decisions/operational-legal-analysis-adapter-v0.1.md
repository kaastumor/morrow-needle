# Operational legal-analysis adapter v0.1

Status: **ACTIVE DESIGN BOUNDARY**  
Owner: P2 / Issue #21

## Decision

The successful Regulation (EU) 2026/2104 live case proves the positive path, but its case builder is not the recurring product loop. The operational monitor must not acquire CELEX-specific branches to reproduce that success.

The next integration boundary is a generic **operational legal-analysis adapter** between source classification and `build_operational_result`.

Inputs are limited to:

- the official feed event;
- the immutable current Source Observation(s);
- the source-change classification and its evidence references;
- any eligible prior baseline;
- canonical resolver/parser/mutation services.

The adapter returns exactly one bounded outcome:

1. `LEGAL_CHANGE_VERIFIED`, with canonical mutation reference(s), official evidence references, explanation projection, and an explicit verification route;
2. `LEGAL_NON_IMPACT_VERIFIED`, only when positive evidence establishes scoped non-impact;
3. `ABSTAIN_LEGAL_UNRESOLVED`, retaining the reason and unknowns.

It does **not** return a public card. Card rendering remains a projection of the operational result.

## Authority boundary

A missing source baseline does not prevent legal verification when an authentic modifying/correcting act independently and explicitly proves the mutation. In that case:

- source classification remains `UNRESOLVED`;
- verification route is `AUTHENTIC_LEGAL_CAUSE`;
- no before/after source diff is claimed;
- no consolidated after-state is fabricated;
- unresolved source-comparison state remains visible on the result/card.

A feed `UPDATE` action, chronology, text similarity, or a model inference can never satisfy this route.

## Representation duplication

Multiple Formex streams or source representations may contain the same legal instruction. Representation occurrences are evidence locations, not independent legal causes. The adapter must collapse semantically identical parsed instructions before mutation emission while retaining the occurrence evidence for provenance/audit.

## Anti-bespoke invariant

Production integration MUST NOT branch on a known CELEX identifier (including `32026R2104`) or a fixture-specific locator/key. A positive operational result must arise from generic parsing and canonical verification rules. Case-specific scripts remain reproducible adversarial fixtures/probes and provenance, not production dispatch logic.

## Idempotence

Given the same event identity, same immutable observations, same eligible baseline and same canonical analyzer version, the adapter must emit the same canonical outcome identity. Reprocessing may add observation/provenance occurrences but must not create a second legal mutation merely because the same instruction appears in another representation or notification.

## Integration gate for Issue #21

The recurring monitor may emit a `CHANGE_FEED` card only after this adapter is wired into `run_operational_monitor_once.py` and tests demonstrate:

- one authentic-cause positive case;
- one representation-only/non-impact case;
- one unresolved/insufficient-evidence abstention;
- duplicate instruction representations do not duplicate mutations;
- rerunning the same evidence is idempotent;
- no CELEX-specific production branch exists.

Until then, the 2026/2104 live builder is proof that the components compose, not proof that the recurring operational loop is complete.
