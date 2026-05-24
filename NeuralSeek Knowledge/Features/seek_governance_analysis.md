# NeuralSeek Seek Governance — Analysis

**Scope:** LLM-level governance (the 9 modules visible under "Seek Governance" in the side nav).
**What it is, end-to-end:** A full AI observability + audit stack — what most vendors sell as a separate paid add-on (Arize, LangSmith, Datadog LLM Observability, W&B Traces) — shipped in the box.

---

## OVERALL POSITIONING

Reframe the entire feature set under one umbrella phrase: **"AI Visibility & Governance."**

Three sub-stories live underneath:

1. **Live AI Health Monitoring** — real-time KPI gauges on confidence, coverage, prompt injection, PII, profanity, cost. The "single pane of glass" for AI ops.
2. **Forensic Traceability** — every question, every answer, every config change, every model decision logged, timestamped, attributable, exportable.
3. **Continuous Optimization** — side-by-side model bake-offs, per-intent and per-document drill-downs, hallucination forensics with one-click remediation.

This is the rare AI platform that lets a CISO, a finance lead, an AI engineer, and a content owner all open the same product and find what they need.

---

## MODULE-BY-MODULE ANALYSIS

### 1. Overview — The Health Dashboard

**What's on screen:** 6 large semicircular gauges showing min/avg/max across:
- Semantic Confidence (1% → 31.2% → 100%)
- Question Resolution (0% → 100%) — answered vs. min-confidence-suppressed
- Prompt Injection score
- Hate, Abuse, Profanity Block %
- Prompt Injection Action (Block / Remove / No Action distribution)
- Questions containing PII
Plus a **Top Intents bubble chart** (avg semantic score × avg KB confidence × frequency).

**What it really is:** A single-pane health monitor that shows in 4 seconds whether the AI deployment is healthy. The min/avg/max bands are a sophisticated touch — they show distribution, not just averages, which is what mature observability looks like.

**Buyer story:** "Open the page. See if your AI is healthy. Right now."

**Underplayed angle:** The min/avg/max banding is genuinely better than what most observability tools show by default. Worth calling out as "distribution-aware monitoring."

---

### 2. Semantic Insights — Anti-Hallucination Forensics

**What's on screen:** 9 gauges:
- Semantic Confidence
- Question Resolution
- Longest Source Phrase in Answer (46/244)
- Top Source Coverage (32.5% / 70% / 100%)
- Total Coverage
- Total Answer Length (36 → 196 → 633 words)
- Answer Source Standard Deviation (0 / 41.3 / 232) — how spread across sources
- Answer Source Jumps (3.2 avg, 24 max)
- Cache Hit % (Cached / Edited / Uncached split)

Plus a **Top Hallucinated Terms** pie chart, with click-to-allowlist functionality.

**What it really is:** This is the deepest hallucination forensics view I've seen in a commercial AI platform. The "Answer Source Jumps" and "Answer Source Standard Deviation" metrics literally show you whether the LLM is stitching answers across too many sources — which is when hallucinations creep in. And the "Top Hallucinated Terms" with click-to-allowlist is a closed-loop remediation workflow.

**Buyer story:** "Watch hallucination happen in real time. Click to fix it."

**Underplayed angle:** The click-to-allowlist hallucinated terms is a closed-loop remediation feature. Most platforms show you the problem; this one fixes it with a click. Worth elevating heavily.

---

### 3. Documentation Insights — Content Performance

**What's on screen:**
- KnowledgeBase Confidence (0% / 9% / 19%)
- KnowledgeBase Coverage (67% / 97% / 100%)
- **Most Referenced Documents** pie (top 6 docs with %)
- **Most Referenced URLs** pie

**What it really is:** Per-document analytics — which docs are actually answering customer questions, which are dead weight. This is gold for content owners and knowledge managers.

**Buyer story:** "Stop guessing which docs matter. See which docs are answering your questions."

**Underplayed angle:** This is also a content-ROI tool. You can argue that NeuralSeek shows the business value of every piece of documentation. Useful for content-team budget justification.

---

### 4. Intent Insights — Per-Intent Drill-Down

**What's on screen:** A lookback-period slider (1–30 days) and two parallel ridge-plot columns:
- Coverage (%) per intent
- Confidence (%) per intent

Sorted descending by frequency. ~30 intents visible, each with a smooth distribution curve.

**What it really is:** Per-intent performance distributions over time. The ridge plot is a sophisticated viz choice — it shows distribution shape, not just averages. You can see intents that are bimodal (sometimes great, sometimes terrible) which is what you need to fix.

**Buyer story:** "Drill into any intent. See exactly where your AI struggles."

