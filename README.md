# NeuralSeek Central Brain

> [!IMPORTANT]
> **Before generating any HTML, slide, mockup, social card, dashboard, or image:** read [BRAND_RULES.md](BRAND_RULES.md). The canvas must be the **"rolling purple glow"** — a `#131316` (near-black) base with **five overlapping `#301E4C` (regal purple) radial-gradient ellipses at varied sizes, positions, and opacities** (plus `background-attachment: fixed`). **Apply the exact CSS in [BRAND_RULES.md RULE 1](BRAND_RULES.md) verbatim — do not improvise the gradient values.** **Never use** dots, grids, mesh, noise, particles, stripes, circuit-board patterns, or any tiled / repeated pattern.
>
> **Logo variant:** On any non-white background (the default, since the canvas is dark), use [`2026_images/NeuralSeek Logos/color_logo_white_text.svg`](2026_images/NeuralSeek%20Logos/color_logo_white_text.svg) — the colored N + white text variant. Only switch to the colored-text variant on genuinely white backgrounds. Full variant table in [BRAND_RULES.md](BRAND_RULES.md) RULE 2.

The canonical, read-only knowledge base for NeuralSeek — optimized for both humans browsing on GitHub and AI tools retrieving content programmatically.

**Single writer**: Lawrence (lawrence@neuralseek.com).
**Everyone else**: read-only.

## 🚨 If you're an AI agent — read [`BRAND_RULES.md`](./BRAND_RULES.md) first

**Applies to every output format** — Word docs (`.docx`), PowerPoint decks (`.pptx`), PDFs, HTML pages, slides, social cards, banners, images, emails. Not just web.

Before generating any NeuralSeek-branded deliverable, read [`BRAND_RULES.md`](./BRAND_RULES.md). It specifies:

- The mandatory canvas background (rolling purple radial gradient — **never dots, grids, mesh, noise, particles, or any pattern**)
- Logo, fonts (Open Sans + JetBrains Mono), and color discipline
- **Format-specific guidance** (RULE 7) for `.pptx`, `.docx`, PDF, HTML, images, emails — so an AI generating a PowerPoint via `python-pptx`, a Word doc via `python-docx`, or a PDF via `weasyprint` has actionable per-format instructions, not just CSS

The full brand book is at [`2026_images/neuralseek-brand-guidelines_2026.md`](./2026_images/neuralseek-brand-guidelines_2026.md), with the canvas rule pinned at the very top.

## What's in here

| Folder | What it holds |
|---|---|
| [`NeuralSeek Knowledge/Features/`](./NeuralSeek%20Knowledge/Features/) | Product reference docs — AI tuning, guardrails, governance, platform settings, LLM-level controls, RFP responses |
| [`NeuralSeek Knowledge/Client Stories/`](./NeuralSeek%20Knowledge/Client%20Stories/) | Deployment case studies — Itochu, Children's Health, Adobe, Verizon, Snap, NatWest, AFP Capital, BROU, Clip, AdMed, PennState, Great Day Improvements, and historical aggregate |
| [`NeuralSeek Knowledge/ROI_Analysis/`](./NeuralSeek%20Knowledge/ROI_Analysis/) | **Defensible ROI / TCO numbers** for cost, savings, time-to-production, build-vs-buy, and competitive-math conversations. Days-to-MVP chart, Itochu analyst-ROI, $2M-stack bake-off, 3-year TCO across 3 paths, modeled guardrail volumes. See [`00-INDEX.md`](./NeuralSeek%20Knowledge/ROI_Analysis/00-INDEX.md) for when to use which file. |
| [`NeuralSeek Knowledge/Knowledge from Calls/`](./NeuralSeek%20Knowledge/Knowledge%20from%20Calls/) | Distilled insights from sales/discovery/training calls — positioning, talk tracks, objection handling, pricing, voice & tone, CTO/CISO angles. See [`00-INDEX.md`](./NeuralSeek%20Knowledge/Knowledge%20from%20Calls/00-INDEX.md). |
| [`NeuralSeek Knowledge/Talk Tracks/`](./NeuralSeek%20Knowledge/Talk%20Tracks/) | **18 curated single-thesis talk tracks** for pitches, posts, and persona conversations (CFO, CISO, CTO, procurement, investors, channel partners). Each one: punchline + why it lands + NeuralSeek tie-in + when to use. See [`00-INDEX.md`](./NeuralSeek%20Knowledge/Talk%20Tracks/00-INDEX.md) for the by-category map and audience-to-track guide. |
| [`NeuralSeek Knowledge/Marketing Alignment Pack/`](./NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/) | **Pitch-ready, third-party-validated content** built from a top-tier VC firm's May 2026 agentic-AI deck. VC-firm-agrees side-by-side one-pager, drop-in "why now" 3-slide segment, refreshed CTO/CISO playbook (Angles 4–6 extending the originals). See [`00-INDEX.md`](./NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/00-INDEX.md). Companion to `ROI_Analysis/` (the rest of the same Marketing Alignment Pack). |
| [`NeuralSeek Knowledge/Partnerships/`](./NeuralSeek%20Knowledge/Partnerships/) | Joint solution briefs and partnership materials (IBM Fusion, eDelta) |
| [`NeuralSeek Knowledge/NeuralSeek Story/`](./NeuralSeek%20Knowledge/NeuralSeek%20Story/) | Company narrative — exec bios, keynote outlines |
| [`2026_images/`](./2026_images/) | Logos, screenshots, headshots, brand assets, partner/client logos |

