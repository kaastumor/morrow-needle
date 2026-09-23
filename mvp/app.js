"use strict";

const CORPUS_URL = "../corpus/index-v0.1.json";

async function loadCorpus() {
  const status = document.querySelector("#corpus-status");
  const root = document.querySelector("#corpus-root");

  try {
    const response = await fetch(CORPUS_URL, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const corpus = await response.json();
    const count = Array.isArray(corpus.cases) ? corpus.cases.length : null;
    status.textContent = count === null
      ? "Canonical corpus loaded. Structural validation follows in MVP-02."
      : `Canonical corpus loaded: ${count} cases.`;
    root.dataset.loaded = "true";
    root.hidden = false;
  } catch (error) {
    status.setAttribute("role", "alert");
    status.textContent = `Could not load the canonical corpus (${error.message}). Start the documented local server and try again.`;
    root.hidden = true;
  }
}

loadCorpus();
