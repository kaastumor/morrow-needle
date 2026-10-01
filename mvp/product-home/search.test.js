"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const SEARCH = path.join(__dirname, "search");
const data = JSON.parse(fs.readFileSync(path.join(SEARCH, "index.json"), "utf8"));
const resources = JSON.parse(fs.readFileSync(path.join(SEARCH, "resources.json"), "utf8"));
const engine = require("./search/medical-engine.js").createEngine(data, resources);
const evidenceView = require("./search/evidence-view.js");
const presenter = evidenceView.createPresenter(engine);
const panel = require("./search/search-panel.js");
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
  for (const question of [
    "When is registration required for importing cosmetics into the EU?",
    "What registration is required for an importer of toys?",
    "When is registration required for importing goods?"
  ]) {
    const result = engine.search(question, {queryLanguage: "en"});
    assert.equal(result.status, "OUTSIDE_MAINTAINED_COVERAGE", question);
    assert.equal(result.primary.length, 0, question);
    assert.equal(result.evidence.length, 0, question);
  }
});

test("NIS2 and AI Act threat cases do not substitute captured medical guidance", () => {
  for (const reference of ["2022/2555", "2024/1689"]) {
    const result = engine.search(reference, {queryLanguage: "en"});
    assert.equal(result.status, "REFERENCE_NOT_IN_SNAPSHOT", reference);
    assert.equal(result.primary.length, 0, reference);
    assert.equal(result.evidence.length, 0, reference);
  }

  for (const question of [
    "When did NIS2 take effect in the Netherlands?",
    "When does the AI Act apply to high-risk systems?"
  ]) {
    const result = engine.search(question, {queryLanguage: "en"});
    assert.notEqual(result.status, "RESULTS", question);
    assert.equal(result.primary.length, 0, question);
    assert.equal(result.evidence.length, 0, question);
  }
});

test("the retained IGJ forecast is visibly qualified without rewriting its source text", () => {
  const result = presenter.present(engine.search("EUDAMED", {queryLanguage: "en"}));
  const forecast = result.cards.find(card => card.id === "igj:s5");
  assert.ok(forecast);
  assert.match(forecast.fullSection.text, /January 2026 \(expected date\)/);
  assert.match(forecast.editorialWarning, /Do not use that forecast as current EUDAMED status/);
  assert.equal(forecast.editorialWarningUrl, "https://health.ec.europa.eu/medical-devices-eudamed/overview_en");
  assert.ok(result.cards.filter(card => card.id !== "igj:s5").every(card => !card.editorialWarning));
});

test("an explicit medical-device question retains its guidance results", () => {
  const result = engine.search("medical device importer registration", {queryLanguage: "en"});
  assert.equal(result.status, "RESULTS");
  assert.ok(result.primary.length > 0);
});

test("home keeps direct paths and a no-script fallback", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  assert.match(html, /id="medical-guidance-search"/);
  assert.match(html, /<noscript>/);
  assert.match(html, /href="\/medical-devices\/"/);
  assert.match(html, /href="\/medical-devices\/#sources"/);
});


test("represented exact identifiers own deterministic internal act routes", () => {
  const mdr = presenter.present(engine.search("2017/745", {queryLanguage: "en"}));
  const ivdr = presenter.present(engine.search("2017/746", {queryLanguage: "en"}));

  assert.deepEqual(mdr.navigation, {
    kind: "act",
    href: "/medical-devices/mdr/",
    label: "Open represented MDR detail",
    notice: "Exact identifier maps to a maintained internal act view. This navigation does not establish applicability or replace the official act."
  });
  assert.deepEqual(ivdr.navigation, {
    kind: "act",
    href: "/medical-devices/ivdr/",
    label: "Open represented IVDR detail",
    notice: "Exact identifier maps to a maintained internal act view. This navigation does not establish applicability or replace the official act."
  });
});

