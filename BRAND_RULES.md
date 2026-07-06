---
title: NeuralSeek — Brand Rules for AI Tools
summary: >-
  The minimum rules any AI must follow when generating ANY NeuralSeek deliverable in ANY format — Word docs (.docx), PowerPoint decks (.pptx), PDFs, HTML pages, slides, social cards, banners, emails, images, marketing collateral. Canvas background is a rolling purple radial gradient — never dots, grids, mesh, noise, or patterns. This file is the TL;DR; the full brand system lives in 2026_images/neuralseek-brand-guidelines_2026.md.
tags: [brand, brand-rules, ai-instructions, canvas, background, gradient, no-dots, no-grids, critical, docx, pptx, pdf, html, slides, all-formats]
priority: critical
applies_to: [word-docs, powerpoint, pdf, html, slides, social-cards, banners, email, images, markdown, any-deliverable]
---

# NeuralSeek — Brand Rules for AI Tools

> **If you are an AI agent generating ANY NeuralSeek deliverable, read this file
> first. The full brand book is at
> [`2026_images/neuralseek-brand-guidelines_2026.md`](2026_images/neuralseek-brand-guidelines_2026.md).
> This file is the non-negotiable subset.**

## ⚠ APPLIES TO EVERY OUTPUT FORMAT — not just HTML

These rules govern **every artifact you produce** when the work is for NeuralSeek:

- 📄 **Word documents** (`.docx`) — reports, whitepapers, RFP responses, letters, memos
- 📊 **PowerPoint decks** (`.pptx`) — pitches, keynotes, customer reviews, board materials
- 📑 **PDFs** — anything exported as PDF, from any source
- 🌐 **HTML pages** — landing pages, dashboards, internal tools, microsites
- 🎞️ **Slides** (Google Slides, Keynote, Reveal.js, any deck format)
- 🖼️ **Images** — social cards, banners, charts, infographics, hero images, headshots
- 📧 **Emails** — HTML email templates, marketing emails, customer-facing comms
- 📝 **Markdown / docs** — knowledge base, READMEs, customer-facing markdown
- 🧾 **Anything else** with the NeuralSeek name or logo on it

If you cannot apply a specific rule because the output format does not support it
(e.g., a CSV file has no styling), preserve the rules you *can* apply (file name,
metadata, embedded asset names) and **never substitute an anti-pattern as a
fallback**. When in doubt, ask the user; never improvise.

Format-specific guidance is in section **RULE 7** below.

---

## RULE 1 — Canvas background is GRADIENT ONLY

The page background MUST be the rolling purple radial-gradient canvas. Five
overlapping radial ellipses on a near-black base. Nothing else on top.

**Never use:**

- ❌ Dot grids / pin-grids / polka dots
- ❌ Square grids / pixel grids / blueprint grids
- ❌ Mesh / wireframe / circuit-board patterns
- ❌ Noise / grain / film texture
- ❌ Particles / star fields / glowing-dot fields
- ❌ Diagonal stripes / hatching
- ❌ Flat solid dark (must have the rolling gradient — flat is wrong)
- ❌ "AI hex" / neural-net decoration patterns
- ❌ Any tiled, repeated, or geometric pattern

**Required CSS — paste verbatim:**

```css
body {
  background-color: #131316;
  background-image:
    radial-gradient(ellipse 1100px 900px at 18% 8%,  #301E4C 0%, transparent 55%),
    radial-gradient(ellipse 900px 750px at 82% 26%, rgba(48, 30, 76, 0.72), transparent 55%),
    radial-gradient(ellipse 1300px 850px at 8% 72%, rgba(48, 30, 76, 0.55), transparent 60%),
    radial-gradient(ellipse 1050px 900px at 92% 96%, #301E4C 0%, transparent 55%),
    radial-gradient(ellipse 800px 600px at 50% 50%, rgba(48, 30, 76, 0.18), transparent 70%);
  background-attachment: fixed;
  background-repeat: no-repeat;
  color: rgba(255, 255, 255, 0.95);
}
```

