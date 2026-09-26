"use strict";

const CASES = Object.freeze([
  Object.freeze({
    id: "gar-en497",
    label: "GAR · EN 497:2022 · formal non-publication",
    standard: "EN 497:2022",
    supportedFrom: "2026-07-23",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/gar-en497-authoritative-dynamic-set-v0.1.json"
  }),
  Object.freeze({
    id: "machinery-en50434",
    label: "Machinery · EN 50434:2014 · restricted citation",
    standard: "EN 50434:2014",
    supportedFrom: "2026-01-12",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/machinery-en50434-restriction-v0.1.json"
  }),
  Object.freeze({
    id: "toy-en71",
    label: "Toy Safety · EN 71-1:2014+A1:2018 · restricted citation",
    standard: "EN 71-1:2014+A1:2018",
    supportedFrom: "2025-09-09",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/toy-safety-authoritative-dynamic-set-v0.1.json"
  }),
  Object.freeze({
    id: "lvd-en60335-2-14",
    label: "LVD · EN 60335-2-14:2006 · formal non-publication",
    standard: "EN 60335-2-14:2006",
    supportedFrom: "2025-07-17",
    supportedThrough: "2026-09-26",
    fixture: "../../fixtures/dependency/lvd-en60335-2-14-formal-nonpublication-v0.1.json"
  }),
  Object.freeze({
    id: "lvd-en60335-2-60",
    label: "LVD · EN 60335-2-60:2003 · future withdrawal",
    standard: "EN 60335-2-60:2003",
    supportedFrom: "2025-07-18",
    supportedThrough: "2027-01-18",
    fixture: "../../fixtures/dependency/lvd-en60335-2-60-scheduled-withdrawal-v0.1.json"
  })
]);

function parseDate(value) {
  const date = new Date(value + "T00:00:00Z");
  if (Number.isNaN(date.valueOf())) throw new Error("invalid date");
  return date;
}

function assertSupportedDate(caseMeta, asOfValue) {
  if (asOfValue < caseMeta.supportedFrom || asOfValue > caseMeta.supportedThrough) {
    throw new Error(
      `date outside frozen evidence window ${caseMeta.supportedFrom} to ${caseMeta.supportedThrough}`
    );
  }
}

function transitionMatches(transition, standard) {
  return transition.member.identifiers.some(
    item => item.scheme === "HARMONISED_STANDARD" && item.value === standard
  );
}

function projectStatus(record, standard, asOfValue) {
  const asOf = parseDate(asOfValue);
  const transitions = record.transitions
    .filter(item => transitionMatches(item, standard))
    .slice()
    .sort((a, b) => a.effective_from.localeCompare(b.effective_from));

  if (!transitions.length) throw new Error("standard not found in canonical record");

  const past = transitions.filter(item => parseDate(item.effective_from) <= asOf);
  const future = transitions.filter(item => parseDate(item.effective_from) > asOf);
  const latest = past.at(-1) || null;
  const next = future[0] || null;
  const state = latest ? latest.after : transitions[0].before;

  let ojState;
  let consequence;
  if (state.membership === "NOT_INCLUDED") {
    ojState = "NOT_CITED";
    consequence = "NOT_AVAILABLE_VIA_THIS_OJ_REFERENCE";
  } else if (state.status === "RESTRICTED") {
    ojState = "CITED_WITH_RESTRICTION";
    consequence = "RESTRICTED_TO_STATED_SCOPE";
  } else {
    ojState = "CITED";
    consequence = "AVAILABLE_WITHIN_COVERED_SCOPE";
  }

  return Object.freeze({asOf: asOfValue, state, ojState, consequence, latest, next});
}

function sourceHref(source) {
  if (!source || typeof source.identifier !== "string") return null;
  if (source.source_type === "EUR_LEX" || source.source_type === "OFFICIAL_JOURNAL") {
    return "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=" + encodeURIComponent(source.identifier);
  }
  return null;
}

