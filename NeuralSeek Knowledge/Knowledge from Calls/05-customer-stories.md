# Customer Stories & Case Studies

Concrete proof points by account — what was sold, what was built, what the ROI looked like, and what's coming next.

---

## Itochu — The Crown Jewel Account

**Context:** Itochu is one of Japan's Sōgō Shōsha trading conglomerates — Lawrence calls them "the Berkshire Hathaway of Japan." Owns and operates 1,000+ entities globally. ~$100B annual revenue.

**Buyer persona:** Tony Chang (the "NeuralSeek perfect customer" archetype) — IT security guy who also owns AI strategy. Akira is another key champion who *loves* logging into NeuralSeek to look at the governance plane.

### Use Case 1 (Original Win) — Research Agents for Public Companies

**What it does:** Custom dashboard, user enters a target public company name, system spits out a formal Itochu-branded PowerPoint with editable slides.

**Scale:** 107 agents in the workflow, ~4 LLM calls per agent on average → 400–500 LLM queries per single research run.

**The Metric:** *"Three weeks of analyst work → 13 minutes."*

**Competitive bake-off won:**
1. AlphaSense (off-the-shelf)
2. S&P Global (off-the-shelf)
3. Internal custom build with hired AI engineers
4. **N8N + 4 security tools** (the explicit comparison)

**Why we won:** Tony's quote — *"If I buy N8N versus NeuralSeek, I would have to buy N8N plus four security tools."*

**The "GE acquisition" feature (great anecdote for showing iteration agility):** Tony asked, "What happens when GE spins off into three companies mid-research?" NeuralSeek dev team took ~10 of the 70-ish agents and made them modular/swappable to handle branching research threads. Total turnaround for this feature: **2 weeks**.

### Timeline (Use to Crush "We'll Build It Ourselves")

- Feb (mid): NeuralSeek devs start building in prep
- Mar 1: Paid engagement starts
- End of March: First MVP delivered
- End of April: Post-iteration approval
- May: In production
- **Total: ~3 months end-to-end**

Compare to the DIY alternative: still mid-hire at month 5.

### Pricing (Use as Reference Pricing)

- Initial: $45K fixed-bid SOW + $2–3K/mo runtime during POC
- Year 1 expansion (signed): **$240K annual**
  - $10K/mo containerized NeuralSeek license ($120K)
  - $7K/mo NeuralSeek FDE ($84K)
  - $3K/mo CPP FDE ($36K)

### Year 2+ Expansion Pipeline

**New Use Case 1 — Private Company Research Agents**
- Harder than public companies (no SEC filings, scrape macro/trend data)
- Library of pre-built standard agents + ability for sales reps to natural-language-build custom ones (e.g., "track battery supply chain risks across APAC automotive suppliers")
- Auto-generated NTL behind the scenes
- 1,000 sales reps as target users (vs. 100 analysts on the original use case)

**New Use Case 2 — Document/Communication Translation (The GPU Honeypot)**
- Replacing Deep L for English ↔ Kanji translation
- Why it matters: kanji-using executives are the most senior at Itochu, communicating the most sensitive enterprise data
- Cannot route through cloud LLMs → containerized NeuralSeek + on-prem LLM + on-prem GPU
- **For CPP/channel partner:** this is the GPU hardware land-and-expand play. Get the customer to ask for GPUs and you're in the NVIDIA gravy train.
- Bidirectional: Kanji ↔ English with auto-reformatting (handles right-to-left + top-to-bottom kanji + image displacement)
- Use case can extend beyond a portal to embedded in Tina (their chat platform), automatic in-flight document translation

### Strategic Rationale for Year 1 Underpricing

Lawrence is deliberately leaving money on the table in year 1 to land the GPU/scale story in year 2 — same playbook as Palantir.

> "Why are we doing a one-year? We could probably get double this. Because when they have this integrated and they have their executives doing all this translation, we then roll this out to 1,000 users. That's the target. This container license for $10K a month is no longer $10K in year two. This is the playbook that Palantir runs."

### Itochu as a Reference

- Lawrence's plan: get Tony on as many stages as possible, run happy hours with him as the highlight speaker
- The N8N quote is the canonical reference Lawrence wants to propagate

---

## Children's Health — Pediatric Hospital

**Context:** One of the largest pediatric hospitals in the US.

**Contract:** **3-year, $400K/yr** — signed (deal closed the night before the April 17 demo).

**Sales context (key competitive win):** Was being pitched by OpenAI's consultant division. NeuralSeek won by leaning on the joint-ownership / anti-lock-in narrative.

### Roadmap (5 use cases in 6 months)

1. Internal chatbot over policy documents
2. Enterprise search
3. OCR documents
4. Portal
5. Call listener
+ pediatrician dashboard (future)

### Architecture (Reference)

