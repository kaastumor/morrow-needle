# Standards cross-check — use standards as adversaries, not as a compliance programme

**Date:** 2026-09-23  
**Status:** REFERENCE AUDIT  
**Decision:** BORROW CONTROLS SELECTIVELY; DO NOT PURSUE CERTIFICATION/FORMAL CONFORMANCE

## Why this check exists

Morrow // Needle is a small, long-lived research/audit project rather than an
organization seeking management-system certification.

Standards are therefore useful as an external design adversary:

- what mature control have we accidentally omitted?
- what project behavior would a disciplined external reviewer expect?
- which practices have we already independently earned?
- which formal controls would be disproportionate process overhead?

This document is **not** a claim that Needle conforms to, implements, or is
certified to any ISO/IEC standard.

## Standards used as lenses

### ISO 9001:2026 — quality management systems

Useful lenses:

- organizational/project context;
- objectives and intended results;
- risk and opportunity;
- documented information;
- controlled operation;
- performance evaluation;
- continual improvement.

Needle already has strong analogues:

- canonical charter;
- explicit success/failure criteria;
- assumptions/risk register;
- decision/audit records;
- deterministic CI and adversarial gates;
- health reviews;
- explicit continue/simplify/redirect/stop decisions.

Important difference:

Needle does not operate a formal QMS. It has no certification scope, formal
management-review process, competence records, customer-satisfaction process or
ISO-defined conformity audit.

Disposition: **borrow principles; do not implement QMS ceremony.**

### ISO 31000:2018 — risk management

This is the closest conceptual match to the current backlog philosophy.

Needle already:

- treats the backlog as a risk register rather than a feature wishlist;
- records assumptions explicitly;
- prioritizes by architectural harm if wrong;
- uses adversarial evidence to reassess risk;
- can treat risks by revising, parking, simplifying or stopping work;
- performs boundary health reviews.

Gap:

Risk criteria are intentionally qualitative rather than organizationally
formalized. That remains appropriate.

Disposition: **strong directional alignment. No separate risk framework needed.**

### ISO/IEC/IEEE 12207:2026 — software life-cycle processes

Needle already has practical controls for:

- conception and architecture decisions;
- implementation and verification;
- configuration/version control through Git;
- maintenance and interface reopen rules;
- operational experimentation;
- explicit retirement/freeze of obsolete mechanisms;
- preserved historical decisions and regressions.

Issue #84's retirement of the scheduled operational monitor is particularly
important: disposal/retirement is part of life-cycle discipline too.

Gaps that are mostly irrelevant at present:

- formal acquisition/supplier process;
- organizational role/process mapping;
- transition/acceptance procedures for external customers;
- project-wide process conformance mapping.

Disposition: **use as a life-cycle sanity check, not a process template.**

### ISO/IEC 25010:2023 — product quality model

Useful characteristics include product-quality concerns such as reliability,
maintainability, security and other quality properties.

Needle currently protects quality through concrete regressions rather than a
formal SQuaRE quality model.

Strong areas:

- functional correctness for pinned legal-information cases;
- reliability/fail-closed behavior;
- maintainability through narrow ownership and versioned contracts;
- security hygiene at repository level;
- traceability/reproducibility.

Areas intentionally underdeveloped:

- performance efficiency;
- interactive usability;
- portability/product compatibility.

Those are reasonable because Needle is currently a research/audit engine, not a
public production product.

Disposition: **use only when a real product/system-quality question arises.**

### ISO/IEC 27001:2022 — information-security management

Needle has repository-level controls that point in the same direction:

- least-privilege GitHub workflows where practical;
- explicit no-secrets/private-material rule;
- sanitation for environment files, private keys, tokens and local paths;
- generated-artifact separation;
- public-source data assumption;
- source/provenance integrity hashes.

Needle does **not** have an ISMS and should not claim one.

Missing formal ISMS concerns include, among others:

- complete asset/risk inventory;
- organization-level access review;
- incident-management process;
- supplier/security governance;
- business continuity/recovery controls;
- formal risk-treatment statement;
- security audit/certification scope.

Current project inputs are intended to be public-source safe and there is no
production service handling sensitive customer data.

