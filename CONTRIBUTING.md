# Contributing to the NeuralSeek Central Brain

This repository is the canonical public knowledge base for
[NeuralSeek](https://neuralseek.ai). It uses a **single-writer model**:
Lawrence ([lawrence@neuralseek.com](mailto:lawrence@neuralseek.com))
is the only person who pushes to `main`. Everyone else contributes
via pull request.

## What changes are welcome

- **Factual corrections** — wrong number, broken link, outdated client
  detail, misspelled name, stale pricing
- **Source attribution** — if you can add a public source to a claim
  that's currently uncited, please do
- **New canonical content** added by NeuralSeek staff — new client
  stories, new talk tracks, new ROI math, refreshed brand assets
- **Translations and accessibility improvements** to existing files

## What changes are not welcome

- Rewording Lawrence's existing talk tracks, ROI analysis, or call-
  derived voice content — these are authored, not collaborative
- Adding new feature names, customer names, or financial figures
  without source verification
- Edits to `BRAND_RULES.md`,
  `2026_images/neuralseek-brand-guidelines_2026.md`, or the canvas
  CSS spec without coordination with the brand owner

## How to contribute

1. Fork the repository on GitHub.
2. Create a branch (`fix/typo-in-natwest-story` or
   `add/new-client-story-foo`).
3. Make your change. Keep commits focused — one logical change per
   commit, descriptive message.
4. If your change adds a new content file, also update:
   - `RAW_INDEX.md` and `RAW_INDEX.txt` (the absolute-URL index)
   - The relevant folder's `00-INDEX.md` if one exists
   - `llms.txt` if the new content is substantial
   - `README.md` "What this knowledge base can answer" if your
     change adds a question the brain can now answer
5. Open a pull request against `main`. Lawrence reviews and merges.

## Brand compliance for visual contributions

If your contribution generates HTML, slides, PDFs, social cards, or
any branded visual output, you **must** follow
[`BRAND_RULES.md`](./BRAND_RULES.md). Specifically:

- Use the rolling purple radial-gradient canvas spec verbatim
  (`#131316` base with five `#301E4C` ellipses)
- **Never** use dots, grids, mesh, noise, particles, stripes, or any
  tiled pattern
- Use the colored-N + white-text logo
  (`2026_images/NeuralSeek Logos/color_logo_white_text.svg`) on
  any non-white background

Pull requests that violate brand rules will be asked to revise
before merge.

## Reporting issues

For factual errors, broken links, or missing canonical content, open
a GitHub issue with the file path and a concrete description of what
needs to change. For brand-misuse reports or licensing questions,
email lawrence@neuralseek.com directly.
