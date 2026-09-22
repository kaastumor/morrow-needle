# Morrow // Needle — Project Health Check

Status: **CANONICAL GATE-BOUNDARY CHECK**

This is not a meeting, scorecard, or recurring ceremony. Run it when a
meaningful gate closes, when a gate grows materially beyond its expected scope,
or when new evidence challenges the project thesis.

Record only changed state and decisions.

## Questions

### North-star alignment

- What user/research question did the completed gate actually make easier to
  answer?
- Did we improve over the strong simpler baseline in the project charter?
- Are we building evidence-backed capability or merely accumulating ontology,
  fixtures and infrastructure?

### Evidence and value

- What real case produced a new discovery, contradiction, useful uncertainty,
  or verified non-impact?
- What produced no value?
- Which claimed capability still lacks a discriminating real-world test?

### Assumptions and risks

- Which entries in `docs/assumptions.md` moved to survives, revise, reject,
  park or experiment?
- What is now the largest project-level risk?
- Did an old risk disappear enough to delete it?

### Complexity

- What permanent code/schema/workflow/process was added?
- What simpler baseline failed and justified it?
- What can now be removed, collapsed or demoted to historical provenance?

### Reproducibility / privacy

- Can consequential outputs still identify source evidence, code/version and
  derivation path?
- Did any private, sensitive or non-public material enter Git, CI, artifacts,
  logs or external services?
- Is local/operational state durable enough for the current horizon without
  becoming a second truth store?

### Direction

Choose exactly one:

- **continue** — the thesis survived and the next experiment is justified;
- **simplify** — keep the purpose, remove machinery;
- **redirect** — evidence supports a different central question;
- **stop** — the strong baseline wins often enough that further project cost is
  not justified.

Then update `BACKLOG.md`. Later horizons do not survive automatically.

## Governance self-check

Before adding a new project-management artifact, ask which concrete failure it
prevents. If an existing document/process already prevents that failure, reuse
it.

Delete or merge governance that becomes ritual, stale, duplicative, or more
expensive than the failure it prevents.
