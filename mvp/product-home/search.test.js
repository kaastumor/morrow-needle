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
const pageNavigation = require("./search/page-navigation.js");

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

test("the stale IGJ forecast is preserved for audit but retired from active evidence", () => {
  const result = presenter.present(engine.search("EUDAMED", {queryLanguage: "en"}));
  assert.equal(result.cards.some(card => card.id === "igj:s5"), false);

  const forecast = engine.sourceContext("igj:s5");
  assert.ok(forecast);
  assert.equal(forecast.evidenceEligible, false);
  assert.equal(forecast.maintenanceStatus, "RETIRED_FROM_ACTIVE_EVIDENCE");
  assert.equal(forecast.maintenanceCheckedAt, "2026-10-01");
  assert.match(forecast.text, /January 2026 \(expected date\)/);
  assert.match(forecast.editorialWarning, /Do not use that forecast as current EUDAMED status/);
  assert.equal(forecast.maintenanceEvidenceUrl, "https://health.ec.europa.eu/medical-devices-eudamed/overview_en");
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


test("exact-reference lookup also honors evidence retirement", () => {
  const retired = structuredClone(data);
  const block = retired.blocks.find(item => item.id === "eudamed:b39");
  assert.ok(block);
  block.evidenceEligible = false;

  const retiredEngine = require("./search/medical-engine.js").createEngine(retired, resources);
  const result = retiredEngine.search("2017/746", {queryLanguage: "en"});

  assert.equal(result.status, "REFERENCE_MENTIONS_ONLY");
  assert.equal(result.primary.some(item => item.id === "eudamed:b39"), false);
  assert.equal(result.primary.some(item => item.id === "operators:b39"), true);
});

test("current EUDAMED timing result remains available after stale-source retirement", () => {
  const result = engine.search("EUDAMED is mandatory now: does that include all six modules?", {queryLanguage: "en", budget: 400});
  assert.equal(result.status, "RESULTS");
  assert.ok(result.primary.some(item => item.sourceId === "eudamed"));
  assert.equal(result.primary.some(item => item.id === "igj:s5"), false);
  assert.match(result.evidence.map(item => item.text).join("\n"), /28 May 2026|first four modules are mandatory|following 4 modules of EUDAMED became mandatory/i);
});

function locate(question, language = "en") {
  return pageNavigation.locate(question, engine.search(question, {queryLanguage: language, budget: 400}));
}

test("ordinary questions reach existing time and role sections without expanding captured evidence", () => {
  assert.equal(locate("What changed in IVDR in 2024, and when do the dates apply?").choices[0].href, "/medical-devices/ivdr/#time");
  const customs = "What changes for low-value customs parcels under EUR 150?";
  const response = engine.search(customs, {queryLanguage: "en"});
  assert.equal(response.primary.length, 0);
  assert.equal(response.evidence.length, 0);
  assert.equal(locate(customs).choices[0].href, "/customs-low-value-imports/#time");
  assert.equal(locate("What are the MDR distributor roles?").choices[0].href, "/medical-devices/mdr/#roles");
  assert.equal(locate("Does EUDAMED include all six modules?").choices[0].href, "/medical-devices/");
});

test("conflicting subjects offer choices and vague questions do not silently choose an act", () => {
  for (const question of ["MDR and IVDR dates", "MDR 2017/746", "2017/745 and 2017/746"]) {
    const result = locate(question);
    assert.equal(result.kind, "clarify", question);
    assert.equal(result.choices.length, 2, question);
    assert.deepEqual(new Set(result.choices.map(item => item.label)), new Set(["Medical devices (MDR)", "In-vitro diagnostics (IVDR)"]));
  }
  const vague = locate("What changed?");
  assert.equal(vague.kind, "clarify");
  assert.deepEqual(vague.choices.map(item => item.href), ["/medical-devices/", "/customs-low-value-imports/#time"]);
});

test("exact page locators honor identifier type and never replace unknown references", () => {
  for (const question of ["2017/746", "32017R0746", "https://data.europa.eu/eli/reg/2017/746/oj"]) {
    assert.equal(locate(question).choices[0].href, "/medical-devices/ivdr/", question);
  }
  assert.equal(locate("https://data.europa.eu/eli/reg_del/2026/1022/oj").choices[0].href, "/customs-low-value-imports/");
  for (const question of ["2017/745 and 2022/2555", "MDR 2024/1689", "https://data.europa.eu/eli/reg_del/2017/746/oj", "https://data.europa.eu/eli/reg/2026/1022/oj", "https://data.europa.eu/eli/reg/2017/746/2024-07-09"]) {
    assert.equal(locate(question), null, question);
  }
});

test("navigation respects unsupported subjects, language and requested-state guards", () => {
  for (const question of ["When does the AI Act apply?", "MDR and cosmetics registration", "MDR as of 2020-01-01", "MDR on 01/02/2026"]) {
    assert.equal(locate(question), null, question);
  }
  assert.equal(locate("2017/746", "nl"), null);
  assert.equal(presenter.present(engine.search("2017/746", {queryLanguage: "nl"})).navigation, null);
  assert.equal(presenter.present(engine.search("2017/745 and 2022/2555", {queryLanguage: "en"})).navigation, null);
});

// Minimal DOM fixture for panel interaction; this is not browser/layout verification.
function panelFixture() {
  const document = {createElement: tag => new Element(tag)};
  class Element {
    constructor(tag) { this.tagName = tag; this.ownerDocument = document; this.children = []; this.attributes = {}; this.listeners = {}; this.textContent = ""; }
    append(...items) { this.children.push(...items); }
    replaceChildren(...items) { this.children = items; }
    setAttribute(name, value) { this.attributes[name] = value; }
    removeAttribute(name) { delete this.attributes[name]; }
    addEventListener(name, handler) { this.listeners[name] = handler; }
    removeEventListener(name) { delete this.listeners[name]; }
    focus() { this.focused = true; }
    all() { return [this, ...this.children.flatMap(child => child.all())]; }
  }
  const root = document.createElement("div");
  return {root, mounted: panel.mount(root, {data, resources, engineFactory: require("./search/medical-engine.js").createEngine})};
}

test("panel separates page navigation from guidance and clears stale links on settings changes", () => {
  const {root, mounted} = panelFixture();
  const view = mounted.search("What changes for low-value customs parcels under EUR 150?");
  assert.equal(view.cards.length, 0);
  assert.equal(root.all().find(item => item.tagName === "a").href, "/customs-low-value-imports/#time");
  assert.match(root.all().find(item => item.attributes.role === "status").textContent, /No captured medical-guidance passage/);
  root.all().find(item => item.tagName === "select").listeners.change();
  assert.equal(root.all().filter(item => item.tagName === "a").length, 0);
  const timing = mounted.search("EUDAMED is mandatory now: does that include all six modules?");
  assert.ok(timing.cards.length > 0);
  assert.match(root.all().find(item => item.attributes.role === "status").textContent, /Results may cover only part of the question/);
  mounted.search("2017/745 and 2022/2555");
  assert.equal(root.all().filter(item => item.tagName === "a" && item.href.startsWith("/")).length, 0);
  mounted.search("MDR and cosmetics registration");
  assert.equal(root.all().filter(item => item.tagName === "a" && item.href.startsWith("/")).length, 0);
  root.all().find(item => item.tagName === "button" && item.textContent === "Clear").listeners.click();
  assert.equal(root.all().find(item => item.tagName === "textarea").value, "");
  mounted.destroy();
  assert.equal(root.children.length, 0);
});
