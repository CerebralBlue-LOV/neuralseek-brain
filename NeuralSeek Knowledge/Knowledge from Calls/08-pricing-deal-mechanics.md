# Pricing & Deal Mechanics

How NeuralSeek prices, packages, and structures deals — including land-and-expand patterns.

---

## Pricing Models (Two Options)

### 1. Runtime Pricing (BYO LLM)

- Customer plugs in their own LLM credentials
- NeuralSeek charges based on runtime horsepower (more complex workflows = higher cost)
- **OCR is explicitly heavy** on runtime — Lawrence is transparent about this with customers
- Available via cloud marketplaces (AWS, Azure, Google, IBM Marketplace) for self-service

### 2. Containerized License (Flat Fee)

- Customer gets a containerized version of NeuralSeek they can deploy anywhere (cloud, on-prem)
- Flat annual fee, unlimited use of NeuralSeek itself
- **Cost stack becomes:** flat NeuralSeek license + customer's infrastructure + customer's LLM tokens
- Use case: customers who want predictable cost, on-prem deployment, or air-gapped environments

---

## TCO Buckets (How to Frame Cost Conversations)

Any AI application has three cost buckets:

| Bucket | Description | NeuralSeek route | DIY route |
|--------|-------------|------------------|-----------|
| 1. AI Platform | The orchestration layer | NeuralSeek license OR runtime | AI engineer salaries ($450–650K/yr) |
| 2. Infrastructure | Cloud or on-prem compute | Customer's bill | Customer's bill |
| 3. LLM | Token costs | Customer's bill | Customer's bill |

**The reframe:** Buckets 2 and 3 exist either way. The decision is whether bucket 1 is a NeuralSeek invoice or a payroll line item.

---

## The Forward-Deployed Engineer (FDE) Model

Two-tier offering — NeuralSeek FDE + Channel Partner FDE.

### Why NeuralSeek's FDEs are 8–10x cheaper than OpenAI's

- OpenAI Forward-Deployed Engineer: $450–650K/yr salary
- NeuralSeek FDE: $36–60K/yr (offshore in Colombia)
- **Why the gap:** NeuralSeek FDEs don't have to hand-code the hard parts. They reuse what NeuralSeek built once. Drag-and-drop deployment vs. custom-stitching every engagement.

### FDE Pricing Reference (from Itochu deal)

- NeuralSeek FDE billed to customer: $7K/mo ($84K/yr)
- CPP (channel partner) FDE billed to customer: $3K/mo ($36K/yr)

### Talent Strategy

- NeuralSeek devs in US + offshore (Colombia, with stops in Cali and Medellín)
- Lawrence and Mark are actively traveling to scale the offshore team

---

## The Itochu Deal Structure (Reference Pricing)

### Original Deal (Public Company Research Agents)

- Fixed-bid SOW: **$45K**
- Plus runtime during POC: **$2–3K/mo**
- ~3 months end-to-end (Feb → May)

### Year 1 Expansion (Verbally Agreed; ~$240K/yr total)

- **$10K/mo containerized NeuralSeek license** = $120K/yr
- **$7K/mo NeuralSeek FDE** = $84K/yr
- **$3K/mo CPP FDE** = $36K/yr

### Why Lawrence Deliberately Underpriced Year 1

> "Why are we doing a one-year? We could probably get double this. Because when they have this integrated and they have their executives doing all this translation, we then roll this out to 1,000 users. That's the target. This container license for $10K a month is no longer $10K in year two. This is the playbook that Palantir runs."

**The Palantir playbook:**
- Land at a discount with land-and-expand FDE coverage
- Year 2: container license multiplier as scale grows (1,000+ users)
- Year 2: FDE multiplier as new business units request use cases
- The $45K initial SOW becomes a 7-figure ACV "very rapidly"

---

## Children's Health Deal Structure

- **3-year commitment**
- **$400K/yr**
- Includes containerized NeuralSeek
- Multiple use cases in scope (chatbot, enterprise search, OCR, portal, call listener, pediatrician dashboard)

**Critical strategic note:** Customer paid for a license that covers *all* their AI use cases for that period. Variable cost per new use case = just LLM tokens. This is the "five use cases on the roadmap, single license" upsell argument.

---

## What You Cannot Buy

**Cannot:** White-label + unlimited resale.

Lawrence's policy (from Anonymous AI Startup call):
> "I cannot sell you a containerized license and then let you sell unlimited on top of us. We can do rev-share stuff — if you're charging people $2,000/mo, we can come up with a per-something rate aligned to your pricing. But we'd have to have a conversation about protecting us."

**The rev-share model exists** for partners building branded products on top of NeuralSeek — needs to be aligned to their downstream pricing.

---

## Discovery / POC Concessions

For early-stage prospects:
- **~1 month free environment** for proof-of-concept exploration
- BYO LLM credentials if you're going to push volume
- Lawrence will throw a NeuralSeek dev at it for partner relationships
- Equity-for-build deals exist (used with at least one non-technical founder)

---

## Channel Partner Economics (CPP Model)

CPP gets paid through:
1. CPP-billed FDE labor (e.g., $3K/mo to Itochu)
2. Underlying infrastructure (cloud, networking, services) — major TCO grower
3. **GPU hardware** (the big land-and-expand prize when customer goes on-prem)

> "Yes, we're still a cloud infrastructure company, but we are very much becoming an AI company. The cornerstone of that practice is built around NeuralSeek. It's not only the AI bucket that's growing for us, but it grows all of our other businesses as well." — Paul O'Dell

---

## The GPU Land-and-Expand (Channel Goldmine)

The strategic prize for CPP-type partners is GPU sales:

