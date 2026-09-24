# Cycle 2 Run D — adversarial corpus/protocol transfer scan

Issue: #159  
Parent: #155  
Date: 2026-09-24  
Disposition: **ADOPT_FOR_EXPERIMENT**

## Proven Needle anchors

Run D tests whether the surviving Needle contribution transfers beyond legal
documents:

- adversarial corpus with durable evidence ownership;
- DERIVATION versus EVALUATION separation;
- exposure/contamination discipline;
- SURFACED_TRAP_ADJUDICATION versus LATENT_TRAP_DETECTION;
- time-bounded evidence claims;
- preservation of parity/negative outcomes.

The target must be consequential document interpretation, not another generic
LLM benchmark.

## Target setting — scholarly-record status

Retractions, corrections, expressions of concern and other post-publication
updates can materially change whether and how a scientific paper should be
relied upon.

The underlying article text may remain accessible and persuasive while its
**current scholarly status** changes.

This makes the target structurally close to Needle's source-role/time/status
failures without being a legal-document problem.

## Independent target evidence

### 2026 multi-tool study

Labenbacher et al. evaluated nine general/research-focused GenAI tools on 15
retracted articles.

Five standardized tasks were used:

1. topic overview from article keywords;
2. relevant articles for the topic;
3. summarize the named article;
4. ask explicitly whether the named article is retracted;
5. ask why it was retracted.

The first three tasks can expose failure to flag status during ordinary research
use; the final two explicitly surface the status question.

The study found that no tool handled all cases consistently. Retracted articles
were frequently included in topic overviews without warning.

Source:

- https://www.jmir.org/2026/1/e88766

### 2025 latent-quality study

Thelwall tested 217 retracted or otherwise concerning articles by asking
ChatGPT 4o-mini to evaluate research quality from title + abstract, 30 times per
article.

Across 6,510 generated quality reports, none mentioned the relevant retraction,
correction or ethical problem.

Source:

- https://onlinelibrary.wiley.com/doi/full/10.1002/leap.2018

This is strong evidence that the failure exists even when status is not named in
the user task.

## Strong existing alternative

The scholarly ecosystem already has mature status infrastructure.

### Crossmark

Crossref's Crossmark is designed to expose the current status of research
outputs, including:

- corrections;
- retractions;
- updates.

It can be embedded in HTML/PDF and exposes metadata through the Crossref REST
API.

Source:

- https://www.crossref.org/services/crossmark/

### Retraction Watch via Crossref

Crossref acquired the Retraction Watch database and exposes retraction metadata
through:

- the Crossref REST API;
- a downloadable public dataset updated every working day.

It supplements publisher metadata where publishers have not supplied the full
status record.

Source:

- https://www.crossref.org/documentation/retrieve-metadata/retraction-watch/

Therefore the discovery problem is **not** lack of a status registry.

A strong research baseline can query current scholarly status directly.

## Structural correspondence

The Needle-relevant failure is:

```text
document content remains accessible
    ↓
post-publication status changes
    ↓
research system interprets/summarizes/cites content
    ↓
status is not checked or surfaced
    ↓
user treats content as ordinary current evidence
```

The important state is not merely:

`ARTICLE_EXISTS`

but:

`ARTICLE_STATUS_AS_OF(T)`

Examples include:

- active/current;
- corrected;
- expression of concern;
- partially retracted;
- retracted;
- removed/withdrawn.

The interpretation consequence depends on the status and the user's job.

## Existing-evaluation check

This field is not empty.

The 2026 JMIR study already contains both:

- ordinary literature-pathway tasks; and
- explicit retraction questions.

It also reports the frequency with which retracted articles appear in topic
overviews without warning.

The 2025 Thelwall study is an even stronger latent-status probe because the
quality-evaluation prompt did not ask about retraction.

So Needle cannot claim to invent retraction-aware evaluation.

## The construct gap

The current evidence does reveal a narrower evaluation-design opportunity.

### 1. Surfaced and latent modes should not be blended

Questions 4–5 in the JMIR study explicitly surface retraction status.

Questions 1–3 test a different behavior: whether status is noticed and qualified
during ordinary research work.

A combined 5/5 outcome is useful operationally, but it should not be interpreted
as one homogeneous construct.

Needle already learned this exact lesson in #88/#95:

> resolving a named trap is not the same as detecting it unprompted.

