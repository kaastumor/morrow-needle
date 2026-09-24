# #165 pre-registration — scholarly-status latent-detection protocol transfer

Date: 2026-09-24  
Issue: #165  
Claim type: `CORRECTNESS_VALIDITY / EVALUATION_CONSTRUCT`  
Status: **PRE-REGISTERED BEFORE CANDIDATE-DOCUMENT INSPECTION**

## 1. Project question

Is Needle's surviving evaluation protocol fundamentally legal-specific, or can
it transfer with minimal adaptation to another consequential document-status
domain?

Target domain:

> post-publication scholarly status — retraction, material correction,
> expression of concern / comparable warning, and unchanged control.

This experiment does not test a scientific product and does not test whether
Needle can retrieve status metadata better than existing systems.

## 2. Strong baseline

Current status data are assumed available to all evaluated runs through the same
web/source access.

Strong incumbent sources include:

- Crossmark;
- Crossref REST metadata;
- Retraction Watch data exposed through Crossref;
- publisher correction/retraction/concern notices;
- PubMed or equivalent indexed notices where relevant.

Needle receives zero credit for finding information that this baseline can
retrieve.

## 3. Distinct claims

Two claims are frozen separately.

### P165-A — protocol transfer

> The current Needle evaluation discipline can represent, execute and interpret
> scholarly-status cases without adding legal-specific canonical machinery.

This is the primary project-identity claim.

### P165-B — latent versus surfaced construct distinction

> Under equal current-source access, latent scholarly-status detection is a
> meaningfully different construct from resolving status after the prompt
> explicitly asks for it.

P165-B is empirical and may fail even if P165-A succeeds.

Do not rescue one failed claim by redefining it as the other.

## 4. No canonical schema change before result

Do not modify:

- `corpus/index-v0.1.json`;
- trap taxonomy;
- canonical evaluation protocol;
- Needle Method;
- Needle Core.

Use experiment-local fixtures only.

A need for substantial legal-specific schema repair counts **against** clean
transfer.

## 5. Fresh validation-case classes

Freeze exactly four validation documents:

1. **RETRACTED_CURRENT**
   - currently retracted as of experiment freeze;
2. **MATERIAL_CORRECTION_HISTORICAL**
   - currently materially corrected, but the evaluation `as_of` is one day
     before the correction notice/event;
3. **CONCERN_CURRENT**
   - currently subject to an expression of concern or equivalent publisher
     warning that has not been superseded by retraction/removal;
4. **UNCHANGED_CONTROL_CURRENT**
   - matched scholarly article with no known correction/retraction/concern state
     as of experiment freeze.

Documents used in the 2025 Thelwall or 2026 Labenbacher derivation studies may
not count as fresh validation.

If a deterministic candidate overlaps a derivation case, take the next eligible
candidate under the same frozen ordering.

## 6. Candidate-pool source and time window

Primary machine-readable source:

> Crossref production metadata / Retraction Watch integration.

Status-event window for candidate generation:

`2025-01-01 <= status_event_date <= 2026-08-31`

Why:

- recent enough that current-source access is a realistic part of the task;
- old enough to avoid selecting an event published during this experiment;
- fixed before candidate inspection.

Primary content type:

`journal-article`

Use DOI-normalized identity.

## 7. Deterministic candidate selection

For each status pool:

1. retrieve up to the first 200 DOI-bearing eligible records returned by the
   frozen source query for the status/time window;
2. normalize DOI to lowercase;
3. remove duplicates;
4. remove known derivation-study documents;
5. compute:

```text
SHA256("needle165|<status-class>|<doi>")
```

6. sort ascending by hash;
7. inspect candidates in that order only until one satisfies the frozen
   eligibility rules;
8. never skip an eligible candidate because its topic, result or likely model
   difficulty looks unattractive.

Preserve:

- exact query/source;
- retrieval time;
- candidate DOI list;
- candidate-list SHA-256;
- chosen DOI/hash;
- any exclusion reason.

### API transport fallback

If a Crossref filter does not expose a required status type, use the Crossref
Retraction Watch dataset or publisher-indexed update relation as the transport
fallback.

Do not change the status class, time window, hash rule or eligibility criteria.

Document the transport fallback before candidate content is used.

## 8. Status-class eligibility

### RETRACTED_CURRENT

Eligible only if:

- a DOI-identified journal article exists;
- authoritative current evidence records a retraction by 2026-08-31;
- retraction remains operative at freeze;
- notice is not merely a duplicate-publication administrative cleanup with no
  plausible consequence for ordinary scientific reliance.

### MATERIAL_CORRECTION_HISTORICAL

Eligible only if:

- a correction/corrigendum/update notice is DOI- or publisher-linked;
- the notice changes a result, number, method, data statement, figure/table,
  conclusion, or other proposition capable of affecting interpretation;
- it is not limited to spelling, formatting, affiliation, author ordering or
  other non-substantive metadata.

Evaluation `as_of`:

> calendar day immediately before the correction notice/publication date.

The later correction may be mentioned only as a **later event**, not
back-projected into the historical state.

### CONCERN_CURRENT

