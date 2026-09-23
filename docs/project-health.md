# Morrow // Needle — Project Health Check

Status: **CANONICAL GATE-BOUNDARY CHECK**

This is not a scorecard, recurring ceremony or KPI dashboard. Run it when a
meaningful gate closes, after a cluster of architecture-changing discoveries,
when automation grows materially, or when new evidence challenges the project
thesis.

Record changed state and decisions, not activity volume.

## North-star alignment

- What concrete research/user question became easier to answer?
- What does the current value-evidence ledger say **against** the project thesis,
  not only for it?
- Has distinctiveness been re-tested against the strongest boring baseline
  recently enough for the current project maturity?
- Did the work outperform or safely complement the strongest simpler baseline?
- Are we preserving research/audit value, or rebuilding a stopped product
  roadmap through architecture?
- Would an idle backlog be healthier than the proposed next task?

### Competing project identities

At a wide-angle review, formulate at least three plausible identities:

1. the current/incumbent identity;
2. a deliberately **smaller** identity that preserves only the demonstrated
   contribution;
3. a materially different adjacent identity suggested by the evidence.

Do not give the incumbent home-field advantage.

Ask which identity best explains the accumulated value evidence and which new
experiment would distinguish them.

## Canonical freshness

- Do README, project charter, backlog, assumptions and package metadata describe
  the same current direction?
- Does any closed issue or historical gate still appear as the current horizon?
- Are historical documents clearly marked when later decisions supersede their
  product or architecture framing?
- Does the canonical ownership map still identify one owner per consequential
  fact?

## Problem / contribution / form / implementation

- Are we confusing the real problem with the current project/product form?
- Is the claimed contribution actually distinct from the integration of existing
  tools?
- Could the same contribution survive in a much smaller artifact: a method,
  fixture corpus, evaluation protocol, convention, prompt set or library?
- Has implementation architecture become part of the identity merely because
  it already exists?
- If the contribution claim changed, did its evaluation protocol change with it?

## Evidence and adversarial sufficiency

- Which real official case produced the finding?
- What plausible alternative explanation was tested?
- Is there a negative/fail-closed regression, not only a happy-path fixture?
- Before introducing a new causal family, is there an independent orthogonal
  proof case, unless the first case is itself a foundation blocker?
- Did the adversary attack ownership/boundaries rather than merely add another
  example?
- Which claimed capability still lacks a discriminating real-world test?
- Are acceptance criteria still testing the intended capability, or were they
  weakened because the current environment could not execute the harder test?
- Is an implemented method being analytically promoted without evidence for the
  next maturity stage?

## Assumptions and risks

- Which entries in `docs/assumptions.md` moved?
- What is now the largest project-level risk?
- Is ontology creep, infrastructure creep or workflow creep becoming a bigger
  risk than missing capability?
- Did an old risk disappear enough to delete rather than archive?

## Precedents and subtraction

- Have we searched sideways into adjacent disciplines, products, research
  methods and terminology rather than only direct category peers?
- For each strong precedent, choose one disposition:
  **reuse / benchmark / learn from / remove from our scope**.
- Did precedent research make the project smaller anywhere? If it only enlarged
  the backlog, challenge the research value.
- Is the claimed uniqueness merely that nobody combines the same components, or
  does the combination enable behavior the components/baseline cannot?

## Complexity and leanness

- What permanent code/schema/workflow/process was added?
- What simpler baseline demonstrably failed and justified it?
- Can any workflow, schema, projection or process now be demoted to historical
  provenance or manual diagnostics?
- Is a one-case workflow rerunning tests already covered by the global suite?
- Are generated files or snapshots accumulating in Git when an artifact or
  provenance record would be safer?
- Is file/schema/workflow count growing because of evidence, or because previous
  experiments never retired?
- Can the valuable artifact shrink while preserving the demonstrated
  contribution?

Do not create a complexity score. Name the concrete surface and decide whether
it still earns its maintenance cost.

## Automation / GitHub behavior

- Which scheduled workflows can mutate `main` or durable project state?
- Does each scheduled job still serve the current horizon?
- Are live endpoint failures separated from deterministic branch CI?
- Are branch protection, required checks and force-push restrictions verified?
  If repository administration cannot be inspected, record them as UNVERIFIED
  rather than assuming.
- Does each permanent workflow own a unique gate, schedule, live probe, artifact
  or permission boundary? If not, prefer the shared test workflow.

## Reproducibility / privacy / sanitation

- Can consequential outputs identify official evidence, code/version and
  derivation path?
- Did private, sensitive or non-public material enter Git, CI, artifacts, logs
  or external services?
- Are local machine paths, environment files, credentials and large generated
  artifacts prevented before they become repository history?
- Is operational state truly canonical, or has it become a second truth store?
- If evidence is retained only in a cache, is deletion explicitly blocked until
  migration?

## Direction

Choose exactly one:

- **continue** — the thesis survived and another experiment is justified;
- **simplify** — keep the purpose but retire machinery;
- **redirect** — evidence supports a different central question;
- **stop** — the strong baseline wins often enough that further cost is not
  justified.

A health check may legitimately choose **continue + simplify operations** when
the research thesis is healthy but old execution machinery no longer serves it.

Then reconcile `BACKLOG.md`, assumptions, `docs/value-evidence.md` and any
affected decision/runbook.

Every completed horizon ends with a fresh **continue / simplify / redirect /
stop** decision. Completing the horizon itself never authorizes the next one.

## Governance self-check

Before adding a project-management artifact, metric, workflow or policy, ask
which concrete failure it prevents. If an existing control already prevents that
failure, reuse it.

Prefer:

- a regression over a checklist;
- a single invariant over a score;
- a current canonical document over another status document;
- an explicit idle state over a manufactured roadmap.

Delete or merge governance that becomes ritual, stale, duplicative or more
expensive than the failure it prevents.
