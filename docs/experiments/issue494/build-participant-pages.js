"use strict";

const fs = require("node:fs");
const path = require("node:path");

const DIR = __dirname;
const OUTPUTS = Object.freeze({
  a: "participant-a.html",
  b: "participant-b.html"
});

function participantCopy(sourceFile) {
  let html = fs.readFileSync(path.join(DIR, sourceFile), "utf8");

  html = html.replace(
    /<nav aria-label="Comparison pages">[\s\S]*?<\/nav>/,
    '<p class="small" aria-label="Study context">Needle #494 reading study</p>'
  );

  html = html.replace(
    /<a href="https:\/\/github\.com\/kaastumor\/morrow-needle\/issues\/494">#494<\/a>/g,
    "#494 research record"
  );

  const forbidden = [
    'href="specimen.html"',
    'href="baseline.html"',
    'href="evidence.md"',
    'href="protocol.md"',
    "github.com/kaastumor/morrow-needle/issues/494"
  ];

  for (const marker of forbidden) {
    if (html.includes(marker)) {
      throw new Error(`participant page leaks research/comparison route: ${marker}`);
    }
  }

  return html;
}

function buildParticipantPages() {
  const pages = {
    a: participantCopy("specimen.html"),
    b: participantCopy("baseline.html")
  };

  fs.writeFileSync(path.join(DIR, OUTPUTS.a), pages.a, "utf8");
  fs.writeFileSync(path.join(DIR, OUTPUTS.b), pages.b, "utf8");

  return {pages, outputs: OUTPUTS};
}

if (require.main === module) {
  buildParticipantPages();
  process.stdout.write("Built #494 participant-isolated reading pages.\n");
}

module.exports = {OUTPUTS, participantCopy, buildParticipantPages};
