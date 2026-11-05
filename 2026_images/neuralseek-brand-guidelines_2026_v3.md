---
title: NeuralSeek Brand Guidelines 2026 v3
version: v3 (revised 2026-11-05)
status: current
source: neuralseek-brand-guidelines_2026_v3.md
tags: [brand, brand-guidelines, v3, design-system, typography, color, light-mode, dark-mode, sora, albert-sans, social, decks, pdf]
replaces: v2.1 (archived at 2026_images/archive/brand-guidelines-v2.1/)
summary: >-
  The current violet website palette, in light and dark mode. Typography: Sora (headings), Albert Sans (text),
  JetBrains Mono (system data). Applies to the website, social, partnerships, PDFs and the newsletter. Replaces Open Sans and Quicksand.
---

# NeuralSeek Brand Guidelines v3

## 1. What changes from v2.1
| Topic | v2.1 / today | v3 |
|---|---|---|
| Headings | Open Sans (web), Quicksand (social) | Sora 600 |
| Text | Open Sans | Albert Sans 400/500 |
| Data, IDs, labels | JetBrains Mono | JetBrains Mono (unchanged) |
| Palette | Dark-first, 4 accents | The website's current violet palette |
| Mode | Dark only | Light and dark, both official |
| Scope | Web | Web, social, partnerships, PDFs, newsletter |

Voice, taglines and the asset catalog (logo files, nodes, connectors, screenshots) carry over from v2.1 and live in `BRAND_RULES.md` (RULE 2, RULE 6, RULE 8).

v3 keeps the current palette because the website's figures (aurora, cube, particles) are violet. Other palettes clashed with them in testing.

## 2. Typography
| Role | Family | Weights | Use |
|---|---|---|---|
| Headings | Sora | 600 (700 only for very short social pieces) | H1–H3, post headlines, covers |
| Text | Albert Sans | 400 for body text; 500 for emphasis and buttons | Paragraphs, menus, buttons, forms, captions |
| System | JetBrains Mono | 400, 500 | Uppercase eyebrows, IDs, model names, code |

```html
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&family=Albert+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```
```css
--font-display: 'Sora', system-ui, sans-serif;
--font-body: 'Albert Sans', system-ui, sans-serif;
--font-mono: 'JetBrains Mono', ui-monospace, monospace;
```

Type scale (desktop). On mobile, H1 drops to 40–44 px and H2 to 28–32 px. Body text stays at 16 px.

| Level | Size | Line height | Letter spacing |
|---|---|---|---|
| H1 | 64–76 px | 1.05 | −0.03em |
| H2 | 40–48 px | 1.1 | −0.02em |
| H3 | 24–28 px | 1.2 | −0.01em |
| Body | 17–18 px | 1.5 | 0 |
| Small text | 14 px | 1.5 | 0 |
| Eyebrow (mono) | 12 px, uppercase | 1.4 | +0.08em |

