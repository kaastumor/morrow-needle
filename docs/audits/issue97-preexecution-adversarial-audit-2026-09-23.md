# Issue #97 pre-execution adversarial audit

**Date:** 2026-09-23  
**Status:** V0.1 RETIRED UNEXECUTED / V0.2 REQUIRED  
**Scope:** exact sealed v0.1 prompts, answer key, runner and decision rule

## Bottom line

Do **not** execute the sealed v0.1 packet.

The legal answer key is supportable, the sealing/execution boundary is sound,
and no investigator response has been produced. The defect is construct
validity and decision efficiency: several prompts still cue their trap, the
controls are too weak, the two arms use visibly different answer formats, and a
single stochastic pair per case could be overinterpreted.

Retiring v0.1 before execution is cheaper and scientifically cleaner than
spending on a result whose interpretation would remain contestable.

The sealed v0.1 artifacts remain immutable historical evidence. No prompt/key
bytes are rewritten in place.

## What survived adversarial review

### Legal key integrity

The decisive legal propositions were rechecked against official sources:

- EU–Chile ITA entry into force: 1 February 2025; AFA has a distinct lifecycle
  and partial provisional application from 1 June 2025.
- Haringvliet / C-281/16: Decision 2015/72 was declared invalid insofar as the
  Haringvliet listing omitted Leenheerenpolder.
- EN 50434:2014: Decision (EU) 2026/80 adds a restriction for shredders whose
  shredding means can exceed 300 r/min, affecting Annex I points 1.1.2(a) and
  1.3.3.
- Temu: designated 31 May 2024; general DSA rules already applied, while the
  stricter VLOP obligations reached their later post-notification point
  (Commission material identifies 3 October 2024 for the risk-assessment
  obligation).
- Regulation 2026/305: April 2026 corrigendum changes the English February
  source strings later rendered in the nominally 6-February consolidation.
- Regulation 1169/2011: the July 2026 corrigendum is NL-only and changes Article
  25(2) from `uiterste consumptiedatum` to `consumptietermijn`.

The answer-key truth is not the reason for retirement.

## Adversarial findings

### 1. Latency is uneven; two cases are still close to surfaced adjudication

The v0.1 source-state case asks for the exact wording “when it was published,”
then tells the investigator it found a **consolidated** representation carrying
different strings. That naturally focuses attention on historical-vs-current
source state. Worse, the exact corrected strings are search terms that readily
surface the corrigendum.

The Dutch Article 25 case explicitly presents a **legacy Dutch wording versus
English wording** and asks whether the difference implies a distinct legal
requirement. That already directs attention to language-version divergence and
source freshness.

These are legitimate legal-research tasks, but they are weak evidence for the
strong construct “would the Method notice a hidden trap that an ordinary
workflow would not notice?”

Temu and the shredder are intermediate: the date/speed facts are task-native,
but also unusually diagnostic. Chile and Haringvliet are the cleanest latent
cases.

### 2. Negative controls are too trivial

The NIS2 deadline and GDPR application-date controls are direct article lookups.

They can catch a catastrophic Method failure, but they do not seriously test
the expected downside of a checklist: over-diagnosing a trap in a task that
looks similar to an adversarial case but is actually straightforward.

A better control is a **near-miss control**:

- same harmonised-standard setting, but below the >300 r/min restriction;
- same VLOP lifecycle setting, but at a date after the additional obligations
  have become applicable.

Those controls directly test overcorrection.

### 3. R and M output formats reveal the arm

R returns four headings.

M returns eight headings including `TIME / STATE` and
`FORBIDDEN INFERENCES`.

That creates two problems:

1. a grader can identify the Method arm immediately;
2. #97 would partly retest the packaging advantage already seen in #87 rather
   than isolating latent detection.

For a detection gate, both arms should return the **same output schema**.
Method may use its checklist internally, but the visible reporting contract
should be held constant.

### 4. One stochastic response per arm is insufficient for a project-level win

The v0.1 decision rule could treat two R-fail/M-pass pairs across two classes as
stronger Method evidence.

But each arm/case has only one stochastic model response.

If both workflows have nonzero per-run error variance under an underlying parity
state, discordant pairs can appear by chance. The exact probability is unknown
and case-dependent; therefore a positive discordance should be **replicated
before it changes project identity**.

The efficient solution is adaptive replication: do not replicate parity cases;
replicate only apparent rescues or regressions.

### 5. Fixed 16-call execution spends the full budget even on an obvious null

v0.1 always executes:

- 6 adversaries × 2 arms;
- 2 controls × 2 arms;
- **16 calls**.

A sequential gate can answer the most likely null with:

- 4 strong adversaries × 2 arms;
- 2 near-miss controls × 2 arms;
- **12 initial calls**.

That is 25% fewer calls before any token-shape differences.

Spend more only if the first stage finds a discordant result worth confirming.

### 6. Method claim needs narrower wording

The Method arm explicitly carries a checklist of source/time/scope/language
failure modes.

If it wins, the supported claim is not “Needle is generally smarter.”

It is:

> the bounded Needle checklist improves latent-trap detection for this
> GPT-5.6-Sol/high/web workflow on the tested classes.

That is still useful if true.

## V0.1 disposition

V0.1 is:

- correctly pre-registered;
- correctly sealed;
- never executed;
- **retired before execution after sponsor-requested adversarial audit**.

Its hashes remain evidence that no post-result tuning occurred. There are no
results to discard.

Do not run:
`issue97-latent-runner-v0.1.zip`

## V0.2 design requirements

V0.2 must:

1. use the same output headings for R and M;
2. keep Method's checklist internal to the M instruction;
3. start with four strongest latent adversaries;
4. replace trivial controls with two matched near-miss controls;
5. use only 12 initial calls;
6. blind grading to arm labels where practically possible;
7. replicate every discordant pair before it counts as a rescue/regression;
8. keep the original answer-key truth independently supported;
9. spend additional calls only when the first stage produces a real signal;
10. never mutate v0.1 artifacts.

## Selected V0.2 Stage-1 adversaries

Retain, with prompt rewrite before a new seal:

- EU–Chile parallel instrument lifecycle;
- Haringvliet judicial validity/text divergence;
- EN 50434:2014 at 320 r/min;
- Temu as-of 15 June 2024.

Retire from the decisive first stage:

- Regulation 2026/305 historical archive case — cue/search leakage too high;
- Dutch Article 25 language case — conflict is too explicitly surfaced.

Those cases remain useful research material, but not worth paid first-stage
latent-detection calls.

## Matched near-miss controls

### Shredder control

Same standard/product family, but shredding means max 250 r/min.

Decision 2026/80's >300 r/min restriction should not be over-applied to that
machine.

### Temu control

Same VLOP lifecycle, but status date 15 October 2024.

Official Commission material states the stricter VLOP obligations/risk
assessment applied from 3 October 2024, so Method must not invent continuing
non-applicability.

## Scientific consequence

This audit improves the experiment **before any model output exists**.

It does not select cases based on observed R failure and therefore does not
violate the anti-cherry-picking principle.

The proper next action is V0.2 pre-registration and sealing, not v0.1 execution.