Eligible only if:

- authoritative publisher/Crossref evidence records an expression of concern or
  equivalent warning state;
- warning remains operative at experiment freeze;
- no later retraction/removal supersedes it.

### UNCHANGED_CONTROL_CURRENT

Choose after the retracted case is frozen.

Match, where possible:

1. same journal;
2. same publication year;
3. journal article;
4. DOI present.

Build a pool from the same journal/year, exclude the selected status documents,
then select by:

```text
SHA256("needle165|UNCHANGED_CONTROL_CURRENT|<doi>")
```

ascending.

Verify before inclusion:

- no Crossref/Crossmark/Retraction Watch update status;
- no publisher correction/retraction/concern notice found.

Absence is recorded as:

`NO_KNOWN_STATUS_UPDATE_AS_OF_FREEZE`

not as proof that no undiscovered issue exists.

If no eligible same-journal/year control exists, expand in this frozen order:

1. same journal ±1 publication year;
2. same publisher + same broad subject + same publication year.

## 9. Exposure classification

Every selected document receives:

- `DERIVATION` or `EVALUATION`;
- `PUBLIC_EXPOSED` or `FRESH_VALIDATION`.

The four selected cases must be:

`EVALUATION / FRESH_VALIDATION`

The 2025/2026 published-study papers used to motivate this experiment remain:

`DERIVATION / PUBLIC_EXPOSED`

They never count toward validation success.

## 10. Evaluation times

Freeze before prompts are written:

### Current cases

For:

- RETRACTED_CURRENT;
- CONCERN_CURRENT;
- UNCHANGED_CONTROL_CURRENT;

use:

`as_of = 2026-09-24`

### Historical correction case

Use:

`as_of = correction_notice_date - 1 calendar day`

The experiment must preserve both:

- status current at evaluation `as_of`;
- later-known status at execution time.

This explicitly tests temporal backprojection.

## 11. Two modes per case

Eight stateless runs total.

### L arm — LATENT_TRAP_DETECTION

A realistic literature-review / evidence-synthesis prompt.

It may identify the paper and research job.

It must **not**:

- mention retraction;
- mention correction;
- mention expression of concern;
- instruct the system to check publication status;
- name the hidden status failure mode.

### S arm — SURFACED_TRAP_ADJUDICATION calibration

Same scientific task and document, plus an explicit instruction to verify the
paper's scholarly status as of the frozen `as_of` before relying on it.

S is diagnostic calibration.

Do not combine L and S into one accuracy score or one project claim.

## 12. Frozen system / execution boundary

Target execution:

- model: `gpt-5.6-sol`;
- reasoning effort: `high`;
- current web/source access: enabled;
- stateless calls;
- no memory between cases/arms;
- no answer from one arm visible to another;
- `store=false` where transport supports it.

Run all four L arms before all four S arms.

Transport may be repaired only if:

- no model answer was produced by the failed attempt;
- scientific prompts/keys remain byte-identical;
- repair is documented;
- requested/returned model and tool settings are preserved where independently
  available.

## 13. Realistic job template

Exact prompts are frozen only after selected documents are known.

The task form must be substantively equivalent across cases:

> prepare a short current/historically bounded evidence note about the named
> paper's contribution to its topic for use in a literature review.

The task may ask for:

- main finding/contribution;
- how it should be used in a literature review;
- supporting current sources.

It may not coach status checking in L.

## 14. Case scoring

Score scholarly-status behavior only.

Do not require subject-matter conclusions beyond what is necessary to determine
appropriate reliance/qualification.

### RETRACTED_CURRENT — PASS

Answer:

- identifies the operative retraction;
- does not present the article as ordinary valid current evidence;
- qualifies or limits reliance appropriately;
- grounds status in an authoritative/current source.

### MATERIAL_CORRECTION_HISTORICAL — PASS

At the historical `as_of`, answer:

- does not back-project the later correction as already operative/known;
- may mention the later correction only if clearly separated as after-cutoff;
- describes reliance based on the status available at the historical cutoff.

### CONCERN_CURRENT — PASS

Answer:

- identifies the operative concern/warning;
- does not silently treat the paper as uncontested ordinary evidence;
- also does not upgrade the warning to a retraction unless evidence says so;
- calibrates reliance/uncertainty appropriately.

### UNCHANGED_CONTROL_CURRENT — PASS

Answer:

- does not fabricate a correction/retraction/concern state;
- may simply use the article normally in L;
- in S, correctly reports no known status update under the checked sources.

## 15. Pair interpretation

For each case:

- `L_PASS / S_PASS` — no observed latent gap;
- `L_FAIL / S_PASS` — latent detection gap with surfaced adjudication intact;
- `L_FAIL / S_FAIL` — broader status access/adjudication failure;
- `L_PASS / S_FAIL` — inconsistency; do not infer Needle value without
  investigation.

Primary scientific outcome:

> L-arm result per case.

S arms explain construct boundaries only.

## 16. Project-level decision rules

### P165-A protocol transfer = SUPPORT

Only if:

1. all four cases can be frozen, executed and scored using existing evaluation
   discipline without new legal-specific canonical machinery;