- **Containerized NeuralSeek on-prem** (in their Azure tenant)
- **Vector DB:** Postgres or Elasticsearch (running in-cluster)
- **LLM (Phase 1):** Microsoft Azure AI Foundry (GPU availability constraint — fastest time to market)
- **LLM (Phase 2 long-term):** Locally hosted model on-prem (cost crossover as load grows)
- **AKS cluster** hosting the entire stack

### Implementation Team (Children's Health-side stakeholders)

- John Price — Project Manager (focused on 90-day MVP scope)
- Jamie Grandfield — Program Director, Technical Design & Delivery
- Joshua Hester — Principal Architect
- Derek Sliger — Senior Director, InfoSec
- Stephen Clark — Director of Security (HIPAA/NIST CSF focus)
- Leonard Kyle — Risk assessment
- Benjamin Belezmo — IAM/GRC
- Laura West — Senior Director, Digital Products (UX/UI focus)
- Daniel Rodriguez — Mobile Solutions Architect
- Angela Kaiser — Organizational change management
- Matthew Parnapy — IAM access controls

### PHI Strategy

- Customizing built-in PII detectors + RegEx to flag/mask PHI categories
- Optional: on-prem LLM + GPU for filtering anything that *might* be PHI before sending elsewhere
- "Pediatricians clamoring for AI dashboards" — strong internal demand pull

---

## Great Day Improvements — HR/Engineering

**Context:** Home improvement company doing **$3 billion a year across the United States**. Verticals: patios, dog houses, kitchens, baths — anything home improvement.

**Champion:** **Soo Jin** (CTO) — "she adores Lawrence." On the website as a featured testimonial.

**Use case shipped:** Yeti — an HR chatbot, rolled out at all-hands on a recent Wednesday. Soo Jin presented to the entire company.

**The killer metric for Great Day:**
> "Most enterprises spend millions of dollars custom-building a chatbot that leverages internal documents, Salesforce data and Databricks data. We do it for $3,000 a month."

**The internal-political dynamic to learn from:** John Kosh (head of dev/engineering, 6 reports) is *cold* to NeuralSeek because he's the AI-engineer-resistance archetype — buying NeuralSeek means he doesn't need to hire 6 more devs underneath him. Soo Jin (CTO) bought NeuralSeek over John's resistance.

**Lesson for sales:** anticipate AI-engineer headcount-protection objections from the engineering leader. Pitch around them by going to the CTO/CISO/business leader who controls the budget.

**Other future use cases:** Deep research workflows (e.g., "How is the Iran conflict going to affect Great Day Improvements?") — multi-step decomposition → sub-question research → best-practices research → Harvard Business Review research → consolidated output. Demo'd to Children's Health as an example of what's possible.

---

## Santander — Early Stage Discovery (Capital Markets / CIB)

**Buyer:** Bilal Akrout — manages Capital Markets infrastructure, app development, and risk (market risk, VAR, sensitivity, P&L) for Corporate & Investment Banking.

**Status:** First exploratory conversation. Already had a (small) existing NeuralSeek install somewhere in the org via IBM consulting back channel — Lawrence used this as a credibility opener.

**Key concerns surfaced:**
- Data validity / hallucination prevention (callback to a year-old HPE PCAI conversation that died on this exact concern)
- LLM flexibility (explicitly wants the ability to swap LLMs without re-prompting)
- Productivity uplift vs. headcount reduction (philosophically prefers the productivity framing)
- Heavy use of ChatGPT Enterprise + Devin already; doesn't want to displace, wants to augment

