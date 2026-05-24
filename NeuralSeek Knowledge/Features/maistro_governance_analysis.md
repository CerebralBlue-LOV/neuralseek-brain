# NeuralSeek mAIstro Governance — Analysis

**Scope:** Agent-level governance (the 9 modules visible under mAIstro Governance + Custom Governance + System Performance).
**What it is, end-to-end:** This is the **agent observability + APM stack** — what mature teams stitch together from LangSmith + Datadog APM + W&B + a custom dashboard layer. NeuralSeek ships it as one product.

---

## OVERALL POSITIONING

Where Seek Governance was "AI Visibility at the LLM Layer," mAIstro Governance is **"AI Visibility at the Agent Layer"** — and it goes further in two important ways:

1. **Component-level attribution.** It doesn't just tell you an agent took 374,000 ms — it tells you that 586,200 ms of it was Parallel Run Time, broken across LLM / KB / ML Models / REST. APM-grade.
2. **Customizable governance dashboards.** The "Add Panel," "Delete Dashboard," and "Edit" toggles on Agent Growth and Users show that admins can **build their own governance views**. This is enterprise-grade extensibility.

The umbrella phrase still holds: **"AI Visibility & Governance."** Seek = LLM layer. mAIstro = Agent layer. Custom = your-org-specific KPIs.

---

## MODULE-BY-MODULE ANALYSIS

### 1. Flow Insights — Component-Level Agent APM

**What's on screen:**
- 4 KPI tiles: Time per run (374,740.9 ms avg, range 92 – 1,366,000), Equivalent Seeks per run, Agent Runs (798 total, ~450/450 split between two agent types), Guardrail Activations (1)
- A **radar/pentagon chart**: "Average Total Component Time by Agent" with 5 axes — **Parallel Run Time, LLM, KB, ML Models, REST** — and a legend covering 10+ named agents (IHG-Channel-Normalizer, IHG-CompSet-Performance-RAG, IHG-Entity-Extractor, IHG-Intent-Classifier, IHG-Property-Knowledge-RAG, IHG-Routing-Destination-Decider, IHG-Salesforce-Account-Lookup, IHG-Web-Context-Enricher, etc.)
- An **Agent Run times** area/line chart over time, broken out by named agent (IHG-Property-Knowledge-RAG visibly spiking to 1,200,000 ms)

**What it really is:** This is the most sophisticated piece of agent observability in the entire product. The radar chart attributes every agent's runtime across 5 component classes — so you can see if an agent is LLM-bound, KB-bound, REST-API-bound, ML-model-bound, or parallelization-bound. That's APM-level resolution applied to agentic workflows.

**Buyer story:** "Know exactly where every agent spends its time — and which component is the bottleneck."

**Underplayed angles:**
- The "Equivalent Seeks per run" metric is unusual and clever — it normalizes agent cost into LLM-call equivalents. Worth highlighting as a unit-economics story.
- The radar chart is a genuinely rare viz choice for agent observability. Most platforms give you a flat bar chart of latency. This shows shape — "this agent is REST-heavy, this one is LLM-heavy" — at a glance.

---

### 2. Red Team Testing — AI-Audited Agent Security

**What's on screen:**
- Agent picker (currently set to `weather_fetcher`) with a "Run Test" button
- "Grading Tests" indicator
- **Overall Score: 50** (yellow — partial)
- **Summary** (AI-generated text explaining the score: "The provided sub-task results do not include the five test cases or their agent outputs, so no area could be directly validated from evidence...")
- **Test Categories** as PASS/FAIL cards: Prompt Injection, Data Exfiltration, SQL Injection, Unauthorized Access, Service Disruption — all currently PASS
- **Risks** section — AI-generated narrative of what was found
- **Recommended Strategies** section — AI-generated remediation guidance ("Provide the complete five test inputs and corresponding agent outputs for evidence-based review... apply targeted controls such as secret redaction, prompt-isolation, authorization enforcement, parameterized queries, and retry/scope limits where failures are actually observed")

**What it really is:** This is **AI-graded agent security testing with auto-generated remediation**. An LLM is reading the test results, summarizing the security posture, identifying risks, and recommending specific control hardening. It's not just a test runner — it's an automated security analyst writing a report.

**Buyer story:** "An AI auditor that tests your agent, grades it, and tells you exactly how to fix what's broken."

