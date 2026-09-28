# Repository session contract

GitHub `main` is the canonical project authority. Treat local checkouts as work surfaces
and verify them against `main` before relying on their state. Chats, Codex handovers and
other conversational summaries are non-canonical inputs: use them to find questions, then
reconcile them with the repository before acting.

## Start every session here

Read in this order:

1. `BACKLOG.md` for the current mode, sole WIP and immediate priority;
2. the active issue and its PR, if any, for the frozen task contract and pending evidence;
3. `docs/project-charter.md` for durable purpose, boundaries and ownership;
4. `docs/way-of-working.md` for delivery, discovery and verification rules.

Before reactivating parked architecture or claiming that a capability does not exist,
inspect `docs/history/README.md`, `docs/history/asset-register.md`, the relevant decision
record and the evidence that parked or rejected it. History preserves memory; it does not
authorise reactivation.

## Environment roles

- **Codex** is the primary repository-native environment for implementation, engineering,
  testing and verification.
- **ChatGPT** is the sponsor, research, strategy and exploration environment.

Neither environment is a truth store. Decisions and evidence that constrain future work
must be reconciled into the appropriate repository owner (`BACKLOG.md`, active issue/PR,
charter, Way of Working, foundation, assumptions, value evidence or history) before the
session ends.

## Operating discipline

- Keep **WIP = 1** for active execution: one issue, one branch, one PR.
- Put evidence before scope and compare against the strongest boring baseline.
- Preserve negative, parity and stop evidence; do not rescue failed claims post hoc.
- Fail closed when evidence, provenance, execution or verification is missing or malformed.
- Do no fake work: never claim research, observation, execution, testing, review or source
  access that did not occur.
- Do not copy mutable WIP, current counts, issue status or queue state into this file. Read
  their canonical owners instead.
