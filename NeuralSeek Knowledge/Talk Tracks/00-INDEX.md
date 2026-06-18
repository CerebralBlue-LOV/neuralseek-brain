# Talk Tracks — Index

Nineteen single-thesis talk tracks for NeuralSeek conversations. Each file follows the same shape: **Punchline** (the line itself), **Why this lands** (the mechanism), **NeuralSeek tie-in** (the bridge to product), **Use** (when to deploy it).

Use these when a prompt asks for: a quote, a soundbite, a pitch opener, a CISO line, a board-deck zinger, an objection-handler, a LinkedIn-post lead, or "how do I explain [thing] to a [persona]?"

These are **different from** [`../Knowledge from Calls/06-sales-talk-tracks.md`](../Knowledge%20from%20Calls/06-sales-talk-tracks.md) and [`../Knowledge from Calls/12-punch-line-talk-tracks.md`](../Knowledge%20from%20Calls/12-punch-line-talk-tracks.md) — those are call-derived patterns. The Talk Tracks here are formally curated single-thesis lines validated by a top-tier venture firm's published agentic-AI thesis, designed to be lifted into pitches and posts verbatim.

## By category

### Mental models (the cleanest analogies)

| # | Thesis | Use when… |
|---|---|---|
| [TT-01](TT-01-from-calculator-to-strategist.md) | "Chatbot = calculator. Agent = strategist." | Opening with a non-technical CFO, board member, or new prospect |
| [TT-02](TT-02-the-loop-is-the-agent.md) | "The loop is the agent" (ReAct — perceive/plan/act/observe/repeat) | Whiteboarding "what is an AI agent?" |
| [TT-19](TT-19-docker-for-ai.md) | "NeuralSeek = Docker for AI" — one package bundles the model, your data, and the guardrails; runs the same everywhere | First conversation / mixed room; when you need ONE analogy that works for technical and non-technical at once |

### Why now / macro context

| # | Thesis | Use when… |
|---|---|---|
| [TT-03](TT-03-every-major-computing-paradigm.md) | "Every major computing paradigm looked like a feature before it looked like infrastructure" | Conference keynote opener; LinkedIn lead; board "is AI structural or cyclical?" |
| [TT-04](TT-04-why-now-inference-costs-fell.md) | "Inference costs fell ~1000× in three years" | Any "why now is AI ready for enterprise" pitch |
| [TT-05](TT-05-agents-proliferate-per-workflow.md) | "Agents proliferate per workflow, not per user" | CFO / CTO budget conversations; token-cost-control pitches |
| [TT-06](TT-06-always-on-attack-surface.md) | "An always-on attack surface that never sleeps" (M365 Copilot EchoLeak) | Every CISO / regulated-industry discovery call |

### Where NeuralSeek sits in the market

| # | Thesis | Use when… |
|---|---|---|
| [TT-07](TT-07-as-models-commoditize.md) | "As models commoditize, advantage shifts to whoever coordinates them best" | Every investor / partnership conversation — LLM-agnostic positioning |
| [TT-08](TT-08-whoever-owns-the-workflow.md) | "Whoever owns the workflow owns the value" | Single-line opener slide at the start of any NeuralSeek deck |
| [TT-09](TT-09-the-5-layer-agent-stack.md) | The 5-Layer Agent Stack table — NeuralSeek touches every layer | Sales kit one-pager, investor deck, partnership conversations |
| [TT-10](TT-10-salesforce-consumption-pricing.md) | "Salesforce moved from per-seat to consumption pricing (Headless 360, April 2026)" | Salesforce-aware buyers; channel / VAR partnership conversations |
| [TT-11](TT-11-open-source-coding-layer-parallel.md) | "OpenClaw for coding, NeuralSeek for regulated enterprise" | Technical buyers familiar with the Claude Code / Cursor ecosystem |

### Explaining how NeuralSeek works to non-technical people