### 2. Status must be time-bounded

A paper can be validly unretracted at time T1 and retracted at T2.

Using current status to grade a historically bounded research task can
back-project later knowledge.

The evaluation must freeze:

- query/evaluation time;
- status-known-by time;
- relevant status source;
- whether a retraction/correction existed at that time.

### 3. Model knowledge and retrieval must be separated

Thelwall used a fixed ChatGPT model whose training cutoff predated some tested
retractions.

That is useful evidence of practical behavior, but it can confound:

- inability to know current status;
- failure to check status;
- failure to interpret status.

A construct-valid test of **latent status detection** should give comparator arms
equivalent current-status access and vary only the evaluated workflow/method.

### 4. Derivation cases cannot validate the same mechanism blindly

High-profile known retractions used to discover/calibrate the failure should not
then be counted as fresh blind validation of status detection.

That maps directly onto Needle's DERIVATION / EVALUATION separation.

## Explicit boundary

Retraction status is not equivalent to:

> every statement in the paper is false and must never be mentioned.

A retracted work may still be relevant for:

- history of a controversy;
- research-integrity analysis;
- methodological discussion;
- describing the retraction event itself.

A good evaluation must score the **appropriate qualification/reliance decision**
for the task, not automatic exclusion.

This boundary prevents a simplistic "retracted = forbidden" benchmark.

## One falsifiable transfer hypothesis

Working label:

`SCHOLARLY_STATUS_LATENT_DETECTION`

Hypothesis:

> Needle's evaluation protocol can be transferred with minimal change to
> scientific evidence-synthesis tasks to measure latent detection of
> post-publication scholarly-status changes more cleanly than evaluations that
> mix explicit status questions, historical/current status and exposed
> derivation cases.

This is a protocol/evaluation hypothesis, not a product hypothesis.

## Smallest discriminating experiment

If #160 selects this candidate:

1. freeze four fresh scholarly documents selected independently of model output:
   - one retracted;
   - one materially corrected;
   - one expression-of-concern / equivalent warning;
   - one matched unchanged control;
2. freeze an `as_of` time for each case;
3. establish status from Crossmark / Crossref / publisher / Retraction Watch;
4. classify any case used to design the rubric as DERIVATION, not validation;
5. create realistic evidence-synthesis/research prompts that do **not** mention
   status;
6. use the same source/web access in all comparator arms;
7. pre-register:
   - what counts as status detection;
   - what counts as safe qualification;
   - when reliance becomes consequentially wrong;
8. grade LATENT_TRAP_DETECTION only;
9. optionally include a separate surfaced-status calibration, never blend its
   score with latent detection.

### Success

The transfer succeeds if:

- the current Needle protocol can represent the scientific cases with only
  domain labels/rubrics, not legal-specific machinery;
- it cleanly prevents time-backprojection and surfaced/latent construct mixing;
- the resulting test answers a question that existing retraction studies leave
  ambiguous;
- at least one fresh case makes the distinction consequential.

### Kill

Reject if:

- the protocol requires legal-specific semantics to function;
- existing scientific evaluation practice already supplies the same
  pre-registration/exposure/time/mode discipline with no meaningful gap;
- the only contribution is renaming ordinary retraction checking;
- or no realistic latent task produces a consequential difference.

## Relative-value boundary

Crossmark / Retraction Watch already own the status-data problem.

Needle gets no credit for:

- retrieving retraction metadata;
- building a status registry;
- adding a Crossmark lookup UI;
- telling researchers to check retractions.

The only candidate contribution is **evaluation construct discipline**.

## Run D disposition

# **ADOPT_FOR_EXPERIMENT**

Retain one bounded candidate:

> `SCHOLARLY_STATUS_LATENT_DETECTION`

Why retain it:

- independent studies show a real consequential failure;
- the target is materially different from legal document analysis;
- existing status infrastructure is strong, so the experiment cannot win by
  inventing retrieval;
- Needle has a specific earned protocol lesson — surfaced versus latent
  detection — that maps directly onto the target;
- success or failure would materially inform whether the surviving Needle core
  is legal-specific or more general.

Do not build:

- retraction tooling;
- Crossref integration;
- a scientific-literature product;
- a generic benchmark platform;
- a new ontology.

Only the bounded protocol-transfer experiment may be considered at #160.