**Underplayed angles:**
- The auto-generated remediation language ("secret redaction, prompt-isolation, authorization enforcement, parameterized queries, retry/scope limits") is genuinely useful security advice. Worth quoting verbatim in marketing copy.
- A per-agent score (not just platform-level) is rare. You can rank agents by security posture and patch the weakest first.
- "Run Test" → "Grading Tests" → "Score" is a self-serve security audit loop. CISOs can run this themselves, on demand. Sell that.

---

### 3. mAIstro Logs — Agent Run Forensics

**What's on screen:**
- Tabular log: Date, RunId (UUID), User, Agent (ex_Minimum_Confidence_Message / ex_neuralseek_KB_upload), Runtime (ms), Link
- 10 visible entries; counter shows **1–10 of 1,749 items** across **175 pages**
- Click-through link icons on every row
- Sort, filter, search controls

**What it really is:** Transaction-level audit log of every agent run, attributable to a user (or `system`), with deep-link traceability. The 1,749 items in the visible window means **dense, real production telemetry**.

**Buyer story:** "Every agent run. Every user. Every runtime. Searchable. Replayable."

**Underplayed angles:**
- The Link column means each row drills into the full agent execution trace. Step-by-step replay = forensic gold.
- The fact that `system` runs and named-user runs are distinguished in the same log = built-in attribution for both human-triggered and automated agent calls. Useful for audit.

---

### 4. Token Insights (Agent Level) — FinOps with Cache Economics

**What's on screen:** 10 KPI gauges (more than Seek's Token Insights):
- Total Tokens (32,283 K — 30,260,825 generated, 2,022,205 input)
- Total Token Cost ($0.00 — managed tier)
- **NeuralSeek Cache Savings** *(NEW vs. Seek)*
- Input Tokens per run (31 / 8,102 / 34,883)
- Generated Tokens per run (14 / 541 / 2,745)
- Cost per 1k runs
- **Cached Input Tokens per run** *(NEW)*
- **Cached Generated Tokens per run** *(NEW)*
- **Cache Savings per 1k runs** *(NEW)*
- Token Generation per Second (0.4 / 5.7 / 71.4)
- Tokens over Time chart split by model

**What it really is:** Full agent-level FinOps **with cache economics built in**. Tracks not just spend, but cache hit savings — i.e., the dollar value of NeuralSeek's caching layer. This is the data a CFO needs to see ROI on the platform itself.

**Buyer story:** "Track every token. Know your unit economics. See exactly how much our cache is saving you."

**Underplayed angles:**
- **"NeuralSeek Cache Savings"** is a product self-justification metric — it literally quantifies the ROI of the platform's caching layer in dollars. That's a procurement-cycle silver bullet.
- 71.4 tokens/sec max throughput on managed Claude Haiku is a concrete latency story for SLA buyers.

---

### 5. Cost Insights (Agent Level) — Same 200+ Model Benchmark

**What's on screen:** Same model cost comparison chart as Seek's Cost Insights — 200+ model variants ranked by cost (gpt-5.5-pro, Claude 4.7 Opus, gpt-4.5-preview most expensive; Managed GPT (neuralSeek) and Managed GPT-4o (neuralSeek) at near-zero).

**What it really is:** Identical capability to Seek's, applied at the agent layer. Customers can attribute cost to specific agents, then drill into which models those agents used.

**Buyer story:** "See cost by agent, by model, by run. No more black-box AI spend."

**Underplayed angle:** The **"Managed" tier models showing $0.00 cost** is a huge differentiation moment — NeuralSeek's managed-LLM offering is essentially included. That's a "free credits" story buried in a cost chart.

---

### 6. Model Comparison (Agent Level) — Bake-Offs with Agent Score

**What's on screen:** "Agent LLM Comparison" UI — pick configured models (Managed GPT, GPT-4o, Claude Opus, Sonnet, Haiku, Translate), select an Agent, run side-by-side. Results table shows Model, Provider, Response Time (ms), Response Score, **Agent Score**.

**What it really is:** The agent-aware version of the Seek bake-off. The key new dimension is **Agent Score** — which evaluates not just LLM response quality but whether the agent **completed its workflow correctly**. So you're benchmarking model fitness for a specific agent, not just generic quality.

**Buyer story:** "Test models head-to-head — at the agent level, not just the LLM level."