**Underplayed angle:** Ridge plots over a 30-day window means you can spot regressions. This is essentially **AI performance drift detection** at the intent level. That phrase ("drift detection") is hot in 2026 buyer vocabulary.

---

### 5. Token Insights — Operational Telemetry

**What's on screen:** 6 gauges:
- Total Tokens (29.97M total, 1.96M generated of 31,929K)
- Total Token Cost ($0.00 — managed tier, real customer would show real $)
- Input Tokens per Seek (2 / 17094.2 / 36396)
- Generated Tokens per Seek (40 / 1120 / 3183)
- Cost per 1k Seeks
- Token Generation per Second (0.3 / 2.2 / 15.9)

Plus a **Tokens over Time** area chart split by model (Managed Claude Haiku Input/Generated visible).

**What it really is:** Operational telemetry. Throughput, capacity, cost per unit. The token-generation-per-second metric especially is unusual — most platforms don't expose throughput.

**Buyer story:** "Track every token. Know your unit economics."

**Underplayed angle:** Tokens-per-second is a latency/throughput proxy. Combined with cost-per-1k-seeks, this is the data a CFO needs to model unit economics. Sell this to finance.

---

### 6. Cost Insights — Model Cost Comparison

**What's on screen:** A massive horizontal bar chart ranking model cost across ~200+ specific model variants — gpt-5.5-pro (azure), Claude 4.7 Opus, Claude 4.6 Sonnet, o3-deep-research, GPT-4o, etc. Each row shows actual relative cost.

**What it really is:** A model cost benchmark across every model the customer can connect. Live, real-data ranking.

**Buyer story:** "See exactly what each model costs you. Decide where to spend."

**Underplayed angle:** The chart shows **200+ specific model variants** — a number worth elevating. Combined with the 9 providers from earlier, this becomes "200+ model variants, 9 providers, live cost data." That's a procurement story.

---

### 7. Seek Logs — Forensic Audit Trail

**What's on screen:** A tabular log with columns:
- Date (2026-05-10 22:20:27)
- Session (MC41-MTU3-OTQ3)
- Question (full text)
- Answer (full LLM response)
- Intent (FAQ-Complete_List_Supported_LLM_Providers)
- Category
- Score (%)
- Latency (ms)

Plus filter + search.

**What it really is:** Transaction-level audit log of every question and answer the AI handled, with the full metadata trail attached. Sortable, searchable, filterable. This is the SIEM-level visibility that compliance teams demand.

**Buyer story:** "Every conversation. Every answer. Every metric. Searchable."

**Underplayed angle:** Combined with the export-to-S3/Splunk/Datadog/SIEM capability from the Audit & Compliance guardrails, this becomes the **complete forensic record** for any AI-driven decision. For regulated sectors, this is a hard requirement, not a nice-to-have.

---

### 8. Model Comparison — Built-In LLM Bake-Off

**What's on screen:** "Seek LLM Comparison" UI — pick any number of configured models (showing Managed GPT, Managed GPT-4o, Claude Opus, Sonnet, Haiku, Translate), enter a question, run side-by-side. Results table shows Model, Provider, Response Time (ms), Semantic Score, LLM Rank.

**What it really is:** The LLM bake-off as a first-class governance feature, not a buried admin tool. Lives right next to the dashboards, accessible to anyone with governance permissions.

**Buyer story:** "Test models head-to-head before you commit."

**Underplayed angle:** The fact that this is a **persistent governance feature** (with "Previous Runs" tab) rather than a one-off testing tool means decisions are archived for procurement and audit. This is rare.

---

### 9. Configuration Insights — Git-for-AI-Configs

**What's on screen:** A version-comparison diff view ("CHANGES IN THIS VERSION:") showing red/green redlines on JSON config (apikey, charCount, elasticSchema, kbCacheTimeout, link, maxDocs, projectId, serviceUrl), with attribution to `lawrence@neuralseek.com` and timestamp range (7:38:31 PM MAY 9, 2026 – 4:01:51 PM MAY 10, 2026). Bottom shows a timeline scrubber across versions.

**What it really is:** **Git-style version control for AI configuration**, with diffs, timestamps, and user attribution. This is huge for enterprise change management, audit, and compliance.

**Buyer story:** "Every config change. Versioned. Attributable. Diffable. Rewindable."

**Underplayed angle:** This is one of your strongest enterprise features and the screenshot is the only one without an obvious headline metric. It deserves its own marketing moment. **"Git for your AI configuration"** is the headline.

---

## CROSS-CUTTING THEMES

### Theme A: Distribution-Aware Monitoring
Most gauges show **min / average / max** — not just averages. Mature observability. Worth a callout: "We don't hide the tails — we surface them."

