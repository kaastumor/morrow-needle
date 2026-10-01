"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const {APP_FILES, REGIME_FILES, REGIME_V2_FILES, MEDICAL_SUMMARY_FILES, MEDICAL_ACT_ROUTES, CUSTOMS_CONTRAST_FILES, PRODUCT_HOME_FILES, PRODUCT_SEARCH_FILES, PILOT_FILES, FIXTURE_FILES, buildStaticDemo} = require("./build-static-demo.js");

const ROOT = path.resolve(__dirname, "..", "..");
const DIST = path.join(ROOT, "dist");

test("static bundle contains frozen Candidate-B plus the separate regime prototype", () => {
  const manifest = buildStaticDemo();

  assert.deepEqual(manifest.appFiles, APP_FILES);
  assert.deepEqual(manifest.fixtureFiles, FIXTURE_FILES);
  assert.deepEqual(manifest.regimeFiles, REGIME_FILES);
  assert.deepEqual(manifest.regimeV2Files, REGIME_V2_FILES);
  assert.deepEqual(manifest.medicalSummaryFiles, MEDICAL_SUMMARY_FILES);
  assert.deepEqual(manifest.medicalActRoutes, MEDICAL_ACT_ROUTES);
  assert.deepEqual(manifest.customsContrastFiles, CUSTOMS_CONTRAST_FILES);
  assert.deepEqual(manifest.productHomeFiles, PRODUCT_HOME_FILES);
  assert.deepEqual(manifest.productSearchFiles, PRODUCT_SEARCH_FILES);
  assert.deepEqual(manifest.pilotFiles, PILOT_FILES);
  assert.deepEqual(manifest.pilotRoutes, ["/research/issue494/a/", "/research/issue494/b/"]);
  assert.equal(manifest.fixtureFiles.length, 5);
  assert.equal(manifest.liveMonitoring, false);
  assert.equal(manifest.externalValueProven, false);

  for (const file of APP_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "mvp", "candidate-b", file)));
  }

  for (const file of REGIME_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "regime", file)));
  }

  for (const file of REGIME_V2_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "regime-v2", file)));
  }

  for (const file of MEDICAL_SUMMARY_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "medical-devices", file)));
  }

  for (const file of CUSTOMS_CONTRAST_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "customs-low-value-imports", file)));
  }

  for (const arm of ["a", "b"]) {
    for (const file of PILOT_FILES) {
      assert.ok(fs.existsSync(path.join(DIST, "research", "issue494", arm, file)));
    }
    const html = fs.readFileSync(path.join(DIST, "research", "issue494", arm, "index.html"), "utf8");
    for (const forbidden of ["protocol.md", "evidence.md", 'href="specimen.html"', 'href="baseline.html"', "github.com/kaastumor/morrow-needle/issues/494"]) {
      assert.equal(html.includes(forbidden), false, forbidden);
    }
  }

  for (const file of FIXTURE_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "fixtures", "dependency", file)));
  }

  for (const route of MEDICAL_ACT_ROUTES) {
    const detail = path.join(DIST, "medical-devices", route, "index.html");
    assert.ok(fs.existsSync(detail));
    const detailHtml = fs.readFileSync(detail, "utf8");
    assert.match(detailHtml, /Core act · source-bounded orientation/);
  }
  assert.ok(fs.existsSync(path.join(DIST, "medical-devices", "act-detail.css")));

  assert.ok(fs.existsSync(path.join(DIST, "index.html")));
  for (const file of PRODUCT_SEARCH_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "search", file)));
  }
  assert.ok(fs.existsSync(path.join(DIST, "product-shell.css")));
  assert.ok(fs.existsSync(path.join(DIST, "build-manifest.json")));
});

test("product entry and retained routes have a static return path while research stays isolated", () => {
  buildStaticDemo();
  const routes = ["index.html", "medical-devices/index.html", "medical-devices/mdr/index.html", "medical-devices/ivdr/index.html", "customs-low-value-imports/index.html", "regime-v2/index.html", "mvp/candidate-b/index.html"];
  for (const route of routes) {
    const html = fs.readFileSync(path.join(DIST, route), "utf8");
    assert.match(html, /Needle EU/);
    assert.match(html, /class="product-shell__brand" href="\/"/);
    assert.match(html, /href="\/#coverage"|href="#coverage"/);
    assert.match(html, /href="\/product-shell\.css"/);
  }
  const home = fs.readFileSync(path.join(DIST, "index.html"), "utf8");
  assert.doesNotMatch(home, /http-equiv="refresh"/);
  assert.match(home, /href="\/medical-devices\/"/);
  assert.match(home, /href="\/mvp\/candidate-b\/"/);
  assert.match(home, /href="\/customs-low-value-imports\/"/);
  const medical = fs.readFileSync(path.join(DIST, "medical-devices", "index.html"), "utf8");
  assert.match(medical, /href="\/regime-v2\/#explore"/);
  assert.match(medical, /href="\/regime-v2\/#changes"/);
  const deeper = fs.readFileSync(path.join(DIST, "regime-v2", "index.html"), "utf8");
  for (const fragment of ["explore", "changes", "expert"]) assert.match(deeper, new RegExp(`id="${fragment}"`));
  assert.match(deeper, /Return to medical-device overview/);
  for (const arm of ["a", "b"]) {
    const research = fs.readFileSync(path.join(DIST, "research", "issue494", arm, "index.html"), "utf8");
    assert.doesNotMatch(research, /product-shell__nav/);
  }
});

test("bundle is generated from canonical fixture paths rather than a committed second dataset", () => {
  buildStaticDemo();

  for (const file of FIXTURE_FILES) {
    const canonical = fs.readFileSync(
      path.join(ROOT, "fixtures", "dependency", file),
      "utf8"
    );
    const bundled = fs.readFileSync(
      path.join(DIST, "fixtures", "dependency", file),
      "utf8"
    );
    assert.equal(bundled, canonical);
  }
});
