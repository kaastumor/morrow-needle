"use strict";

const fs = require("node:fs");
const path = require("node:path");

const ROOT = path.resolve(__dirname, "..", "..");
const DIST = path.join(ROOT, "dist");
const {participantCopy} = require("../../docs/experiments/issue494/build-participant-pages.js");
const {ACTS} = require("../medical-act-detail/acts.js");
const {renderActPage} = require("../medical-act-detail/render.js");

const APP_FILES = Object.freeze([
  "index.html",
  "styles.css",
  "app.js"
]);

const REGIME_FILES = Object.freeze([
  "index.html",
  "styles.css",
  "app.js"
]);

const REGIME_V2_FILES = Object.freeze([
  "index.html",
  "styles.css",
  "app.js"
]);

const MEDICAL_SUMMARY_FILES = Object.freeze([
  "index.html",
  "styles.css",
  "app.js"
]);

const MEDICAL_ACT_ROUTES = Object.freeze(["mdr", "ivdr"]);

const CUSTOMS_CONTRAST_FILES = Object.freeze([
  "index.html",
  "styles.css"
]);

const PRODUCT_HOME_FILES = Object.freeze(["index.html", "search.css"]);

const PRODUCT_SEARCH_FILES = Object.freeze([
  "app.js",
  "evidence-view.js",
  "index.json",
  "language.js",
  "medical-engine.js",
  "resources.json",
  "search-panel.js",
  "search.js",
  "word-forms.js"
]);

const PILOT_FILES = Object.freeze(["index.html", "style.css"]);

const FIXTURE_FILES = Object.freeze([
  "gar-en497-authoritative-dynamic-set-v0.1.json",
  "machinery-en50434-restriction-v0.1.json",
  "toy-safety-authoritative-dynamic-set-v0.1.json",
  "lvd-en60335-2-14-formal-nonpublication-v0.1.json",
  "lvd-en60335-2-60-scheduled-withdrawal-v0.1.json"
]);

function copyFile(source, destination) {
  fs.mkdirSync(path.dirname(destination), {recursive: true});
  fs.copyFileSync(source, destination);
}

function buildStaticDemo() {
  fs.rmSync(DIST, {recursive: true, force: true});

  const appOut = path.join(DIST, "mvp", "candidate-b");
  const regimeOut = path.join(DIST, "regime");
  const regimeV2Out = path.join(DIST, "regime-v2");
  const medicalSummaryOut = path.join(DIST, "medical-devices");
  const customsContrastOut = path.join(DIST, "customs-low-value-imports");
  const productHomeOut = DIST;
  const medicalActStyle = path.join(DIST, "medical-devices", "act-detail.css");
  const fixturesOut = path.join(DIST, "fixtures", "dependency");
  const pilotAOut = path.join(DIST, "research", "issue494", "a");
  const pilotBOut = path.join(DIST, "research", "issue494", "b");

  for (const file of APP_FILES) {
    copyFile(path.join(__dirname, file), path.join(appOut, file));
  }

  for (const file of REGIME_FILES) {
    copyFile(
      path.join(ROOT, "mvp", "regime-constellation", file),
      path.join(regimeOut, file)
    );
  }

  for (const file of REGIME_V2_FILES) {
    copyFile(
      path.join(ROOT, "mvp", "regime-density-v0.2", file),
      path.join(regimeV2Out, file)
    );
  }

  for (const file of MEDICAL_SUMMARY_FILES) {
    copyFile(
      path.join(ROOT, "mvp", "medical-devices-summary", file),
      path.join(medicalSummaryOut, file)
    );
  }

  for (const file of CUSTOMS_CONTRAST_FILES) {
    copyFile(
      path.join(ROOT, "mvp", "customs-low-value-imports", file),
      path.join(customsContrastOut, file)
    );
  }

  copyFile(path.join(ROOT, "mvp", "medical-act-detail", "styles.css"), medicalActStyle);
  for (const route of MEDICAL_ACT_ROUTES) {
    const act = ACTS[route];
    const routeDir = path.join(DIST, "medical-devices", route);
    fs.mkdirSync(routeDir, {recursive: true});
    fs.writeFileSync(path.join(routeDir, "index.html"), renderActPage(act), "utf8");
  }

  for (const file of PRODUCT_HOME_FILES) {
    copyFile(path.join(ROOT, "mvp", "product-home", file), path.join(productHomeOut, file));
  }
  for (const file of PRODUCT_SEARCH_FILES) {
    copyFile(
      path.join(ROOT, "mvp", "product-home", "search", file),
      path.join(productHomeOut, "search", file)
    );
  }
  copyFile(path.join(ROOT, "mvp", "product-shell.css"), path.join(DIST, "product-shell.css"));

  fs.mkdirSync(pilotAOut, {recursive: true});
  fs.mkdirSync(pilotBOut, {recursive: true});
  fs.writeFileSync(path.join(pilotAOut, "index.html"), participantCopy("specimen.html"), "utf8");
  fs.writeFileSync(path.join(pilotBOut, "index.html"), participantCopy("baseline.html"), "utf8");
  copyFile(path.join(ROOT, "docs", "experiments", "issue494", "style.css"), path.join(pilotAOut, "style.css"));
  copyFile(path.join(ROOT, "docs", "experiments", "issue494", "style.css"), path.join(pilotBOut, "style.css"));

  for (const file of FIXTURE_FILES) {
    copyFile(
      path.join(ROOT, "fixtures", "dependency", file),
      path.join(fixturesOut, file)
    );
  }

  const manifest = {
    artifact: "candidate-b-static-demo",
    generatedFrom: "canonical repository files",
    appFiles: APP_FILES,
    fixtureFiles: FIXTURE_FILES,
    regimeFiles: REGIME_FILES,
    regimeV2Files: REGIME_V2_FILES,
    medicalSummaryFiles: MEDICAL_SUMMARY_FILES,
    medicalActRoutes: MEDICAL_ACT_ROUTES,
    medicalActStyle: "medical-devices/act-detail.css",
    customsContrastFiles: CUSTOMS_CONTRAST_FILES,
    productHomeFiles: PRODUCT_HOME_FILES,
    productSearchFiles: PRODUCT_SEARCH_FILES,
    productShellFile: "product-shell.css",
    pilotFiles: PILOT_FILES,
    pilotRoutes: ["/research/issue494/a/", "/research/issue494/b/"],
    externalValueProven: false,
    liveMonitoring: false
  };

  fs.writeFileSync(
    path.join(DIST, "build-manifest.json"),
    JSON.stringify(manifest, null, 2) + "\n",
    "utf8"
  );

  return manifest;
}

if (require.main === module) {
  const manifest = buildStaticDemo();
  process.stdout.write(
    `Built bounded Needle EU product routes with ${manifest.fixtureFiles.length} canonical fixtures.\n`
  );
}

module.exports = {APP_FILES, REGIME_FILES, REGIME_V2_FILES, MEDICAL_SUMMARY_FILES, MEDICAL_ACT_ROUTES, CUSTOMS_CONTRAST_FILES, PRODUCT_HOME_FILES, PRODUCT_SEARCH_FILES, PILOT_FILES, FIXTURE_FILES, buildStaticDemo};
