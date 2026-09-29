# Needle EU shared UI slice — browser evidence

Status: **review evidence; customer-readiness gate open**. Checked the locally generated `dist` from this branch on 29 September 2026. This is not deployed-serving evidence for the follow-up PR.

## Side-by-side route review

The four retained routes were opened in the Codex in-app Chromium browser at a 1280 px desktop viewport, then 390 px and 320 px viewports. Each rendered its heading, shared navigation and four-field evidence/limits panel. Visual review found the same editorial type scale, small-radius controls and restrained surface boundaries. Browser screenshots were observed during the check but could not be saved as PR attachments in this environment.

| Route | Desktop document/viewport width | 390 px document/viewport width | 320 px document/viewport width |
| --- | ---: | ---: | ---: |
| `/` | 1265/1280 | 375/390 | 305/320 |
| `/medical-devices/` | 1265/1280 | 375/390 | 305/320 |
| `/regime-v2/` | 1265/1280 | 375/390 | 305/320 |
| `/mvp/candidate-b/` | 1265/1280 | 375/390 | 305/320 |

Widths include the browser's vertical scrollbar. No page-level horizontal overflow was measured at these viewports.

## Navigation and keyboard

- Home → medical-device overview → relationship browser `#explore` → overview returned to `/medical-devices/`.
- Home → known-standard status → Home returned to `/`.
- Keyboard Tab reached the skip link with a visible solid focus outline. The medical Expert control changed its pressed state. The relationship Explore control activated with Return after focus, changed its pressed state and updated the fragment. The standards search form's Check status button received a visible focus outline.
- `/regime/` and #494 participant routes were not included in product navigation. The full build suite includes the participant isolation and source-destination parity checks.

## Remaining gate

Actual 200% browser zoom was **not verified**. The in-app browser did not change zoom when sent its zoom shortcuts. A separate headless Chrome/Edge attempt with a 2× browser device scale failed to start because the GPU process exited. Neither attempt is counted as a zoom pass. Run a real 200% browser zoom check on all four routes before treating this slice as customer ready.

The legal sources and external destinations were not independently revalidated in this visual pass. Customer pitch and external recruitment remain paused.
