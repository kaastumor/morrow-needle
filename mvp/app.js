"use strict";

const CORPUS_URL = "../corpus/index-v0.1.json";
const CASE_ID = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const ROLES = new Set(["DERIVATION", "EVALUATION"]);
const EVALUATION_MODES = new Set(["SURFACED_TRAP_ADJUDICATION", "LATENT_TRAP_DETECTION"]);

function requireString(value, label) {
  if (typeof value !== "string" || value.trim() === "") throw new Error(`${label} must be a non-empty string`);
  return value;
}

function projectCorpus(corpus) {
  if (!corpus || typeof corpus !== "object" || Array.isArray(corpus)) throw new Error("corpus root must be an object");
  if (!Array.isArray(corpus.cases)) throw new Error("corpus.cases must be an array");
  if (!corpus.trap_classes || typeof corpus.trap_classes !== "object" || Array.isArray(corpus.trap_classes)) throw new Error("corpus.trap_classes must be an object");

  const knownTraps = new Set(Object.keys(corpus.trap_classes));
  const seenIds = new Set();
  const cases = corpus.cases.map((entry, index) => {
    const at = `cases[${index}]`;
    const id = requireString(entry?.id, `${at}.id`);
    if (!CASE_ID.test(id)) throw new Error(`${at}.id has unsupported format: ${id}`);
    if (seenIds.has(id)) throw new Error(`duplicate case id: ${id}`);
    seenIds.add(id);

    const title = requireString(entry.title, `${at}.title`);
    const domain = requireString(entry.domain, `${at}.domain`);
    const jurisdiction = requireString(entry.jurisdiction, `${at}.jurisdiction`);
    const decisiveTrap = requireString(entry.decisive_trap, `${at}.decisive_trap`);
    if (!Array.isArray(entry.trap_classes) || entry.trap_classes.length === 0) throw new Error(`${at}.trap_classes must be a non-empty array`);
    const trapClasses = entry.trap_classes.map((trap) => {
      requireString(trap, `${at}.trap_classes[]`);
      if (!knownTraps.has(trap)) throw new Error(`${at} references unknown trap class: ${trap}`);
      return trap;
    });

    const role = entry.provenance?.role;
    if (!ROLES.has(role)) throw new Error(`${at}.provenance.role is unsupported: ${String(role)}`);

    let evaluationMode = null;
    if (entry.evaluation_mode !== undefined) {
      if (!EVALUATION_MODES.has(entry.evaluation_mode)) throw new Error(`${at}.evaluation_mode is unsupported: ${String(entry.evaluation_mode)}`);
      evaluationMode = entry.evaluation_mode;
    }
    if (entry.evaluation_result !== undefined && role !== "EVALUATION") throw new Error(`${at}.evaluation_result is only supported for EVALUATION cases`);
    if (evaluationMode !== null && role !== "EVALUATION") throw new Error(`${at}.evaluation_mode is only supported for EVALUATION cases`);

    return Object.freeze({ id, title, domain, jurisdiction, decisiveTrap, trapClasses: Object.freeze([...trapClasses]), role, evaluationMode });
  });

  const roleCounts = { DERIVATION: 0, EVALUATION: 0 };
  const modeCounts = { SURFACED_TRAP_ADJUDICATION: 0, LATENT_TRAP_DETECTION: 0, UNSPECIFIED: 0 };
  for (const entry of cases) {
    roleCounts[entry.role] += 1;
    if (entry.role === "EVALUATION") modeCounts[entry.evaluationMode ?? "UNSPECIFIED"] += 1;
  }
  return Object.freeze({ cases: Object.freeze(cases), summary: Object.freeze({ totalCases: cases.length, trapClasses: knownTraps.size, roleCounts: Object.freeze(roleCounts), modeCounts: Object.freeze(modeCounts) }) });
}

function renderSummary(summary, root) {
  const values = { "summary-total": summary.totalCases, "summary-traps": summary.trapClasses, "summary-derivation": summary.roleCounts.DERIVATION, "summary-evaluation": summary.roleCounts.EVALUATION, "summary-surfaced": summary.modeCounts.SURFACED_TRAP_ADJUDICATION, "summary-latent": summary.modeCounts.LATENT_TRAP_DETECTION, "summary-unspecified": summary.modeCounts.UNSPECIFIED };
  for (const [id, value] of Object.entries(values)) root.querySelector(`#${id}`).textContent = String(value);
}

async function loadCorpus() {
  const status = document.querySelector("#corpus-status");
  const root = document.querySelector("#corpus-root");
  try {
    const response = await fetch(CORPUS_URL, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const projection = projectCorpus(await response.json());
    renderSummary(projection.summary, root);
    status.textContent = `Canonical corpus validated: ${projection.summary.totalCases} cases.`;
    root.dataset.loaded = "true";
    root.hidden = false;
  } catch (error) {
    status.setAttribute("role", "alert");
    status.textContent = `Corpus unavailable or invalid (${error.message}). Nothing was rendered.`;
    root.hidden = true;
  }
}

if (typeof module !== "undefined" && module.exports) module.exports = { projectCorpus };
if (typeof document !== "undefined") loadCorpus();
