"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const {ACTS} = require("./medical-act-detail/acts.js");
const {renderActPage} = require("./medical-act-detail/render.js");

const MVP = __dirname;

function readSource(rel) {
  return fs.readFileSync(path.join(MVP, rel), "utf8");
}

function retainedHtml() {
  return new Map([
    ["home", readSource("product-home/index.html")],
    ["medical", readSource("medical-devices-summary/index.html")],
    ["mdr", renderActPage(ACTS.mdr)],
    ["ivdr", renderActPage(ACTS.ivdr)],
    ["customs", readSource("customs-low-value-imports/index.html")],
    ["regime-v2", readSource("regime-density-v0.2/index.html")],
    ["candidate-b", readSource("candidate-b/index.html")]
  ]);
}

test("WP7 retained public route contracts keep common navigation and return affordances", () => {
  for (const [route, html] of retainedHtml()) {
    assert.match(html, /Needle EU/, route);
    assert.match(html, /href="\/"/, route);
    assert.match(html, /product-shell\.css/, route);
  }
});

test("WP7 retained routes expose keyboard-visible entry points and focus targets", () => {
  for (const [route, html] of retainedHtml()) {
    assert.match(html, /class="skip-link"/, route);
    assert.match(html, /id="main"/, route);
  }
  const shell = readSource("product-shell.css");
  assert.match(shell, /:focus-visible/);
  assert.match(shell, /\.skip-link:focus/);
});

test("WP7 deep links remain present in rendered MDR IVDR and contrast contracts", () => {
  for (const act of Object.values(ACTS)) {
    const html = renderActPage(act);
    for (const fragment of ["time", "relationships", "sources"]) {
      assert.match(html, new RegExp('id="' + fragment + '"'));
      assert.match(html, new RegExp('href="#' + fragment + '"'));
    }
    assert.match(html, /href="\/medical-devices\/"/);
    assert.match(html, /href="\/#search-heading"/);
  }

  const customs = readSource("customs-low-value-imports/index.html");
  for (const fragment of ["scope", "time", "relationships", "sources"]) {
    assert.match(customs, new RegExp('id="' + fragment + '"'));
    assert.match(customs, new RegExp('href="#' + fragment + '"'));
  }
});

test("WP7 narrow-layout source contracts avoid horizontal-scroll dependence", () => {
  const cssFiles = [
    "product-shell.css",
    "product-home/search.css",
    "medical-act-detail/styles.css",
    "customs-low-value-imports/styles.css",
    "regime-density-v0.2/styles.css"
  ];
  for (const rel of cssFiles) {
    const css = readSource(rel);
    assert.doesNotMatch(css, /overflow-x:\s*(?:scroll|auto)/, rel);
  }
  assert.match(readSource("product-shell.css"), /@media \(max-width: 38rem\)/);
  assert.match(readSource("product-home/search.css"), /@media \(max-width: 38rem\)/);
  assert.match(readSource("customs-low-value-imports/styles.css"), /@media\(max-width:46rem\)/);
});

test("WP7 disclosure and no-script fallbacks remain represented", () => {
  const home = readSource("product-home/index.html");
  assert.match(home, /<noscript>/);
  const evidenceView = readSource("product-home/search/evidence-view.js");
  assert.match(evidenceView, /node\('details'\)|createElement\('details'\)/);
  assert.match(evidenceView, /document\.createElement\('summary'\)|node\('summary'/);
});
