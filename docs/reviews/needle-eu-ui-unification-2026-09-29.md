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

## Real 200% browser zoom — verified

The missing zoom gate was rerun independently on Jeroen-PC against a **fresh archive of exact PR head `c7f2c287586b07787770f91ff5befce27e53b2d9`**. The archive was rebuilt with `node scripts/vercel-build.js`; all **107/107 tests passed** before the browser check.

A clean, visible **Google Chrome 146.0.7680.165** profile was launched at a physical window width of 1280 px with Chrome remote debugging enabled. Browser metrics were recorded before and after using Chrome's own keyboard zoom commands:

1. at 100%, all four routes reported `devicePixelRatio = 1`, `visualViewport.scale = 1`, and an inner CSS viewport of about 1264 px;
2. Chrome was focused, reset with **Ctrl+0**, then zoomed using Chrome's actual **Ctrl + +** command until the browser reported `devicePixelRatio = 2`;
3. at 200%, all four routes reported `devicePixelRatio = 2`, `visualViewport.scale = 1`, and an inner CSS viewport of about 632 px.

That DPR/viewport change distinguishes this check from CSS root-font enlargement, device-scale emulation or pinch zoom.

| Route | 200% client width | 200% document width | Page overflow |
| --- | ---: | ---: | --- |
| `/` | 624 | 624 | no |
| `/medical-devices/` | 624 | 624 | no |
| `/regime-v2/` | 624 | 624 | no |
| `/mvp/candidate-b/` | 624 | 624 | no |

No page-level horizontal overflow was observed at true 200% browser zoom.

The legal sources and external destinations were not independently revalidated in this visual pass. The UI/coherence acceptance evidence is now complete for sponsor review; customer pitch and external recruitment remain paused until the sponsor decides the next gate.