> "If CPP could get every one of their customers to come to you and ask for GPUs, you will make money hands over fist. That's why NVIDIA's stock is crazy. They're in high demand. GPUs are high-ticket items. You sell managed service on the hardware. You sell refreshes when GPUs burn out. It's a never-ending gift."

**The path:**
1. NeuralSeek lands on a use case
2. Use case requires on-prem (data sensitivity, air-gap)
3. On-prem requires GPU box
4. Channel partner sells the GPU + managed service + refreshes
5. NeuralSeek runs containerized alongside the GPU

---

## Pricing Conversation Discipline

**Be transparent:**
- "We have an amazing pricing model — very transparent."
- Runtime billing is usage-based, like LLM token billing
- Containerized license is fixed

**Position concessions deliberately:**
- Year 1 underpricing → year 2 expansion (Palantir playbook)
- Fixed-bid SOW for the initial engagement to de-risk the customer
- The expensive part (FDE labor) is significantly cheaper than the alternative (in-house AI engineers)

---

## Internal Funding Status (Use Selectively)

Lawrence is raising a seed round at the time of these calls:
- **~$5M at a $50M valuation**
- Bootstrapped + revenue-generating for 3+ years before this raise
- Lawrence has joked he might tell the VCs to screw off after Children's Health and Itochu wins
- *"We're a bootstrap startup. We're fucking gritty. We were birthed out of a consultant shop."*

**Use this signaling:**
- Pro: shows the company is not vapor — real revenue, real customers
- Pro: shows hunger (they'll engage)
- Pro: at-valuation suggests the company expects to grow significantly (good signal for buyers worried about vendor stability)
- Caveat: don't overshare with risk-averse enterprise buyers who want to see Series B+ stability

---

## The VAR / VAD Channel Architecture

From Oy Interview 2 — the formal distribution model Lawrence is building out.

### The Three-Tier Margin Structure

```
NeuralSeek → VAD (Value Added Distributor) → VAR (Value Added Reseller) → End Customer
```

| Layer | Sells at | Margin per dollar |
|-------|----------|-------------------|
| NeuralSeek | $0.75 to VAD | NeuralSeek keeps 75¢ |
| VAD | $0.80 to VAR | VAD adds 5¢ |
| VAR | $1.00 to customer | VAR adds 20¢ |

**Lawrence's strategic context:**
> "Yes, we have a dedicated sales team, but it's only going to be for our biggest and most juicy ops. I'm about to ink a contract with one of the biggest VARs — they have thousands of resellers they'll push it to. They do all the distribution, we sit back and make sure the product doesn't blow up."

### Why this is the right model for NeuralSeek
- Founder Lawrence "hates prospecting" — channel layers solve the lead-gen problem
- No need for a 50-person direct sales team
- No customer success org needed (consultants own the retention via renewal credit)
- No inbound lead handling team
- NeuralSeek focuses on product + biggest direct accounts only

### The Consultant Recruit Pitch
> "I have 10–15 consultants that resell my software and I give them a revenue percentage. They get revenue credit when the customer renews — so now they're the customer success team and the horizontal selling team."

The recurring revenue tied to renewal credit makes consultants ALSO the customer success function.

---

## The FDE Margin Economics (Behind the Scenes)

A truthful internal-pricing reality Lawrence shared in Oy Interview 2:

> "Software is just air, dude. I'm selling air. There's no margin on it at all for us. Then this is a different margin game — one guy offshore that costs me $4,000/month, I distribute him for clients at like a 25x margin."

| Product Type | Lawrence's COGS | Customer Pays | Margin |
|--------------|-----------------|---------------|--------|
| NeuralSeek (software) | very low | ~$10K/mo | "air" (essentially 100%, but small absolute dollars per seat) |
| FDE (NeuralSeek dev) | $4K/mo (offshore Colombian dev) | ~$3K-$7K/mo | varies — but distributed across multiple clients yields strong margins |

### The VC-Storytelling Tension
> "VC funds are giving me a 40x multiple on SaaS ARR but a smaller multiple on FDE services revenue. So I'm doing a sneakier play — this VC fund is the only one that's going to know about this. The next round, I'm going to mush all the money together. We're wheeling and dealing million-plus contracts, but half is for the software, half is for bodies to install."

**Implication for deal structuring:** Lawrence is consciously bundling FDE + software into combined contracts so the optics look more "SaaS-y" to future investors.

---

## "Half Software, Half Bodies" — The Combined Contract Pattern

The standard expansion deal structure Lawrence likes:

> "We're wheeling and dealing million-plus contracts. But half of the contract is for the software, and the other half is for a body of people to install."

This is in line with Palantir's playbook. The Itochu year-1 expansion ($240K) maps to this exactly:
- $120K software (containerized license)
- $120K bodies ($84K NeuralSeek FDE + $36K CPP FDE)

---

## The Self-Service Pricing Tier Concept

A pattern Oy surfaced (validated by Lawrence's existing model) — most B2B SaaS forgets that *implementation* can be its own pricing tier.

Three product tiers worth considering:
1. **Self-serve software** — customer figures it out, slow ramp, cheap
2. **Software + bodies** — NeuralSeek FDE handles implementation, fast ramp, mid-tier price
3. **Software + full white-glove** — for enterprise; full team of NeuralSeek + channel FDE, premium price

Lawrence's note: most startups *only* sell tier 1 because they fear the optical impact on SaaS multiples. NeuralSeek explicitly sells all three.

---

## Future-State Mentions

- The 10M/yr consultant arm (NeuralSeek's parent) will be **merged into the SaaS company** before/around the funding announcement. Legacy consultant headcount will be converted to FDE roles.
- Future containerized licenses will explicitly grow over time — Itochu's $10K/mo licence is anticipated to multiply in year 2 as user count grows.
