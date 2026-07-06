# Product Screenshots — Index

NeuralSeek product-UI captures, organized for LLM/agent navigation. Use these in product explainers, feature pages, decks, one-pagers, and anywhere a real product surface beats a mockup.

**Raw URL pattern:** `https://raw.githubusercontent.com/CerebralBlue-LOV/neuralseek-brain/main/2026_images/Product%20Screenshots/<subfolder>/<file>` (URL-encode spaces as `%20`; subfolder and file names below are already URL-safe kebab-case). If raw.gh times out, swap the prefix per the mirror rule in [`RAW_INDEX.md`](../../RAW_INDEX.md): `https://cdn.jsdelivr.net/gh/CerebralBlue-LOV/neuralseek-brain@main/<path>`.

---

## ⭐ START HERE — `full-screen/` (use these first)

Full-page captures of every governance surface. **These are the preferred, most-frequently-used images** — reach for a full-screen shot first; only drop to a component close-up (folders below) when you need one specific widget or metric.

| File | Shows |
|---|---|
| [`full-screen/seek-overview-full.png`](full-screen/seek-overview-full.png) | Seek Governance Overview — confidence, resolution, prompt-injection, HAP, PII gauges + Top Intents. **The single best "NeuralSeek governance" shot.** |
| [`full-screen/maistro-agent-insights-full.png`](full-screen/maistro-agent-insights-full.png) | mAIstro Agent Insights — runs, run times, execution timeline, component timing. **The single best "agent observability" shot.** |
| [`full-screen/maistro-agent-details-full.png`](full-screen/maistro-agent-details-full.png) | Per-agent drill-down — run time, invocations, latency distribution, P50/P95, phase mix |
| [`full-screen/maistro-cost-insights-1-full.png`](full-screen/maistro-cost-insights-1-full.png) · [`-2-full`](full-screen/maistro-cost-insights-2-full.png) | mAIstro cost dashboards |
| [`full-screen/maistro-model-comparison-full.png`](full-screen/maistro-model-comparison-full.png) | Agent LLM Comparison — side-by-side model results (LLM-agnostic proof) |
| [`full-screen/maistro-red-team-testing-full.png`](full-screen/maistro-red-team-testing-full.png) | Red Team Testing — adversarial test categories, results, recommended strategies |
| [`full-screen/maistro-token-insights-full.png`](full-screen/maistro-token-insights-full.png) | mAIstro token telemetry — cost ranking, cache savings, tokens over time |
| [`full-screen/seek-configuration-insights-full.png`](full-screen/seek-configuration-insights-full.png) | Configuration Insights — the "Git for your AI configuration" surface |
| [`full-screen/seek-cost-insights-1-full.png`](full-screen/seek-cost-insights-1-full.png) · [`-2`](full-screen/seek-cost-insights-2-full.png) · [`-3`](full-screen/seek-cost-insights-3-full.png) | Seek cost dashboards |
| [`full-screen/seek-documentation-insights-full.png`](full-screen/seek-documentation-insights-full.png) | KnowledgeBase coverage, confidence, most-referenced documents |
| [`full-screen/seek-intent-insights-full.png`](full-screen/seek-intent-insights-full.png) | Intent coverage % and confidence % |
| [`full-screen/seek-model-comparison-full.png`](full-screen/seek-model-comparison-full.png) | Seek-side LLM comparison |
| [`full-screen/seek-seek-logs-full.png`](full-screen/seek-seek-logs-full.png) | Seek Logs — full audit-trail view (Replay Functionality surface) |
| [`full-screen/seek-semantic-insights-full.png`](full-screen/seek-semantic-insights-full.png) | Semantic scoring — hallucination bloom, top hallucinated terms, source coverage |
| [`full-screen/seek-token-insights-full.png`](full-screen/seek-token-insights-full.png) | Seek token telemetry — cost orbit, token intensity, tokens over time |

**Quick picks by story:** governance pitch → `seek-overview-full` · observability → `maistro-agent-insights-full` · anti-hallucination → `seek-semantic-insights-full` · audit/Replay → `seek-seek-logs-full` · LLM-agnostic → `maistro-model-comparison-full` · security/red-team → `maistro-red-team-testing-full` · cost control → `maistro-token-insights-full`.

---

## Component close-ups by area

Every widget from each full screen, cropped as an individual image. Use when a deliverable needs one specific metric or chart.

### `maistro-governance/` — the mAIstro (multi-agent) governance pane

