"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const {APP_FILES, REGIME_FILES, REGIME_V2_FILES, FIXTURE_FILES, buildStaticDemo} = require("./build-static-demo.js");

const ROOT = path.resolve(__dirname, "..", "..");
const DIST = path.join(ROOT, "dist");

test("static bundle contains frozen Candidate-B plus the separate regime prototype", () => {
  const manifest = buildStaticDemo();

  assert.deepEqual(manifest.appFiles, APP_FILES);
  assert.deepEqual(manifest.fixtureFiles, FIXTURE_FILES);
  assert.deepEqual(manifest.regimeFiles, REGIME_FILES);
  assert.deepEqual(manifest.regimeV2Files, REGIME_V2_FILES);
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

  for (const file of FIXTURE_FILES) {
    assert.ok(fs.existsSync(path.join(DIST, "fixtures", "dependency", file)));
  }

  assert.ok(fs.existsSync(path.join(DIST, "index.html")));
  assert.ok(fs.existsSync(path.join(DIST, "build-manifest.json")));
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