**If gradients are unavailable** (raster image generators that struggle with them):
fall back to flat `#1a1424` and state "gradient unavailable in this format."
**Never** fall back to dots or grids.

**Why:** Dots and grids communicate "AI sparkle" — the exact aesthetic NeuralSeek
positions *against*. The gradient communicates "institutional, calm, governed"
to CISO / compliance buyers.

---

## RULE 2 — Logo is full-color, always — and pick the right variant for the background

- The NeuralSeek mark sweeps **cyan → trust blue → indigo → magenta**, top-left
  to bottom-right.
- **Never** recolor it. **Never** flatten it. **Never** place it on busy imagery.
- Minimum clear space: 1× the cap-height of the wordmark on every side.

### Logo variant selection — pick by background

The brand canvas is dark by default, so the **colored N + white text** variant
is the right choice for nearly every NeuralSeek deliverable. Only switch to the
colored-text variant when the background is genuinely white or near-white (print
docs, light-mode exports, formal letterhead).

| Background | Use this file | Path |
|---|---|---|
| **Dark / brand canvas / any non-white surface (DEFAULT)** | `color_logo_white_text.svg` — colored N mark with white wordmark | [`2026_images/NeuralSeek Logos/color_logo_white_text.svg`](2026_images/NeuralSeek%20Logos/color_logo_white_text.svg) |
| **White / near-white / light-mode print** | `neuralseek__colored_logo_and_name.png` — colored N mark with colored wordmark | [`2026_images/NeuralSeek Logos/neuralseek__colored_logo_and_name.png`](2026_images/NeuralSeek%20Logos/neuralseek__colored_logo_and_name.png) |
| **Mark only — no wordmark needed (small UI, favicon, footer chip)** | `neuralseek_colored_just_logo.png` — colored N mark alone | [`2026_images/NeuralSeek Logos/neuralseek_colored_just_logo.png`](2026_images/NeuralSeek%20Logos/neuralseek_colored_just_logo.png) |
| **All-white fallback** when even the colored N would clash (overlaid on photography, single-color print, etched/embossed) | `neuralseek_all_white_logo_and_name.png` — monochrome white wordmark + mark | [`2026_images/NeuralSeek Logos/neuralseek_all_white_logo_and_name.png`](2026_images/NeuralSeek%20Logos/neuralseek_all_white_logo_and_name.png) |

**Default presumption:** If you cannot inspect the background or you are unsure,
use `color_logo_white_text.svg`. The brand canvas is dark; the colored-N + white-text
combination is the workhorse logo for almost every NeuralSeek visual.

---

## RULE 3 — Two fonts only

- **Open Sans** — every word a human reads (headings, body, navigation, forms).
- **JetBrains Mono** — every identifier the system writes (model names, run IDs,
  policy references, code).
- No other fonts.

---

## RULE 4 — Color discipline

- **Blue governs.** Governance, audit, security, admin surfaces stay blue.
- **Purple creates.** AI-creation surfaces use indigo (`#5B2DFF`) → magenta (`#A24BFF`).
- **Cyan signals.** `#1FB6FF` for highlights and pointers.
- **Magenta accents.** Sparingly. Only on creation surfaces.
- **Never** mix governance-blue and creation-magenta on the same surface.

Brand hex palette:

| Token | Hex | Use |
|---|---|---|
| Canvas | `#131316` | Page background base |
| Regal Purple | `#301E4C` | Background glow accent (5 radial gradients) |
| Cyan | `#1FB6FF` | Highlights, pointers, signal |
| Trust Blue | `#2D5BFF` | Governance, system, admin |
| Indigo | `#5B2DFF` | Creation surfaces, action gradient start |
| Magenta | `#A24BFF` | Creation surfaces, action gradient end |
| Ink (cards) | `#2A2638` | Default card surface (lifted ~2 shades above canvas) |
| Surface-2 | `#1F1C28` | Recessed surfaces (table headers, code) |
| Approve / Warn / Block | `#22C55E` / `#F59E0B` / `#EF4444` | Status colors |