| Subfolder | Files | What's inside |
|---|---|---|
| [`agent-details/`](maistro-governance/agent-details/) | 12 | Per-agent metrics: `average-run-time`, `invocations`, `latency-distribution`, `latency-over-period`, `p50`, `p95`, `peak`, `phase-mix`, `time-in-phase`, `agent-compared-to-other-agents`, `time-of-day-of-runs`, `guardrails-left` |
| [`agent-insights/`](maistro-governance/agent-insights/) | 11 | Fleet-level: `agent-runs`, `agent-run-times`, `agent-execution-timeline`, `agent-run-ranking`, `average-total-component-time`, `component-timing-guitar-chart`, `concurrency-delay`, `equivalent-seeks-per-run`, `guardrail-activations`, `time-per-run` + legacy `governance-maistro-flow-insights.webp` |
| [`model-comparison/`](maistro-governance/model-comparison/) | 9 | `agent-selection`, `new-comparison`, `previous-runs`, `results`, per-model cards (`claude-4-sonnet`, `claude-3.5-haiku`, `managed-claude-haiku`, `managed-gpt`) + legacy webp |
| [`red-team-testing/`](maistro-governance/red-team-testing/) | 5 | `agent-selection`, `test-categories`, `test-results`, `risks`, `recommended-strategies` |
| [`token-insights/`](maistro-governance/token-insights/) | 15 | `total-token-cost`, `llm-cost-ranking`, `cost-per-1k-runs`, `neuralseek-cache-savings`, `cached-token-volume`, `tokens-over-time`, `token-distribution`, `token-direction-mix`, `llm-token-mix`, `input-tokens-per-run`, `generated-tokens-per-run`, `token-generation-per-second`, `total-tokens`, `agent-runs`, `agent-run-ranking` |
| root | 1 | `maistro-logs.png` — the mAIstro log viewer |

### `seek-governance/` — the Seek (RAG/retrieval) governance pane

| Subfolder | Files | What's inside |
|---|---|---|
| [`overview/`](seek-governance/overview/) | 12 | The headline gauges: `semantic-confidence`, `question-resolution`, `prompt-injection`, `prompt-injection-action`, `hate-abuse-profanity-block`, `questions-containing-pii`, `governance-rings`, `category-landscape`, `intent-confidence-distribution`, `intent-semantic-to-kb-relationship`, `top-intent` + legacy webp |
| [`semantic-insights/`](seek-governance/semantic-insights/) | 13 | **The anti-hallucination proof**: `hallucination-bloom`, `top-hallucinated-terms`, `semantic-confidence`, `semantic-quality`, `semantic-distribution`, `top-source-coverage`, `total-coverage`, `longest-source-phrase-in-answer`, `answer-source-jumps`, `answer-source-standard-deviation`, `cache-hit-pct`, `question-resolution`, `total-answer-length` |
| [`configuration-insights/`](seek-governance/configuration-insights/) | 29 | `slide-1` … `slide-29` — the full Configuration Insights walkthrough ("Git for your AI configuration") |
| [`documentation-insights/`](seek-governance/documentation-insights/) | 9 | `knowledgebase-coverage`, `knowledgebase-confidence`, `most-reference-documents`, `most-referenced-urls`, `documentation-flow`, `category-intent-filter-relationships`, `intent-ratings-and-semantic-scores`, `ratings-and-semantic-score-distribution`, `user-ratings` |
| [`intent-insights/`](seek-governance/intent-insights/) | 2 | `coverage-pct`, `confidence-pct` |
| [`model-comparison/`](seek-governance/model-comparison/) | 7 | `new-comparison`, `previous-runs`, `comparison-results`, per-model cards (`claude-4-sonnet`, `claude-3.5-haiku`, `managed-claude-haiku`, `managed-gpt`) |
| [`seek-logs/`](seek-governance/seek-logs/) | 10 | `log-<date>-<time>.png` — individual Replay/audit log entries |
| [`token-insights/`](seek-governance/token-insights/) | 10 | `total-token-cost`, `cost-orbit`, `cost-per-1k-seeks`, `tokens-over-time`, `token-distribution`, `llm-token-intensity`, `input-tokens-per-seek`, `generated-tokens-per-seek`, `filter-landscape`, `total-tokens` |

### Other product surfaces

| Folder | Files | What's inside |
|---|---|---|
| [`maistro-editor/`](maistro-editor/) | 3 | The mAIstro build surface: `flow_seek.png` (seek-node flow), `maistro-agent-editor-slack-databricks-flow.webp` (drag-and-drop editor), `maistro-agent-visualizer-patient-care.webp` (multi-agent visualizer) |
| [`neuralworks/`](neuralworks/) | 5 | NeuralWorks (governed AI notetaker) UI: `neuralworks_call1.png` … `call5.png` — see [`Features/neuralworks-ai-notetaker.md`](../../NeuralSeek%20Knowledge/Features/neuralworks-ai-notetaker.md) |

---

## Conventions

- **kebab-case filenames**, no spaces/colons — every path is URL-safe and Windows-safe.
- The folder path carries the context (`seek-governance/semantic-insights/hallucination-bloom.png` reads as a sentence).
- Full-page captures live ONLY in `full-screen/`; category folders hold component crops.
- When adding new screenshots: full page → `full-screen/<product>-<page>-full.png`; component → `<product>-governance/<page>/<component>.png`; then add a row here.
- Brand rules for using these in deliverables: [`BRAND_RULES.md`](../../BRAND_RULES.md) (RULE 8 catalogs all visual assets). Folder-level map of all of `2026_images/`: [`IMAGE_MAP.md`](../IMAGE_MAP.md).