function collectEvidence(record, projection) {
  const refs = [];
  for (const source of record.legal_basis_refs || []) refs.push(source);
  if (projection.latest) refs.push(...projection.latest.source_refs);
  if (projection.next) refs.push(...projection.next.source_refs);

  const seen = new Set();
  return refs.filter(source => {
    const key = [source.identifier, source.locator].join("|");
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
}

function eventBlock(title, event) {
  if (!event) return `<div class="event"><strong>${title}:</strong> none in this record for the selected date.</div>`;
  return `<div class="event">
    <strong>${title}:</strong> ${escapeHtml(event.transition_id)}<br>
    <strong>Effective:</strong> ${escapeHtml(event.effective_from)}<br>
    <strong>Scope:</strong> ${escapeHtml(event.scope.statement)}
  </div>`;
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderCard(record, caseMeta, projection) {
  const dependency = record.dependencies[0];
  const evidence = collectEvidence(record, projection);
  const evidenceHtml = evidence.map(source => {
    const href = sourceHref(source);
    const label = `${source.identifier} — ${source.locator}`;
    return href
      ? `<li><a href="${escapeHtml(href)}" target="_blank" rel="noreferrer">${escapeHtml(label)}</a></li>`
      : `<li>${escapeHtml(label)}</li>`;
  }).join("");

  const guardrails = record.forbidden_inferences
    .map(item => `<li>${escapeHtml(item)}</li>`)
    .join("");

  return `
    <h3>${escapeHtml(caseMeta.label)}</h3>
    <p><span class="status-badge">${escapeHtml(projection.ojState)}</span></p>
    <dl class="status-grid">
      <dt>As of</dt><dd>${escapeHtml(projection.asOf)}</dd>
      <dt>Regime</dt><dd>${escapeHtml(dependency.governing_rule.act_id)} · ${escapeHtml(dependency.governing_rule.provision)}</dd>
      <dt>Standard</dt><dd>${escapeHtml(caseMeta.standard)}</dd>
      <dt>Frozen evidence window</dt><dd>${escapeHtml(caseMeta.supportedFrom)} to ${escapeHtml(caseMeta.supportedThrough)}</dd>
      <dt>Presumption consequence</dt><dd>${escapeHtml(projection.consequence)}</dd>
    </dl>
    ${eventBlock("Latest owning event", projection.latest)}
    ${projection.next ? eventBlock("Next already-fixed event", projection.next) : ""}
    <h4>Official evidence</h4>
    <ul class="evidence-list">${evidenceHtml}</ul>
    <h4>What this does not mean</h4>
    <ul class="guardrail-list">${guardrails}</ul>
  `;
}

async function loadCase(caseMeta, asOfValue, fetcher = fetch) {
  assertSupportedDate(caseMeta, asOfValue);
  const response = await fetcher(caseMeta.fixture, {cache: "no-store"});
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const record = await response.json();
  return {record, projection: projectStatus(record, caseMeta.standard, asOfValue)};
}

function populateCaseSelect(select) {
  for (const entry of CASES) {
    const option = document.createElement("option");
    option.value = entry.id;
    option.textContent = entry.label;
    select.append(option);
  }
}

function applyDateBounds(caseMeta, dateInput) {
  dateInput.min = caseMeta.supportedFrom;
  dateInput.max = caseMeta.supportedThrough;
  if (dateInput.value < caseMeta.supportedFrom || dateInput.value > caseMeta.supportedThrough) {
    dateInput.value = "2026-09-26";
    if (dateInput.value < caseMeta.supportedFrom || dateInput.value > caseMeta.supportedThrough) {
      dateInput.value = caseMeta.supportedThrough;
    }
  }
}

async function updateView() {
  const select = document.querySelector("#case-select");
  const dateInput = document.querySelector("#as-of");
  const status = document.querySelector("#load-status");
  const card = document.querySelector("#status-card");
  const caseMeta = CASES.find(entry => entry.id === select.value);

  if (!caseMeta) return;

  applyDateBounds(caseMeta, dateInput);
  status.textContent = "Loading official-state fixture…";
  card.hidden = true;

  try {
    const {record, projection} = await loadCase(caseMeta, dateInput.value);
    card.innerHTML = renderCard(record, caseMeta, projection);
    card.hidden = false;
    status.textContent = "Status derived from the frozen official-evidence record.";
  } catch (error) {
    status.textContent = `Status unavailable: ${error.message}`;
  }
}

function boot() {
  const select = document.querySelector("#case-select");
  const dateInput = document.querySelector("#as-of");
  populateCaseSelect(select);
  select.addEventListener("change", updateView);
  dateInput.addEventListener("change", updateView);
  updateView();
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {CASES, parseDate, assertSupportedDate, projectStatus, sourceHref, collectEvidence};
}
if (typeof document !== "undefined") {
  boot();
}
