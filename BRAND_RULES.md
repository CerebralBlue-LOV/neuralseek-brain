---
title: NeuralSeek — Brand Rules for AI Tools
summary: >-
  The minimum rules any AI must follow when generating ANY NeuralSeek deliverable in ANY format. Brand v3: the website's violet palette in light and dark, Sora + Albert Sans + JetBrains Mono, light PDFs and brochures, a generated-texture system for social and decks. This file is the TL;DR; the full brand system lives in 2026_images/neuralseek-brand-guidelines_2026_v3.md.
tags: [brand, brand-rules, ai-instructions, v3, light-mode, dark-mode, sora, albert-sans, critical, docx, pptx, pdf, html, slides, all-formats]
priority: critical
applies_to: [word-docs, powerpoint, pdf, html, slides, social-cards, banners, email, images, markdown, any-deliverable]
---

# NeuralSeek — Brand Rules for AI Tools

> **Brand v3 (2026-11-04).** v2.1 (dark-only canvas, Open Sans) is archived in `2026_images/archive/brand-guidelines-v2.1/`.
>
> **If you are an AI agent generating ANY NeuralSeek deliverable, read this file
> first. The full brand book is at
> [`2026_images/neuralseek-brand-guidelines_2026_v3.md`](2026_images/neuralseek-brand-guidelines_2026_v3.md).
> This file is the non-negotiable subset.**

## APPLIES TO EVERY OUTPUT FORMAT — not just HTML

These rules govern **every artifact you produce** when the work is for NeuralSeek:

- **Word documents** (`.docx`) — reports, whitepapers, RFP responses, letters, memos
- **PowerPoint decks** (`.pptx`) — pitches, keynotes, customer reviews, board materials
- **PDFs** — anything exported as PDF, from any source
- **HTML pages** — landing pages, dashboards, internal tools, microsites
- **Slides** (Google Slides, Keynote, Reveal.js, any deck format)
- **Images** — social cards, banners, charts, infographics, hero images, headshots
- **Emails** — HTML email templates, marketing emails, customer-facing comms
- **Markdown / docs** — knowledge base, READMEs, customer-facing markdown
- **Anything else** with the NeuralSeek name or logo on it

If you cannot apply a specific rule because the output format does not support it
(e.g., a CSV file has no styling), preserve the rules you *can* apply (file name,
metadata, embedded asset names) and **never substitute an anti-pattern as a
fallback**. When in doubt, ask the user; never improvise.

Format-specific guidance is in section **RULE 7** below.

---

## RULE 1 — Backgrounds: light and dark, from the website tokens

Both modes are official. Pick by channel (see RULE 7).

| Token | Light | Dark |
|---|---|---|
| canvas | `#FAF9FC` | `#131316` |
| surface-2 | `#F2EFF9` | `#1F1C28` |
| surface (cards) | `#E9E4F4` | `#2A2638` |
| surface-elev | `#FFFFFF` | `#332F42` |
| wash | `#DDD3F3` | `#301E4C` |

- Web: flat canvas, alternating with surface-2. Neutrals first.
- PDFs and print: white `#FFFFFF`.
- Social and decks: generated Night (dark) or Dawn (light) textures from the `neuralseek-social-design` skill. Decks: max 2 backgrounds per deck, no grain. Social: one palette per piece, 3–4% grain allowed.
- Official texture files: `2026_images/textures/` (`social/` 1080×1350 and `deck/` 1920×1080, see its README). Use them as they are.
- If neither the files nor the `neuralseek-social-design` skill is available, use the flat canvas and brand tokens from this file. Never improvise textures, glows or gradients.

**Never use:**

- Dot grids / polka dots
- Glows or radial orbs pasted on flat black; colored shadows
- Noise or grain in decks, PDFs or the website
- Website point-cloud figures (book, network, bridge, globe, scale, cube) outside the website
- Stock imagery, "AI hex" or circuit-board decoration
- The hairline + grid and frosted glass in the website UI (they belong to the social/deck system only)

**Why:** NeuralSeek sells to risk and compliance buyers. Calm neutrals, real product screenshots and one violet accent read as institutional; effects read as "AI sparkle".

---

## RULE 2 — Logo is full-color, always — and pick the right variant for the background

- The NeuralSeek mark sweeps **cyan → trust blue → indigo → magenta**, top-left
  to bottom-right.
