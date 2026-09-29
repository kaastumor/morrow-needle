"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const Search = require("./search/search.js");
const View = require("./search/evidence-view.js");

const data = require("./search/index.json");
const resources = require("./search/resources.json");
const engine = Search.createEngine(data, resources);
const presenter = View.createPresenter(engine);

test("maintained search excludes experimental and national sources", () => {
  assert.deepEqual(Object.keys(data.sources).sort(), ["actors", "eudamed", "operators"]);
  assert.equal(resources.registry.languages.length, 24);
  for (const unit of [...data.sections, ...data.blocks]) {
    assert.ok(data.sources[unit.sourceId]);
    assert.equal(unit.text, unit.lines.map(line => line.text).join("\n"));
    for (const line of unit.lines) {
      assert.equal(data.sources[unit.sourceId].lines.find(x => x.line === line.line)?.text, line.text);
    }
  }
});

test("ordinary question presents source-bound text and complete context", () => {
  const found = presenter.present(engine.search("When is actor registration mandatory?", {queryLanguage: "en"}));
  assert.ok(found.cards.length);
  for (const card of found.cards) {
    assert.equal(card.kind, "section");
    assert.equal(card.sourceLanguage, "en");
    assert.equal(card.fullSection.text, data.sections.find(s => s.id === card.id).text);
    assert.match(card.preview.notice, /section|excerpt|complete/i);
    assert.match(card.url, /^https:\/\//);
  }
});

test("exact act reference is a guidance mention, not retrieved act text", () => {
  const found = presenter.present(engine.search("2017/745", {queryLanguage: "en"}));
  assert.equal(found.status, "REFERENCE_MENTIONS_ONLY");
  assert.ok(found.cards.length);
  assert.ok(found.cards.every(c => c.kind === "locator" && /not available/.test(c.notice)));
});

test("unsupported and missing-language states remain explicit", () => {
  assert.equal(engine.search("neutrino planet", {queryLanguage: "en"}).status, "NO_SUPPORTED_TERMS");
  const dutch = engine.search("EUDAMED actor registratie", {queryLanguage: "nl"});
  assert.equal(dutch.primary.length, 0);
  assert.equal(dutch.coverage.sameLanguageSourceAvailable, false);
  const allowed = engine.search("EUDAMED actor registratie", {queryLanguage: "nl", allowOtherLanguages: true});
  assert.ok(allowed.primary.every(hit => hit.sourceLanguageFallback));
});

test("built route loads the retained modules and keeps no-script official links", () => {
  const html = fs.readFileSync(path.join(__dirname, "index.html"), "utf8");
  for (const name of ["language", "word-forms", "search", "evidence-view", "search-panel"]) {
    assert.match(html, new RegExp(`search/${name}\\.js`));
  }
  assert.match(html, /id="needle-search"/);
  assert.match(html, /https:\/\/eur-lex\.europa\.eu\/eli\/reg\/2017\/745/);
  assert.match(html, /https:\/\/eur-lex\.europa\.eu\/eli\/reg\/2017\/746/);
});