### Theme B: Closed-Loop Remediation
The "click hallucinated term to allowlist it" pattern is closed-loop. So is "tag a doc with a re-sort value." These aren't just dashboards — they're **dashboards that fix problems in one click**.

### Theme C: Full Forensic Stack
Seek Logs + Configuration Insights + Audit & Compliance Guardrails = full forensic record. Every question, every answer, every config change. Versioned. Attributable. Exportable. This is the SIEM-grade audit story.

### Theme D: Distribution Drill-Down
Almost every aggregate metric has a per-intent or per-document drill-down. The ridge plots in Intent Insights are a great example. "Aggregate to anomaly to action in three clicks" is the pattern.

### Theme E: Live Cost & Throughput Telemetry
Token-level cost, per-1k-seek cost, tokens-per-second, cost ranking across 200+ models — this is FinOps for AI, built in. CFO-grade unit economics.

---

## DRAFT HEADLINE STATS (for the eventual page)

| Stat | Number / Source |
|---|---|
| Live governance modules | **9** (Overview, Semantic, Documentation, Intent, Token, Cost, Seek Logs, Model Comparison, Configuration) |
| KPI metrics surfaced live | **35+** distinct gauges/charts across modules |
| Model variants benchmarked | **200+** (from the Cost Insights chart) |
| Configurable lookback window | **1–30 days** (Intent Insights slider) |
| Audit attribution coverage | **100%** — every config change tied to a named user with timestamp |
| Export destinations | **S3, Splunk, Datadog, SIEM** (syslog/CEF/JSON) |
| Closed-loop remediation paths | At least **3** (hallucinated term allowlist, re-sort tagging, intent curation) |

---

## RECOMMENDED PAGE STRUCTURE (when we get there)

A possible page layout for the **AI Visibility & Governance** page, anchored on Seek Governance for now:

1. **Hero** — "AI Visibility, Built In. Not Bolted On." with stat strip (9 governance modules, 35+ live metrics, 200+ models tracked, 100% audit coverage)
2. **The Three Pillars** — Live Monitoring · Forensic Traceability · Continuous Optimization
3. **Module 1 — The Health Dashboard** (Overview screenshot, framed as "the 4-second check-in")
4. **Module 2 — Hallucination Forensics** (Semantic Insights, framed around the click-to-allowlist story)
5. **Module 3 — Content Performance** (Documentation Insights, framed as "the ROI of your KB")
6. **Module 4 — Per-Intent Drift Detection** (Intent Insights ridge plots, framed as "AI drift detection")
7. **Module 5 — FinOps for AI** (Token + Cost Insights, framed for finance buyers)
8. **Module 6 — The Forensic Record** (Seek Logs, framed as SIEM-grade)
9. **Module 7 — Built-In LLM Bake-Off** (Model Comparison, framed as "no procurement guesswork")
10. **Module 8 — Git for AI Configuration** (Configuration Insights — this is the closer)
11. **CTA strip** — "Open the dashboard your CISO has been asking for"

---

## DIFFERENTIATORS WORTH PROTECTING

Things on these screens that I don't think competitors have:

1. **Click-to-allowlist hallucinated terms** — closed-loop remediation from a dashboard.
2. **Configuration diff view with user attribution** — Git-for-configs is rare in AI platforms.
3. **Ridge-plot distributions per intent** — most platforms show averages; this shows shape.
4. **Answer Source Jumps + Source Standard Deviation** — these are very advanced hallucination-leading-indicator metrics.
5. **200+ model cost benchmark in live customer data** — not a static comparison page; uses the customer's actual usage.
6. **Top Hallucinated Terms surfaced by source domain** (Knowledge Repository vs. Configure vs. Mistral vs. Anthropic) — that's hallucination provenance.

---

## OPEN QUESTIONS BEFORE WE BUILD THE PAGE

1. **mAIstro Governance** — you mentioned this as the other half. Do you want me to do the same analysis for those modules (Flow Insights, Red Team Testing, mAIstro Logs, Token Insights, Cost Insights, Model Comparison) next?
2. **Naming the umbrella** — "AI Visibility & Governance" or "AI Observability & Audit" or just "AI Governance"? Each pulls a slightly different buyer.
3. **Counting** — do you want a defensible number like "35+ live governance metrics" alongside the "112 AI Guardrails" number we settled on? They'd pair well as twin pillars.
4. **The Configuration Insights screenshot** — that one's the strongest enterprise story but the screenshot is the messiest. Want me to mock up a cleaner version for the page?
5. **Industry benchmarks** — do you have any internal benchmarks (avg time-to-detect-drift, % of hallucinations caught, etc.) we could quote? Those would make the visibility story concrete.