**Lead opportunities pitched:**
1. Risk team peer-to-peer bank analysis (demo'd — high/medium/low risk stack ranking from FFIEC reports)
2. Pairing NeuralSeek with their CodeGen tools (Devin + Cloud Code) for token-cost reduction
3. Sales/M&A research agents (similar to Itochu's 1,000-user sales rep play)

**Next action:** Find an internal use case to do a quick custom POC. Paul O'Dell + Lawrence on follow-up.

**Geographic angle:** Santander opening a big Miami office. NeuralSeek is Miami-based. The investing VC fund is well-connected to Miami banking ecosystem.

---

## NatWest Bank — Original Reference Account

**What we built:** Multiple — global chatbot, PII detection (this is where the UK phone number RegEx came from in the built-in PII library).

**Reuse value:** Every demo Lawrence gives includes built-in PII detectors with "UK phone number" visible — proof point that we've handled real regulated UK financial services.

---

## Penn State — Public-Facing Chatbot

**What we built:** Global chatbot for the university.

**Reuse value:** Source of NeuralSeek's prompt-injection guardrail hardening — Lawrence's quote: *"You can imagine the college kids banging up against it, trying to make it do stupid things."*

---

## Online Casino — Token Protection Origin Story

**What we built:** Customer chatbot.

**Reuse value:** Origin of the minimum-text and maximum-length token guardrails — *"At 2am in the morning, frustrated that they lost a lot of money, [users] were banging up their chatbot trying to drive their token costs up."*

---

## Latin American Banks — Attribution Protection Origin

**What we built:** Customer-facing chatbots for multiple Latin American banks.

**Reuse value:** Origin of NeuralSeek's "attribution protection" guardrail — bank chatbots were being manipulated by users to say bad things about the bank itself. Lawrence now ships this as a default-on guardrail.

---

## Verizon, Adobe, Snap — Foundational Production Accounts

**What we built:** Various, multi-year production deployments.

**Reuse value:** Foundational credibility — Verizon has explicitly tried to remake NeuralSeek multiple times internally and can't reverse-engineer the NTL compression. This is THE moat story.

---

## BRO Bank (Uruguay) — Semantic-Scoring Edge Case

**What we use it for:** A demo example showing how NeuralSeek's semantic scoring catches truly subtle hallucination.

**The story:** Lawrence doesn't have the word "Uruguay" in his source docs. The LLM "knows" from training data that BRO stands for the Uruguayan bank. NeuralSeek catches this as ungrounded — the answer wasn't in *his* source data even though it's technically correct.

---

## Hitachi (mentioned in CPP Training)

Cited by Paul O'Dell as a "prime example" of how the AI/NeuralSeek practice grows the entire CPP business — not just AI revenue but infrastructure and services too.

---

## Anonymous AI Startup — Channel/White-Label Discussion (May 19)

**Context:** Pre-revenue startup building in legal + healthcare. The CEO is non-technical. the Founding CRO and their CTO drove the call.

**Discussed deal mechanics:**
- White-label allowed for "pointed solutions" (vs. horizontal AI middleware plays)
- **Cannot sell containerized license + let them resell unlimited** — must be a rev-share aligned to their pricing
- Free demo environment for ~1 month if BYO LLM credentials for heavy usage

**Their interests:**
- OCR + PII for legal documents (with 100% confidence requirement — Lawrence honest that NeuralSeek won't catch-all SLA accept that liability)
- Multi-LLM agility
- Fastest path to market with their first clients

**Reusable pattern:** the "give equity to dev shop, dev shop builds on NeuralSeek" model — already used with one non-technical founder.

---

## Disney (The "Large Animated Mouse Character") — POC

**Context:** Mid-POC at the time of the Children's Health demo (Apr 17). Video tools use case, very cautious about public release.

**Volume:** ~30–40 custom governance/guardrail workflows for different regional requirements.

**Reuse value:** Shows depth of custom-governance use cases the platform handles.

---

## Adobe / Snapchat — Originals

Mentioned as foundational early production go-lives alongside Verizon and NatWest. Used for general credibility ("we've been in production at scale for 3+ years").

---

## MetLife — In Progress (Active Pursuit)

**Context:** One of the largest insurance companies in the world.

**Lawrence's connection:** Personal friend network — he sold to Morgan Stanley for years at IBM, and several Morgan Stanley execs moved over to MetLife. Bumped into him via Slack.

**Status:** About to close. Lawrence wants to pull them into the upcoming brand film (verbal, not confirmed).

**Sales hook:** Lawrence knows the GRC (Governance, Risk, Compliance) people personally — same "no-fun police" archetype as the typical CISO ICP.

---

## Itochu — The Deeper Story (Updated from Oy Interviews)

Beyond what's in the public-company research agent story, the strategic depth of the Itochu relationship:

**Itochu Corporate's structure:**
- Owns / manages / buys / sells / operates **4,000 subsidiaries** across grocery, textiles, machinery, metals, minerals, energy, chemicals, food. *"They own a satellite company. They own a missile-making company."*
- $100B+ annual revenue
- Corporate Itochu mandates technology direction down to all subsidiaries

**Tony Chang (the lead champion at Corporate Itochu) is doing more than buying:**
- Introduced Lawrence to a consultant shop that's getting kickback referrals
- He gets revenue credit through that consultant shop (incentive aligned)
- He's already verbally committed to be the on-camera lead for NeuralSeek's brand film
- He's going to circulate the brand film to all of Itochu's subsidiaries as the corporate-blessed technology
- *"He's not going to bank his career on something he doesn't believe in. He's not going to risk his livelihood. But this is the vision."*

**The video direction Lawrence is comfortable with (from Tony):**
> "We could have him say, 'I evaluated Anthropic, OpenAI, and I chose NeuralSeek.' We could have him go up there and say, 'this is the most revolutionary technology I've ever seen.'"

**Strategic value:** every subsidiary of Itochu is now a NeuralSeek prospect with the corporate stamp of approval.

---

## The "Golden Goose" Three (Marketing-Approved Reference Accounts)

From Oy Interview 2 — Lawrence flagged three customers as the public-facing testimonial accounts:

1. **Itochu** — the big enterprise validator
2. **Children's Health** — the regulated healthcare validator
3. **Great Day Improvements** — the cost-savings validator ("$3K/month vs. millions to build")

Other customers exist in production (Verizon, Adobe, NatWest, Snap, Latin American banks, Penn State, online casinos, etc.) but those wins are *"all without marketing approval"* — not green-lit for case studies.
