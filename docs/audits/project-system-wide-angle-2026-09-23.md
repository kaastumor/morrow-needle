# Wide-angle project-system audit — 2026-09-23

**Issue:** #84  
**Direction:** **CONTINUE RESEARCH/AUDIT MODE + SIMPLIFY OPERATIONS**

## Executive conclusion

Morrow // Needle is still aligned with its current purpose.

The strongest part of the project is not the number of schemas or tests. It is
the repeated discipline of separating kinds of legal truth, preserving official
evidence, and allowing adversarial cases to reopen frozen assumptions.

The foundation does **not** need a redesign.

The main risks have moved outward:

1. successful discovery can cause ontology creep;
2. historical product machinery can continue running after the product thesis
   has stopped;
3. case-specific CI can accumulate faster than unique CI responsibilities;
4. canonical/meta documentation can lag behind the repo's actual decisions.

This audit found one concrete operating defect large enough to fix immediately:
the old operational monitor was still using Git as a six-hour live-state
database even though public-product expansion had been stopped.

## Evidence reviewed

The audit inspected:

- current charter, backlog and assumptions;
- Morrow Constitution / Foundation v0.1;
- repository layout and tracked-file sizes;
- sanitation script;
- unit/foundation/retrieval and representative case-specific workflows;
- operational monitor/pilot code and state contract;
- provenance ledger contract;
- recent commits and open issues;
- current project-health procedure.

At the start of the audit the repository contained approximately:

- 51 JSON schemas;
- 72 Python test files;
- 50+ documentation files;
- 100+ JSON fixtures;
- 52 Python source files;
- 25 GitHub Actions workflow files.

Those counts are context, not targets.

## What is structurally strong

### 1. Repository is genuinely canonical

Important decisions, adversaries, fixtures and regressions live in GitHub rather
than only in chat memory.

The backlog is a risk register, not a feature wishlist.

The autonomous worker explicitly idles when there is no eligible work.

### 2. Evidence ownership is unusually disciplined

The project has repeatedly refused to collapse:

- source observation into legal mutation;
- text state into legal effect;
- set state into application time;
- metric truth into rule evaluation;
- categorical finding into geometry;
- geometry into time;
- judicial interpretation into textual mutation.

That pattern is more important than any individual schema.

### 3. Reopen rules work

Temporal v0.1 and Legal Spatial State v0.1 were not treated as sacred.

Official adversaries demonstrated real semantic loss and earned narrow v0.2
extensions.

This is healthy foundation behavior.

### 4. Negative results survive

Parity, non-impact, unresolved evidence and “do not build this” conclusions are
retained.

The project has already stopped a public-product direction rather than using new
architecture to rationalize it.

### 5. Dependency footprint remains lean

Runtime dependencies are still minimal.

No database, queue, vector store, frontend framework or custom model system has
been introduced without a current need.

## Foundation improvement made in this audit

The old Foundation ontology sketch was too document/mutation-centric for the
project that now exists.

Rather than add a universal graph, the Foundation now carries a **canonical
ownership map**.

It identifies distinct owners for:

- source/provenance truth;
- text/mutation truth;
- identity/lineage;
- temporal/procedural state;
- authoritative set state;
- authoritative metrics;
- authoritative categorical findings;
- legal spatial state;
- judicial holdings;
- derived semantic/evaluation objects;
- read-side audit/presentation projections.

A new constitutional invariant is added:

> **Canonical ownership is singular.**

Interactions between contracts do not permit one contract to silently copy or
reclassify another contract's truth.

This is the main defense against ontology creep.

## Operational-pilot finding

This was the clearest project-system defect.

The scheduled Operational Needle monitor:

- ran every six hours;
- had `contents: write`;
- copied generated state/results/cards/reports into `data/`;
- committed directly to `main`;
- produced 47 commits with message
  `Advance operational Needle pilot state`.

Four tracked operational files were roughly:

- 3.1 MB state;
- 3.1 MB latest results;
- 1.9 MB latest cards;
- 1.2 MB last report.

The rest of the repository falls sharply below those sizes.

This did not mean the files could simply be deleted.

The state snapshot contains hash-verified SOURCE_OBSERVATION provenance records,
and the workflow itself documented that these observations had no other promoted
durable owner.

### Resolution

Issue #84 freezes, rather than deletes, the pilot.

The operational workflow now:

- has no schedule;
- has read-only repository permission;
- never promotes state to `main`;
- runs a live cycle only with explicit manual opt-in;
- uploads the result as a diagnostic artifact.

The current state remains a historical regression/evidence snapshot.

A future migration may extract its unique Source Observations into a durable
ledger and then remove bulky snapshot data, but that is not necessary while the
live-monitor horizon is inactive.

No replacement database is justified.