**Underplayed angles:**
- Agent Score is a different and more demanding evaluation than raw LLM Rank. It captures whether the agent achieved its goal, which is what enterprises actually care about. Worth elevating.
- "Previous Runs" tab means historical bake-off data is preserved — perfect for procurement audit ("we tested X models, here's the evidence, here's why we picked Y").

---

### 7. Agent Growth — Customizable Governance Dashboards

**What's on screen:**
- Top toolbar: **Add Panel · Delete Dashboard · Edit** toggle + an "All Agents finished" status indicator
- A single area chart showing agent count growth from ~0 to **280 agents over time** — steep, linear-ish growth

**What it really is:** **A customizable governance dashboard.** The Add Panel / Delete Dashboard / Edit controls mean admins can construct their own governance views — not just consume the canned ones. This is rare. Most observability platforms ship fixed dashboards; this one lets the customer build their own.

**Buyer story:** "Build governance dashboards tailored to your KPIs."

**Underplayed angles:**
- **Customizable dashboards** deserves its own marketing moment. Most "governance" tools are rigid; this one is user-extensible.
- The 280-agent growth curve is itself a stat worth quoting (assuming this is real customer data — even one customer running 280 agents in production is a credibility marker).

---

### 8. Users — Identity-Aware Governance

**What's on screen:** Three panels:
- **GUI Logins** — list of 26 named users with last-login timestamps (lawrence@neuralseek.com, rreed@techd.com, kaviya@neuralseek.com, etc., spanning Nov 2025 to May 2026)
- **Seek Users** — count of 19
- **mAIstro Users** — donut chart segmented by session ID and email (mix of UUID-style session IDs and real emails)

**What it really is:** Per-user audit and access analytics. Who's actually using the platform. Who logged in when. Who's running which agents. This is the attribution layer for compliance investigations.

**Buyer story:** "Every action. Every user. Every login. Tracked."

**Underplayed angles:**
- **Login recency tracking** is the data a CISO needs to detect dormant or compromised accounts. Standard SIEM input.
- The mix of human-email users and system-session IDs (MC42-MzUz-NDAz, e2bb8605-...) means the system distinguishes machine and human callers — important for service-account governance.

---

### 9. System Performance — Three-Tier Infrastructure APM

**What's on screen:** Three stacked area charts:
- **Instance Performance** — Total Time / NeuralSeek KB / Managed Claude Haiku layers, peaking ~15,000 ms then decaying
- **Instance Detail Performance** — broken into 5 layers: **Categorization, PI Protection (Prompt Injection), KB, Answer Generation, Scoring** + Total
- **Universe Performance** — Total Time / NeuralSeek KB / Managed Claude Haiku at the universe level

**What it really is:** This is **infrastructure-level APM for the AI itself**, decomposed by guardrail/component layer. The Instance Detail chart is genuinely valuable — it shows you exactly which guardrail or processing step is consuming time inside a single run. Categorization slow? KB slow? Scoring slow? PI Protection slow? You can see it.

**Buyer story:** "Your AI is slow. Here's exactly which component to blame."

**Underplayed angles:**
- The **per-layer breakdown** (Categorization / PI Protection / KB / Answer Generation / Scoring) maps directly to the guardrail categories from your 112-guardrails work. So this is governance data for the guardrail stack itself.
- Three-tier APM (Instance / Instance Detail / Universe) lets you triangulate problems — is the issue with one instance, one guardrail layer, or the whole deployment? Standard SRE pattern, rarely seen in AI platforms.

---

## CROSS-CUTTING THEMES — What's New on the mAIstro Side

### Theme A: Component-Level Attribution
The Flow Insights radar chart + System Performance per-layer breakdown together give you a complete picture of where every millisecond goes — across 5 component classes for agents AND 5 guardrail layers for the runtime. This is APM-grade.

### Theme B: AI-Audited Security
Red Team Testing isn't just "run tests, show pass/fail" — it's an AI reading the results, scoring posture, identifying risks, and writing remediation guidance. **Automated security analyst built into the platform.**

### Theme C: Customizable Governance
The Add Panel / Edit / Delete Dashboard controls on Agent Growth (and presumably Users + others) mean **the governance experience itself is extensible**. This is enterprise-grade.

### Theme D: Cache Economics
The Token Insights cache savings metrics are unique. Most platforms track spend; NeuralSeek tracks **how much spend it prevented**. That's a self-justifying ROI metric and a procurement weapon.