- **Never** recolor it. **Never** flatten it. **Never** place it on busy imagery.
- Minimum clear space: 1× the cap-height of the wordmark on every side.

### Logo variant selection — pick by background

Pick by background: colored N + ink text on light backgrounds (web light mode,
PDFs, brochures, partner pieces), colored N + white text on dark backgrounds
(dark mode, LinkedIn company page, YouTube, Night textures).

| Background | Use this file | Path |
|---|---|---|
| **Dark backgrounds** | `color_logo_white_text.svg` — colored N mark with white wordmark | [`2026_images/NeuralSeek Logos/color_logo_white_text.svg`](2026_images/NeuralSeek%20Logos/color_logo_white_text.svg) |
| **Light backgrounds** | `neuralseek__colored_logo_and_name.png` — colored N mark with colored wordmark | [`2026_images/NeuralSeek Logos/neuralseek__colored_logo_and_name.png`](2026_images/NeuralSeek%20Logos/neuralseek__colored_logo_and_name.png) |
| **Mark only — no wordmark needed (small UI, favicon, footer chip)** | `neuralseek_colored_just_logo.png` — colored N mark alone | [`2026_images/NeuralSeek Logos/neuralseek_colored_just_logo.png`](2026_images/NeuralSeek%20Logos/neuralseek_colored_just_logo.png) |
| **All-white fallback** when even the colored N would clash (overlaid on photography, single-color print, etched/embossed) | `neuralseek_all_white_logo_and_name.png` — monochrome white wordmark + mark | [`2026_images/NeuralSeek Logos/neuralseek_all_white_logo_and_name.png`](2026_images/NeuralSeek%20Logos/neuralseek_all_white_logo_and_name.png) |

**If you cannot inspect the background,** use the variant that matches the channel's default mode in RULE 7.

---

## RULE 3 — Three fonts

| Role | Family | Weights |
|---|---|---|
| Headings | **Sora** | 600 (700 only for very short social pieces) |
| Text, menus, buttons, forms | **Albert Sans** | 400 body, 500 emphasis and buttons |
| System labels, IDs, model names, code | **JetBrains Mono** | 400, 500 |

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Albert+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

- Never weight 300. Never mono in paragraphs or marketing headings.
- Open Sans and Quicksand are retired. Never Inter, Geist or Space Grotesk.
- Fallbacks for Office files and email: Sora → Arial; Albert Sans → Calibri/Arial; JetBrains Mono → Consolas.

---

## RULE 4 — Color discipline (violet palette)

| Token | Light | Dark | Use |
|---|---|---|---|
| foreground | `#171322` | `#F8FAFC` | Main text |
| muted-foreground | `#59546C` | `#90A1B9` | Secondary text |
| brand | `#7A57E0` | `#A78BFA` | Key phrase, CTA, links |
| brand-hi | `#4C2E96` | `#C9B8F0` | Violet text (small text in light mode) |
| brand-mid | `#6A4BD0` | `#8B6FD1` | Hover, icons |
| brand-deep | `#5A3FA3` | `#6B4FA8` | Solid blocks |
| brand-shade | `#2A1A5E` | `#301E4C` | Deep backgrounds |
| Approve / Warn / Block | `#22C55E` / `#F59E0B` / `#EF4444` | same | Status only |

- Neutrals first. Solid violet only for the CTA, the key phrase and at most one block per screen or piece.
- Max 3 violet tones per piece. One primary CTA per screen.
- Category colors (pink, orange, blue, teal, yellow, purple, indigo, green) only for marketplace cards and charts.

---

## RULE 5 — Key phrase in solid violet, never gradient text

