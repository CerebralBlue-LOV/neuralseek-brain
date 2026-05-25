# E. Guardrails in Action — Illustrative Model

*Itochu and Children's Health.*

## Modeling note (required before publishing)

> ⚠ **The numbers below are an illustrative model** based on each customer's known volume profile and typical industry guardrail-trigger rates — **not direct customer telemetry**.
>
> Label them clearly in any published collateral (e.g., *"modeled estimate based on portfolio averages"*) and confirm with each customer before publishing the numbers attached to that customer's name.

## Illustrative customer-specific examples

| Customer | Guardrail in action (illustrative model) |
|---|---|
| **Itochu** — 107 agents, 500 analysts, ~400–500 LLM calls per research run, generating Itochu-branded financial deliverables sourced from SEC EDGAR, XBRL, live web, and private documents | • **~5,000+ semantic-grounding interventions per month** — NeuralSeek's proprietary semantic-lineage model catching ungrounded financial claims before they reach an Itochu-branded report<br>• **~10,000+ confidentiality and PII redactions per month** — protecting private deal research and client identifiers across 500 analysts<br>• **Token-cost monitoring caps** preventing runaway LLM spend on 500 × multiple-reports-per-week query volume |
| **Children's Health** — HIPAA-grade chatbot live for clinicians, content filtering tuned for pediatric care, role-scoped SSO across 8,000+ staff | • **~2,000+ PHI redaction events per month** — built-in PII detectors plus pediatric-care RegEx patterns protecting patient identifiers in every clinician prompt<br>• **~500+ off-topic and policy-violation deflections per month** — content filtering tuned for clinical pathways and pediatric-specific safety<br>• **Full audit log on every prompt and response** — every interaction replayable for compliance, with role-based access enforced per unit |

## The on-record, fully defensible portfolio claim

> *"NeuralSeek ships with 118 AI guardrails active by default — covering prompt injection, PII / PHI redaction, attribution protection, semantic grounding, and token-cost limits. Every guardrail trigger is logged and replayable. From Fortune 500 trading houses to HIPAA-regulated pediatric hospitals, our customers trust the same governance pane."*

## Suggested visual

Pair the portfolio claim with a screenshot of the 118-guardrails catalog page from the brain. Customers respond strongly to the visual density of the full list.

## Source

- [NeuralSeek Knowledge / Features / neuralseek_118_ai_guardrails_listing.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Features/neuralseek_118_ai_guardrails_listing.md)
- Itochu client story: [NeuralSeek Knowledge / Client Stories / itochu.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Client%20Stories/itochu.md)
- Children's Health client story: [NeuralSeek Knowledge / Client Stories / childrens-health.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Client%20Stories/childrens-health.md)
