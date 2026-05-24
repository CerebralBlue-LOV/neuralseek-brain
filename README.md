# NeuralSeek Central Brain

The canonical, read-only knowledge base for NeuralSeek — optimized for both humans browsing on GitHub and AI tools retrieving content programmatically.

**Single writer**: Lawrence (lawrence@neuralseek.com).
**Everyone else**: read-only.

## 🚨 If you're an AI agent — read [`BRAND_RULES.md`](./BRAND_RULES.md) first

Before generating any NeuralSeek-branded visual (HTML page, slide, mockup, social card, dashboard, marketing image), read [`BRAND_RULES.md`](./BRAND_RULES.md). It specifies the mandatory canvas background (rolling purple radial gradient — **never dots, grids, mesh, noise, particles, or any pattern**), the logo rule, fonts, and color discipline. The full brand book is at [`2026_images/neuralseek-brand-guidelines_2026.md`](./2026_images/neuralseek-brand-guidelines_2026.md), with the canvas rule pinned at the very top.

## What's in here

| Folder | What it holds |
|---|---|
| [`NeuralSeek Knowledge/Features/`](./NeuralSeek%20Knowledge/Features/) | Product reference docs — AI tuning, guardrails, governance, platform settings, LLM-level controls, RFP responses |
| [`NeuralSeek Knowledge/Client Stories/`](./NeuralSeek%20Knowledge/Client%20Stories/) | Deployment case studies — Itochu, Children's Health, Adobe, Verizon, Snap, NatWest, AFP Capital, BROU, Clip, AdMed, PennState, Great Day Improvements, and historical aggregate |
| [`NeuralSeek Knowledge/Knowledge from Calls/`](./NeuralSeek%20Knowledge/Knowledge%20from%20Calls/) | Distilled insights from sales/discovery/training calls — positioning, talk tracks, objection handling, pricing, voice & tone, CTO/CISO angles. See [`00-INDEX.md`](./NeuralSeek%20Knowledge/Knowledge%20from%20Calls/00-INDEX.md). |
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

## Content conventions

- **Markdown is canonical.** PDFs, DOCX, and PPTX originals live in `source/` subfolders alongside their converted markdown. The markdown is what AIs should retrieve; the originals are kept in case someone needs to send a customer the actual deck or document.
- **Images extracted from documents** live in per-folder `media/` directories and are referenced by relative paths from the markdown.
- **Frontmatter** on every converted file gives a structured summary for retrieval.

## Updating

Lawrence pushes directly to `main`. To propose a change, anyone else opens a PR — Lawrence reviews and merges.

## Source files

Original DOCX, PDF, and PPTX files are preserved in `source/` subfolders inside each topic directory (e.g., `NeuralSeek Knowledge/Features/source/`). Don't edit the markdown alone if the source needs to change — update the source, re-run conversion, and commit both.
