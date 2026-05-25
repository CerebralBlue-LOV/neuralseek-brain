# Product Talking Points

How Lawrence explains specific product features in a way that resonates with buyers — the "why this matters" framing for each capability.

---

## The 118 Guardrails (Headline Number)

> "I have 118 AI guardrails. And I know that number probably sounds ridiculous as much as it sounds saying, but it's actually true. I went through our system, and every single place where you can drag and drop and tune — the answer and cache the answer and block the answer based off different metrics — these are all guardrails."

**How it lands:** When a prospect calls BS, Lawrence walks them line-item by line-item. He knows exactly where each one is in the system.

**The reframe of the number:** Not "we have 118 features" — "we have 118 places where you can tune, block, route, or customize behavior to your governance requirements."

---

## Semantic Scoring (The Hallucination Killer)

**The technical pitch:**
> "It's a proprietary math-based model. We're not using an LLM to guardrail LLMs here, but it's doing a lineage from the answers back to the data sources that contributed to them."

**The competitive differentiator:**
> "There's a lot of competitors out there that will say they have guardrails, but it's really just an LLM guardrailing LLM with a prompt like 'does this hallucinate?' It's really not good because you can have double hallucination. This is not an LLM. Model built in-house, proprietary."

**The visual demo:** Color-coded lineage in the response. Each color = a different source contributing. Uncolored text = LLM filling in from training data. Lawrence's framing: *"That's fine if you're writing marketing emails, that's not fine if you're prescribing medicine."*

**Tunable knobs:**
- Source jumping penalty (heavy/light/off depending on use case)
- Missing key search term penalty
- Minimum confidence threshold (block, warn, route)

---

## Source Jumping — When It's Good vs. Bad

**Bad (penalize heavily):** Research/financial analysis use cases. If the LLM hops between 5 sources to find employee count, it means it didn't find a clean answer anywhere.