---

## RULE 5 — Gradient text on important phrases

- Title gradient: `linear-gradient(90deg, #FDFEFF 0%, #7BABFF 100%)` for
  governance phrases.
- Pink variant: `linear-gradient(90deg, #FDFEFF 0%, #E170FC 100%)` for creation
  phrases.
- **One gradient phrase per heading.** Never two. Never on body text. Never on
  labels or mono identifiers.

---

## RULE 6 — Voice & tone

NeuralSeek sells to CISOs, CROs, CCOs in regulated industries (gov, healthcare,
banking). Voice is:

- Calm, considered, declarative.
- Built for governance, not for vibes.
- "Built to be trusted in regulated rooms."
- Use the punch-line talk tracks in
  [`NeuralSeek Knowledge/Knowledge from Calls/12-punch-line-talk-tracks.md`](NeuralSeek%20Knowledge/Knowledge%20from%20Calls/12-punch-line-talk-tracks.md)
  for sales angles.

Avoid: "AI sparkle" language, hype phrases, generic "transform your business"
copy, anything that sounds like a generic AI startup.

---

## RULE 7 — Format-specific application

The rules above (background, logo, fonts, color, voice) apply to **every** output
format. Below is the concrete guidance for each common deliverable type. If your
output format is not listed, apply the closest match and preserve the spirit:
dark canvas, rolling purple gradient (where renderable), Open Sans + JetBrains
Mono, brand-palette colors, full-color logo, no anti-patterns.

### 📊 PowerPoint (`.pptx`) — pitches, decks, customer reviews, board materials

- **Slide master background:** solid fill `#131316`. If gradient fills are
  supported by your generation library (python-pptx `gradient_stops`,
  python-pptx-templater, etc.), use a linear or radial gradient from
  `#301E4C` (top-left) to `#131316` (bottom-right) instead.
- **Title font:** Open Sans Semibold 32pt (fallback chain: Open Sans → Calibri →
  Arial). Use white `#FFFFFF` by default. Use cyan-to-blue gradient `#FDFEFF →
  #7BABFF` for the single most important phrase per title (if your library
  supports text gradients; otherwise solid `#7BABFF`).
- **Body font:** Open Sans Regular 18pt, white at 95% opacity (`#F2F2F2`).
- **Code / identifiers:** JetBrains Mono 14pt (fallback: Consolas, Courier New).
- **Accent color for key callouts:** `#A24BFF` (creation/AI surfaces) or
  `#1FB6FF` (signals/highlights). Never both on the same slide.
- **Logo placement:** the slide canvas is dark, so use
  `2026_images/NeuralSeek Logos/color_logo_white_text.svg` (colored N + white
  text) in the masthead or footer of the slide master so it appears on every
  slide. See the logo variant table in RULE 2 — use the white-text variant on
  any non-white background.
- **Charts:** use the brand palette — cyan, trust-blue, indigo, magenta — in
  that order for series. Use Approve/Warn/Block colors only for status data.
- **Forbidden:** dot-grid backgrounds, mesh patterns, noise textures, particle
  effects, generic "tech" or "AI" slide templates, default Office themes.

### 📄 Word documents (`.docx`) — reports, whitepapers, RFP responses

There are two acceptable Word modes — choose based on intended use:

- **Digital-only mode (preferred default):** dark page background `#131316`
  with white body text. Cover page uses the full rolling-purple gradient (insert
  as a full-bleed image generated from the HTML brand spec, or use Word's
  gradient fill: linear `#301E4C → #131316`).
- **Print mode (use only when the doc will be physically printed):** light
  background (`#FFFFFF`), dark body text (`#0B1220`). All brand colors still
  apply for headings, accent rules, and callouts. Cover page can still use the
  dark canvas as a full-bleed image.

In both modes:

- **Headings:** Open Sans Bold — H1 24pt, H2 18pt, H3 14pt. H1 in `#7BABFF`
  (governance) or `#E170FC` (creation). H2/H3 inherit from H1 family.