For an LLM-optimized index of every file, see [`llms.txt`](./llms.txt).

## How AI tools consume this

This repo is designed to be a retrieval source for AI agents. Three integration patterns:

1. **GitHub MCP server** — point Claude / ChatGPT at this repo via a fine-grained PAT scoped to read this repo only.
2. **Direct raw URLs** — fetch any file via `https://raw.githubusercontent.com/CerebralBlue-LOV/<repo>/main/<path>` with an auth header.
3. **Clone for embedding/indexing** — `git clone` once, build a vector index over the markdown, refresh on each push.

Every converted markdown file has YAML frontmatter (`title`, `summary`, `tags`, `source`) so retrieval tools can rank and filter without reading the body.

## Full File Index (raw links for AI ingestion)

Every text-fetchable knowledge file in this repo, grouped by folder. Each link points to the **raw** GitHub URL on `main` — so a tool like claude.ai (which can only fetch URLs that appear in a prior fetch result) can pick up the README, see this index, and then fetch any individual file.

For a flat, one-URL-per-line list (best for bulk machine ingestion), see [`INDEX.md`](INDEX.md). Total content files indexed: **79**.

### Repository root

- [AGENTS.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/AGENTS.md)
- [BRAND_RULES.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/BRAND_RULES.md)
- [CLAUDE.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/CLAUDE.md)
- [README.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/README.md)
- [llms.txt](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/llms.txt)

### 2026_images

- [neuralseek-brand-guidelines_2026.html](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/2026_images/neuralseek-brand-guidelines_2026.html)
- [neuralseek-brand-guidelines_2026.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/2026_images/neuralseek-brand-guidelines_2026.md)

### NeuralSeek Knowledge / Client Stories

- [AFP-Capital.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/AFP-Capital.md)
- [AdMed.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/AdMed.md)
- [Adobe.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/Adobe.md)
- [BROU.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/BROU.md)
- [Clip.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/Clip.md)
- [NatWest.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/NatWest.md)
- [NeuralSeek-Itochu-Customer-Journey.html](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/NeuralSeek-Itochu-Customer-Journey.html)
- [NeuralSeek-Itochu-UseCase-Review.html](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/NeuralSeek-Itochu-UseCase-Review.html)
- [PennState.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/PennState.md)
- [Snap.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/Snap.md)
- [Verizon.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/Verizon.md)
- [childrens-health.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/childrens-health.md)
- [great-day-improvements.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/great-day-improvements.md)
- [historical-client-stories.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/historical-client-stories.md)
- [itochu.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Client%20Stories/itochu.md)

### NeuralSeek Knowledge / Features

- [NeuralSeek_Documentation_KB.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/NeuralSeek_Documentation_KB.md)
- [all-ai-tuning-and-guardrails.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/all-ai-tuning-and-guardrails.md)
- [detailed-rfp-response.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/detailed-rfp-response.md)
- [llm-api-level-tuning.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/llm-api-level-tuning.md)
- [maistro_governance_analysis.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/maistro_governance_analysis.md)
- [neuralseek-governance.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/neuralseek-governance.md)
- [neuralseek_118_ai_guardrails_listing.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/neuralseek_118_ai_guardrails_listing.md)
- [platform-level-ai-ops-settings.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/platform-level-ai-ops-settings.md)
- [seek_governance_analysis.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Features/seek_governance_analysis.md)

### NeuralSeek Knowledge / Knowledge from Calls

- [00-INDEX.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/00-INDEX.md)
- [01-strategic-positioning.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/01-strategic-positioning.md)
- [02-powerful-quotes.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/02-powerful-quotes.md)
- [03-objection-handling.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/03-objection-handling.md)
- [04-competitive-differentiation.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/04-competitive-differentiation.md)
- [05-customer-stories.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/05-customer-stories.md)
- [06-sales-talk-tracks.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/06-sales-talk-tracks.md)
- [07-product-talking-points.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/07-product-talking-points.md)
- [08-pricing-deal-mechanics.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/08-pricing-deal-mechanics.md)
- [09-market-industry-insights.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/09-market-industry-insights.md)
- [10-lawrence-voice-and-tone.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/10-lawrence-voice-and-tone.md)
- [11-brand-marketing-strategy.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/11-brand-marketing-strategy.md)
- [12-punch-line-talk-tracks.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/12-punch-line-talk-tracks.md)
- [13-cto-ciso-selling-angles.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/13-cto-ciso-selling-angles.md)
- [cto-ciso-selling-angles-visual.html](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Knowledge%20from%20Calls/cto-ciso-selling-angles-visual.html)

