"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const SEARCH = path.join(__dirname, "search");
const data = JSON.parse(fs.readFileSync(path.join(SEARCH, "index.json"), "utf8"));
const resources = JSON.parse(fs.readFileSync(path.join(SEARCH, "resources.json"), "utf8"));
const engine = require("./search/medical-engine.js").createEngine(data, resources);
const app = require("./search/app.js");

test("public search bundle contains only the admitted medical guidance sources", () => {
  assert.equal(app.validateBundle(data, resources), true);
  assert.deepEqual(Object.keys(data.sources).sort(), [...app.APPROVED_SOURCES].sort());
  assert.ok(data.sections.length > 0);
  assert.ok(data.blocks.length > 0);
  assert.ok(data.sections.every(item => app.APPROVED_SOURCES.includes(item.sourceId)));
  assert.ok(data.blocks.every(item => app.APPROVED_SOURCES.includes(item.sourceId)));
  assert.equal(JSON.stringify(data).includes('"returns"'), false);
  assert.equal(JSON.stringify(data).includes('"guarantees"'), false);
});

test("ordinary EUDAMED timing question returns the four-module qualification", () => {
  const result = engine.search("EUDAMED is mandatory now: does that include all six modules?", {queryLanguage: "en", budget: 400});
  assert.equal(result.status, "RESULTS");
  assert.ok(result.primary.some(item => item.sourceId === "eudamed"));
  assert.match(result.evidence.map(item => item.text).join("\n"), /first four modules are mandatory|following 4 modules of EUDAMED became mandatory/i);
});

test("known IVDR reference remains a locator rather than invented act text", () => {
  const result = engine.search("2017/746", {queryLanguage: "en"});
  assert.equal(result.status, "REFERENCE_MENTIONS_ONLY");
  assert.ok(result.primary.length > 0);
  assert.ok(result.primary.every(item => item.reason.includes("mentioned in guidance")));
});

test("generic and outside-coverage questions fail safely", () => {
  assert.equal(engine.search("What changed?", {queryLanguage: "en"}).status, "CLARIFY");
  const consumer = engine.search("A private person sold me used goods: is that the same guarantee as buying second-hand from a professional?", {queryLanguage: "en"});
  assert.equal(consumer.status, "OUTSIDE_MAINTAINED_COVERAGE");
  assert.equal(consumer.primary.length, 0);
});

test("home keeps direct paths and a no-script fallback", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  assert.match(html, /id="medical-guidance-search"/);
  assert.match(html, /<noscript>/);
  assert.match(html, /href="\/medical-devices\/"/);
  assert.match(html, /href="\/medical-devices\/#sources"/);
});