Rules:
- Never use weight 300.
- Set one key phrase per heading in solid violet (`brand`). Never use gradient text.
- Only exception: large customer-result numbers in the "results row" piece may use the logo gradient (#30CCFE → #5281F4 → #4C3DF5 → #A32EF6 → #F98AFE). One number per tile, Sora 600, dark background only.
- Never use mono in paragraphs or marketing headings.
- Keep paragraph lines to about 65 characters at most.

## 3. Color (tokens from the website's src/styles.css)
| Token | Light | Dark | Use |
|---|---|---|---|
| foreground | #171322 | #F8FAFC | Main text |
| muted-foreground | #59546C | #90A1B9 | Secondary text |
| canvas | #FAF9FC | #131316 | Page background |
| surface-2 | #F2EFF9 | #1F1C28 | Alternating sections |
| surface | #E9E4F4 | #2A2638 | Cards |
| surface-elev | #FFFFFF | #332F42 | Featured card, modals |
| wash | #DDD3F3 | #301E4C | Color bands, behind figures |
| brand | #7A57E0 | #A78BFA | Key phrase, CTA, links |
| brand-hi | #4C2E96 | #C9B8F0 | Violet text |
| brand-mid | #6A4BD0 | #8B6FD1 | Hover, icons |
| brand-deep | #5A3FA3 | #6B4FA8 | Solid blocks |
| brand-shade | #2A1A5E | #301E4C | Deep backgrounds |

Contrast:
- foreground on light canvas: 17.4:1.
- brand on light canvas: 4.7:1.
- White on a brand button: 4.9:1.
- Dark brand on #131316: 6.8:1.
- For small violet text in light mode, use brand-hi (9.4:1).

Rules:
- Neutrals come first. Use solid violet only for the CTA, the key phrase and at most one block per screen or piece.
- Use no more than 3 violet tones per piece.
- Use one primary CTA per screen.
- Category colors (pink, orange, blue, teal, yellow, purple, indigo, green) are for marketplace cards and charts only.

## 4. Logo, figures and images
- **Logo:**
  - Light backgrounds: color symbol with ink text.
  - Dark backgrounds: color symbol with white text.
  - Avatars and favicons: symbol only.
  - Clear space: at least the height of the logo's capital letters.
  - Never recolor or invert the logo.
- **Point-cloud figures** (book, network, bridge, globe, scale, cube) are for the **website only**. Never use them on social, decks or partnership pieces. On the website, keep them in their original violets.
- **Product images:**
  - Always use real, recent screenshots from `2026_images/Product Screenshots` in this repo (up to 2600 px). Never use low-res screen grabs or invented UI.
  - Pick screens that show data. Never use empty states (Red Team with no results, Cache Savings at $0).
  - Demo numbers (e.g. 72%, $1.73) may appear as interface, never as a customer result.
  - Screenshots stay flat and straight, with an 8 px radius and a 1 px border. They may bleed off the edge of the frame. No 3D tilt.
- **Photos:** real people and events only, never stock.

## 5. Application by channel
| Channel | Default mode | Format | Key points |
|---|---|---|---|
| Web | Light, with a dark toggle | Responsive | One brand CTA per section |
| LinkedIn company page | Dark | 4:5 (1080×1350); 1200×627 for text-heavy posts | Large Sora heading, a figure or real screenshot, white logo |
| LinkedIn personal accounts | Light | 4:5 or 1200×627 | Real look, soft violets, nothing that looks like an ad |
| YouTube | Dark | Thumbnail 1280×720; banner 2560×1440 | Short heading, product screenshot |
| Partnerships | Light | Letter/A4; posts 4:5 | Logos at the same height with "×" between them. The partner's colors appear only in its logo |
| PDFs | Light, white background | Letter, 2 pages max | Albert Sans 500 for text; brand-deep card for recommendations. See §7 |
| Brochures | Light (white + canvas) | Letter bifold, 4 pages | Dawn on the cover only; one Night block on the back cover. See §7 |
| Newsletter | Light | 600 px wide | Sora headings with an Arial fallback |

Co-branding: follow the partner's own rules for its logo. Each brand keeps its own typeface, so IBM Plex never replaces Sora.

## 6. Visual system for social and decks
Social posts, decks and partnership pieces share one system: an owned color texture, a hairline grid with + markers, frosted-glass tiles for logos, and real screenshots. The `neuralseek-social-design` skill produces it. If the skill is not available, use the flat canvas and brand tokens (§3); never improvise textures, glows or gradients.

**Textures** (generated, never stock):

| Palette | Colors | Use |
|---|---|---|
| Night | #040307 #131316 #2A1A5E #4C3DF5 #A78BFA #C9B8F0 | Base for everything dark. Matches the website hero silk |
| Dawn | #FAF9FC #E9E4F4 #C9B8F0 #7A57E0 #4C3DF5 | Base for everything light |
| Aurora | #301E4C #4C3DF5 #5281F4 #30CCFE | Social only: product and tech |
| Bloom | #401CF4 #A32EF6 #F98AFE | Social only: launches and events |
| Ice | #F7FBFF #DDEBFF #9DC4FF #5281F4 | Social only: partners and governance on light |

**Shapes:**
- A hairline grid in thirds (1 px, 10–14% opacity) with + markers at the crossings.
- Frosted-glass tiles for logos and lockups. For partners, use two tiles joined by a line with a dot at each end.
- A product window: a real, straight screenshot that may bleed off the edge.

| Format | Backgrounds | Palettes | Grain |
|---|---|---|---|
| Social | Varied per piece | One per piece, from the 5 | 3–4% film grain |
| Decks | Max 2 per deck: Night (cover, sections, data, close) and Dawn (product, cases) | Night and Dawn only | None |
| Partnerships | Night, or split Night/Dawn | Night and Dawn | None in decks and PDFs; grain on posts |

## 7. PDFs and brochures (light backgrounds)
| | PDF (solution brief, one-pager) | Brochure (bifold) |
|---|---|---|
| Background | White #FFFFFF | White, with canvas #FAF9FC on inside pages; Dawn texture on the cover only |
| Dark area | None; one brand-deep card for the recommendation | One Night block per piece (back cover) |
| Grain | None | None |
| + grid and glass tile | No | Cover only |
| Type | Sora 600 headings, Albert Sans 500 text, mono for eyebrows and step numbers | Same |
| Images | Real repo screenshots, straight, 8 px radius, 1 px border; may bleed off the edge | Same |
| Length | Letter, 2 pages max | Letter bifold, 4 pages |
| Footer | Logo · "Governed AI, in production · neuralseek.com" · page number | Same |

- Results rows use surface-2 with brand-hi numbers. Only approved customer figures; never demo values.
- Quotes only from real customers approved for public use.
- Links: verified URLs only.
- Visual reference: NeuralSeek Brand Kit 2026 (PDF, available from marketing).

## 8. How to request pieces (Claude and the team)
Every request uses the `neuralseek-social-design` skill and includes these fields:

| Field | Example |
|---|---|
| Piece type | LinkedIn post, results row, deck slide, PDF, brochure, partner piece |
| Channel and format | LinkedIn company page, 1080×1350 |
| Mode | Dark or light (default per channel, §5) |
| Palette | One of the 5; decks only Night/Dawn; PDFs and brochures white + Dawn |
| Message | One headline + key phrase in violet |
| Proof | Approved figure or quote, with source |
| Image | File name from `2026_images/Product Screenshots` |
| CTA | One |

Template: "Using the neuralseek-social-design skill, create a [piece type] for [channel/format], [mode], palette [name]. Headline: [text], key phrase: [text]. Proof: [approved figure + source]. Screenshot: [file]. CTA: [text]."

Consistency rules:
- One palette per campaign; every piece in the campaign uses it.
- Run the skill's QA before delivery (fonts, tokens, contrast, no anti-AI patterns, approved figures).
- Official assets (logo, textures, screenshots) come only from the repo.
- The brand owner approves new templates before they go into the skill.

## 9. Voice and position (carried over from v2.1)
**Position:** NeuralSeek is the AI development environment regulated enterprises deploy under policy, with guardrails, governance and audit lineage built in.

**Tagline:** Governed AI, in production. (Also in use: "Built to be trusted in regulated rooms.")

Do:
- Lead with operator nouns: guardrails, policy, lineage, attestation, evidence, controls.
- Show dense, real product screens: governance panels, audit logs, policy editors.
- Put every ID, hash and model name in JetBrains Mono.
- Keep one primary CTA per surface.
- Show compliance posture where it fits (SOC 2 · HIPAA).

Don't:
- Casual voice, emojis or "Let's build something amazing!" CTAs.
- Superlatives: "the only", "world-class", "best-in-class".
- Robots, brains, neural-network swooshes or floating 3D objects.

Asset catalog (logos, workspace nodes, connectors, data sources, screenshots): `BRAND_RULES.md` RULE 8 and `2026_images/IMAGE_MAP.md`.

## 10. Anti-AI rules (never use)
- **Backgrounds:**
  - Lavender on every website background at once.
  - Dot grids.
  - More than 2 backgrounds, or more than one palette, in a single deck.
  - Grain in decks.
  - Website point-cloud figures on social or decks.
- **Glass and the + grid:** allowed only in the social/deck system, never in the website UI.
- **Effects:**
  - Glows, radial orbs pasted on flat black, colored shadows.
  - Gradient text (except big result numbers, §2).
  - Decorative particles beyond the official figures; animated arrows.
- **Icons and layout:**
  - Lucide-style icons, emojis, sparkle icons.
  - Rows of identical cards, bento grids.
  - Fake terminals and demos that aren't real.
- **Typography:** Inter, Geist or Space Grotesk; Open Sans or Quicksand anywhere; light weights.
- **Copy:** em dashes; the "It's not X, it's Y" formula.