### NeuralSeek Knowledge / Marketing Alignment Pack

- [00-INDEX.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/00-INDEX.md)
- [F-vc-firm-agrees-onepager.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/F-vc-firm-agrees-onepager.md)
- [G-why-now-segment.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/G-why-now-segment.md)
- [H-ciso-talk-track-refresh.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Marketing%20Alignment%20Pack/H-ciso-talk-track-refresh.md)

### NeuralSeek Knowledge / NeuralSeek Story

- [AI-Salon-Keynote-Outline.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/NeuralSeek%20Story/AI-Salon-Keynote-Outline.md)
- [neuralseek-executive-team.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/NeuralSeek%20Story/neuralseek-executive-team.md)

### NeuralSeek Knowledge / Partnerships

- [edelta-complements-neuralseek.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Partnerships/edelta-complements-neuralseek.md)
- [ibm-fusion-ns-solution-brief.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Partnerships/ibm-fusion-ns-solution-brief.md)

### NeuralSeek Knowledge / ROI_Analysis

- [00-INDEX.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/00-INDEX.md)
- [A-days-to-mvp.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/A-days-to-mvp.md)
- [B-itochu-analyst-roi.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/B-itochu-analyst-roi.md)
- [C-itochu-bakeoff-vs-stack.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/C-itochu-bakeoff-vs-stack.md)
- [D-build-vs-buy-tco.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/D-build-vs-buy-tco.md)
- [E-guardrails-in-action.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/ROI_Analysis/E-guardrails-in-action.md)

### NeuralSeek Knowledge / Talk Tracks

- [00-INDEX.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/00-INDEX.md)
- [TT-01-from-calculator-to-strategist.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-01-from-calculator-to-strategist.md)
- [TT-02-the-loop-is-the-agent.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-02-the-loop-is-the-agent.md)
- [TT-03-every-major-computing-paradigm.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-03-every-major-computing-paradigm.md)
- [TT-04-why-now-inference-costs-fell.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-04-why-now-inference-costs-fell.md)
- [TT-05-agents-proliferate-per-workflow.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-05-agents-proliferate-per-workflow.md)
- [TT-06-always-on-attack-surface.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-06-always-on-attack-surface.md)
- [TT-07-as-models-commoditize.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-07-as-models-commoditize.md)
- [TT-08-whoever-owns-the-workflow.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-08-whoever-owns-the-workflow.md)
- [TT-09-the-5-layer-agent-stack.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-09-the-5-layer-agent-stack.md)
- [TT-10-salesforce-consumption-pricing.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-10-salesforce-consumption-pricing.md)
- [TT-11-open-source-coding-layer-parallel.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-11-open-source-coding-layer-parallel.md)
- [TT-12-three-pillars-of-agentic-intelligence.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-12-three-pillars-of-agentic-intelligence.md)
- [TT-13-seek-node-agent-harness-compressed.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-13-seek-node-agent-harness-compressed.md)
- [TT-14-ai-engineer-in-a-box.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-14-ai-engineer-in-a-box.md)
- [TT-15-governance-is-architecture.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-15-governance-is-architecture.md)
- [TT-16-even-anthropic-cant-get-governance-right.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-16-even-anthropic-cant-get-governance-right.md)
- [TT-17-price-per-completed-task.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-17-price-per-completed-task.md)
- [TT-18-companies-that-act-now.md](https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/NeuralSeek%20Knowledge/Talk%20Tracks/TT-18-companies-that-act-now.md)

## Content conventions

- **Markdown is canonical.** PDFs, DOCX, and PPTX originals live in `source/` subfolders alongside their converted markdown. The markdown is what AIs should retrieve; the originals are kept in case someone needs to send a customer the actual deck or document.
- **Images extracted from documents** live in per-folder `media/` directories and are referenced by relative paths from the markdown.
- **Frontmatter** on every converted file gives a structured summary for retrieval.

## Updating

Lawrence pushes directly to `main`. To propose a change, anyone else opens a PR — Lawrence reviews and merges.

## Source files

Original DOCX, PDF, and PPTX files are preserved in `source/` subfolders inside each topic directory (e.g., `NeuralSeek Knowledge/Features/source/`). Don't edit the markdown alone if the source needs to change — update the source, re-run conversion, and commit both.
