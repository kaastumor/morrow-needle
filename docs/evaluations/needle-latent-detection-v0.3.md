# Needle latent-trap detection gate v0.3 — manual Temporary Chat stage

**Issue:** #97  
**Status:** PRE-REGISTERED BEFORE EXECUTION  
**Evaluation mode:** LATENT_TRAP_DETECTION  
**Execution medium:** ChatGPT consumer UI / Temporary Chat / Unpersonalized  
**Initial cost:** no metered API calls  
**Initial runs:** 8

## Why v0.3

After project-level review, the expensive question was narrowed again.

Needle's durable identity is the adversarial corpus + evaluation protocol. Method
is now an optional hypothesis. Therefore the first paid/effortful question should
be the cheapest one capable of falsifying Method value.

V0.2 is retired unexecuted. Its scientific design remains sound, but its 12-call
API first stage spends on controls before we know whether there is any Method
signal at all.

V0.3 uses only the four strongest latent adversaries from v0.2.

## Initial stage

Four cases, each run once in R and once in M:

1. EU–Chile parallel agreement lifecycle
2. Haringvliet / Leenheerenpolder judicial invalidity
3. EN 50434:2014 garden shredder at 320 r/min
4. Temu DSA status as of 15 June 2024

Total: **8 independent chats**.

The exact R/M prompts are byte-identical to the corresponding v0.2 prompts.

## Execution boundary

Each run must use a completely new ChatGPT Temporary Chat configured
**Unpersonalized** before the first message.

For all eight chats:

- select GPT-5.6 Sol;
- select High reasoning/thinking;
- paste exactly one frozen prompt as the first message;
- allow web search;
- no project context;
- no memory/personalization;
- no follow-up;
- no correction/retry after a substantive answer;
- save the full answer unchanged.

This execution medium is intentionally different from the v0.2 API boundary.
The result therefore supports a claim about the practical consumer-ChatGPT
workflow, not byte-identical API behaviour.

## Initial stop rule

If all four adversarial pairs are R-pass / M-pass:

> stop after 8 chats.

Latent-detection value is not demonstrated. Do not spend on matched controls,
replication or harder cases.

## Signal handling

If any case is discordant:

- do not interpret the single pair as a Method win/loss;
- blind-grade the initial outputs first;
- then run the already-designed matched controls and confirmation pairs only if
  the frozen v0.2 confirmation logic remains applicable;
- any further paid/manual execution must be separately frozen before use.

## Grading

Both arms use the same visible headings. Grading is against the frozen hidden
answer key, with arm identity concealed where practical.

Primary adversarial pair classes:

- R fail / M pass — apparent Method rescue;
- R pass / M pass — parity;
- R fail / M fail — unsolved;
- R pass / M fail — apparent Method regression.

A single discordant pair is never enough for a project-level claim.

## No architectural consequence

Even a positive Method signal can earn only a bounded optional detection role.
It cannot resurrect Core, Full Needle, or any prior product architecture.

## Mutation rule

After this file and the v0.3 manifest are committed, any change to:

- the eight prompts;
- run order;
- execution settings;
- grading key;
- initial stop rule

requires a new version.

No model output has been produced at the time of this pre-registration.