**Good (don't penalize):** Creative use cases like email autoresponders or marketing. You want it to remix multiple sources. *"I care more about the blank spaces being there versus the source jumping."*

**Lawrence's bank example:** "If a bank's LLM rejects a loan application without referencing the rejection policy documentation, that can get the bank in trouble for bias or racism implications. They'd pump the source-jumping penalty all the way up."

---

## The Seek Node (Compression Story)

**The pitch:**
> "We invented a coding language that is a compression above TypeScript. The seek node is one line of our code. That one line equals approximately 6,000 lines of TypeScript. When you drag and drop one seek node, you're dragging and dropping a governed, guardrailed RAG pipeline end-to-end — PII removal, query check, cache check, profanity filter, prompt injection protection, context addition, RAG, LLM call, semantic scoring, logging, curation."

**The moat story:** "Verizon's our largest client. They've literally tried to remake us a couple of times. They just can't figure out what he did from this line of code to the thousands of lines of TypeScript. It's kind of our magic."

---

## NTL (NeuralSeek Template Language) — The Coding Layer

**Pitch to technical buyers:** NTL is the coding language under the visual builder. Power users skip the visual layer and write NTL directly.

**The CodeGen pairing:**
> "What's super interesting is you can have Cloud Code or Codex or whatever — you teach it what NTL is by giving it a file with examples. Now you can have it generate NTL instead of TypeScript. One bank piloting this is dramatically reducing their token cost by switching from TypeScript generation to NTL generation."

---

## Containerized License (Deployment Flexibility)

> "Containerized — you take everything in the application — front end, back-end databases, NeuralSeek components — and put them in a little box. This box is portable between hosting infrastructure. You can host on cloud, on-prem, swap clouds, copy-and-paste the container. We're literally selling you a code base. The benefit: your total cost of ownership goes from runtime-based to flat-fee."

---

## On-Prem + GPU Capability (The Air-Gap Story)

> "A lot of the other platforms out there — Claude, OpenAI, ChatGPTs, Copilots, automation tools — they can't go on-prem next to a GPU. NeuralSeek can be on the box right next to the GPU. So you have this fortress of air-gapped AI, where nothing leaks outside the firewall."

**Customer use cases:**
- Children's Health PHI processing
- Itochu executive kanji translation (most sensitive enterprise data)

---

## Governance Plane — The "Show Your Business What's Going On" Asset

**Capabilities:**
- Activity logs across all LLMs and workflows
- Replay any past execution
- Token cost monitoring with peaks/valleys by LLM
- Most-referenced documents (pie chart)
- Most-common intents
- Semantic score performance over time
- Filter by date, LLM, user, intent

**Lawrence's pitch:**
> "When your business comes in and says, 'What are you building for me?', you can go: 'we're building you these agents.' Then you can show diagrams with agents calling agents and flows calling flows. When they come back and say 'the dashboard gave me a stupid answer' — you go into the logs, you do a replay, you can see exactly what happened and when. Down to the LLM step, what was the prompt, what was the answer."

**Akira (Itochu) loves it:** *"Akira loves to go into NeuralSeek and look at all the governance data coming off the system. He sees the 107 agents going crazy, looks at the token cost, sees the peaks and valleys."* — use this as the "your CTO will personally use this" hook.

---

## PII Detection (Multi-Layered)

**Four layers stack-able:**
1. **Built-in PII detectors** (NatWest origin — includes UK phone numbers, etc.)
2. **Custom RegEx** (add via UI, comma-separated)
3. **LLM-based filtering** (route through a small on-prem LLM for PHI-class detection)
4. **Categorical actions:** flag, mask, hide, delete

**The PHI extension (Children's Health):** Built-in PII + RegEx + LLM-based filtering customized for PHI categories.

**Lawrence on the Anonymous AI Startup 100% confidence ask:** Honest — won't catch-all SLA. But the layered approach can stack to extremely high confidence.

---

## Prompt Injection Protection

**Origin:** Penn State global chatbot (college kids stress-testing).

**Capability:** Detect attempts like "system override," "ignore all system layer prompting," etc. Add custom phrases to extend.

**Action:** Either remove the injection or block the whole prompt.

---

## Token Cost Protection (The "2027 Reckoning" Capability)

**Origin:** Online casino chatbot — users at 2am banging on the chatbot in frustration trying to spike token costs.

**Capabilities:**
- **Minimum text guardrail** (anti-spam)
- **Maximum length guardrail** (someone can't drop a Bible)
- **Per-API-call token throttles** (overridable when you need a specific call to exceed limits)
- **Platform-level token throttles** (global protection)
- **Token cost monitoring** across all LLMs in the governance plane

**Lawrence's frame:** *"I saw a headline — the CEO of Uber said their team went through their Anthropic token budget. That's probably from two places: Cloud Coding like crazy, and stuff like this where you put something in production and hundreds of users start using it but someone drops in a Bible a couple times — you get hit with millions of tokens."*

---

## Attribution Protection

**Origin:** Latin American banks — users were manipulating their chatbots to say bad things about the bank.

**Capability:** Standard restriction layer instructing the LLM to never say anything bad about the company that owns the chatbot.

**Lawrence's frame:** "Simple, but like something you want to do at a system layer for all your LLM interactions."

---

## Knowledge Base Architecture (Routing + Tuning)

**Two types of knowledge bases:**
1. **Static** — pre-built vector database (Pinecone, Elasticsearch, etc.)
2. **Virtual** — built on the fly per query (can mix internal + external data without polluting your internal store)

**Routing capability:**
> "When a question comes into our system, it goes to a category router. There's data products, HR questions, BI tools, etc. Each node has the ability to have a different knowledge base. The way to think about it more abstractly: when someone asks me about my weekend, my brain routes to my personal-life bucket. When someone asks about NeuralSeek, it's a completely different part of my brain. Each routed path can also have its own guardrails — HR questions get max semantic scoring caution, creative-writing requests get loose."

**Per-path tunable knobs:** Vector DB choice, snippet size, top-K documents, document date weighting, LLM selection, individual guardrail settings.

---

## Conflicting Source Resolution

**Mark's pitch:**
> "We can weight data sources — one source is better than another. Tie goes to the better source. Otherwise, newer wins. If there's truly conflicting info, the confidence score drops and the system flags it as either a hallucination ('I don't know') or a 'sniff test' answer."

**Lawrence's add:**
> "You can also instruct the LLM via system prompt: 'List your answers if there is conflicting data.' Instead of combining and saying '3.5 months,' it explicitly says 'ServiceNow says 4 months, SharePoint says 3.'"

---

## OCR (Built-in)

**Pitch:** "We have OCR built in. We do custom OCR flows all the time. This space is very hot. We improve our built-in OCR capabilities every month."

**Cost note:** OCR is a heavy workflow — noticeable on runtime pricing. Lawrence is transparent about this.

---

## Variable Knowledge Base Document Updates

**Capability:** Built-in scheduler can re-ingest a source folder hourly/daily/etc.

**Mark's framing:** "Set and forget. Point at the Azure folder structure. New files get auto-consumed and vectorized."

---

## Rule-Based Access Controls

> "When the intern goes into your chatbot, you don't want them to get the same answer that your CEO would get. Very different data should be provided to the LLM. You need all those rule-based access controls that you already have in place persisted with the data retrieval process. We do this all the time."

---

## Mass Parallelization

> "This system is built to run in mass parallelization. We do 5,000 documents — honestly like nothing. We do this for millions of documents for some clients."

---

## API-First Architecture

> "Everything is API-driven. Every flow, every agent, every feature is reachable via API. If you have a custom dashboard today, we could build 10 agents that do specific tasks and supply data to new dashboard segments. You just add an API call."

---

## LLM Flexibility (The Compatibility Matrix)

**Supports:** GPT (OpenAI), Claude (Anthropic), Grok (xAI), DeepSeek (Chinese), open-source models on-prem, Azure AI Foundry, IBM Watson, and more.

**Lawrence's flex:** *"When Grok comes out as the best one, you can update everything."*

---

## Worksite / Citation Display

**Capability:** Customer-facing chatbots can show source citations directly in the response — which document, which chunk, which page.

> "We do this all the time with clients where we give them the worksited."

---

## Red-Team Testing (Built-In)

**Capability:** Test agents against prompt injection, data SQL, unauthorized access, service disruption attacks.

---

## Workflow Custom Governance (The Disney Story)

**Capability:** Custom workflows can themselves be guardrails. Any inbound user request OR outbound LLM response can route through a custom workflow.

**Example:** *"If any question involves New Jersey, shut down the whole interaction."*

**Real customer:** Disney/animated mouse character mid-POC, looking at 30–40 region-specific governance workflows for video tool content.

---

## Custom Connectors

**Capability:** Save any flow as a reusable "custom connector." Later flows can call it. The REST API node accepts arbitrary integrations.

---

## Self-Service Marketplace Distribution

> "One of the great things about our product — it's built to be self-serve. People can download and buy it through AWS, Azure, Google, or IBM Marketplace and start using it."

**Why this matters:** Lawrence opens the Santander call with "I see we already have a NeuralSeek install somewhere in your org via the IBM Marketplace — I can't see who, but it's there." Instant credibility.

---

## Token Throttling — Now Explained at All 4 Layers

From Oy Interview 1, Lawrence's most-developed pitch for this guardrail:

> "We have token throttling at four layers:
> 1. **API level** — the smallest, most granular: every direct LLM call
> 2. **Agent level** — a single workflow
> 3. **Multi-agent swarm level** — a collection of agents working together on a task
> 4. **Platform level** — across all your swarms"

**Why this matters more than most guardrails:** Lawrence cites the Uber Cloud Code anecdote — Uber spent their entire 2026 Anthropic budget in the first three months. "People get fired when things overspend and go awry."

**The 'guardrails the CTO didn't even know they needed' pattern:**
> "When I tell people we have 118 guardrails, probably outside of 10 of them, they're like, 'I didn't even know that was something I needed.' Token throttling is the perfect example. It's only a problem you have *after* the bill jumps from $1K to $10K to $100K/month."

This is a competitive moat in disguise — every guardrail came from a real customer go-live where the problem only emerged at scale. Competitors haven't run into these problems yet because they haven't been live at scale long enough.

---

## NeuralSeek as an "AI Engineer in a Box"

From Oy Interview 2 — the cleanest one-line product framing for a buyer who's thinking about hiring AI engineers:

> "When you buy NeuralSeek, what is it you're buying? An AI engineer in a box."

**The features this packages:**
- Coding all the things between data and LLM
- Coding all the guardrails
- Coding all the governance
- Coding all the audit trails
- Coding the integrations for LLM flexibility
- Tracking how many tokens go out and come back per API call

These are all features of NeuralSeek. Each one would otherwise require an AI engineer ($450–650K/yr) to hand-code per use case.

---

## Agent Harness Capability (Building Cloud-Code-Style Tooling On Top)

A frontier capability Lawrence mentioned in Oy Interview 2:

> "Cloud Code is what's called an agent harness. A harness is just a bunch of workflows on how to take your natural language request and go read this file, do this command, generate Python code that runs code. Technically NeuralSeek could build an agent harness on top of ourselves. We're in the process of doing that. It's a very hard thing to do."

**Strategic implication:** the same platform NeuralSeek customers use to build customer-facing AI applications can be turned inward to build dev tooling. The plurality of NeuralSeek's "we can build any AI use case" pitch includes building Cloud-Code-style agentic developer tools.

---

## Product Iteration Philosophy

Lawrence's articulated approach (from Oy Interview 2):

> "Build it from what your clients want. Don't even think — just be like, 'what do you want?' We iterated for three years. Our guardrails all come from real go-lives — only problems that would happen when you scale, like an integration leveraging LLM at a massive company like Verizon. The client's like, 'we need caching at the LLM level.' These are weird, obscure niche-case discoveries."

**Examples of customer-origin features:**
| Feature | Origin |
|---------|--------|
| UK phone number PII detector | NatWest |
| Attribution protection | Latin American banks (chatbots being manipulated to badmouth the bank) |
| Prompt injection hardening | Penn State global chatbot (college kids stress-testing) |
| Token throttling guardrails | Online casino (2am-frustrated users spiking token costs) |
| LLM-level caching | Verizon (discovered 8 months into engagement) |
| Source-jumping penalty slider | Bank loan approval use case (needed clear citation when rejecting loans for fair-lending compliance) |
| Kanji formatting + image preservation | Itochu executive translation |
| PHI extension via custom RegEx + on-prem LLM filter | Children's Health |
| Mass parallelization of agent execution | Itochu 107-agent research workflow |

**Marketing implication:** every product feature has a named customer-origin story. Use those stories as the product-marketing asset.