| # | Thesis | Use when… |
|---|---|---|
| [TT-12](TT-12-three-pillars-of-agentic-intelligence.md) | "Three Pillars of Agentic Intelligence" (Reasoning / Memory / Knowledge — Greek temple analogy) | Whiteboarding how NeuralSeek's category routing works |
| [TT-13](TT-13-seek-node-agent-harness-compressed.md) | "The seek node = the agent harness, compressed (1 NTL line ≈ 6,000 lines of TypeScript)" | Technical buyer demos, especially after Claude Code / Cursor exposure |
| [TT-14](TT-14-ai-engineer-in-a-box.md) | "An AI engineer in a box" (validated by the $20-sub-burns-$163-of-compute economics) | Buy-vs-build conversations; "you don't need to hire 6 AI engineers" |

### The NeuralSeek POV — why our architecture is correct

| # | Thesis | Use when… |
|---|---|---|
| [TT-15](TT-15-governance-is-architecture.md) | "Governance is a property of the architecture, not the model" — **the watershed quote** | CISO conversations, board presentations, regulatory-defense narratives. THE single line for a slide. |
| [TT-16](TT-16-even-anthropic-cant-get-governance-right.md) | "Even Anthropic can't get governance right" — Claude Code leak, Amazon Q outages, the 250K-failed-API-calls-per-day data | Every regulated-enterprise conversation; LinkedIn posts about competitor failures |
| [TT-17](TT-17-price-per-completed-task.md) | "Price per completed task, not cost per token" | Pricing / TCO conversations; procurement objections about per-token pricing |
| [TT-18](TT-18-companies-that-act-now.md) | "Companies that act now will lead the next stage" | Closing slide of any pitch deck; the "decision urgency" segment |

## Quick selection by audience

| Audience | Lead with | Then |
|---|---|---|
| **CFO / Board** | TT-01 → TT-03 → TT-18 | Pair with [`../ROI_Analysis/D-build-vs-buy-tco.md`](../ROI_Analysis/D-build-vs-buy-tco.md) |
| **CISO** | TT-06 → TT-15 → TT-16 | Pair with [`../Features/neuralseek-governance.md`](../Features/neuralseek-governance.md) |
| **CTO** | TT-02 → TT-09 → TT-13 | Pair with [`../Features/all-ai-tuning-and-guardrails.md`](../Features/all-ai-tuning-and-guardrails.md) |
| **Procurement** | TT-17 → TT-10 → TT-14 | Pair with [`../ROI_Analysis/C-itochu-bakeoff-vs-stack.md`](../ROI_Analysis/C-itochu-bakeoff-vs-stack.md) |
| **Investors** | TT-03 → TT-07 → TT-08 → TT-15 | Pair with [`../NeuralSeek Story/neuralseek-executive-team.md`](../NeuralSeek%20Story/neuralseek-executive-team.md) |
| **Channel / VAR partners** | TT-10 → TT-11 → TT-08 | Pair with [`../Knowledge from Calls/08-pricing-deal-mechanics.md`](../Knowledge%20from%20Calls/08-pricing-deal-mechanics.md) |
| **Technical demo audience** | TT-09 → TT-12 → TT-13 | Pair with the seek-node visual + 118 guardrails listing |
| **Mixed / first-touch room** | TT-19 → TT-01 → TT-08 | Lean on "no vendor lock-in" for the enterprise close |

## Cross-references

- ROI numbers to back these up: [`../ROI_Analysis/00-INDEX.md`](../ROI_Analysis/00-INDEX.md)
- Call-derived versions of similar themes: [`../Knowledge from Calls/06-sales-talk-tracks.md`](../Knowledge%20from%20Calls/06-sales-talk-tracks.md), [`../Knowledge from Calls/12-punch-line-talk-tracks.md`](../Knowledge%20from%20Calls/12-punch-line-talk-tracks.md), [`../Knowledge from Calls/13-cto-ciso-selling-angles.md`](../Knowledge%20from%20Calls/13-cto-ciso-selling-angles.md)
- Guardrail catalog (referenced in TT-09, TT-16): [`../Features/neuralseek_118_ai_guardrails_listing.md`](../Features/neuralseek_118_ai_guardrails_listing.md)
- Voice & tone replication: [`../Knowledge from Calls/10-lawrence-voice-and-tone.md`](../Knowledge%20from%20Calls/10-lawrence-voice-and-tone.md)
