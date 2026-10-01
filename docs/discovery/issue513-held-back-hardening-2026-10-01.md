# #513 — WP7 held-back replay and hardening

Date: 1 October 2026  
Canonical pre-exposure revision: `007a4624bb7d50f2925188c7bdf70bff5f9befbb`

Status: **FIRST_EXPOSURE_COMPLETE — no critical product misrepresentation observed**

The four held-back cases were selected and their expectations frozen in #513 before any
product/test mutation.

## First-exposure results

| Case | Input | Raw product status | Internal navigation | First-exposure disposition |
| --- | --- | --- | --- | --- |
| R1 Machinery Regulation | `2023/1230` | `REFERENCE_NOT_IN_SNAPSHOT` | none | SAFE_LIMIT |
| R1 ordinary machinery | “Does the Machinery Regulation already apply and replace Directive 2006/42/EC?” | `REFERENCE_NOT_IN_SNAPSHOT` | none | SAFE_LIMIT |
| R2 Consumer Credit Directive | `2023/2225` | `REFERENCE_NOT_IN_SNAPSHOT` | none | SAFE_LIMIT |
| R2 ordinary consumer credit | “Do the new EU consumer credit rules apply from 20 November 2025?” | `OUTSIDE_MAINTAINED_COVERAGE` | none | SAFE_LIMIT |
| R3 Danish-only corrigendum | `2026/90645` | `REFERENCE_NOT_IN_SNAPSHOT` | none | SAFE_LIMIT |
| R3 ordinary language question | “Did the 3 August 2026 corrigendum change the English ecodesign rules for electronic displays?” | `OUTSIDE_MAINTAINED_COVERAGE` | none | SAFE_LIMIT |
| R4 withdrawn SEP proposal | `2023/0133` | `REFERENCE_NOT_IN_SNAPSHOT` | none | SAFE_LIMIT |
| R4 ordinary proposal-status question | “Is the EU standard essential patents proposal still ongoing?” | `NO_SUPPORTED_TERMS` | none | SAFE_LIMIT |

No held-back input produced a captured medical result, a represented MDR/IVDR shortcut or
an invented nearby act.

## Source-backed expected boundaries

### R1 — Machinery Regulation 2023/1230

Official EUR-Lex shows the current consolidated version dated 27 Jul 2026. Article 54 states
general application from 20 Jan 2027, while specified articles apply earlier. Article 51
repeals Directive 2006/42/EC with effect from 20 Jan 2027 and Article 52 preserves specified
transition effects.

**Boundary retained:** on the 1 Oct 2026 product revision, a statement that the Machinery
Regulation already generally applies or has already wholly replaced Directive 2006/42/EC
would be wrong.

### R2 — Directive 2023/2225 on consumer credit

EUR-Lex records transposition/adoption by 20 Nov 2025 and application of national measures
from 20 Nov 2026, alongside later reporting/review deadlines.

**Boundary retained:** transposition and application are distinct, and the EU directive does
not establish a particular Member State's implementation state.

### R3 — Regulation 2019/2021 / corrigendum 2026/90645

The underlying electronic-display ecodesign Regulation remains in force. Corrigendum
2026/90645 of 3 Aug 2026 is authentic in Danish only.

**Boundary retained:** a Danish-only correction is not a global English-version mutation,
and a corrigendum is not a standalone core act.

### R4 — COM(2023) 232 / procedure 2023/0133(COD)

EUR-Lex records the proposal, a European Parliament first-reading position in February 2024,
and Commission withdrawal on 6 Oct 2025.

**Boundary retained:** historical legislative steps do not make the proposal current or
operative after withdrawal.

## Interpretation

All four reserved cases passed the **search safety** boundary through abstention/outside
coverage. None provides positive evidence of broad legal-answer capability.

No WP7 product repair is justified from the first exposure. After this checkpoint the four
cases become ordinary regression inputs.

## Browser-hardening boundary

WP7 still separately owns pinned-revision keyboard/reflow/deep-link/200%-zoom evidence.
Source/unit/static checks may support those layers, but an actual 200% browser observation
must remain BLOCKED / NOT_TESTED if no authorized browser runtime is available.
