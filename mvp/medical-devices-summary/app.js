"use strict";

const root = document.documentElement;
const buttons = Array.from(document.querySelectorAll("[data-view]"));

function setDetailLevel(level) {
  const next = level === "expert" ? "expert" : "public";
  root.dataset.detail = next;
  for (const button of buttons) {
    button.setAttribute("aria-pressed", String(button.dataset.view === next));
  }
}

for (const button of buttons) {
  button.addEventListener("click", () => setDetailLevel(button.dataset.view));
}

setDetailLevel(root.dataset.detail);
