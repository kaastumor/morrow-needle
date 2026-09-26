# Issue #348 — direction review after Reference Pack v0.2 release

Date: 2026-09-26  
Selected mode: **USE — ORTHOGONAL FAILURE-ANALYSIS REPLICATION**  
Next WIP: **#349 — orthogonal external failure replication through Reference Pack v0.2**

## Trigger

Reference Pack v0.2 is now merged and canonical.

The release preserves the same frozen 81-case / 26-class scientific source as v0.1 and
adds one earned surface:

> `failure-analysis-guide.md`

It deliberately does **not** add:

- a structured external-failure dataset;
- a generalized packet schema;
- a new boundary registry;
- a new canonical failure-analysis object.

#343 explicitly deferred those stronger structures until an orthogonal use showed that the
same packet elements recur.

## Current evidence

### #214

Hard null for corpus-assisted latent diagnostic/correctness advantage.

### #327

`BASELINE_SUFFICIENT` for generic post-answer legal-research companion use.

### #339

First direct positive failure-analysis use:

> **NEEDLE_VALUE_PACK_GAP**

Repository-level Needle added reusable packet value, but v0.1 did not surface it well.

### v0.2

v0.2 directly addresses the observed navigation gap through:

- no-class handling;
- scientific/reuse-status guidance;
- source-state discipline;
- boundary/opposite-error guidance;
- regression-conversion rules;
- truth-owner navigation.

It has not yet been tested on an independent second external failure.

## Mode comparison

### USE — selected

The highest-value uncertainty is now operational:

> does the #339 packet value replicate on a materially different public legal-AI failure,
> and can v0.2 guide the work without broad repository archaeology?

This test can falsify two different hypotheses:

1. packet value may not replicate;
2. packet value may replicate but v0.2 may still leave material navigation burden.

It can also test whether the candidate packet fields recur strongly enough to justify a
future structured external-failure layer.

This directly follows the replication gate imposed by #343.

### DISCOVER — not selected

The external role/substitute landscape has already been investigated enough to define and
test the failure-analysis job.

Another literature/competitor pass now has lower information gain than applying the
released surface.

### REVIEW / RELEASE — not selected

v0.2 has just shipped.

A v0.3, machine-readable packet layer or richer release before orthogonal use would reverse
the evidence-first sequence established by #343.

### CONSOLIDATE — not selected

The stale live backlog is reconciled by this review itself.

No other live ownership conflict or duplicated truth store is currently blocking use.

### MAINTAIN — not selected

The v0.2 implementation passed:

- Python unit tests;
- canonical corpus validation;
- browser projection tests;
- repository sanitation.

The failed first implementation attempt exposed and repaired only deterministic checksum
ordering and direct-script import mechanics.

No remaining correctness/integrity trigger dominates the replication question.

## Orthogonal replication source

Use:

> **Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models**

This source is already part of #335's accepted external comparison set.

It is materially different from #339's `Hallucination-Free?` source:

- different study/dataset;
- general-purpose LLM legal hallucination evaluation;
- different task construction;
- independent author labels.

## What #349 must test

### Packet value

Against a frozen strong ordinary postmortem, does Needle again add material reusable
structure?

### v0.2 navigation value

Use v0.2 **before** broader repository history.

Record whether the guide supplies the required method/owners directly or whether broad
project archaeology remains necessary.

### Structured-layer signal

Compare the second packet with #339.

Field recurrence alone is not enough.

A future machine-readable layer needs:

- recurrent materially useful fields;
- stable semantics;
- a plausible canonical membership/truth owner;
- lower complexity than repeated manual analysis.

## Decision

# **SELECT USE — ORTHOGONAL FAILURE-ANALYSIS REPLICATION**

Next WIP:

> **#349 — orthogonal external failure replication through Reference Pack v0.2**

The result may be positive, null or uninterpretable.

No new corpus case/class, v0.3, structured packet layer, product claim or superiority claim
is authorised by #348.