Disposition: **current controls are proportionate; revisit if private data,
external users, production hosting or secrets enter scope.**

### ISO/IEC 42001:2023 — AI management systems

Needle already has several relevant AI-governance principles:

- model output is not authoritative merely because a model produced it;
- official evidence outranks models;
- uncertainty/abstention survives;
- deterministic and model/human/hybrid derivations remain distinguishable;
- consequential claims require traceable evidence;
- sponsor/project-health review can reject model-driven expansion.

Needle does not operate a formal organization-wide AI Management System.

Missing formal-management-system elements such as organizational roles,
AI-specific management objectives, formal impact/risk review and supplier/model
governance would be disproportionate at current scope.

Disposition: **the Morrow Constitution already captures the controls most
relevant to this project. Do not add an AIMS layer.**

## Cross-standard conclusion

The important surprise is that Needle's project system is not obviously
immature relative to these standards.

It has independently converged on many mature ideas:

- context before implementation;
- risk-based prioritization;
- traceability;
- controlled change;
- verification;
- documented decisions;
- corrective action after failures;
- continual improvement;
- retirement of obsolete mechanisms;
- least privilege;
- explicit uncertainty;
- auditability.

The main difference is deliberate:

> Needle implements these principles as lightweight evidence-backed project
> controls rather than as a certifiable organizational management system.

That is appropriate.

## Concrete gaps exposed

### 1. Build/dependency reproducibility is weaker than research reproducibility

The repository has no lock/constraints file.

`pyproject.toml` intentionally uses bounded dependency ranges.

This means:

- legal fixtures and derivation logic are heavily versioned;
- the exact third-party Python environment is not equivalently pinned.

This is a real asymmetry.

Current risk is limited because:

- dependency count is tiny;
- CI repeatedly exercises the current ranges;
- Needle is not a deployed safety-critical product.

Decision:

**do not add a packaging/lock ecosystem solely for compliance.**

Reopen when:

- a dependency upgrade causes semantic regression;
- exact historical executable reproduction becomes a research requirement;
- production deployment appears;
- dependency surface grows materially.

At that point prefer the smallest constraints/lock mechanism already supported
by the chosen Python tooling.

### 2. GitHub Actions use major-version action tags

The workflows generally use references such as `actions/checkout@v4` and
`actions/setup-python@v5`.

Full immutable commit-SHA pinning would improve supply-chain reproducibility but
also creates maintenance overhead.

Current project risk is low because workflows do not deploy production code and
scheduled write-to-main automation has been retired.

Decision:

**record but do not change now.**

Revisit if workflows gain secrets, deployment privileges, sensitive inputs or
production responsibilities.

### 3. GitHub branch protection remains unverified

This is not an ISO gap so much as an assurance gap.

The installed GitHub integration cannot inspect administrative branch rules.

Sponsor-side verification remains useful:

- no force-push/delete on main;
- deterministic required checks;
- autonomous changes through PRs where practical.

## Controls explicitly NOT adopted

Do not create, merely to resemble ISO practice:

- a QMS manual;
- formal certification target;
- ISO clause-by-clause compliance matrix;
- RACI matrix for a one-sponsor research project;
- monthly management-review ceremony;
- generic CAPA bureaucracy;
- numeric project-health score;
- mandatory code-coverage KPI;
- organization-wide ISMS;
- organization-wide AIMS;
- quality-manager/security-manager roles;
- document numbering/approval bureaucracy.

Any of those may become justified if the project becomes an organization,
service, regulated product or multi-team system. They are not justified now.

## Standards policy for Morrow // Needle

Standards are **reference adversaries**, not roadmap authorities.

Use a standard when:

1. the project enters a materially new operating context;
2. a health audit suspects a missing class of control;
3. security/privacy/safety stakes increase;
4. a product/service/user-facing horizon reopens;
5. external certification or assurance becomes a real requirement.

When consulting one:

- identify the concrete control/problem;
- compare existing Needle practice;
- adopt only the smallest useful control;
- preserve project-specific evidence over ceremonial conformance;
- never state ISO conformity/certification without a real scoped assessment.

No recurring standards audit is required.