- One key phrase per heading in solid violet. Never two. Flat backgrounds: `brand` (#7A57E0 light, #A78BFA dark). On textures: #5A3FA3 on Dawn/Ice, #C9B8F0 on Night/Aurora/Bloom.
- Layout for social and decks (type scale, panels, default palette per piece, partner lockup): v3 guidelines §6 and `2026_images/brand-examples/`.
- No gradient text anywhere, with one exception: big customer-result numbers in the "results row" piece may use the logo gradient (`#30CCFE → #5281F4 → #4C3DF5 → #A32EF6 → #F98AFE`), on dark only, one number per tile.
- Only approved customer figures. Demo values (e.g. 72%, $1.73) may appear inside UI screenshots, never as results.


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

| Channel | Default mode | Notes |
|---|---|---|
| Web | Light, dark toggle | One brand CTA per section |
| LinkedIn company page | Dark | 1080×1350 or 1200×627; Night or a social palette |
| LinkedIn personal | Light | Soft violets, nothing that looks like an ad |
| YouTube | Dark | Thumbnail 1280×720 |
| Partnerships | Light | Logos at equal height with "×"; partner colors only in its logo |
| PDFs | Light, white | Letter, 2 pages max |
| Brochures | Light | Letter bifold, 4 pages |
| Newsletter | Light | 600 px wide |

### PowerPoint (`.pptx`) and slides
- Max 2 backgrounds per deck: Night (cover, sections, data, close) and Dawn (product, cases). No grain.
- Titles Sora 600 (fallback Arial), body Albert Sans (fallback Calibri), identifiers JetBrains Mono.
- Key phrase in solid `brand` violet. Real product screenshots, straight, 8 px radius, 1 px border.
- Logo variant per background (RULE 2).

### Word documents (`.docx`)
- White page, foreground `#171322` text. Headings Sora 600 (fallback Arial), body Albert Sans 11 pt (fallback Calibri).
- Accent rules and callouts in `brand` / `brand-deep`. Footer: logo + "Governed AI, in production · neuralseek.com".

### PDFs and brochures
- White background, Albert Sans 500 text, Sora 600 headings, mono for eyebrows.
- PDF: one brand-deep card for the recommendation, no dark areas, no textures.
- Brochure: Dawn texture and + grid on the cover only; white and canvas inside; one Night block on the back cover.
- Results rows on surface-2 with brand-hi numbers. Footer: logo · "Governed AI, in production · neuralseek.com" · page number.

### HTML pages
- Use the RULE 1 and RULE 4 tokens with `light-dark()` or a `prefers-color-scheme` switch.
- Load the fonts from RULE 3. `body { font-family: 'Albert Sans', system-ui, sans-serif; }`, headings `'Sora'`, `pre, code { font-family: 'JetBrains Mono', ui-monospace, monospace; }`.

### Images, banners, social cards
- Generated textures from the `neuralseek-social-design` skill (Night, Dawn, Aurora, Bloom, Ice), one palette per piece and per campaign.
- Hairline grid in thirds with + markers, frosted-glass logo tiles, real screenshots that may bleed off the edge.
- Never website point-cloud figures, stock photos or invented UI.

### Emails
- Light, 600 px wide. Sora headings with Arial fallback; Albert Sans body with Arial fallback.

### Markdown / docs
- Styling is controlled by the host. Keep descriptive filenames, full-color logo embeds and YAML frontmatter.

### Anything else
1. Light or dark tokens from RULE 1 and RULE 4.
2. Sora + Albert Sans + JetBrains Mono.
3. Full-color logo, never recolored.
4. Voice from RULE 6.
5. Never substitute an anti-pattern as a fallback. Ask first.


---

## RULE 8 — Visual asset catalog: use these exact files

When a deliverable needs to show a NeuralSeek workspace node, an enterprise app
connector, a third-party data source, or a logo lockup, **use the canonical
brand-approved asset from `2026_images/`**. Do not pull logos from Google
Images, vendor websites, or any other source — those won't match the brand
treatment, and many vendor logos have specific monochrome/color restrictions
the brand-approved versions already handle.

This catalog carries over the asset files from v2.1 (archived in
`2026_images/archive/brand-guidelines-v2.1/`) and is the source of truth for
which file to use. The v3 guidelines
([`2026_images/neuralseek-brand-guidelines_2026_v3.md`](2026_images/neuralseek-brand-guidelines_2026_v3.md))
point here for assets.

### 8.1 Logo lockups (4 variants)

Already covered in detail in RULE 2 above. Summary:

- Dark backgrounds: `2026_images/NeuralSeek Logos/color_logo_white_text.svg`
- Light backgrounds: `2026_images/NeuralSeek Logos/neuralseek__colored_logo_and_name.png`
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

### 8.5 LinkedIn banner templates (v2.1, pending redesign to v3)

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

The full brand book at `2026_images/neuralseek-brand-guidelines_2026_v3.md` is the
source of truth for everything not listed here. This file is the AI-critical
subset. If you see a conflict, follow the full brand book — and please flag the
conflict so it can be reconciled.
