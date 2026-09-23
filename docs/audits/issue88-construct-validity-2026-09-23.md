# Issue #88 construct-validity audit — trap detection vs adjudication

**Issue:** #95  
**Date:** 2026-09-23  
**Status:** CONSTRUCT INTERPRETATION REPAIRED  
**Historical experiment:** Issue #88 / adversarial failure gate

## Why this audit exists

Issue #88 was designed after #87 produced a ceiling effect. It selected six fresh
cases from pre-registered failure strata and compared a strong source-grounded
baseline (R) with Needle Method (M).

The experiment itself remains valid: the cases were fresh, sealed before
execution, run statelessly under matched model/source access, and all six pairs
were R-pass / M-pass.

The interpretive problem is narrower:

> Did #88 test whether the baseline could **detect a latent trap**, or whether it
> could **correctly adjudicate a trap already surfaced by the question**?

Inspection of the exact revealed prompts shows the latter.

## Exact prompt-cue audit

The R and M arms for each case received the same case question. M additionally
received the Method instructions. Therefore the cues below were available to
both arms before either produced an answer.

| Case | Failure family | Cue embedded in sealed question | Construct actually tested |
|---|---|---|---|
| `adv-polish-visa-backprojection` | source-state / ex-post back-projection | asks whether the dated consolidation proves what the official Polish text showed on that date, then explicitly asks separately for historical source state and current corrected text | SURFACED_TRAP_ADJUDICATION |
| `adv-nis2-italian-heading` | language / corrigendum asymmetry | explicitly asks what the authentic Italian heading displayed before the corrigendum, what changed, and what may or may not be inferred from other languages/body | SURFACED_TRAP_ADJUDICATION |
| `adv-chatgpt-vlose-applicability` | designation/status != downstream application | explicitly says “Distinguish designation status from the application date” and warns not to invent an exact day without notification evidence | SURFACED_TRAP_ADJUDICATION |
| `adv-harmonised-standard-restriction` | unchanged identifier/text with changed legal effect | asks specifically for “the legal effect of the restriction and its timing,” including a deferred part of the Decision | SURFACED_TRAP_ADJUDICATION |
| `adv-ets-private-verifier` | private source origin != legally recognised role | explicitly asks for the bounded legal role of the accredited verifier, the public-authority role that remains, and the account consequence | SURFACED_TRAP_ADJUDICATION |
| `adv-licence-1300-boundary` | sub-day temporal boundary | gives 12:59 and 13:01 observations and explicitly asks why date-only storage loses a legally material boundary | SURFACED_TRAP_ADJUDICATION |

None of this is a flaw in sealing or execution. It is a **construct-labeling
problem**: the experiment asked a narrower question than later project prose
sometimes implied.

## What #88 establishes

Within the tested construct:

- all six fresh sealed R/M pairs were R-pass / M-pass;
- once the dangerous distinction was surfaced or strongly cued, the strong
  baseline resolved it correctly in every case;
- Needle Method produced no correctness rescue;
- Method did not regress any case;
- the stop rule against inventing a harder post-result benchmark remains valid;
- the project was still right to remove Method from the default identity.

This remains strong negative/parity evidence against a claim that Method is
needed merely to **adjudicate an already identified legal-information trap**.

## What #88 does not establish

#88 did not test whether, from a realistic ordinary request that does not name
the hidden issue:

- R would spontaneously notice the relevant trap;
- M would notice it more reliably than R;
- either arm would ask for missing temporal/source/scope evidence before making
  a consequential claim;
- the corpus failure classes are “easy” in ordinary research use.

Those are **latent-trap detection** questions.

They remain unmeasured.

## Canonical evaluation modes

Future evaluation must pre-register one of two modes.

### SURFACED_TRAP_ADJUDICATION

The question identifies or strongly cues the dangerous distinction.

Examples:

- “distinguish designation from application”;
- “reconstruct the historical source state rather than the current
  consolidation”;
- “account for a sub-day legal boundary.”

This mode tests whether the investigator resolves a known/surfaced issue
correctly.

### LATENT_TRAP_DETECTION

The task is realistic but does not identify the hidden failure mechanism.

The investigator must notice the issue before producing a consequential answer.

A latent-detection prompt may include facts naturally present in the real task,
but must not contain evaluator-authored instructions that reveal the decisive
trap, its category, or the correction the evaluator expects.

## Why the distinction matters

A method can plausibly add value at three different points:

1. **detection** — noticing that a seemingly ordinary request hides a dangerous
   source/time/scope/authority problem;
2. **adjudication** — resolving that problem correctly once identified;
3. **handoff/persistence** — preserving the result for later researchers or
   sessions.

#87 mainly tested handoff/persistence.  
#88 tested surfaced-trap adjudication.  
Neither provides clean evidence about latent-trap detection.

That separation is now part of the canonical protocol.

## No retroactive rescue

This audit does not revive Needle Method.

The correct disposition is:

- surfaced adjudication advantage: **not demonstrated; parity in #88**;
- handoff/persistence advantage: **bounded packaging benefit only; no default
  Core advantage**;
- latent detection advantage: **untested**.

Untested is not positive evidence.

## No immediate new gate

The six #88 cases are public and exposed. Rewriting them into vaguer questions
would not create fresh latent-detection evidence.

A future latent-detection experiment would require:

- a claim worth testing;
- fresh independently selected cases;
- realistic prompts fixed before results;
- a sealed answer key and detection criterion;
- the new evaluation mode declared before execution.

This audit therefore changes interpretation and protocol, not the current
backlog horizon.

## Durable consequence

#88 should henceforth be described as:

> six fresh sealed **surfaced-trap adjudication** cases, all R-pass / M-pass.

Do not describe it as proving that the baseline would independently discover
the same traps when they are latent.
