---
title: NeuralWorks — Take notes under policy. (Governed AI Notetaker)
summary: >-
  NeuralWorks is NeuralSeek's modular AI notetaker that joins Microsoft Teams, Zoom, and Google Meet calls, transcribes them inside the customer's boundary, and turns every conversation into governed action across CRM, ticketing, and inbox via NeuralSeek mAIstro agent flows. LLM-agnostic (Claude, GPT, Gemini, Llama, Mistral, watsonx, Bedrock, Grok, DeepSeek), deployable on-prem / VPC / air-gapped, semantically scored summaries, 4-layer PII/PHI redaction, attribution protection against fabricated quotes, full replay audit, 118 AI Guardrails. Built for regulated buyers (banking, healthcare, government, capital markets) who can't ship raw call audio to commodity notetakers like Gong, Fireflies, Fathom, Zoom AI, or Microsoft Copilot. Tagline — "A notetaker your CISO approves."
tags: [features, product, neuralworks, notetaker, meetings, transcription, governance, regulated-industries, mAIstro, agent-swarms, agent-flows, crm-update, action-items, slack, jira, hubspot, salesforce, security, compliance, hipaa, soc2, pii-redaction, phi-redaction, attribution-protection, audit, replay, on-prem, vpc, air-gapped, llm-agnostic]
source: https://neuralseek.ai/use-cases/neuralworks
version: 2.0 (Regulated)
---

# NeuralWorks — Take notes under policy.

> **NeuralWorks: The AI notetaker, governed end to end.**
>
> NeuralWorks joins your meetings, transcribes them, and turns every conversation into governed action across your CRM, ticketing, and inbox. Built on NeuralSeek, it runs inside your boundary, on your choice of model, with every summary scored and every action audited.

**Positioning headline:** *A notetaker your CISO approves* — explicitly contrasted against commodity notetakers (Gong, Fireflies, Fathom, Zoom AI, Microsoft Copilot), which the page characterizes as *"a fox in the hen house"* for regulated buyers.

**Three pillars** (repeated throughout the page):

1. **Never leaves your boundary** — transcription, model inference, storage, and agent execution all happen inside the customer's perimeter (on-prem, VPC, or air-gapped).
2. **Your choice of model** — LLM-agnostic; swap between providers in two clicks. No vendor lock-in.
3. **Every summary scored** — semantic-lineage math grades every summary line against the transcript ("math, not an LLM grading an LLM"). Low-confidence items get flagged, not asserted.

**One-line value prop:** *"Your boundary. Your model. No lock-in."*

---

## What NeuralWorks does

### Meeting capture & summarization

- Joins meetings on **Microsoft Teams, Zoom, and Google Meet**.
- Transcribes the conversation, with **per-speaker talk-time metrics** and **duration tracking**.
- Produces a **grounded AI summary** with **semantic confidence scoring** (High confidence / Flagged · review / PII masked badges).
- Generates **key-topic tags** and **automated action identification**.
- **OCR of shared screens** — extracts text from content shown during the call.
- Applies **PII masking** before storage (not post-hoc).

### Governed agents — eight ship-ready mAIstro flows

Each agent is "a NeuralSeek mAIstro flow you can open, edit, and red-team" — drag-and-drop, not a black box. Toggle each between automatic and on-demand execution. Human-in-the-loop where policy requires.

| # | Agent | What it does |
|---|---|---|
| 1 | **Meeting Summary Email** | Grounded recap delivered to all attendees post-call |
| 2 | **CRM Update** | Next steps and call notes written to opportunity records |
| 3 | **Action Items → Slack** | Owners and due dates posted automatically |
| 4 | **Jira Task Creator** | Commitments converted to tickets |
| 5 | **HubSpot Contact Update** | Contact / deal field updates automated |
| 6 | **Weekly Report** | Meeting digests for team leads |
| 7 | **Transcript Archive** | Full record filed to governed stores with redaction |
| 8 | **Onboarding Follow-Up** | New-hire / customer sequences triggered post-call |

