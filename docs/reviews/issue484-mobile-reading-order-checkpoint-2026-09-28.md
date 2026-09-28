# #484 — Mobile first-read checkpoint

Date: 2026-09-28  
Status: **partial internal UI/UX implementation checkpoint**

This record concerns the public explainer's presentation. It does not change or add evidence to Needle's historical scientific claims or frozen corpus.

## Observed gap

The existing `auto/484-summary-ui-ux` branch placed its seven-link contents rail before the purpose summary in document order. At 375 CSS px, the summary began 879 px from the top; at 320 CSS px, it began 947 px from the top. The contents list occupied the first mobile screen before the explanation. The accepted #484 contract calls for purpose and relevance to lead the first reading path.

The repaired `main` page was separately rendered as a comparator. Its summary began at 657 px at 375 CSS px and 711 px at 320 CSS px. These are local rendered layout measurements, not user-comprehension or task-time evidence.

## Change

Move the unchanged “What these rules do” section before the contents navigation in the HTML. CSS grid keeps the contents rail beside the summary and article at desktop width; at widths up to 64 rem, the order becomes summary → contents → remaining article. The navigation remains a single semantic `nav` with the same seven native anchors.

## Verification

- Local Chrome rendering at 1440, 375 and 320 CSS px: summary begins at 359, 449 and 516 px respectively. At desktop width the contents rail remains beside the summary.
- At 375 and 320 CSS px, the summary is visible in the first viewport, the contents follows it, and document width equals viewport width.
- “Dates and current operation” navigation reaches `#dates` at all three widths; all local hash targets resolve. The desktop contents rail remains sticky while navigating.
- Focused static tests: 23 passed, including a new reading-order and responsive-grid regression.
- The moved summary text and official-source link are unchanged. All 35 anchor destinations match the prior branch head, and the branch's visible legal qualifications and source sections remain in normal flow.

The rendered checks use local files and a headless browser. They do not establish behavior in an authenticated or deployed preview, accessibility with assistive technology, or a user-value gain. This checkpoint does not finish #484's full internal comparison or authorize outreach, publication or merge.
