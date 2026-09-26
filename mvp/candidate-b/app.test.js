"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const {CASES, assertSupportedDate, projectStatus, sourceHref} = require("./app.js");

const ROOT = path.join(__dirname, "..", "..");

function loadFixture(caseId) {
  const meta = CASES.find(entry => entry.id === caseId);
  const fixturePath = path.join(__dirname, meta.fixture);
  return {meta, record: JSON.parse(fs.readFileSync(fixturePath, "utf8"))};
}

test("prototype uses exactly the five frozen #411 cases", () => {
  assert.deepEqual(CASES.map(entry => entry.id), [
    "gar-en497",
    "machinery-en50434",
    "toy-en71",
    "lvd-en60335-2-14",
    "lvd-en60335-2-60"
  ]);
});

test("query date 2026-09-26 yields the frozen current states", () => {
  const expected = new Map([
    ["gar-en497", "NOT_CITED"],
    ["machinery-en50434", "CITED_WITH_RESTRICTION"],
    ["toy-en71", "CITED_WITH_RESTRICTION"],
    ["lvd-en60335-2-14", "NOT_CITED"],
    ["lvd-en60335-2-60", "CITED"]
  ]);

  for (const [caseId, state] of expected) {
    const {meta, record} = loadFixture(caseId);
    assert.equal(projectStatus(record, meta.standard, "2026-09-26").ojState, state);
  }
});

test("future LVD withdrawal is visible without being applied early", () => {
  const {meta, record} = loadFixture("lvd-en60335-2-60");
  const before = projectStatus(record, meta.standard, "2026-09-26");
  const after = projectStatus(record, meta.standard, "2027-01-18");

  assert.equal(before.ojState, "CITED");
  assert.equal(before.next.effective_from, "2027-01-18");
  assert.equal(after.ojState, "NOT_CITED");
  assert.equal(after.latest.effective_from, "2027-01-18");
});

test("formal non-publication changes owning event without inventing citation", () => {
  for (const caseId of ["gar-en497", "lvd-en60335-2-14"]) {
    const {meta, record} = loadFixture(caseId);
    const projection = projectStatus(record, meta.standard, "2026-09-26");
    assert.equal(projection.ojState, "NOT_CITED");
    assert.ok(projection.latest);
  }
});

test("Machinery restriction preserves citation while narrowing presumption", () => {
  const {meta, record} = loadFixture("machinery-en50434");
  const projection = projectStatus(record, meta.standard, "2026-09-26");

  assert.equal(projection.ojState, "CITED_WITH_RESTRICTION");
  assert.equal(projection.consequence, "RESTRICTED_TO_STATED_SCOPE");
  assert.match(projection.latest.scope.statement, /300 r\/min/);
});

test("official evidence links resolve from CELEX identifiers", () => {
  assert.equal(
    sourceHref({source_type:"EUR_LEX", identifier:"CELEX:32026D0080"}),
    "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D0080"
  );
});

test("static prototype states the product-compliance boundary", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  assert.match(html, /does not determine full product compliance/i);
  assert.match(html, /does not replace the standard text, testing/i);
  assert.doesNotMatch(html, /unique|best|superior|automates CE compliance/i);
});

test("prototype is responsive and keyboard-focus visible", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");
  assert.match(html, /class="skip-link"/);
  assert.match(css, /:focus-visible/);
  assert.match(css, /@media \(max-width: 42rem\)/);
});


test("each case exposes a bounded frozen evidence window", () => {
  for (const meta of CASES) {
    assert.ok(meta.supportedFrom);
    assert.ok(meta.supportedThrough);
    assert.doesNotThrow(() => assertSupportedDate(meta, meta.supportedFrom));
    assert.doesNotThrow(() => assertSupportedDate(meta, meta.supportedThrough));
  }
});

test("prototype refuses unsupported historical dates instead of inventing state", () => {
  const meta = CASES.find(entry => entry.id === "toy-en71");
  assert.throws(
    () => assertSupportedDate(meta, "2020-01-01"),
    /outside frozen evidence window/
  );
});
