# Needle adversarial failure gate v0.1 — Issue #88

**Date:** 2026-09-23  
**Status:** COMPLETE / PARITY  
**Purpose:** determine whether Needle Method prevents consequential legal-research failures on fresh cases selected from failure mechanisms discovered before the gate.

## Why #87 is insufficient for this claim

Needle Relay #87 produced 15/15 substantively correct Stage-B conclusions across R/M/C.

That is useful evidence about handoff reconstruction burden, but it creates a ceiling effect for the stronger project question:

> does Needle prevent an error that an equally capable ordinary research workflow would actually make?

Issue #88 tests that question without selecting cases because a baseline already failed them.

## Fixed failure strata

Fresh cases may be admitted only from failure mechanisms already evidenced before #88:

1. source-state / ex-post back-projection;
2. language or corrigendum scope asymmetry;
3. status/set-state separated from legal applicability;
4. unchanged parent text with changed legal effect;
5. source origin separated from legal authority/recognition;
6. temporal precision or boundary loss.

The deriving cases in Issues #61, #64, #67, #77, #78, #81, #83 and #85 are calibration material, not test cases.

## Phase A arms

### R — strong boring baseline

- GPT-5.6 Sol;
- high reasoning;
- web search;
- official/primary sources preferred;
- explicit instruction to answer carefully, identify uncertainty, and explain the legal basis;
- no Needle vocabulary/checklist;
- no repository access.

### M — Needle Method

Exactly the same model, reasoning and source access, plus explicit discipline for:

- source origin versus legal authority/recognition;
- exact target and scope;
- source-state-as-of versus ex-post/current legal state;
- temporal perspective and operative boundary;
- authentic-language/expression scope where relevant;
- uncertainty and unresolved points;
- forbidden inferences.

No canonical persistence in Phase A.

## Primary outcomes

The primary evidence is consequential answer behavior, not note aesthetics or source-reopening counts.

Record:

- correct/incorrect conclusion;
- consequential false claim;
- unsupported certainty;
- current/historical inversion;
- source-state/ex-post confusion;
- status/application confusion;
- language/scope projection;
- source-origin/authority confusion;
- temporal-boundary loss;
- correct abstention;
- decisive sources used;
- whether the reasoning explains why the conclusion follows.

Simple source reopening is not a failure.

## Decision matrix

- R fail / M pass -> strong Method evidence for that pre-registered failure class.
- R pass / M pass -> parity; Needle-specific value not demonstrated for that case.
- R fail / M fail -> Method does not solve that failure class.
- R pass / M fail -> negative evidence against Method.

Do not reinterpret these categories after results exist.

## Phase B — Core only when persistence has a job

A Phase-A case may enter Phase B only if:

1. Method first produces a correct representation;
2. a pre-sealed changed follow-up requires historical/repeated-state reconstruction rather than restating Question A;
3. persistence has a plausible existing canonical owner, or a separately preserved failure independently earns a repair.

Compare M versus C on that follow-up.

Core earns problem-class value only from an actual M-degradation/C-preservation event, or a material repeated-query cost reduction that a competent Method dossier cannot match.

M/C parity leaves Core optional.

## Blinding and execution

Before any R/M execution:

- final admissible cases are fixed;
- exact prompts and answer keys are sealed;
- hidden files remain outside Git;
- SHA-256 commitments are committed;
- same execution boundary is used for all arms;
- one stateless request per investigator;
- no answer key, repository context, conversation object or previous-response context is supplied.

No Method prompt repair is allowed after observing an R failure.

## Architecture guardrail

A hard case does not authorise implementation.

No Full-Needle surface re-enters during this gate. Core contracts are not repaired during Phase A. The gate tests the present Method, not a moving target.

## Stop condition

The gate succeeds scientifically even if Needle fails.

If R and M remain parity across genuinely adversarial fresh cases, the project must reduce the strength of its Method-distinctiveness claim rather than inventing a harder benchmark after the fact.


## Sealed Phase-A suite — 2026-09-23

The six exact cases and R/M prompts were fixed before any investigator run.

Case IDs:

1. `adv-polish-visa-backprojection`
2. `adv-nis2-italian-heading`
3. `adv-chatgpt-vlose-applicability`
4. `adv-harmonised-standard-restriction`
5. `adv-ets-private-verifier`
6. `adv-licence-1300-boundary`

The public hash commitments are canonical in:

`fixtures/value-gates/issue88-sealed-manifest-v0.1.json`

Phase A requires exactly 12 stateless requests: six R and six M.

Execution properties are frozen:

- `gpt-5.6-sol`;
- reasoning effort `high`;
- web search enabled;
- `store=false`;
- one independent request per run;
- no conversation object;
- no `previous_response_id`;
- no repository context;
- no answer key;
- no cross-arm outputs.

The no-admin PowerShell runner is intentionally kept outside Git until execution
because it contains the exact sealed questions. Its SHA-256 is committed in the
public manifest.

Do not repair Method, replace cases, or add Core before the 12 Phase-A results
exist.


## Phase-A result — 2026-09-23

Execution integrity passed:

- 12/12 requests completed;
- six R and six M;
- all returned `gpt-5.6-sol`;
- high reasoning, web search, `store=false`, stateless;
- 12 unique response IDs;
- every successful-run `prompt_sha256` matches the exact precommitted sealed prompt packet;
- revealed prompt and answer-key artifacts match their SHA-256 commitments.

The Windows runner required a transport-only UTF-8 repair after the original
wrapper failed at HTTP JSON parsing before any investigator response existed.
No scientific input changed.

Outcome under the pre-registered matrix:

- `adv-polish-visa-backprojection`: R PASS / M PASS;
- `adv-nis2-italian-heading`: R PASS / M PASS;
- `adv-chatgpt-vlose-applicability`: R PASS / M PASS;
- `adv-harmonised-standard-restriction`: R PASS / M PASS;
- `adv-ets-private-verifier`: R PASS / M PASS;
- `adv-licence-1300-boundary`: R PASS / M PASS.

No consequential baseline failure, no Method rescue, no Method regression.

Therefore the gate's stop condition applies: do not invent a harder benchmark
after seeing parity.

Phase B is not run. Issue #87 already tested persistence/handoff and found no
Core-over-Method win; #88 produced no new evidence warranting Core re-entry.

Project decision:

> **Shrink the default identity to Needle adversarial corpus + evaluation protocol.**

Needle Method remains an optional handoff/reporting convention. Needle Core
remains optional case-earned persistence. Full Needle remains parked.

Canonical result:
`fixtures/value-gates/issue88-phase-a-results-v0.1.json`

Canonical audit:
`docs/audits/needle-adversarial-failure-gate-2026-09-23.md`
