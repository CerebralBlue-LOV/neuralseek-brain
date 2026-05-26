# Marketing Alignment Pack — Index

Drop-in pitch and positioning content built from **third-party data** (primarily a top-tier Silicon Valley venture firm's May 2026 "A Primer on AI Agents" deck). These are the pieces that let NeuralSeek make architectural and economic claims **without sounding like a vendor** — every assertion has external validation behind it.

Use these whenever a prompt asks for: a pitch deck section, a board-grade narrative, third-party-validated positioning, CISO arguments with named-incident evidence, a "why now" segment, or a side-by-side competitive table.

## The three pieces (this folder)

| File | What it is | When to use |
|---|---|---|
| [F-vc-firm-agrees-onepager.md](F-vc-firm-agrees-onepager.md) | **Six structural claims** from the VC firm's deck, each in a side-by-side table with the matching NeuralSeek capability. Models commoditize → orchestration accrues / workflow is the control point / 5-layer stack / governance is architecture / Anthropic-Amazon-Microsoft failures / price-per-task. | Investor decks, partnership conversations, third-party-validation segments. Each row is a clean one-slide build. |
| [G-why-now-segment.md](G-why-now-segment.md) | **Drop-in 3-slide segment** for any NeuralSeek deck. Slide 1: every paradigm looked like a feature. Slide 2: 1000× inference-cost drop. Slide 3: agent proliferation 139%/524% CAGR. Optional NeuralSeek closer slide. | Any pitch deck that needs urgency without vendor-pitch tone. Standalone executive briefing. Conference opener. Website hero anchor. |
| [H-ciso-talk-track-refresh.md](H-ciso-talk-track-refresh.md) | **3 new CTO/CISO selling angles** (Angles 4, 5, 6) that extend the original three in `Knowledge from Calls/13-cto-ciso-selling-angles.md`. Each angle: buyer mental state + full talk track + key hooks + why-it-lands + deployment moments. Ends with a 6-angle playbook table. | Every CISO discovery call. Security-questionnaire responses. CISO-targeted LinkedIn posts timed to industry incidents. |

## Pack relationships — where the rest of the pack lives

This folder holds **F–H** (positioning + CISO content). The other five files in the Marketing Alignment Pack are **ROI / TCO / competitive math**, which live in [`../ROI_Analysis/`](../ROI_Analysis/) because they're useful well beyond pitch contexts:

- A — `../ROI_Analysis/A-days-to-mvp.md` (time-to-production by customer)
- B — `../ROI_Analysis/B-itochu-analyst-roi.md` (Itochu analyst $-saved math)
- C — `../ROI_Analysis/C-itochu-bakeoff-vs-stack.md` (Tony Chang's "$2M stack" bake-off)
- D — `../ROI_Analysis/D-build-vs-buy-tco.md` (3-year TCO across 3 paths)
- E — `../ROI_Analysis/E-guardrails-in-action.md` (illustrative guardrail volumes)

For the ROI / TCO routing, start at [`../ROI_Analysis/00-INDEX.md`](../ROI_Analysis/00-INDEX.md).

## Tight coupling with Talk Tracks

F, G, H are the **expanded, deck-ready versions** of several Talk Tracks. When you use them, you may also want the punchier soundbites:

| This file | Pairs with Talk Tracks |
|---|---|
| F (VC firm agrees one-pager) | [TT-07](../Talk%20Tracks/TT-07-as-models-commoditize.md), [TT-08](../Talk%20Tracks/TT-08-whoever-owns-the-workflow.md), [TT-09](../Talk%20Tracks/TT-09-the-5-layer-agent-stack.md), [TT-15](../Talk%20Tracks/TT-15-governance-is-architecture.md), [TT-16](../Talk%20Tracks/TT-16-even-anthropic-cant-get-governance-right.md), [TT-17](../Talk%20Tracks/TT-17-price-per-completed-task.md) |
| G (Why-now 3-slide segment) | [TT-03](../Talk%20Tracks/TT-03-every-major-computing-paradigm.md), [TT-04](../Talk%20Tracks/TT-04-why-now-inference-costs-fell.md), [TT-05](../Talk%20Tracks/TT-05-agents-proliferate-per-workflow.md) |
| H (CISO talk-track refresh) | [TT-06](../Talk%20Tracks/TT-06-always-on-attack-surface.md), [TT-15](../Talk%20Tracks/TT-15-governance-is-architecture.md), [TT-16](../Talk%20Tracks/TT-16-even-anthropic-cant-get-governance-right.md). Also extends [`../Knowledge from Calls/13-cto-ciso-selling-angles.md`](../Knowledge%20from%20Calls/13-cto-ciso-selling-angles.md). |

## When to assemble which combination

| Goal | Use this combination |
|---|---|
| **Investor pitch — third-party-validated** | G (why-now segment) → F (six-claim side-by-side) → close with TT-18 |
| **CISO meeting** | H (Angle 4 → Angle 5 → Angle 6, weaving in 1–3 from original 13-cto-ciso-selling-angles.md) |
| **Board briefing** | G (10-min executive briefing) + selected rows from F (governance + price-per-task) |
| **Conference keynote** | G slide 1 → G slide 2 → G slide 3 → F row 4 (governance is architecture) → NeuralSeek pitch |
| **Cold CISO outreach (LinkedIn)** | H Angle 6 opener (the Amazon/Anthropic/Microsoft three-incident open) |
| **RFP / security-questionnaire response** | H Angle 5's four-property procurement list, lifted verbatim |
| **Channel / VAR / partner conversation** | F rows 1, 3, 6 + ROI_Analysis/C (the bake-off math) |

## Source attribution

All third-party citations point back to a top-tier Silicon Valley venture firm's **"A Primer on AI Agents: The 5 Layers of AI Agents"** (May 2026), with page references inline. Cross-reference with the brain's existing positioning files for the NeuralSeek-specific delivery details.
