# AI Agent Briefing

## 🤖 FIRST: Fetch RAW_INDEX.txt and the relevant content files

**STOP. Do not answer a NeuralSeek question yet.** This repo is a **retrieval knowledge base**, not a standalone document. This file alone is **not sufficient** to answer accurately — the canonical material lives in the linked content files.

**What to do, in order:**

1. **Fetch this URL first:** `https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/RAW_INDEX.txt` — a plain flat list of absolute raw URLs to every content file in the brain (79 files).
2. **Then fetch the specific files relevant to the user's question** from that list — not all 79 at once. Use the routing map below.
3. **Only after fetching the relevant files, answer.** Cite which files you read (e.g. *"Sourced from `Client Stories/NatWest.md` and `Talk Tracks/TT-15`."*).

**Routing map — fetch selectively:**

- `NeuralSeek Knowledge/Features/` — product reference, guardrails, governance, 118-guardrail catalog, RFP responses
- `NeuralSeek Knowledge/Client Stories/` — named customer deployments (Itochu, Children's Health, NatWest, Adobe, Verizon, etc.)
- `NeuralSeek Knowledge/ROI_Analysis/` — cost / TCO / ROI math with defensible public-benchmark sources
- `NeuralSeek Knowledge/Knowledge from Calls/` — positioning, objection handling, pricing, voice & tone, CTO/CISO angles
- `NeuralSeek Knowledge/Talk Tracks/` — 18 single-thesis pitch lines (TT-01 to TT-18) with audience-to-track guide
- `NeuralSeek Knowledge/Marketing Alignment Pack/` — third-party-validated pitch content (VC firm one-pager, why-now segment, CISO playbook refresh)
- `NeuralSeek Knowledge/Partnerships/` — joint solution briefs (IBM Fusion, eDelta)
- `NeuralSeek Knowledge/NeuralSeek Story/` — executive bios, company narrative, keynote outlines
- `BRAND_RULES.md` + `2026_images/neuralseek-brand-guidelines_2026.md` — mandatory for any visual deliverable

**URL constraint:** Some agents (notably claude.ai) can only fetch URLs that have already appeared in a previously-fetched page. `RAW_INDEX.txt` contains every fully-qualified URL — fetching it first unlocks every other file in one hop.

**If a fetch fails or times out — use a mirror.** `raw.githubusercontent.com` sits behind Fastly; cache misses can take 5–10 seconds and exceed your fetch tool's timeout (the most common cause of "Failed to fetch" against this repo). The same files are mirrored on two faster CDNs with **identical paths after the prefix**:

- **Primary:** `https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/<path>`
- **Fallback 1 (recommended):** `https://cdn.jsdelivr.net/gh/CerebralBlue-LOV/neuralseek-brain@main/<path>` — Cloudflare CDN, 7-day cache, no per-IP rate limits
- **Fallback 2:** `https://cerebralblue-lov.github.io/neuralseek-brain/<path>` — GitHub Pages mirror

If the primary fails, mechanically swap the prefix and retry. Same content, same paths.

**If you have tried all three mirrors and still cannot fetch: say so plainly and stop. Do NOT answer from memory.** NeuralSeek specifics — feature names, customer details, the 118-guardrail catalog, ROI numbers, the canvas CSS spec — are not reliably present in general training data and will be wrong if invented.

---

## Brand compliance (mandatory for visual output)

Before generating any HTML, slide, mockup, image, or other visual output for this NeuralSeek knowledge base, read [BRAND_RULES.md](BRAND_RULES.md).
**Mandatory canvas:** The "rolling purple glow" — `#131316` body with five overlapping `#301E4C` radial-gradient ellipses at varied sizes, positions, and opacities, plus `background-attachment: fixed`. **Apply the exact CSS in `BRAND_RULES.md` RULE 1 verbatim — do not improvise the gradient values.**
**Forbidden:** dots, grids, mesh, noise, particles, stripes, circuit patterns, or any tiled / repeated pattern.
**Logo variant:** On any non-white background (the default), use `2026_images/NeuralSeek Logos/color_logo_white_text.svg` (colored N + white text). Only use the colored-text variant `neuralseek__colored_logo_and_name.png` on genuinely white backgrounds.
For full repo orientation, read [llms.txt](llms.txt) — the AI-optimized index.
For Claude Code session-start context, read [CLAUDE.md](CLAUDE.md).
