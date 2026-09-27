"use strict";

function branchSet(value) {
  return new Set(String(value || "").trim().split(/\s+/).filter(Boolean));
}

function applyFocus(view, map, buttons, status) {
  map.dataset.view = view;

  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(button.dataset.focus === view));
  }

  for (const object of map.querySelectorAll("[data-macro-object]")) {
    const branches = branchSet(object.dataset.branches);
    const inFocus = view === "all" || branches.has(view);
    object.classList.toggle("is-context", !inFocus);
  }

  if (view === "mdr") {
    status.textContent = "MDR focused. IVDR-only material stays visible as sibling context.";
  } else if (view === "ivdr") {
    status.textContent = "IVDR focused. MDR-only material stays visible as sibling context.";
  } else {
    status.textContent = "Whole regime shown. MDR and IVDR branches are both in focus.";
  }
}

function boot() {
  const map = document.querySelector("#regime-map");
  const status = document.querySelector("#focus-status");
  const buttons = Array.from(document.querySelectorAll("[data-focus]"));

  if (!map || !status || !buttons.length) return;

  for (const button of buttons) {
    button.addEventListener("click", () => {
      applyFocus(button.dataset.focus, map, buttons, status);
    });
  }
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {branchSet, applyFocus};
}

if (typeof document !== "undefined") {
  boot();
}