test("ordinary medical results continue only to the bounded overview", () => {
  const view = presenter.present(engine.search("medical device importer registration", {queryLanguage: "en"}));
  assert.equal(view.status, "RESULTS");
  assert.deepEqual(view.navigation, {
    kind: "overview",
    href: "/medical-devices/",
    label: "Continue in medical-device overview",
    notice: "No single act identity was inferred from these guidance matches. Use the bounded overview to choose the represented branch."
  });
});

test("outside and unknown-reference states gain no internal act shortcut", () => {
  const outside = presenter.present(engine.search("When did NIS2 take effect in the Netherlands?", {queryLanguage: "en"}));
  const unknown = presenter.present(engine.search("2022/2555", {queryLanguage: "en"}));
  assert.equal(outside.navigation, null);
  assert.equal(unknown.navigation, null);
});

test("search panel module parses with connected-navigation rendering available", () => {
  assert.equal(typeof panel.mount, "function");
  assert.equal(typeof evidenceView.renderContinuation, "function");
});


test("WP6 D6-D8 exact references and ordinary wording fail closed", () => {
  for (const reference of ["2026/1323", "2026/1022", "2025/90725"]) {
    const result = engine.search(reference, {queryLanguage: "en"});
    assert.equal(result.status, "REFERENCE_NOT_IN_SNAPSHOT", reference);
    assert.equal(result.primary.length, 0, reference);
    assert.equal(result.evidence.length, 0, reference);
    assert.equal(presenter.present(result).navigation, null, reference);
  }

  const decision = engine.search("Which Member States does Decision 2026/1323 apply to?", {queryLanguage: "en"});
  assert.equal(decision.status, "REFERENCE_NOT_IN_SNAPSHOT");
  assert.equal(presenter.present(decision).navigation, null);

  const customs = engine.search("When do the temporary EUR 3 customs duty data requirements apply?", {queryLanguage: "en"});
  assert.equal(customs.status, "NO_SUPPORTED_TERMS");
  assert.equal(presenter.present(customs).navigation, null);

  const corrigendum = engine.search("What did the September 2025 corrigendum to Regulation 2024/2956 change?", {queryLanguage: "en"});
  assert.equal(corrigendum.status, "REFERENCE_NOT_IN_SNAPSHOT");
  assert.equal(presenter.present(corrigendum).navigation, null);
});


test("WP7 held-back cases remain fail-closed after first exposure", () => {
  for (const reference of ["2023/1230", "2023/2225", "2026/90645", "2023/0133"]) {
    const result = engine.search(reference, {queryLanguage: "en"});
    assert.equal(result.status, "REFERENCE_NOT_IN_SNAPSHOT", reference);
    assert.equal(result.primary.length, 0, reference);
    assert.equal(result.evidence.length, 0, reference);
    assert.equal(presenter.present(result).navigation, null, reference);
  }

  const machinery = engine.search("Does the Machinery Regulation already apply and replace Directive 2006/42/EC?", {queryLanguage: "en"});
  assert.equal(machinery.status, "REFERENCE_NOT_IN_SNAPSHOT");
  assert.equal(presenter.present(machinery).navigation, null);

  const credit = engine.search("Do the new EU consumer credit rules apply from 20 November 2025?", {queryLanguage: "en"});
  assert.equal(credit.status, "OUTSIDE_MAINTAINED_COVERAGE");
  assert.equal(presenter.present(credit).navigation, null);

  const corrigendum = engine.search("Did the 3 August 2026 corrigendum change the English ecodesign rules for electronic displays?", {queryLanguage: "en"});
  assert.equal(corrigendum.status, "OUTSIDE_MAINTAINED_COVERAGE");
  assert.equal(presenter.present(corrigendum).navigation, null);

  const proposal = engine.search("Is the EU standard essential patents proposal still ongoing?", {queryLanguage: "en"});
  assert.equal(proposal.status, "NO_SUPPORTED_TERMS");
  assert.equal(presenter.present(proposal).navigation, null);
});
