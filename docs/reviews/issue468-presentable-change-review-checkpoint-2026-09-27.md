# #468 — Presentable change-review checkpoint

Date: 2026-09-27  
Status: **READY FOR DEPLOYMENT GATE — DO NOT MERGE ON FAILED VERCEL**

## Review surface

The medical-devices `/regime/` prototype now presents three connected layers:

1. **Regime map**
   - three predecessor directives;
   - MDR / IVDR sibling core branches;
   - transition/change lane;
   - implementing, delegated, EUDAMED and non-binding-guidance families;
   - proposal lane kept separate.

2. **Change review**
   - three frozen upstream-change controls;
   - DIRECT_REVIEW / DOWNSTREAM_REVIEW / CONTEXT_ONLY / NO_PROPAGATION / OUT_OF_SCOPE;
   - queue inclusion and stop reasons are both visible;
   - review candidate is explicitly not equated with changed legal effect.

3. **Research diagnostics**
   - known coverage omission;
   - branch-sample omission;
   - represented/reviewed transition trigger;
   - structural-gap candidate: none asserted.

The page also exposes:
- an at-a-glance regime summary;
- direct section navigation;
- frozen evidence-date boundary;
- official source links.

## Review thesis

> The legal web is useful when it compresses structure and produces small explainable review queues. It fails when graph reachability or missing nodes are mistaken for legal conclusions.

## Deployment state

Repository test check on prior #470 head passed.

Vercel status on that head failed, but the connected Vercel API cannot retrieve that GitHub-linked deployment/log record.

This checkpoint intentionally creates a fresh exact-head deployment attempt.

Acceptance rule:
> merge #470 only after Vercel reports SUCCESS on the new exact head.

No LVD P8 files are modified by this checkpoint.