- **Body:** Open Sans Regular 11pt.
- **Code / identifiers / API refs:** JetBrains Mono 10pt.
- **Footer:** include "NeuralSeek · Built to be trusted in regulated rooms" and
  a small color logo aligned right.
- **Forbidden:** Calibri-default Word documents with no styling, generic
  Microsoft templates, dot/grid page borders, any "AI"-themed clipart.

### 📑 PDFs — exported from any source

PDFs inherit the rules of their source format:

- **PDF from Word:** apply Word rules above.
- **PDF from HTML:** apply HTML rules (RULE 1's CSS spec). Use
  `--print-background` in headless Chrome / wkhtmltopdf / weasyprint so the
  rolling-gradient canvas actually renders in the PDF.
- **PDF from PowerPoint:** apply PowerPoint rules above.
- **Standalone PDF generators (reportlab, fpdf, etc.):** dark canvas
  `#131316`, Open Sans (embed the font), brand colors, no anti-patterns.

### 🌐 HTML pages — landing pages, microsites, dashboards, internal tools

- Use the exact CSS in **RULE 1** verbatim.
- Load Open Sans and JetBrains Mono via Google Fonts:
  ```html
  <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  ```
- Set `body { font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif; }`.
- Set `pre, code { font-family: 'JetBrains Mono', ui-monospace, monospace; }`.
- All other rules from RULES 1–6 apply.

### 🖼️ Images, banners, social cards, hero graphics

- **Canvas:** dark `#131316` with the 5-blob rolling purple radial gradient
  (`#301E4C`). If your image generator (DALL·E, Imagen, Midjourney, Stable
  Diffusion) cannot reliably produce gradients, fall back to flat `#1a1424`
  and explicitly state "gradient unavailable in this format." **Never** fall
  back to dots, grids, mesh, or "AI"-aesthetic patterns.
- **Logo:** always full-color, from `2026_images/NeuralSeek Logos/`. Never
  recolor, flatten, or place on busy imagery. **For the dark brand canvas
  (the default case for almost every image), use the colored-N + white-text
  variant: `color_logo_white_text.svg`.** Only switch to the colored-text
  variant (`neuralseek__colored_logo_and_name.png`) if the background is
  genuinely white or near-white. See the variant table in RULE 2 for the
  full picker.
- **Templates to copy from:** the existing LinkedIn banners
  ([`neuralseek-linkedin-banner-company.svg`](2026_images/NeuralSeek%20Logos/neuralseek-linkedin-banner-company.svg),
  [`neuralseek-linkedin-banner-personal.svg`](2026_images/NeuralSeek%20Logos/neuralseek-linkedin-banner-personal.svg))
  are good reference templates for proportions and treatment.

### 📧 Emails — HTML and plain-text

- **HTML emails:** use the dark canvas gradient, but include a flat-color
  fallback `background-color: #1a1424;` because some email clients (Outlook
  desktop, certain mobile clients) do not render CSS gradients reliably.
- **Plain-text emails:** include the color logo as an inline attachment. Keep
  voice consistent with RULE 6 — calm, declarative, no AI sparkle.

### 📝 Markdown / docs (READMEs, knowledge base entries)

- The rendering host (GitHub, GitLab, etc.) controls the styling, so you can't
  apply the canvas directly.
- What you *can* control: descriptive image filenames, full-color logo embeds,
  consistent code-block language tags, brand-voice copy throughout.
- Add YAML frontmatter (`title`, `summary`, `tags`, `source`) so AI retrieval
  works well.

### 🧾 Anything else

If you cannot find your format in the list above, default to:
1. Dark canvas (`#131316`) with the rolling purple gradient where renderable.
2. Open Sans + JetBrains Mono.
3. Brand-palette colors only.
4. Full-color NeuralSeek logo, never recolored.
5. Voice from RULE 6.
6. **Never** substitute an anti-pattern as a fallback. Ask first.

---

## RULE 8 — Visual asset catalog: use these exact files

When a deliverable needs to show a NeuralSeek workspace node, an enterprise app
connector, a third-party data source, or a logo lockup, **use the canonical
brand-approved asset from `2026_images/`**. Do not pull logos from Google
Images, vendor websites, or any other source — those won't match the brand
treatment, and many vendor logos have specific monochrome/color restrictions
the brand-approved versions already handle.

This catalog mirrors the assets shown in
[`2026_images/neuralseek-brand-guidelines_2026.md`](2026_images/neuralseek-brand-guidelines_2026.md).
The two files stay aligned — that brand book is the priority source if anything
diverges.

### 8.1 Logo lockups (4 variants)

Already covered in detail in RULE 2 above. Summary:

- Dark / non-white background (DEFAULT): `2026_images/NeuralSeek Logos/color_logo_white_text.svg`
- White / light-mode background: `2026_images/NeuralSeek Logos/neuralseek__colored_logo_and_name.png`
- Mark only (small UI, favicon): `2026_images/NeuralSeek Logos/neuralseek_colored_just_logo.png`
- All-white monochrome fallback: `2026_images/NeuralSeek Logos/neuralseek_all_white_logo_and_name.png`

### 8.2 Workspace nodes — the visual grammar of mAIstro flows

Every capability in the NeuralSeek workspace is rendered as a square, neutrally-styled node icon. Use these when showing mAIstro flow diagrams, architecture slides, or "what NeuralSeek does" overviews. All paths are under `2026_images/nodes/`.

**Models** (Send To LLM variants — extend with additional `send_to_*.png` files in the folder when you need a specific model):
- `nodes/send_to_claude_4_sonnet.png`
- `nodes/send_to_managed_gpt_5_4.png`
- `nodes/send_to_llama_3_2_90b_vision.png`
- `nodes/send_to_deepseek_v3.png`
- `nodes/embeddings.png`
- `nodes/translate.png`

**Knowledge & Retrieval:**
- `nodes/seek.png` — the canonical Seek node (= one drag-and-drop = ~6,000 lines of TypeScript per TT-13)
- `nodes/ns_kb_search.png`
- `nodes/ns_kb_add_document.png`
- `nodes/ns_kb_delete_document.png`
- `nodes/semantic_score.png`
- `nodes/curate.png`

**Guardrails & Governance:**
- `nodes/protect_prompt_injection.png`
- `nodes/remove_pii.png`
- `nodes/profanity_filter.png`
- `nodes/http_guardrails.png`
- `nodes/condition.png`
- `nodes/stop.png`

**Data & Connectors:**
- `nodes/postgres.png`
- `nodes/snowflake.png`
- `nodes/databricks.png`
- `nodes/db2_database.png`
- `nodes/neo4j.png`
- `nodes/redshift.png`

**Generation & Output:**
- `nodes/create_doc.png`
- `nodes/create_pdf.png`
- `nodes/create_powerpoint.png`
- `nodes/generate_image.png`
- `nodes/generate_speech.png`
- `nodes/generate_video.png`

**Logic, Protocol & I/O:**
- `nodes/mcp.png`
- `nodes/a2a.png`
- `nodes/rest.png`
- `nodes/extract.png`
- `nodes/mathematical_calculation.png`
- `nodes/read_cache.png`

> The brand book calls out "60+ workspace nodes" — the catalog above is the curated subset shown in the brand book itself. For other nodes (additional models, additional connectors), browse `2026_images/nodes/` directly and follow the same square-icon visual grammar.

### 8.3 Enterprise app connectors — systems of record

Use these when showing NeuralSeek's native connector ecosystem (one-pagers, RFP responses, integration diagrams). All paths are under `2026_images/Enterprise Apps/`.

- `Enterprise Apps/salesforce.webp`
- `Enterprise Apps/hubspot.png`
- `Enterprise Apps/slack.png`
- `Enterprise Apps/teams.png` — Microsoft Teams
- `Enterprise Apps/gmail.png`
- `Enterprise Apps/zoom.png`
- `Enterprise Apps/sharepoint.png`
- `Enterprise Apps/googledrive.png`
- `Enterprise Apps/box.png`
- `Enterprise Apps/googleCalendar.webp`
- `Enterprise Apps/jira.png`
- `Enterprise Apps/trello.svg`
- `Enterprise Apps/clickup.png`
- `Enterprise Apps/workday.png`
- `Enterprise Apps/snowflake.png`
- `Enterprise Apps/databricks.png`
- `Enterprise Apps/bigquery.svg`
- `Enterprise Apps/Postgresql.png`
- `Enterprise Apps/oracle.png`
- `Enterprise Apps/db2.webp` — IBM Db2
- `Enterprise Apps/neo4j.png`
- `Enterprise Apps/elastic.webp`
- `Enterprise Apps/azure.png` — Microsoft Azure
- `Enterprise Apps/watsonx.png` — IBM watsonx
- `Enterprise Apps/epic.webp`
- `Enterprise Apps/erp.webp`

### 8.4 Third-party data sources — external signals

Use these when showing the search/data/regulatory/prospecting sources NeuralSeek brings inside the policy perimeter. All paths are under `2026_images/3rd Party Data Sources/` unless noted (Hugging Face lives in `LLM Logos/`, PowerPoint in `Enterprise Apps/`).

- `3rd Party Data Sources/bing.png`
- `3rd Party Data Sources/brave.png`
- `3rd Party Data Sources/google search.svg`
- `3rd Party Data Sources/tavilylogo.png`
- `LLM Logos/huggingface.svg` — Hugging Face
- `3rd Party Data Sources/sec_edgar.png`
- `3rd Party Data Sources/nasdaq.png`
- `3rd Party Data Sources/zillow.png`
- `3rd Party Data Sources/attom.png`
- `3rd Party Data Sources/clay.webp`
- `3rd Party Data Sources/instantly.png`
- `3rd Party Data Sources/heyreach.png`
- `Enterprise Apps/powerpoint.png` — PowerPoint (used as a data source for ingestion)

### 8.5 LinkedIn banner templates

For social posts / banners, copy the proportions and treatment from these existing SVGs rather than designing from scratch:

- `2026_images/NeuralSeek Logos/neuralseek-linkedin-banner-company.svg` — company-page banner ("Deploy AI under policy.")
- `2026_images/NeuralSeek Logos/neuralseek-linkedin-banner-personal.svg` — personal/exec banner ("Built to be trusted." + 118 guardrails callout)

### 8.6 Product screenshots — real UI beats mockups

170+ product-UI captures live under `2026_images/Product Screenshots/`, organized
for navigation: **start at
[`Product Screenshots/00-INDEX.md`](2026_images/Product%20Screenshots/00-INDEX.md)**.
The `full-screen/` subfolder holds the 18 full-page hero shots (use these first);
component close-ups are grouped under `maistro-governance/`, `seek-governance/`,
`maistro-editor/`, and `neuralworks/`. Never mock up a NeuralSeek UI when a real
screenshot exists — check the index first.

### Rules for using these assets

- **Use the exact filename** — do not substitute variants from elsewhere on the web.
- **Vendor logos are full color by default.** If a deliverable requires monochrome (single-color print, embossed surface), check `2026_images/whited_logos/` for white-only variants before recoloring anything.
- **Keep aspect ratios.** All logos and node icons are designed at the proportions stored on disk; do not stretch or squash.
- **Sizing.** Logo lockups need 1× the cap-height of the wordmark as minimum clear space on every side (per RULE 2). Node icons render at square aspect, sizes typically 40–80px in flow diagrams, 120–240px when featured.
- **If you need a logo or node icon not listed here**, browse the relevant `2026_images/<folder>/` first. If it's not in the repo, ask before improvising — the brand-approved version may exist but not yet be linked.

---

## If this file conflicts with the full brand book

The full brand book at `2026_images/neuralseek-brand-guidelines_2026.md` is the
source of truth for everything not listed here. This file is the AI-critical
subset. If you see a conflict, follow the full brand book — and please flag the
conflict so it can be reconciled.
