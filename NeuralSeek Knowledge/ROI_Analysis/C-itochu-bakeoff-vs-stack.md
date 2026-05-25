# C. Itochu's Bake-Off — NeuralSeek vs. "N8N + 4 Security Tools"

*Tony Chang's quote, costed out.*

## The on-record quote

> *"If I buy N8N versus NeuralSeek, I would have to buy N8N plus four security tools to get up to the level of governance and guardrails that NeuralSeek has."*
> — **Tony Chang, Director, IT Strategy, Itochu International**

## What it would have cost Itochu to assemble that stack

To match what NeuralSeek delivers out of the box, Itochu would have had to license and integrate:

| What Itochu would have had to buy | Defensible annual list-price range | Point estimate |
|---|---|---|
| **Workflow / orchestration** (N8N Enterprise) | $50K – $100K | $75K |
| **LLM observability / token tracking** (Langfuse, Arize, Datadog LLM) | $30K – $150K | $75K |
| **Audit logging / SIEM** (Splunk, Datadog) | $250K – $1M+ | $600K |
| **AI safety / hallucination detection** (Galileo, Patronus) | $50K – $250K | $120K |
| **Container platform / governance** (Red Hat OpenShift) | $150K – $500K | $300K |
| **Total annual stack cost** | **$530K – $2M+** | **~$1.17M** |
| **+ integration engineering** (~3 FTE AI engineers @ $300K fully loaded, per Levels.fyi 2025) | | **~$900K** |
| **Total to match NeuralSeek** | | **~$2.07M / year** |
| **NeuralSeek (Itochu actual contract)** | | **$240K / year** |
| **Net savings** | | **~$1.83M / year — before counting any analyst-productivity gain** |

## Plus the research-tool alternatives Itochu evaluated and rejected

| Tool considered | 500-seat annual cost (range) |
|---|---|
| **AlphaSense** | $5M – $7.5M / yr |
| **S&P Global Capital IQ** | $2.5M – $6M / yr |

Pricing for both is non-public; ranges sourced from Vendr, Spendhound, and Costbench transaction databases.

## Promo headline

> *"Itochu replaced a $2M / year stack-and-build approach — and a $5–7M / year research-tool subscription — with NeuralSeek at $240K / year. Before counting a single hour of analyst productivity reclaimed."*

## Sources

- [Vendr — Splunk marketplace](https://www.vendr.com/marketplace/splunk)
- [Datadog pricing](https://www.datadoghq.com/pricing/)
- [Galileo AI pricing](https://galileo.ai/pricing)
- [Red Hat OpenShift pricing](https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing)
- [Vendr — AlphaSense marketplace](https://www.vendr.com/marketplace/alphasense)
- [Costbench — S&P Capital IQ](https://costbench.com/software/financial-data-terminals/sp-capital-iq/)
- Itochu client story: [NeuralSeek Knowledge / Client Stories / itochu.md](https://github.com/CerebralBlue-LOV/neuralseek-brain/blob/main/NeuralSeek%20Knowledge/Client%20Stories/itochu.md)
