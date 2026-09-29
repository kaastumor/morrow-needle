"use strict";

const {spawnSync} = require("node:child_process");

function run(command, args) {
  const result = spawnSync(command, args, {stdio: "inherit", shell: false});
  if (result.error) throw result.error;
  if (result.status !== 0) process.exit(result.status ?? 1);
}

run(process.execPath, [
  "--test",
  "mvp/candidate-b/app.test.js",
  "mvp/candidate-b/build-static-demo.test.js",
  "mvp/regime-constellation/app.test.js",
  "mvp/regime-density-v0.2/app.test.js",
  "mvp/medical-devices-summary/app.test.js",
  "docs/experiments/issue494/build-participant-pages.test.js"
]);

run(process.execPath, ["mvp/candidate-b/build-static-demo.js"]);
