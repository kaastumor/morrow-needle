# Needle adversarial failure gate — Phase A audit

**Issue:** #88  
**Date:** 2026-09-23  
**Status:** COMPLETE  
**Decision:** parity across all six pre-registered adversarial strata; reject Method correctness-distinctiveness claim.

## Executive result

Issue #88 was created because #87's 15/15 correct relay result left a ceiling-effect question unresolved:

> does Needle Method actually prevent consequential legal-research mistakes that an equally capable ordinary source-grounded workflow makes?

The answer from Phase A is **not demonstrated**.

All six sealed adversarial pairs ended **R-pass / M-pass**. The strong boring baseline independently caught every pre-registered trap:

1. ex-post consolidation back-projection;
2. authentic-language/corrigendum asymmetry;
3. designation versus downstream application;
4. unchanged identifier/text with changed legal effect;
5. private source origin versus legally recognised role;
6. sub-day / exact-time legal boundary.

There was no R-fail/M-pass rescue, no R-fail/M-fail unresolved mechanism, and no R-pass/M-fail Method regression.

Under the gate's pre-registered decision matrix, every case is therefore **parity for correctness**.

## Integrity

The successful run manifest records 12 completed requests, six R and six M, all returned by `gpt-5.6-sol`, high reasoning, web search enabled, `store=false`, stateless execution, with 12 unique response IDs.

The exact revealed sealed artifacts verify against the pre-run commitments:

- prompts SHA-256: `a8725af696f12eb286a1dec84c6e1df870a2a6ebd3409cee0db97d14f8354659`;
- answer key SHA-256: `8c32ed2c3506b6f508a4093cba171c166b759fb3f475c4956ff84657818cfde0`;
- sealed-artifacts ZIP SHA-256: `b818cb977ddd4e3759b3689d497c3f35d346ef8088a5ff30dc5d192b56549e33`.

Every `prompt_sha256` in the successful run manifest matches the corresponding exact prompt in the revealed sealed packet.

### Windows transport repair

The precommitted runner ZIP hash was `d66f9a00ab18599bb77b227eb21dd8c942d2eeea2d5c8af63b638a8ef90496bc`.

On Windows PowerShell 5.1 it failed at HTTP JSON parsing before any investigator response was produced.

A v2 wrapper was generated with SHA-256 `4c57dc2b45e32fa4b9a47e24b52f58bc9a105d5f632d931ed0281346e7a2f5bb`.

The only repair was transport-level: validate JSON locally, encode the request body explicitly as UTF-8 bytes, and send `application/json; charset=utf-8`.

No question, arm instruction, model, reasoning setting, web permission, storage setting or statelessness rule changed. The successful manifest independently proves that all 12 executed prompt hashes equal the precommitted sealed prompts.

This is recorded as a transparent execution-wrapper deviation, not a re-seal.

## Per-case evaluation

| Case | Pre-registered failure mode | R | M | Pair |
|---|---|---|---|---|
| `adv-polish-visa-backprojection` | source-state / ex-post back-projection | PASS | PASS | parity |
| `adv-nis2-italian-heading` | language / corrigendum scope asymmetry | PASS | PASS | parity |
| `adv-chatgpt-vlose-applicability` | status/set-state != application | PASS | PASS | parity |
| `adv-harmonised-standard-restriction` | unchanged text / changed legal effect | PASS | PASS | parity |
| `adv-ets-private-verifier` | source origin != legal authority/recognition | PASS | PASS | parity |
| `adv-licence-1300-boundary` | temporal precision / boundary loss | PASS | PASS | parity |

The R arm did not merely land on the right yes/no answers. It preserved the decisive distinctions demanded by the sealed key: historical source state versus current correction; Italian textual history versus substantive interpretation; notification versus designation; immediate restriction versus deferred deletion; private verification versus retained public powers; and actual receipt versus deemed lodgement.

M did the same with a more explicit source/authority/scope/time/forbidden-inference structure.

No Method rescue occurred.

## Method overhead — descriptive only

The gate did not pre-register token cost as a winner metric, so it is not used to manufacture a score.

Still, the successful manifest records:

- R output tokens: **38,652**;
- M output tokens: **52,817**.

Method therefore emitted about 37% more output tokens across the six cases while reaching the same substantive conclusions.

Input/total-token differences are less clean because web-search retrieval and caching varied between runs. The output difference is preserved as a practical overhead signal, not as a causal performance claim.

## Phase B decision

**Do not run Phase B from this result.**

The purpose of #88 was to discover whether the ordinary baseline actually breaks on pre-registered known failure mechanisms.

It did not.

Creating a new, harder persistence follow-up now because R survived would violate the gate's own stop condition against inventing a harder benchmark after seeing parity. Issue #87 already tested handoff persistence and found no Core-over-Method win.

Core therefore remains optional and does not re-enter the default project identity.

## Project-level interpretation

### H-14 — reject

The claim that Needle Method prevents consequential errors or unjustified certainty on these adversarial legal questions better than an equally capable source-grounded baseline is **not supported**.

The strong baseline solved all six fresh adversaries correctly.

### H-12 — narrow further

#87 still supports one bounded fact: structured Method dossiers can improve handoff/reconstruction packaging.

But #88 shows that the substantive distinctions themselves are not demonstrated to require a Needle-specific method. A capable source-grounded investigator can reconstruct them directly.

Therefore Method should no longer be treated as the primary project contribution. Retain it as an optional handoff/reporting convention where its structure is operationally useful.

### Canonical identity

Shrink again:

> **Morrow // Needle = adversarial legal-research corpus + evaluation protocol**

The durable contribution currently evidenced is the corpus of real legal-information traps, the discipline of pre-registration/sealing/adversarial comparison, the evidence ledger and the project's willingness to preserve parity/negative results.

Needle Method remains available as a convention. Needle Core remains optional persistence. Full Needle remains parked.

This is not project failure. It is the project successfully removing claims it could not distinguish from a strong baseline.

## No replacement horizon

#88 does not create a new feature queue, ontology task or harder benchmark.

The backlog may return to idle research/audit mode. Future work must arise from fresh evidence, a real anomaly, an unresolved canonical claim or an explicit sponsor research question—not from a need to make Needle win.
