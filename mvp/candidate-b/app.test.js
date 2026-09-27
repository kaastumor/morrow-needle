"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const {
  CASES,
  assertSupportedDate,
  findCases,
  projectStatus,
  statusLabel,
  consequenceLabel,
  sourceHref
} = require("./app.js");

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

test("known-standard lookup resolves exact references and useful aliases", () => {
  assert.equal(findCases("EN 60335-2-60:2003")[0].id, "lvd-en60335-2-60");
  assert.equal(findCases("EN 71")[0].id, "toy-en71");
  assert.ok(findCases("LVD").length >= 2);
  assert.deepEqual(findCases("not in frozen set"), []);
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

test("raw internal states are translated into user-facing labels", () => {
  assert.equal(statusLabel("CITED_WITH_RESTRICTION"), "Cited — restriction applies");
  assert.match(consequenceLabel("NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE"), /not available/i);
});

test("official evidence links resolve from CELEX identifiers", () => {
  assert.equal(
    sourceHref({source_type:"EUR_LEX", identifier:"CELEX:32026D0080"}),
    "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32026D0080"
  );
});

test("static prototype states the product-compliance and frozen-data boundaries", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  assert.match(html, /does not determine full product compliance/i);
  assert.match(html, /does not replace the standard text, testing/i);
  assert.match(html, /Frozen demonstration data/i);
  assert.match(html, /not a live monitoring service/i);
  assert.doesNotMatch(html, /unique|best|superior|automates CE compliance/i);
});

test("primary interaction is known-standard lookup rather than internal case selection", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  assert.match(html, /Standard reference/i);
  assert.match(html, /id="standard-query"/);
  assert.doesNotMatch(html, /id="case-select"/);
  assert.doesNotMatch(html, />\s*Case\s*</i);
});

test("prototype is responsive and keyboard-focus visible", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");
  assert.match(html, /class="skip-link"/);
  assert.match(css, /:focus-visible/);
  assert.match(css, /@media \(max-width: 46rem\)/);
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


test("LVD lifecycle view contains the required text-first legal information", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  for (const required of [
    "Directive 2014/35/EU",
    "Council Directive 73/23/EEC",
    "Directive 2006/95/EC",
    "Codified as",
    "Recast as",
    "26 Feb 2014",
    "29 Mar 2014",
    "18 Apr 2014",
    "20 Apr 2016",
    "Directive (EU) 2024/2749",
    "30 May 2026",
    "Article 114 TFEU",
    "Regulation (EC) No 765/2008",
    "Decision No 768/2008/EC",
    "Regulation (EU) No 1025/2012",
    "What flows from Article 12",
    "Coverage and correction"
  ]) {
    assert.ok(html.includes(required), "missing required lifecycle text: " + required);
  }
});

test("LVD lifecycle view keeps relationship semantics in readable text", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Product-law framework/i);
  assert.match(html, /Common legislative framework/i);
  assert.match(html, /Standardisation framework/i);
  assert.match(html, /Amended by/i);
  assert.match(html, /no successor is represented in this evidence view/i);
  assert.doesNotMatch(html, /RELATED_TO/);
  assert.doesNotMatch(html, />\s*all influences\s*</i);
});

test("LVD lifecycle view exposes official evidence and bounded-currentness", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Evidence verified/i);
  assert.match(html, /27 September 2026/i);
  assert.match(html, /Legal view/i);
  assert.match(html, /EUR-Lex consolidation used/i);
  assert.match(html, /CELEX:02014L0035-20260530/);
  assert.match(html, /CELEX:32024L2749/);
  assert.match(html, /not live legal monitoring/i);
  assert.match(html, /does not claim to map every amendment/i);
});

test("LVD lifecycle view links back to the two frozen LVD status examples", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /data-case-id="lvd-en60335-2-14"/);
  assert.match(html, /data-case-id="lvd-en60335-2-60"/);
});

test("lifecycle visual treatment preserves a narrow-screen text layout", () => {
  const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");

  assert.match(css, /\.lifecycle-timeline li/);
  assert.match(css, /\.dependency-chain/);
  assert.match(css, /@media \(max-width: 46rem\)/);
  assert.match(css, /grid-template-columns: 1fr/);
});


