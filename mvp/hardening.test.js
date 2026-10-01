"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const {buildStaticDemo} = require("./candidate-b/build-static-demo.js");

const ROOT = path.resolve(__dirname, "..");
const DIST = path.join(ROOT, "dist");

function read(rel) {
  return fs.readFileSync(path.join(DIST, rel), "utf8");
}

test("WP7 pinned build exposes all retained public routes and return paths", () => {
  buildStaticDemo();
  const routes = [
    "index.html",
    "medical-devices/index.html",
    "medical-devices/mdr/index.html",
    "medical-devices/ivdr/index.html",
    "customs-low-value-imports/index.html",
    "regime-v2/index.html",
    "mvp/candidate-b/index.html"
  ];
  for (const route of routes) {
    assert.ok(fs.existsSync(path.join(DIST, route)), route);
    const html = read(route);
    assert.match(html, /Needle EU/, route);
    assert.match(html, /href="\/"/, route);
    assert.match(html, /product-shell\.css/, route);
  }
});

test("WP7 retained routes expose keyboard-visible entry points and focus targets", () => {
  buildStaticDemo();
  for (const route of [
    "index.html",
    "medical-devices/index.html",
    "medical-devices/mdr/index.html",
    "medical-devices/ivdr/index.html",
    "customs-low-value-imports/index.html",
    "regime-v2/index.html",
    "mvp/candidate-b/index.html"
  ]) {
    const html = read(route);
    assert.match(html, /class="skip-link"/, route);
    assert.match(html, /id="main"/, route);
  }
  const shell = read("product-shell.css");
  assert.match(shell, /:focus-visible/);
  assert.match(shell, /\.skip-link:focus/);
});

test("WP7 deep links remain present in generated MDR IVDR and contrast pages", () => {
  buildStaticDemo();
  for (const route of ["medical-devices/mdr/index.html", "medical-devices/ivdr/index.html"]) {
    const html = read(route);
    for (const fragment of ["time", "relationships", "sources"]) {
      assert.match(html, new RegExp('id="' + fragment + '"'), route + " #" + fragment);
      assert.match(html, new RegExp('href="#' + fragment + '"'), route + " href #" + fragment);
    }
    assert.match(html, /href="\/medical-devices\/"/);
    assert.match(html, /href="\/#search-heading"/);
  }
  const customs = read("customs-low-value-imports/index.html");
  for (const fragment of ["scope", "time", "relationships", "sources"]) {
    assert.match(customs, new RegExp('id="' + fragment + '"'));
    assert.match(customs, new RegExp('href="#' + fragment + '"'));
  }
});

test("WP7 narrow-layout source contracts avoid horizontal-scroll dependence", () => {
  const cssFiles = [
    "product-shell.css",
    "search.css",
    "medical-devices/act-detail.css",
    "customs-low-value-imports/styles.css",
    "regime-v2/styles.css"
  ];
  buildStaticDemo();
  for (const rel of cssFiles) {
    const css = read(rel);
    assert.doesNotMatch(css, /overflow-x:\s*(?:scroll|auto)/, rel);
  }
  assert.match(read("product-shell.css"), /@media \(max-width: 38rem\)/);
  assert.match(read("search.css"), /@media \(max-width: 38rem\)/);
  assert.match(read("customs-low-value-imports/styles.css"), /@media\(max-width:46rem\)/);
});

test("WP7 disclosure and no-script fallbacks remain represented", () => {
  buildStaticDemo();
  const home = read("index.html");
  assert.match(home, /<noscript>/);
  const evidenceView = fs.readFileSync(path.join(ROOT, "mvp", "product-home", "search", "evidence-view.js"), "utf8");
  assert.match(evidenceView, /node\('details'\)|createElement\('details'\)/);
  assert.match(evidenceView, /document\.createElement\('summary'\)|node\('summary'/);
});
