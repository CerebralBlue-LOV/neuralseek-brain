---
title: NeuralSeek brand textures (v3)
summary: >-
  Official generated background textures for brand v3. Use these files instead of generating or improvising backgrounds. Social textures carry 3-4% grain; deck textures have none.
status: current
tags: [brand, v3, textures, backgrounds, social, decks, night, dawn, aurora, bloom, ice]
---

# Brand textures (v3)

Official backgrounds for social posts and decks. They come from the brand guidelines: [`../neuralseek-brand-guidelines_2026_v3.md`](../neuralseek-brand-guidelines_2026_v3.md) (§6). **Use these files as they are. Never generate, recolor or improvise a texture.**

Raw URL pattern for AI tools: `https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/2026_images/textures/<folder>/<file>`

## Social (`social/`, 1080×1350, 4:5, with 3–4% grain)

One texture per piece and one palette per campaign. File names are `<palette>-<style>.jpg`.

| Palette | Mode | Use | Text and logo on top |
|---|---|---|---|
| `night` | Dark | Default for everything dark: company page, events, launches | White text `#F8FAFC`, key phrase `#C9B8F0`, logo `color_logo_white_text.svg` |
| `dawn` | Light | Default for everything light: personal accounts, product, quotes | Ink text `#171322`, key phrase `#5A3FA3`, logo `neuralseek__colored_logo_and_name.png` |
| `aurora` | Dark | Social only: product and tech | Same as night |
| `bloom` | Dark | Social only: launches and events | Same as night |
| `ice` | Light | Social only: partners and governance on light | Same as dawn |

| Style | Look | Use |
|---|---|---|
| `silk` | Smooth flowing light | Default for most pieces |
| `streak` | Motion lines | Launches, events, webinars |
| `ribbon` | One band of color, lots of empty space | Quotes, announcements, text-heavy pieces |

Files: `night-silk`, `night-streak`, `night-ribbon`, `dawn-silk`, `dawn-streak`, `dawn-ribbon`, `aurora-silk`, `aurora-streak`, `aurora-ribbon`, `bloom-silk`, `bloom-streak`, `bloom-ribbon`, `ice-silk`, `ice-streak`, `ice-ribbon` (all `.jpg`).

## Decks (`deck/`, 1920×1080, 16:9, no grain)

Only Night and Dawn, max 2 backgrounds per deck, and the **same style** across the deck (for example `night-silk` + `dawn-silk`).

| File | Use |
|---|---|
| `night-silk.jpg`, `night-streak.jpg`, `night-ribbon.jpg` | Cover, section dividers, data slides, close |
| `dawn-silk.jpg`, `dawn-streak.jpg`, `dawn-ribbon.jpg` | Product and customer slides |

## More textures from the brand kit

Same palettes, in the exact compositions used in the Brand Kit 2026. Use them for the formats named.

| Folder / file | Size | Use |
|---|---|---|
| `signature/night-silk-a.jpg` | 1080×1350 | Signature Night silk (dark default for social) |
| `signature/night-streak-b.jpg` | 1080×1350 | Signature Night streak (webinars, events) |
| `signature/night-silk-c.jpg`, `signature/dawn-silk-c.jpg` | 1080×1350 | Announcements, hiring, quotes |
| `signature/glass-edge-aurora-1.jpg`, `-2.jpg` | 1080×1350 | Partner and product launch posts (dark slab with lit edge) |
| `signature/slab-bloom.jpg` | 1080×1350 | Launch and event posts |
| `signature/ice-gradient-wide.jpg`, `signature/bloom-silk-wide.jpg` | 1200×627 | Text-heavy link posts |
| `wide/night-silk-wide.jpg`, `wide/night-streak-wide.jpg`, `wide/dawn-silk-wide.jpg` | 1920×1080 | YouTube thumbnails, Zoom/Teams backgrounds, web headers (not deck slides: use `deck/`) |
| `carousel/night-streak-panorama-3-slides.jpg` | 3240×1350 | One continuous texture cut into three 1080×1350 carousel slides |
| `banners/linkedin-banner-<palette>.jpg` | 1584×396 | LinkedIn banners: night (company page), dawn (personal), aurora, bloom, ice (campaigns) |
| `email/newsletter-header-*.jpg` | 1200×400 | Newsletter headers (shown at 600×200) |
| `print/brochure-cover-dawn-*.jpg` | 1275×1050 | Top band of a brochure cover (the rest stays white) |
| `print/rollup-night-*.jpg` | 990×2376 | Event roll-up banners (33×80 in) |

## Rules

- Put text directly on the calm area of the texture, with generous empty space. Add a flat `#131316` (dark) or `#FAF9FC` (light) panel only behind more than 3 lines of running text; never box every slide or post.
- Type scale, default palette per piece and reference examples: §6 of the guidelines and [`../brand-examples/`](../brand-examples/README.md).
- Optional on social and deck covers: hairline grid in thirds (1 px, 10–14% opacity) with + markers at the crossings.
- Never add glows, orbs, extra gradients or gradient text on top.
- PDFs and brochures stay white; only the brochure cover may use `dawn` (see §7 of the guidelines).
- Website pages do not use these textures.