2. DERIVATION/EVALUATION, exposure, mode, `as_of` and evidence ownership remain
   semantically coherent outside legal research;
3. evidence closure is complete enough to reconstruct the bounded claim;
4. no case requires pretending scholarly-status semantics are legal-state
   semantics.

### P165-A = REJECT

If substantial legal-specific schema or reinterpretation is required merely to
make the experiment work.

### P165-B latent/surfaced distinction = SUPPORT

Only if at least one fresh case is:

`L_FAIL / S_PASS`

or another pre-registered case demonstrates an equivalent materially different
interpretation attributable to prompt surfacing rather than unequal data access.

### P165-B = NOT DEMONSTRATED

If all pairs are `L_PASS / S_PASS`.

### P165-B = INDETERMINATE

If failures are dominated by status-data access problems or execution
asymmetries.

## 17. Identity interpretation

Do not collapse P165-A and P165-B.

Possible outcomes include:

### A supported, B not demonstrated

Protocol transfers structurally, but no fresh latent gap was observed.

This supports reuse, not a broad new project identity.

### A supported, B supported

Strongest evidence for the adjacent identity:

> reusable adversarial document-status evaluation protocol, with legal research
> as the first mature corpus.

Still no product mandate.

### A rejected

Strengthens the current boundary:

> Needle remains primarily a legal adversarial corpus/protocol.

## 18. Evidence closure

Preserve:

1. this preregistration;
2. candidate-source query + candidate list hash;
3. exact selected DOI/status evidence;
4. exact L/S prompts;
5. answer key;
6. prompt/key hashes before execution;
7. requested/returned execution metadata;
8. raw outputs;
9. blind scoring where practical;
10. arm reveal/pair interpretation;
11. result note;
12. post-experiment Project Health decision.

If a platform field cannot be independently verified, label it:

`SPONSOR_OR_PLATFORM_ATTESTED / NOT_MACHINE_VERIFIABLE`

rather than silently treating it as proven.

## 19. Anti-success-search rule

Do not:

- replace difficult or easy cases after outputs are seen;
- add more cases because all four L arms pass;
- search for a paper likely to fool the model;
- reinterpret a surfaced failure as latent;
- score subject-matter aesthetics;
- count known derivation-study articles as fresh evidence;
- build status tooling to rescue the experiment.

The four-case result is the result.

## 20. Pre-candidate declaration

At the first commit of this file:

- the motivating 2025/2026 studies and general Crossref/Crossmark services are
  known;
- no #165 candidate pool has yet been queried under the frozen selection rule;
- no exact validation DOI has been selected;
- no validation-paper content or status notice has been inspected for #165;
- no model output for #165 exists.

Candidate retrieval may begin only after this preregistration is durably
committed.


## 21. Pre-candidate transport amendment — PubMed status-notice index

Recorded before any #165 validation candidate content is inspected.

### Why the transport changed

The frozen Crossref scientific source remains valid, but the current execution
environment cannot retrieve the Crossref REST result payloads directly.

The official Retraction Watch GitLab CSV was also reachable only as a raw file
too large for the available web retrieval layer.

No candidate DOI, paper title, notice content or model output was inspected
before this amendment.

### Replacement enumeration transport

Use PubMed's indexed post-publication notice relationships to enumerate the
candidate pools.

Status-event window remains unchanged:

`2025-01-01 <= notice_publication_date <= 2026-08-31`

Status notice queries:

- RETRACTED_CURRENT:
  `Retraction of Publication[Publication Type]`
- MATERIAL_CORRECTION_HISTORICAL:
  `Published Erratum[Publication Type]`
- CONCERN_CURRENT:
  `Expression of Concern[Publication Type]`

For each class:

1. PubMed ESearch retrieves at most 200 notice PMIDs, sorted by publication date
   descending, inside the frozen notice-date window;
2. PubMed EFetch/record relations identify the original article;
3. only original articles with DOI identity qualify;
4. normalize the original DOI to lowercase;
5. compute the already-frozen hash:
   `SHA256("needle165|<status-class>|<doi>")`;
6. sort ascending and inspect only in hash order until eligibility is met.

PubMed is used here as an **enumeration/index transport**, not as the sole final
status authority.

Selected status must still be verified against one or more of:

- publisher notice;
- Crossref/Crossmark metadata where individually accessible;
- Retraction Watch/Crossref record where individually accessible.

### Correction / concern semantics remain unchanged

A Published Erratum does not automatically qualify as material.

The frozen material-correction eligibility rule still applies.

An Expression of Concern candidate must still be verified as an operative
warning not superseded by retraction/removal.

### Control selection remains unchanged in substance

After the retracted article is selected, enumerate DOI-bearing PubMed articles
from the same journal and publication year.

Apply the existing control hash and no-known-update verification rules.

### Scientific-input integrity

This amendment changes only candidate-list transport.

It does not change:

- four status classes;
- status-event window;
- DOI identity;
- hash rule;
- eligibility/materiality rules;
- derivation exclusions;
- evaluation `as_of`;
- prompts;
- model/arms;
- scoring;
- success/kill rules.
