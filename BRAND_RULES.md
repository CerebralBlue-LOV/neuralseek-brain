---
title: NeuralSeek — Brand Rules for AI Tools
summary: >-
  The minimum rules any AI must follow when generating NeuralSeek-branded visuals. The canvas background is a rolling purple radial gradient — never dots, grids, mesh, noise, or patterns. This file is the TL;DR; the full brand system lives in 2026_images/neuralseek-brand-guidelines_2026.md.
tags: [brand, brand-rules, ai-instructions, canvas, background, gradient, no-dots, no-grids, critical]
priority: critical
---

# NeuralSeek — Brand Rules for AI Tools

> **If you are an AI agent generating NeuralSeek-branded visuals, content, or
> code, read this file first. The full brand book is at
> [`2026_images/neuralseek-brand-guidelines_2026.md`](2026_images/neuralseek-brand-guidelines_2026.md).
> This file is the non-negotiable subset.**

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

## RULE 2 — Logo is full-color, always

- The NeuralSeek mark sweeps **cyan → trust blue → indigo → magenta**, top-left
  to bottom-right.
- **Never** recolor it. **Never** flatten it. **Never** place it on busy imagery.
- Minimum clear space: 1× the cap-height of the wordmark on every side.

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

## If this file conflicts with the full brand book

The full brand book at `2026_images/neuralseek-brand-guidelines_2026.md` is the
source of truth for everything not listed here. This file is the AI-critical
subset. If you see a conflict, follow the full brand book — and please flag the
conflict so it can be reconciled.