## Sanitation finding

Before #84, sanitation protected structural hygiene but had several gaps.

It now additionally prevents:

- tracked `.env.*` files;
- obvious embedded private-key / GitHub-token markers;
- obvious absolute local user paths;
- tracked generated `artifacts/`;
- accidental new tracked files larger than 1 MB.

The four frozen operational snapshots are explicit temporary large-file
exceptions because evidence deletion is not a sanitation function.

A root `.gitignore` was added so generated/private files are prevented before
they reach the sanitation gate.

No secret-scanning or lint dependency was added.

## CI / GitHub assessment

### What is good

The project has clear deterministic gates:

- full Python unit/regression suite;
- repository sanitation;
- composed foundation audit;
- specialized integration contracts where useful.

Live-source availability is often correctly separated from deterministic branch
truth through manual jobs.

### What is too fragmented

There are 25 workflow files.

Many case-specific workflows rerun deterministic test subsets that are already
covered by the complete unit suite. Some also build previews or expose optional
live probes, which may justify keeping them.

The static evidence is enough to call this **CI topology debt**, but not enough
to safely bulk-delete workflows without run telemetry.

Future consolidation rule:

> A permanent workflow should own at least one unique responsibility: a required
> gate, schedule, live probe, artifact, or permission boundary.

If it only reruns a subset of tests already covered globally, prefer the shared
unit/foundation workflow and retain the case as a fixture/test rather than a
workflow.

The retired operational schedule is the first concrete application of that
rule.

### GitHub administration limitation

The installed integration receives HTTP 403 when reading branch-protection
settings.

Therefore this audit cannot verify whether `main` currently requires PRs or
status checks.

Status: **UNVERIFIED**, not absent.

Sponsor-side settings worth confirming:

- block force-push/delete on `main`;
- require passing sanitation + unit tests for ordinary PRs;
- use foundation audit as a required check where practical;
- require short-lived PRs for scheduled/autonomous changes.

No CODEOWNERS, CONTRIBUTING, SECURITY policy, Dependabot configuration or PR
template is added now. For a private single-sponsor research project they would
currently create more process than demonstrated protection.

## Adversarial quality assessment

The adversarial method is one of the project's strongest components.

A good Needle adversary currently does four things:

1. names a concrete claim that can be wrong;
2. uses authoritative evidence rather than synthetic edge cases where possible;
3. tests the simplest existing owner first;
4. leaves a regression, negative result or bounded architecture change.

Recent work improved further by demanding orthogonal confirmation before adding
new causal families.

That should remain a norm, not an absolute ritual: a single case may reopen a
foundation when semantic loss is already decisive.

### What not to add

No generic fuzzing framework, mutation-testing platform, model-vs-model debate
system or code-coverage target is justified at present.

Generic code coverage would be weaker evidence than the current official-case
coverage for the project's main risks.

Property/fuzz testing should be introduced only when a concrete parser,
normalizer or resolver bug class shows that example-based adversaries are
insufficient.

## Discovery Lane assessment

Discovery is not a side activity anymore; in research mode it is often the way
new falsifiable questions enter the project.

The old “one discovery for every three foundation cycles” rule is obsolete.

New trigger:

> after roughly 2–3 schema- or architecture-changing discovery runs, perform a
> wide-angle health/leanness check before adding another permanent abstraction.

This is complexity-triggered, not calendar-triggered.

Negative or no-change discoveries do not require ceremony.

## Health signals worth retaining

Do **not** create one project-health score.

Use explicit questions:

- Are canonical north-star documents in agreement?
- Did a closed issue become a zombie “current task”?
- Did any automation outlive its purpose?
- Is generated state accumulating in Git?
- Does every workflow have a unique responsibility?
- Does every new canonical owner have a demonstrated failure behind it?
- Was an independent adversary used before generalizing a causal family?
- Is any derived view becoming a competing truth store?
- Are we preserving evidence merely because it is evidence, or because a
  current question still needs it?
- Is idle now the correct state?

Those questions produce actions. A score would hide them.

## Remaining bounded debt

### Frozen operational provenance

The large pilot state still owns unique Source Observations.

Do not delete it until those records are explicitly migrated or judged no
longer required.

This is parked debt, not an active infrastructure project.

### CI topology

Case-specific workflows should be progressively reviewed against the unique-
responsibility rule.

Do not perform a bulk cleanup without telemetry or a concrete maintenance need.

### Branch protection

Must be checked in GitHub settings by someone with repository-administration
visibility.

## Direction

**CONTINUE research/audit mode. SIMPLIFY operations.**

No foundation rewrite.
No product restart.
No new infrastructure.
No health dashboard.

The next project task should again be a concrete falsifiable research question
or a demonstrated maintenance failure. Until then, idle is correct.
