# D. Build-vs-Buy TCO — Anchored to 5 AI Use Cases

*Generalizing the Great Day Improvements "$3K / month vs. millions" line.*

## What you'd have to build to match NeuralSeek

To match what NeuralSeek bundles as a single platform, an enterprise would need to build the following stack of AI capabilities **before** they can ship a single business use case on top of it:

| Capability | Build complexity |
|---|---|
| LLM flexibility + dynamic LLM routing | High |
| 118 AI guardrails | Very high |
| Governance pane (UI + audit + replay) | High |
| 100+ enterprise app integrations + custom API connector framework | High |
| Workflow visualizer | Medium |
| Containerization for on-prem deployment | Medium |
| Caching system + token-cost optimization | Medium |
| Token-cost monitoring | Low |
| **Proprietary semantic-lineage anti-hallucination model** (the moat — customers have repeatedly tried and failed to recreate it) | Very high |
| PII detection + redaction | Medium |
| Prompt-injection detection + redaction | Medium |
| Vector DB connectivity | Low |
| Tunable RAG pipelines | High |

## Realistic build estimate

**12 full-time US AI engineers, working on this exclusively for one full year.**

- **$3.6M** to build the underlying platform (12 engineers × $300K fully-loaded per Levels.fyi 2025)
- **+ ~$1M / year** ongoing platform maintenance
- **+ 12 months** of time before a single use case ships

## The three paths to 5 AI use cases (3-year TCO)

**The unit of comparison is 5 production AI use cases** — the same scope Children's Health has on contract today (HIPAA chatbot, clinical policy chat, OCR for referral packets, cohort analytics, and call analytics for distress signals).

| Path | What it really means | Year 1 | Year 2 | Year 3 | 3-Year TCO for 5 use cases |
|---|---|---|---|---|---|
| **Build the platform yourself, then build 5 use cases on top** | 12-AI-engineer team for 12 months building the platform first ($3.6M), then 5 use-case builds at ~$300K each ($1.5M), plus ongoing maintenance and new-use-case dev | $5.1M | $1.5M | $1.5M | **~$8.1M** (and the business waits 12+ months for the *first* use case to ship) |
| **Best-of-breed vendor stack** — buy a separate point product for every layer (one for LLM observability, one for SIEM/audit, one for hallucination detection, one for container governance, one for workflow orchestration), then pay an internal integration team to wire all of them together for *every new use case* | ~$1.2M / yr in vendor licenses + ~$900K / yr for a 3-engineer integration team to keep the stack working and onboard each new use case | $2.1M | $2.1M | $2.1M | **~$6.3M** (and you own the integration debt forever) |
| **NeuralSeek** | Unlimited-container NeuralSeek license + Forward Deployed Engineer model — same platform delivers all 5 use cases with no marginal platform cost per additional use case | **$200K unlimited-container NeuralSeek + $200K FDE = $400K** | $400K | $400K | **~$1.2M** |

## Promo headlines (pick one)

> *"Five production AI use cases. Three paths. $8M vs. $6M vs. $1.2M over three years. The difference is whether you're paying to build infrastructure — or paying to ship outcomes."*

> *"Most enterprises spend a year and 12 AI engineers building what NeuralSeek hands you on day one — for $400K a year, unlimited containers, every use case included."*

## Sources

- [Levels.fyi — AI Engineer Compensation Trends Q3 2025](https://www.levels.fyi/blog/ai-engineer-compensation-trends-q3-2025.html)
- Children's Health 5-use-case scope: [NeuralSeek Knowledge / Client Stories / childrens-health.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Client%20Stories/childrens-health.md)
- Great Day Improvements pricing reference: [NeuralSeek Knowledge / Client Stories / great-day-improvements.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Client%20Stories/great-day-improvements.md)