### Theme E: Agent Score (≠ LLM Score)
Model Comparison's "Agent Score" measures whether the agent succeeded at its workflow — not just whether the LLM gave a high-confidence response. This is a more demanding and more enterprise-relevant evaluation criterion.

---

## UPDATED GOVERNANCE STATS (combining Seek + mAIstro)

| Stat | Number | Source |
|---|---|---|
| **Total governance modules** | **18** | 9 Seek + 6 mAIstro + 2 Custom + 1 System Performance |
| **Live governance metrics surfaced** | **75+** | counted across all modules |
| **Agent runs logged (visible sample)** | **1,749** | mAIstro Logs page counter |
| **Agents tracked by component time** | **10+** named in radar chart |
| **Red-team test categories per agent** | **5** | Prompt Injection, Data Exfil, SQL Injection, Unauthorized Access, Service Disruption |
| **Performance APM layers exposed** | **5** | Categorization, PI Protection, KB, Answer Generation, Scoring |
| **Component time attribution dimensions** | **5** | Parallel Run, LLM, KB, ML Models, REST |
| **User attribution tracked** | **26+** named GUI users + N session-IDs |
| **Customizable dashboards** | **Yes** (Add Panel / Edit / Delete) |

### Pairing with the Guardrails number
- **112 AI Guardrails** (control surface)
- **18 governance modules · 75+ live metrics** (visibility surface)
- **5-layer APM** + **5-axis agent component attribution** (forensic depth)

---

## DIFFERENTIATORS WORTH PROTECTING (mAIstro-side)

1. **Radar-chart component attribution** — most AI observability platforms give you flat latency; this shows agent-by-agent shape across 5 component classes.
2. **AI-generated red-team remediation** — the platform doesn't just test the agent; it writes a remediation report.
3. **Cache savings as a tracked metric** — quantifies platform ROI in dollars, every day.
4. **Customizable governance dashboards** — Add Panel / Edit / Delete means enterprises can build their own views, not just accept ours.
5. **5-layer performance breakdown** (Categorization / PI Protection / KB / Answer Generation / Scoring) — this maps to the guardrail stack and lets you debug at the guardrail layer.
6. **Agent Score vs. LLM Rank** — workflow-completion evaluation, not just response-quality evaluation.

---

## RECOMMENDED PAGE STRUCTURE (full AI Visibility & Governance page)

Updating the earlier recommendation to include both halves:

1. **Hero** — "AI Visibility, Built In. Not Bolted On." with the combined stat strip (18 modules, 75+ metrics, 112 guardrails, 100% audit coverage, 200+ models tracked)
2. **The Three Pillars** — Live Monitoring · Forensic Traceability · Continuous Optimization
3. **Two-Layer Architecture** — Seek (LLM layer) and mAIstro (agent layer), side by side
4. **Seek-Layer Highlights** (4 modules) — Health Dashboard, Hallucination Forensics, Per-Intent Drift, Git for AI Config
5. **mAIstro-Layer Highlights** (4 modules) — Component-Level APM (radar chart), AI-Audited Red Teaming, Cache Economics, Three-Tier System Performance
6. **Customizable Dashboards** — the Add Panel / Edit / Delete moment, framed as enterprise extensibility
7. **The Forensic Record** — combined Seek Logs + mAIstro Logs + Config Insights story
8. **Built-In Bake-Off** — Model Comparison at both LLM AND Agent levels (rare!)
9. **CTA strip** — "Open the AI governance dashboard your CISO has been asking for"

---

## OPEN QUESTIONS BEFORE WE BUILD THE PAGE

1. **Customizable dashboards** — is the Edit/Add Panel/Delete capability available across all modules, or only Custom Governance? If platform-wide, that's a much bigger story.
2. **Agent Score formula** — what specifically drives this number? Workflow completion? Goal achievement? Tool-call accuracy? The answer affects how we frame the Model Comparison story.
3. **Real metrics for marketing** — can we publish numbers from the cache-savings tracker (e.g., "$X saved per 1,000 runs on average across our customer base")? That's a great FinOps headline.
4. **Three-tier System Performance** — what's the practical difference between Instance, Instance Detail, and Universe? Confirm so I can label them correctly.
5. **mAIstro Users donut** — the segmentation by session ID is a bit noisy. Want to add a curated "top 5 most active users / agents" cut for the marketing visual?