test("LVD applicability separates formal addressee from practical scope dimensions", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  for (const required of [
    "Who / what does this concern?",
    "Formal addressee",
    "EU Member States",
    "Object / material scope",
    "Market activity",
    "Economic operators",
    "Territory / market context",
    "Time represented here"
  ]) {
    assert.ok(html.includes(required), "missing applicability dimension: " + required);
  }

  assert.match(html, /50–1,000 V AC/);
  assert.match(html, /75–1,500 V DC/);
  assert.match(html, /Union market in the course of a commercial activity/i);
  assert.match(html, /does not determine a reader's national implementation position/i);
});

test("LVD scope exposes Annex II exclusions without inventing alternative regimes", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Major Annex II exclusions/i);
  assert.match(html, /explosive atmosphere/i);
  assert.match(html, /radiology and medical purposes/i);
  assert.match(html, /plugs and socket outlets for domestic use/i);
  assert.match(html, /custom-built evaluation kits/i);
  assert.match(html, /does not by itself tell you which other EU or national legal regime applies/i);
});

test("LVD actor orientation names roles but refuses personalised role determination", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  for (const role of ["Manufacturer", "Authorised representative", "Importer", "Distributor"]) {
    assert.match(html, new RegExp(role, "i"));
  }

  assert.match(html, /role orientation, not a determination of which role you occupy/i);
  assert.match(html, /Article 6 — full source/i);
  assert.match(html, /Article 9 — full source/i);
});

test("operative dependencies distinguish definition imports from procedural dependencies", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Operative legal dependencies/i);
  assert.match(html, /imports definition from/i);
  assert.match(html, /LVD Article 2\(9\)/i);
  assert.match(html, /Regulation \(EU\) No 1025\/2012 · Article 2\(1\)\(c\)/i);
  assert.match(html, /uses procedure in/i);
  assert.match(html, /Articles 10\(6\) and 11/i);
  assert.match(html, /Why this matters here/i);
  assert.match(html, /does not mean the whole external Regulation is automatically imported/i);
  assert.match(html, /eli\/reg\/2012\/1025\/2024-12-13\/eng/);
});

test("LVD presumption section keeps Articles 12, 13 and 14 distinct", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Article 12 provides/i);
  assert.match(html, /Article 13 provides a route involving published IEC safety provisions/i);
  assert.match(html, /Article 14 provides a further national-standard route/i);
  assert.match(html, /not a general certificate of full product compliance/i);
});

test("Navigator exposes a correction route and independent-status boundary", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /Coverage and correction/i);
  assert.match(html, /issues\/new/);
  assert.match(html, /independent research prototype/i);
  assert.match(html, /not an EU institution or official legal service/i);
});


test("applicability cards explicitly reveal where expanded detail can be found", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  const js = fs.readFileSync(path.join(__dirname, "app.js"), "utf8");

  assert.match(html, /See exclusions below ↓/);
  assert.match(html, /data-details-target="lvd-exclusions"/);
  assert.match(html, /id="lvd-exclusions"/);
  assert.match(html, /See role details below ↓/);
  assert.match(html, /data-details-target="lvd-actors"/);
  assert.match(html, /id="lvd-actors"/);
  assert.match(js, /target\.open = true/);
  assert.match(js, /summary\.focus/);
});

test("lineage is presented as an explicit typed relationship path", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /class="lineage-path"/);
  assert.match(html, />Codified as</);
  assert.match(html, />Recast as</);
  assert.match(html, /Earlier regime/);
  assert.match(html, /Current focal act/);
});

test("framework context uses a relationship ledger rather than equal-weight cards", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /class="relation-ledger"/);
  assert.match(html, /class="relation-row"/);
  assert.match(html, /class="relation-kind">Legal basis/);
  assert.match(html, /class="relation-kind">Amended by/);
});

test("operative dependencies visually encode focal provision, relation and external provision", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");

  assert.match(html, /class="operative-routes"/);
  assert.match(html, /class="dependency-path"/);
  assert.match(html, /Focal provision/);
  assert.match(html, /External provision/);
  assert.match(html, /imports definition from/);
  assert.match(html, /uses procedure in/);
  assert.match(html, /Why this matters here/i);
});

test("relationship layouts collapse to one-dimensional reading order on narrow screens", () => {
  const css = fs.readFileSync(path.join(__dirname, "styles.css"), "utf8");

  assert.match(css, /\.lineage-path\s*\{[\s\S]*grid-template-columns:/);
  assert.match(css, /@media \(max-width: 58rem\)/);
  assert.match(css, /\.dependency-path\s*\{[\s\S]*grid-template-columns: 1fr/);
  assert.match(css, /\.relation-row\s*\{[\s\S]*grid-template-columns: 1fr/);
});
