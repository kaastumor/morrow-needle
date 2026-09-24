"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const { projectCorpus } = require("./app.js");

function caseRecord(overrides = {}) {
  return {
    id: "safe-case",
    title: "Safe case",
    domain: "test",
    jurisdiction: "EU",
    trap_classes: ["TRAP"],
    provenance: { issue: 1, role: "DERIVATION" },
    decisive_trap: "A concrete trap.",
    ...overrides
  };
}

function corpus(cases) {
  return { trap_classes: { TRAP: "Trap description" }, cases };
}

test("projects summary without mutating canonical input", () => {
  const input = corpus([
    caseRecord(),
    caseRecord({ id: "evaluation-case", provenance: { issue: 2, role: "EVALUATION" }, evaluation_mode: "LATENT_TRAP_DETECTION", evaluation_result: "R_PASS_M_PASS" })
  ]);
  const before = JSON.stringify(input);
  const projection = projectCorpus(input);
  assert.equal(JSON.stringify(input), before);
  assert.deepEqual(projection.summary, {
    totalCases: 2,
    trapClasses: 1,
    roleCounts: { DERIVATION: 1, EVALUATION: 1 },
    modeCounts: { SURFACED_TRAP_ADJUDICATION: 0, LATENT_TRAP_DETECTION: 1, UNSPECIFIED: 0 }
  });
});

test("fails closed when cases array is missing", () => {
  assert.throws(() => projectCorpus({ trap_classes: {} }), /cases must be an array/);
});

test("fails closed on malformed and duplicate case IDs", () => {
  assert.throws(() => projectCorpus(corpus([caseRecord({ id: "Bad ID" })])), /unsupported format/);
  assert.throws(() => projectCorpus(corpus([caseRecord(), caseRecord()])), /duplicate case id/);
});

test("fails closed on unknown trap and unsupported evaluation metadata", () => {
  assert.throws(() => projectCorpus(corpus([caseRecord({ trap_classes: ["UNKNOWN"] })])), /unknown trap class/);
  assert.throws(() => projectCorpus(corpus([caseRecord({ provenance: { role: "EVALUATION" }, evaluation_mode: "MAGIC" })])), /evaluation_mode is unsupported/);
  assert.throws(() => projectCorpus(corpus([caseRecord({ evaluation_result: "PASS" })])), /only supported for EVALUATION/);
});