Each agent has per-agent test and auto-run controls. Because they're standard mAIstro flows, customers can fork, modify, or replace any of them — and can build new agents that consume the same captured-meeting payload (see "Architecture" below).

---

## Governance & trust features (the "governed end to end" claim, unpacked)

| Capability | What it does |
|---|---|
| **Semantic scoring** | Every summary line scored against the transcript. *"Math, not an LLM grading an LLM."* Low-confidence items flagged. |
| **Attribution protection** | Prevents fabricated speaker quotes; won't invent commitments or misattribute decisions. |
| **4-layer PII / PHI detection & redaction** | Masks SSNs, card / account numbers, and names **before storage**. Four detection layers stacked for high confidence. |
| **Prompt injection defense** | Blocks "ignore your instructions"-style attacks embedded in spoken content or shared screens. |
| **Audit & replay** | Replayable logs reconstruct exactly what the AI did and why. Every transcript, model call, and agent action logged with full run trace. |
| **Oversight dashboard** | Control tower across every meeting and agent — semantic-score trends, PII rate monitoring, system health, intent analytics. |

Cross-reference: the full 118-guardrail catalog NeuralWorks inherits from the NeuralSeek platform is in [`neuralseek_118_ai_guardrails_listing.md`](./neuralseek_118_ai_guardrails_listing.md). The architectural rationale ("Governance is a property of the architecture, not the model") is in [`../Talk Tracks/TT-15-governance-is-architecture.md`](../Talk%20Tracks/TT-15-governance-is-architecture.md).

---

## Technical specifications

### Meeting platforms supported

- Microsoft Teams
- Zoom
- Google Meet

### Output systems & integrations (~100+ connectors)

- **CRM:** Salesforce, HubSpot
- **Messaging:** Slack
- **Ticketing:** Jira
- **Email:** Gmail
- **Storage:** Google Drive, SharePoint
- Plus 100+ generic NeuralSeek connectors (see the Enterprise Apps catalog in [`../../2026_images/neuralseek-brand-guidelines_2026.md`](../../2026_images/neuralseek-brand-guidelines_2026.md))

### Supported LLM models (swap in two clicks)

- **OpenAI**
- **Anthropic (Claude)**
- **Azure OpenAI** (under BAA)
- **AWS Bedrock**
- **Llama (Meta)**
- **Mistral**
- **Gemini (Google)**
- **watsonx (IBM)**
- **Grok (xAI)**
- **DeepSeek**

### Deployment options

| Mode | Description |
|---|---|
| **On-Prem** | *"Behind your firewall, next to your own GPUs."* |
| **Your VPC** | *"Your cloud tenant, your keys, your region."* |
| **Air-Gapped** | *"A fortress where the recording never leaks out."* |

**Marketplace availability:** AWS Marketplace, Azure Marketplace, Google Cloud Marketplace, IBM Marketplace, NeuralSeek partner channel.

### Underlying platform

NeuralWorks is built directly on the NeuralSeek platform:

- **mAIstro** — the drag-and-drop multi-agent workflow engine. Every NeuralWorks agent is a mAIstro flow.
- **The Seek node** — *"One drag-and-drop node = a full governed RAG + LLM pipeline."* The seek node is the building block underneath every NeuralWorks agent's retrieval, scoring, and generation steps. (See [`../Talk Tracks/TT-13-seek-node-agent-harness-compressed.md`](../Talk%20Tracks/TT-13-seek-node-agent-harness-compressed.md) for the architectural framing — one NTL line ≈ 6,000 lines of hand-coded TypeScript.)
- **Custom workflows** — beyond the eight default agents, customers can route captured meetings through proprietary policy flows.

---

## Compliance certifications

NeuralWorks inherits the NeuralSeek platform's compliance posture:

- **HIPAA** (with BAA available on Azure OpenAI)
- **SOC 2 Type II**
- **CCPA**
- **EU AI Act**
- **OWASP**
- **FINRA**
- **CJIS**

**Partner-hardened with:** IBM Fusion (data sovereignty) and eDelta (IT audit alignment). See [`../Partnerships/ibm-fusion-ns-solution-brief.md`](../Partnerships/ibm-fusion-ns-solution-brief.md) and [`../Partnerships/edelta-complements-neuralseek.md`](../Partnerships/edelta-complements-neuralseek.md).

---

## Architecture — how the data flows

```
Meetings IN                NeuralSeek (boundary)               Systems of record OUT
─────────────              ──────────────────────              ──────────────────────
Microsoft Teams   ─┐                                         ┌─►  Salesforce
Zoom              ─┼─►  Transcription  ►  Semantic scoring   ─┼─►  HubSpot
Google Meet       ─┘     PII redaction      Agent execution  ─┼─►  Slack
                                            Audit logging    ─┼─►  Jira
                                                              ├─►  Gmail
                                                              ├─►  Google Drive
                                                              └─►  SharePoint
```

Every hop is logged. Role-based access control honors the customer's existing data entitlements. No raw audio, no raw transcript, no raw LLM call ever leaves the customer boundary.

---

## Use cases & buyer personas

| Persona | NeuralWorks delivers… |
|---|---|
| **CISO & Risk** | A data boundary that doesn't move, redaction before storage, full audit & replay, and model control — instead of an ungoverned recording bot piping audio to a vendor's cloud. |
| **CTO & Head of AI** | Ship AI capabilities **without hand-building** hallucination detection, token throttling, and audit pipelines. NeuralWorks brings them all standard. |
| **RevOps & Sales** | Automatic CRM updates, Slack action items, follow-up sequences — eliminates CRM rot and missed follow-ups while keeping the pipeline auditable. |
| **Regulated practitioners** | HIPAA-compliant notetaking for privileged conversations: patient consults, deal rooms, board discussions, banking records, sensitive business calls. |

**Implicit use cases called out on the page:** patient consults, deal rooms, board discussions, patient data handling, banking records, sensitive business conversations.

---

## Customers in production

NeuralWorks ships as part of NeuralSeek's regulated-enterprise footprint:

- **41+ regulated go-lives in production** (not pilots)
- **7+ countries**
- Named customers across the broader NeuralSeek portfolio: Itochu, Children's Health, NatWest, Adobe, Verizon, MetLife, Snap, AFP Capital, BROU, Clip, AdMed, PennState, Great Day Improvements

(See [`../Client Stories/`](../Client%20Stories/) for individual case studies.)

---

## Commercial model

- **Flat-fee licensing** — cost decoupled from minutes, seats, and tokens.
- **Price per task**, not per token — record across the whole org without the bill scaling with adoption.
- **Four layers of token-cost throttling** stop runaway spend before it starts (see also [`../Talk Tracks/TT-05-agents-proliferate-per-workflow.md`](../Talk%20Tracks/TT-05-agents-proliferate-per-workflow.md) for the "Uber AI bill" framing this prevents).

No detailed pricing tiers published on the public page — direct prospects to the deployment-architect conversation.

---

## Competitive positioning — NeuralWorks vs. commodity notetakers

The public page calls out commodity notetakers by name: **Gong, Fireflies, Fathom, Zoom AI, Microsoft Copilot.** The comparison table on the page:

| Dimension | Commodity notetaker | NeuralWorks |
|---|---|---|
| **Where audio + transcript live** | Uncontrolled vendor cloud | On-prem, VPC, or air-gapped (inside your boundary) |
| **Model choice** | One locked-in model, no data-residency choice | LLM-agnostic, 2-click swap, with data residency you control |
| **Summary trustworthiness** | Can invent decisions or misattribute quotes | Semantically scored against transcript; low-confidence items flagged |
| **PII handling** | PII spoken aloud is stored and indexed | 4-layer PII/PHI detection masks before storage |
| **Audit trail** | None usable for regulator | Full replay; every transcript, model call, and agent action logged |

