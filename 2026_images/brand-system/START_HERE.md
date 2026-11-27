---
title: NeuralSeek Brand System — START HERE (for any agent or designer)
version: v3 brand system 1.0 (2026-11-27)
status: current
priority: critical
applies_to: [social, linkedin, decks, pdf, one-pager, brochure, video, youtube, reels, email, newsletter, banners]
summary: >-
  Locked templates, tokens, fonts and textures that produce NeuralSeek marketing assets that look the same
  no matter which agent makes them. Fill the template; never design from scratch.
---

# NeuralSeek Brand System: START HERE

**Rule zero: do not design. Fill a template.** Every NeuralSeek marketing asset is made by copying a template from `templates/`, changing only the text inside `[data-slot]` elements and the frame attributes, and rendering it with `render.py`. Layout, fonts, colors, sizes, textures, logo and spacing are locked.

## 1. Pick the template

| You need | Template | Size | Output |
|---|---|---|---|
| LinkedIn / Instagram post (event, webinar, quote, announcement) | `social-post.html` · `data-layout="text"` | 1080×1350 | PNG |
| Company-page product post with a real screenshot | `social-post.html` · `data-layout="product"` | 1080×1350 | PNG |
| Partner post (NeuralSeek × partner) | `social-post.html` · `data-layout="partner"` | 1080×1350 | PNG |
| Link post, blog share, text-heavy post | `social-landscape.html` | 1200×627 | PNG |
| Deck (cover, section, content, statement, close) | `deck.html` | 1920×1080 | PDF (one page per slide) |
| Solution brief, one-pager, partner brief | `one-pager.html` | Letter, 2 pages | PDF |
| Reels, Shorts, Stories, vertical video cards | `video-9x16.html` (title, caption, end) | 1080×1920 | PNG per frame |
| YouTube / landscape video cards, lower third | `video-16x9.html` (title, end, lower third) | 1920×1080 | PNG per frame (lower third transparent) |
| Newsletter / email header | `email-header.html` | 1200×400 | PNG |

Previews of every template: `previews/`. Not on the list? Ask the brand owner (marketing). Do not invent a new layout.

## 2. Fill it

Change only:
- **Text inside `[data-slot]`.** Wrap exactly ONE key phrase per headline in `<span class="kp">…</span>`.
- **Frame attributes:**
  - `data-palette`: `night` | `dawn` | `aurora` | `bloom` | `ice`.
  - `data-texture`: `silk` | `streak` | `ribbon`.
  - `data-layout`: social post only.
- **Screenshot `src`:** a real file from `2026_images/Product Screenshots/`.
- **Delete** an element you don't need. Never leave it empty.

Or put the copy in a JSON file (see `examples-content/`) and pass `--content`.

Never change: the `<style>` block, `tokens/brand.css`, sizes, positions, fonts, colors, or the scrim (the soft shading that keeps text readable).

## 3. Choose the palette

| Palette | Mode | Use |
|---|---|---|
| `night` | dark | **Default.** Company page, webinars, events, deck cover/section/close, video |
| `dawn` | light | Personal accounts, quotes, product and content slides |
| `aurora` | dark | Product and tech posts (social and video only) |
| `bloom` | dark | Launches and brand events only (social and video only) |
| `ice` | light | Partners and governance on light (social and video only) |

- One palette per campaign.
- Decks: `night` + `dawn` only, max 2 backgrounds.
- PDFs: white, no texture.
- Email: dawn silk, dawn ribbon or ice silk.

## 4. Render and check

```bash
pip install playwright && python -m playwright install chromium
python render.py templates/social-post.html --content my-post.json --out out/
```

`render.py` exits with an error when:
- the fonts did not load;
- a headline is over its line limit;
- text leaves the safe margin;
- text overlaps the logo or screenshot;
- a palette is not allowed in that format.

**Fix the copy, never the layout.** If a headline does not fit, shorten it, or use `data-size="m"` / `"s"` on the headline.

If you cannot run code (design tools, video editors), use the same files directly:
- **Backgrounds:** `2026_images/textures/{social|landscape|vertical|video-16x9|deck|email}/` at full resolution.
- **Fonts:** `fonts/`.
- **Colors and sizes:** `tokens/brand-tokens.json`.
- **Composition:** copy the matching preview in `previews/` exactly.

## 5. Copy rules (checked by reviewers)

| Element | Limit |
|---|---|
| Headline | Max 3 lines (deck titles 2) |
| Sub | Max 2 lines |
| CTA | One per piece |

- **Voice:** operator nouns: guardrails, policy, lineage, audit, evidence, controls. Tagline: "Governed AI, in production."
- **Never:**
  - em dashes;
  - emojis;
  - "It's not X, it's Y";
  - "the only", "world-class", "best-in-class";
  - exclamation CTAs.
- **Numbers:** only approved customer figures with a source; never demo numbers as results.
- **Images:** real product screenshots only. No stock, robots, brains, fake UI, or website point-cloud figures.
- **Never add:**
  - glows or extra gradients;
  - icons;
  - card grids;
  - other fonts (Inter, Geist, Space Grotesk, Open Sans, Quicksand).

## 6. Files

```
brand-system/
  START_HERE.md            ← this file
  NeuralSeek-Brand-System-for-Agents.pdf   ← visual one-glance reference (for people and vision agents)
  tokens/brand-tokens.json ← colors, fonts, sizes, palettes, texture paths (machine-readable)
  tokens/brand.css         ← locked stylesheet used by every template
  fonts/                   ← Sora 600/700, Albert Sans 400/500, JetBrains Mono 400/500 (woff2, SIL OFL: free for commercial use)
  templates/               ← the only layouts allowed
  examples-content/        ← sample JSON copy for render.py
  previews/                ← what each template must look like
  render.py                ← fill + render + QA
../textures/               ← official backgrounds, full resolution (never regenerate)
../NeuralSeek Logos/       ← logo files (white text on dark, ink text on light)
```

Full brand book: [`../neuralseek-brand-guidelines_2026_v3.md`](../neuralseek-brand-guidelines_2026_v3.md). If anything here conflicts with an older file, this folder wins.

## Prompt to give any agent

> Make NeuralSeek marketing assets only with the brand system at https://github.com/CerebralBlue-LOV/neuralseek-brain/tree/main/2026_images/brand-system. Read START_HERE.md first. Pick the template for the format, fill only the [data-slot] text and the palette/texture attributes, and render with render.py (or, without code, use the full-resolution textures, fonts and tokens and match the preview exactly). Do not design new layouts, colors, fonts or effects. Copy: [headline + key phrase], [sub], [CTA], [screenshot file], [palette].
