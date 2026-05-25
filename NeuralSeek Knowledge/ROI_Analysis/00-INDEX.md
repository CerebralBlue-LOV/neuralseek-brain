# ROI Analysis — Index

Defensible, source-cited ROI and TCO numbers for NeuralSeek. Use these whenever a prompt asks about:

- **Time to production** ("how fast can NeuralSeek ship?", "how long does deployment take?")
- **Cost savings** (analyst productivity, $-per-report, headcount-equivalents)
- **Build-vs-buy** ("should we build this ourselves?", "what's the TCO?")
- **Competitive math** vs. N8N, AlphaSense, S&P Capital IQ, point-tool stacks, DIY platforms
- **Guardrails volume** ("how many things does NeuralSeek actually catch?")

All figures are triangulated from public benchmarks (BLS, Glassdoor, Robert Half, Levels.fyi, Vendr, Costbench) and direct customer-engagement records. Original sources are linked in each file.

## When to retrieve which file

| File | Pull this when the prompt is about… | Headline number |
|---|---|---|
| [A-days-to-mvp.md](A-days-to-mvp.md) | Time-to-production speed, deployment timelines, "weeks not quarters" framing, MVP rollouts | **2–15 weeks** to production across 5 named customers |
| [B-itochu-analyst-roi.md](B-itochu-analyst-roi.md) | Analyst productivity ROI, $-per-report, knowledge-worker time savings, Itochu story | **3 weeks → 13 minutes** across 500 analysts (~$10.5M/yr conservative) |
| [C-itochu-bakeoff-vs-stack.md](C-itochu-bakeoff-vs-stack.md) | Competing vs. N8N, point-tool stacks, "build a stack of 5 tools" arguments. Tony Chang's quote. AlphaSense / S&P Capital IQ replacement | **$2.07M assembled stack → $240K NeuralSeek** (~$1.83M/yr saved) |
| [D-build-vs-buy-tco.md](D-build-vs-buy-tco.md) | Build-vs-buy decisions, 3-year TCO, "we have an internal AI team" objection, 12-engineer build estimate | **$8.1M build / $6.3M best-of-breed / $1.2M NeuralSeek** over 3 years for 5 use cases |
| [E-guardrails-in-action.md](E-guardrails-in-action.md) | Guardrail volume, "what does NeuralSeek actually catch?", PII/PHI redaction proof, semantic-grounding interventions | **~5,000 grounding interventions + ~10,000 PII redactions / mo** at Itochu (illustrative model) |

## Guardrails on usage

- File **E is an illustrative model**, not customer telemetry. Label any number lifted from it as "modeled estimate based on portfolio averages" and confirm with the customer before attributing to them publicly.
- File **A** uses anonymized copy for NatWest ("a UK retail bank serving millions") until marketing approval changes. Other names are cleared.
- All $ figures in B, C, D are conservative defaults — aggressive variants are documented inside each file if a more aggressive framing is needed.
- Always link the source row in any deck or slide that cites these numbers.

## Cross-references

- Source case studies: [`../Client Stories/itochu.md`](../Client%20Stories/itochu.md), [`../Client Stories/childrens-health.md`](../Client%20Stories/childrens-health.md), [`../Client Stories/great-day-improvements.md`](../Client%20Stories/great-day-improvements.md), [`../Client Stories/NatWest.md`](../Client%20Stories/NatWest.md), [`../Client Stories/Clip.md`](../Client%20Stories/Clip.md)
- Guardrail catalog: [`../Features/neuralseek_118_ai_guardrails_listing.md`](../Features/neuralseek_118_ai_guardrails_listing.md)
- Sales talk tracks that use these numbers: [`../Knowledge from Calls/06-sales-talk-tracks.md`](../Knowledge%20from%20Calls/06-sales-talk-tracks.md), [`../Knowledge from Calls/08-pricing-deal-mechanics.md`](../Knowledge%20from%20Calls/08-pricing-deal-mechanics.md)