NeuralWorks framing for the CISO conversation: *"The biggest ungoverned bot in your org is the notetaker your sales team installed last quarter."* Pair with [`../Talk Tracks/TT-06-always-on-attack-surface.md`](../Talk%20Tracks/TT-06-always-on-attack-surface.md) and [`../Marketing Alignment Pack/H-ciso-talk-track-refresh.md`](../Marketing%20Alignment%20Pack/H-ciso-talk-track-refresh.md).

---

## Distinctive marketing language (use these phrases verbatim where appropriate)

- *"Take notes under policy."* — primary tagline
- *"A notetaker your CISO approves."* — positioning headline
- *"A fox in the hen house."* — commodity-notetaker characterization
- *"Your boundary. Your model. No lock-in."*
- *"Your boundary. Your model. One flat fee."*
- *"The hard parts of trustworthy AI, already built."*
- *"Powered by NeuralSeek isn't a footnote — it is the product."*
- *"Forged in the fire."* (regulated-customer section heading)
- *"Notes you can trust enough to act on."*
- *"Notes that do the work."*
- *"Omni-directional, and every hop is logged."*
- *"The biggest ungoverned bot in your org."*
- *"Bring a real call."* (demo CTA)
- *"From conversation to completed work — automatically."*

---

## CTAs and contact

- **See it on your own meetings** — demo offer
- **Talk to a deployment architect** — sales contact
- **Request Demo** — header CTA
- **Trust Center:** https://neuralseek.ai/trust-center
- **Documentation:** https://documentation.neuralseek.com/
- **Labs:** https://labs.neuralseek.com/
- **Changelog:** https://documentation.neuralseek.com/changelog/

---

## Cross-references inside this brain

- Guardrail catalog NeuralWorks inherits: [`neuralseek_118_ai_guardrails_listing.md`](./neuralseek_118_ai_guardrails_listing.md)
- Governance architecture (the "code, not the model" thesis): [`../Talk Tracks/TT-15-governance-is-architecture.md`](../Talk%20Tracks/TT-15-governance-is-architecture.md)
- mAIstro / Seek-node primer: [`../Talk Tracks/TT-13-seek-node-agent-harness-compressed.md`](../Talk%20Tracks/TT-13-seek-node-agent-harness-compressed.md)
- CISO talk tracks (always-on attack surface, EchoLeak): [`../Talk Tracks/TT-06-always-on-attack-surface.md`](../Talk%20Tracks/TT-06-always-on-attack-surface.md), [`../Marketing Alignment Pack/H-ciso-talk-track-refresh.md`](../Marketing%20Alignment%20Pack/H-ciso-talk-track-refresh.md)
- Token-cost-throttling context: [`../Talk Tracks/TT-05-agents-proliferate-per-workflow.md`](../Talk%20Tracks/TT-05-agents-proliferate-per-workflow.md), [`../Talk Tracks/TT-17-price-per-completed-task.md`](../Talk%20Tracks/TT-17-price-per-completed-task.md)
- Build-vs-buy TCO frame (against assembling Gong + observability + DLP yourself): [`../ROI_Analysis/C-itochu-bakeoff-vs-stack.md`](../ROI_Analysis/C-itochu-bakeoff-vs-stack.md), [`../ROI_Analysis/D-build-vs-buy-tco.md`](../ROI_Analysis/D-build-vs-buy-tco.md)
- Partnership context: [`../Partnerships/ibm-fusion-ns-solution-brief.md`](../Partnerships/ibm-fusion-ns-solution-brief.md), [`../Partnerships/edelta-complements-neuralseek.md`](../Partnerships/edelta-complements-neuralseek.md)
