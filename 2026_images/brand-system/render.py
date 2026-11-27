#!/usr/bin/env python3
"""
NeuralSeek brand renderer. Turns a filled template into final PNG / PDF files and checks it.

  pip install playwright && python -m playwright install chromium
  python render.py templates/social-post.html                       # PNG per frame
  python render.py templates/social-post.html --content my.json     # fill slots from JSON, then render
  python render.py templates/deck.html --pdf                        # one PDF, one page per frame
  python render.py templates/one-pager.html                         # PDF (template asks for it)

content.json (all keys optional):
  {
    "_palette": "night", "_texture": "silk", "_layout": "product",   # applied to every frame
    "headline": "Governed AI, <span class=\"kp\">in production</span>",
    "sub": "...", "eyebrow": "...", "cta": "...",
    "screenshot": "../../Product Screenshots/maistro-editor/flow_seek.png",
    "frames": [ { "headline": "...", "_palette": "dawn" }, ... ]           # per-frame values, in order
  }

The script exits with code 1 if a QA check fails (fonts missing, text over its line limit,
text overlapping the logo/screenshot, text outside the safe margin). Fix the copy, not the layout.
"""
import argparse, json, pathlib, sys
from playwright.sync_api import sync_playwright

FILL_JS = """
(c) => {
  const setFrame = (f, data) => {
    for (const [k, v] of Object.entries(data || {})) {
      if (k === 'frames') continue;
      if (k.startsWith('_')) { f.setAttribute('data-' + k.slice(1), v); continue; }
      f.querySelectorAll('[data-slot="' + k + '"]').forEach(el => {
        if (el.tagName === 'IMG') el.src = v; else if (el.querySelector('img') && k === 'screenshot') el.querySelector('img').src = v; else el.innerHTML = v;
      });
    }
  };
  const frames = [...document.querySelectorAll('.frame')];
  frames.forEach(f => setFrame(f, c));
  (c.frames || []).forEach((d, i) => frames[i] && setFrame(frames[i], d));
}
"""

QA_JS = """
() => {
  const issues = [];
  const fams = ['600 40px Sora', '400 20px "Albert Sans"', '500 20px "JetBrains Mono"'];
  fams.forEach(f => { if (!document.fonts.check(f)) issues.push('Font not loaded: ' + f); });
  const frames = [...document.querySelectorAll('.frame')];
  frames.forEach((fr, i) => {
    const n = 'frame ' + (i + 1);
    const R = fr.getBoundingClientRect();
    const text = [...fr.querySelectorAll('[data-slot]')].filter(e => e.tagName !== 'IMG' && !e.classList.contains('window') && e.offsetParent !== null && e.textContent.trim());
    const blocks = [...fr.querySelectorAll('.logo:not(.glass .logo), .window, .lockup')].filter(e => e.offsetParent !== null);
    text.forEach(e => {
      const r = e.getBoundingClientRect();
      const lh = parseFloat(getComputedStyle(e).lineHeight);
      const max = parseInt(e.dataset.maxLines || '0');
      if (max && lh) { const lines = Math.round(r.height / lh); if (lines > max) issues.push(`${n}: "${e.dataset.slot}" has ${lines} lines (max ${max}). Shorten the copy.`); }
      if (r.right > R.right - 40 || r.bottom > R.bottom - 40 || r.left < R.left + 30 || r.top < R.top + 30) issues.push(`${n}: "${e.dataset.slot}" goes outside the safe margin.`);
      if (e.scrollWidth > e.clientWidth + 2) issues.push(`${n}: "${e.dataset.slot}" overflows horizontally.`);
      blocks.forEach(b => {
        if (b.contains(e) || e.contains(b)) return;
        const q = b.getBoundingClientRect();
        if (r.left < q.right && r.right > q.left && r.top < q.bottom && r.bottom > q.top) issues.push(`${n}: "${e.dataset.slot}" overlaps ${b.className.split(' ')[0]}.`);
      });
    });
    const st = getComputedStyle(fr).backgroundImage;
    if (!fr.classList.contains('transparent') && !['flat-dark','flat-light','white'].includes(fr.dataset.palette) && (!st || st === 'none'))
      issues.push(`${n}: no texture for palette="${fr.dataset.palette}" texture="${fr.dataset.texture}" in this format (check allowed palettes).`);
  });
  return issues;
}
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--content")
    ap.add_argument("--out", default="out")
    ap.add_argument("--scale", type=float, default=1)
    ap.add_argument("--pdf", action="store_true")
    ap.add_argument("--no-qa", action="store_true")
    a = ap.parse_args()
    src = pathlib.Path(a.html).resolve()
    out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
    content = json.loads(pathlib.Path(a.content).read_text()) if a.content else None
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 2100, "height": 2200}, device_scale_factor=a.scale)
        pg.goto(src.as_uri(), wait_until="networkidle")
        if content: pg.evaluate(FILL_JS, content)
        pg.evaluate("document.fonts.ready")
        pg.wait_for_timeout(300)
        issues = [] if a.no_qa else pg.evaluate(QA_JS)
        for s in issues: print("QA:", s)
        want_pdf = a.pdf or pg.evaluate("!!document.querySelector('meta[name=ns-output][content=pdf]')")
        frames = pg.query_selector_all(".frame")
        stem = src.stem
        if want_pdf:
            w, h = pg.evaluate("(()=>{const r=document.querySelector('.frame').getBoundingClientRect();return [r.width,r.height]})()")
            pg.add_style_tag(content=f"@page{{size:{w}px {h}px;margin:0}} html,body{{background:none!important}} body.ns-doc{{display:block;padding:0}} .frame{{page-break-after:always;break-after:page}}")
            pg.emulate_media(media="print")
            path = out / f"{stem}.pdf"
            pg.pdf(path=str(path), width=f"{w}px", height=f"{h}px", print_background=True, prefer_css_page_size=True)
            print("PDF:", path)
        else:
            for i, f in enumerate(frames, 1):
                transparent = f.evaluate("e=>e.classList.contains('transparent')")
                if transparent: pg.evaluate("document.documentElement.style.background='transparent';document.body.style.background='transparent'")
                path = out / f"{stem}-{i:02d}.png"
                f.screenshot(path=str(path), omit_background=transparent)
                print("PNG:", path)
        b.close()
    if issues: sys.exit(1)

if __name__ == "__main__":
    main()
