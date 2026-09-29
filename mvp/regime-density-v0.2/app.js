"use strict";

const VIEW_LABELS = Object.freeze({
  overview: "Overview",
  explore: "Explore",
  changes: "Change review",
  expert: "Research diagnostics"
});

function setPressed(buttons, key, datasetName) {
  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(button.dataset[datasetName] === key));
  }
}

function showView(view, buttons, panels, updateHash = true) {
  const key = VIEW_LABELS[view] ? view : "overview";
  setPressed(buttons, key, "viewButton");

  for (const panel of panels) {
    panel.hidden = panel.dataset.viewPanel !== key;
  }

  if (updateHash && typeof history !== "undefined") {
    history.pushState(null, "", "#" + key);
  }

  const active = panels.find(panel => panel.dataset.viewPanel === key);
  const heading = active && active.querySelector("h2");
  if (heading && updateHash) heading.focus();

  return key;
}

function applyBranch(branch, buttons, rows, status, family) {
  setPressed(buttons, branch, "branch");
  for (const row of rows) {
    const branches = new Set(String(row.dataset.rowBranches || "").split(/\s+/).filter(Boolean));
    const inFocus = branch === "all" || branches.has(branch);
    row.classList.toggle("is-context", !inFocus);
  }

  const branchLabel = branch === "all" ? "the whole regime" : branch.toUpperCase();
  status.textContent = "Showing representative " + family + " material for " + branchLabel + ".";
}

function showFamily(family, buttons, panels, status, branch) {
  setPressed(buttons, family, "family");
  for (const panel of panels) {
    panel.hidden = panel.dataset.familyPanel !== family;
  }
  const branchLabel = branch === "all" ? "the whole regime" : branch.toUpperCase();
  status.textContent = "Showing representative " + family + " material for " + branchLabel + ".";
  return family;
}

function showChange(control, buttons, cases, status) {
  setPressed(buttons, control, "changeControl");
  for (const item of cases) {
    item.hidden = item.dataset.changeCase !== control;
  }

  const labels = {
    "reg-2024-1860": "Regulation (EU) 2024/1860",
    "dec-2025-1324": "Decision (EU) 2025/1324",
    "reg-2023-1194": "Regulation (EU) 2023/1194"
  };
  status.textContent = "Showing review queue for " + labels[control] + ".";
}

function boot() {
  const viewButtons = Array.from(document.querySelectorAll("[data-view-button]"));
  const viewPanels = Array.from(document.querySelectorAll("[data-view-panel]"));

  if (viewButtons.length && viewPanels.length) {
    for (const button of viewButtons) {
      button.addEventListener("click", () => showView(button.dataset.viewButton, viewButtons, viewPanels, true));
    }

    for (const button of document.querySelectorAll("[data-open-view]")) {
      button.addEventListener("click", () => showView(button.dataset.openView, viewButtons, viewPanels, true));
    }

    const fromHash = location.hash.replace("#", "");
    showView(VIEW_LABELS[fromHash] ? fromHash : "overview", viewButtons, viewPanels, false);

    window.addEventListener("hashchange", () => {
      const key = location.hash.replace("#", "");
      showView(VIEW_LABELS[key] ? key : "overview", viewButtons, viewPanels, false);
    });
  }

  const branchButtons = Array.from(document.querySelectorAll("[data-branch]"));
  const familyButtons = Array.from(document.querySelectorAll("[data-family]"));
  const familyPanels = Array.from(document.querySelectorAll("[data-family-panel]"));
  const allRows = Array.from(document.querySelectorAll("[data-row-branches]"));
  const exploreStatus = document.querySelector("#explore-status");
  let branch = "all";
  let family = "implementing";

  if (branchButtons.length && familyButtons.length && familyPanels.length && exploreStatus) {
    for (const button of branchButtons) {
      button.addEventListener("click", () => {
        branch = button.dataset.branch;
        applyBranch(branch, branchButtons, allRows, exploreStatus, family);
      });
    }

    for (const button of familyButtons) {
      button.addEventListener("click", () => {
        family = showFamily(button.dataset.family, familyButtons, familyPanels, exploreStatus, branch);
        applyBranch(branch, branchButtons, allRows, exploreStatus, family);
      });
    }
  }

  const changeButtons = Array.from(document.querySelectorAll("[data-change-control]"));
  const changeCases = Array.from(document.querySelectorAll("[data-change-case]"));
  const changeStatus = document.querySelector("#change-status");

  if (changeButtons.length && changeCases.length && changeStatus) {
    for (const button of changeButtons) {
      button.addEventListener("click", () => showChange(button.dataset.changeControl, changeButtons, changeCases, changeStatus));
    }
  }
}

if (typeof module !== "undefined" && module.exports) {
  module.exports = {VIEW_LABELS, setPressed, showView, applyBranch, showFamily, showChange};
}

if (typeof document !== "undefined") boot();
