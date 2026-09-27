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

  for (const child of map.querySelectorAll("[data-child-branches]")) {
    const branches = branchSet(child.dataset.childBranches);
    const inFocus = view === "all" || branches.has(view);
    child.classList.toggle("is-context", !inFocus);
  }

  if (view === "mdr") {
    status.textContent = "MDR focused. IVDR-only material stays visible as sibling context.";
  } else if (view === "ivdr") {
    status.textContent = "IVDR focused. MDR-only material stays visible as sibling context.";
  } else {
    status.textContent = "Whole regime shown. MDR and IVDR branches are both in focus.";
  }
}

function applyChangeControl(control, buttons, cases, status) {
  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(button.dataset.changeControl === control));
  }

  for (const item of cases) {
    const active = item.dataset.changeCase === control;
    item.hidden = !active;
    item.classList.toggle("is-active", active);
  }

  const labels = {
    "reg-2024-1860": "Regulation (EU) 2024/1860",
    "dec-2025-1324": "Decision (EU) 2025/1324",
    "reg-2023-1194": "Regulation (EU) 2023/1194"
  };
  status.textContent = "Showing review candidates for " + labels[control] + ".";
}

function boot() {
  const map = document.querySelector("#regime-map");
  const status = document.querySelector("#focus-status");
  const buttons = Array.from(document.querySelectorAll("[data-focus]"));

  if (map && status && buttons.length) {
    for (const button of buttons) {
      button.addEventListener("click", () => {
        applyFocus(button.dataset.focus, map, buttons, status);
      });
    }
  }

  const changeStatus = document.querySelector("#change-review-status");
  const changeButtons = Array.from(document.querySelectorAll("[data-change-control]"));
  const changeCases = Array.from(document.querySelectorAll("[data-change-case]"));

  if (changeStatus && changeButtons.length && changeCases.length) {
    for (const button of changeButtons) {
      button.addEventListener("click", () => {
        applyChangeControl(button.dataset.changeControl, changeButtons, changeCases, changeStatus);
      });
    }
  }
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {branchSet, applyFocus, applyChangeControl};
}

if (typeof document !== "undefined") {
  boot();
}
