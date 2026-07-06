# NeuralSeek — The 118 AI Guardrails

**Official count:** 118 individually configurable AI guardrails across 18 categories.
Every one auditable, versioned, and attributable to a named user with a timestamp.

---

## Summary by Category

| # | Guardrail Category | Count | Domain |
|---|---|---:|---|
| 1 | Retrieval Grounding Guardrails | 6 | Grounding |
| 2 | Hallucination Prevention Guardrails | 11 | Grounding |
| 3 | Prompt Injection Guardrails | 5 | Adversarial Defense |
| 4 | PII & Sensitive Data Guardrails | 5 | Privacy |
| 5 | Answer Confidence Guardrails | 7 | Answer Quality |
| 6 | Profanity Guardrails | 2 | Content Safety |
| 7 | Attribute Protection Guardrails | 1 | Brand Safety |
| 8 | Intent & Routing Guardrails | 7 | Orchestration |
| 9 | Hybrid Search Guardrails | 4 | Grounding |
| 10 | LLM Control Guardrails | 12 | Orchestration |
| 11 | Memory Guardrails | 6 | Session Governance |
| 12 | Multi-Language Guardrails | 2 | Localization |
| 13 | Output Rendering Guardrails | 8 | Channel Delivery |
| 14 | Audit & Compliance Guardrails | 10 | Governance |
| 15 | Prompt Engineering Guardrails | 3 | Authoring |
| 16 | Secrets & Credential Guardrails | 2 | Security |
| 17 | Model-Agnostic Guardrails | 13 | Orchestration |
| 18 | Red Team & Rogue AI Guardrails | 14 | Adversarial Defense |
| | **TOTAL** | **118** | **18 categories** |

---

## The Full Listing (1 through 118)

### Category 1 — Retrieval Grounding Guardrails (6)
*Domain: Grounding · Controls what comes out of the knowledge base*

1. Document Score Range
2. Date Penalty (freshness weighting)
3. Query Cache
4. Max Docs
5. Snippet Size
6. Max Raw Score

---

### Category 2 — Hallucination Prevention Guardrails (11)
*Domain: Grounding · Sentence-level enforcement that answers stay grounded*

7. Semantic Score threshold
8. Re-Rank
9. Check Titles
10. Check URLs
11. Key Term Penalty
12. Term Penalty
13. Source Jump penalty
14. Total Coverage Weight
15. Re-Rank Min Coverage %
16. Hallucination KW removal (sentence-level)
17. **Hallucinated Term Allowlist — closed-loop remediation** *(NEW)*

---

### Category 3 — Prompt Injection Guardrails (5)
*Domain: Adversarial Defense · Direct and indirect injection*

18. Prompt Injection Removal Threshold
19. Prompt Injection Block Threshold
20. Blocked Word Action
21. Blocked Word List (managed + customer-supplied)
22. **Indirect Prompt Injection Protection — content hidden in retrieved docs / URLs / tool outputs** *(NEW)*

---

### Category 4 — PII & Sensitive Data Guardrails (5)
*Domain: Privacy · 13 detector categories, 5 enforcement actions*

23. PII Action (Mask / Flag / No Action / Hide / Delete)
24. Pre-LLM Regex
25. LLM-Based PII Detection (contextual)
26. Out-of-the-box Detector Library (13 categories)
27. Trust Words

---

### Category 5 — Answer Confidence Guardrails (7)
*Domain: Answer Quality · Sliding-scale thresholds on every gate*

28. Warning %
29. Minimum Confidence %
30. Minimum Confidence % for URL
31. Min Words
32. Max Words
33. Verbosity
34. Force KB

---

### Category 6 — Profanity Guardrails (2)
*Domain: Content Safety · LLM moderation + NeuralSeek-native filter*

35. Filter Mode (LLM moderation / NeuralSeek filter / off)
36. Blocked Reply Text

---

### Category 7 — Attribute Protection Guardrails (1)
*Domain: Brand Safety · Misinformation tolerance*

37. Misinformation Tolerance slider (Rigid ↔ Standard)

---

### Category 8 — Intent & Routing Guardrails (7)
*Domain: Orchestration · Intent classification and multi-agent routing*

38. Match Type (Exact / Vector Similarity / Fuzzy / Keyword / Fuzzy Keyword)
39. Intent Match Threshold %
40. Edit Cache
41. Normal Cache
42. Multi-Agent routing
43. Cache Context
44. Cache KB

---

### Category 9 — Hybrid Search Guardrails (4)
*Domain: Grounding · ELSER + KNN + Re-Sort*

45. Query Type
46. ELSER (toggle + model ID + embedding field)
47. KNN Vector query
48. Re-Sort priority values

---

### Category 10 — LLM Control Guardrails (12)
*Domain: Orchestration · Per-call, per-model behavior*

49. Temperature
50. Top-P
51. Frequency Penalty
52. Max Tokens
53. Min Tokens
54. Streaming
55. Per-Call model selection
56. Model selection
57. Cache
58. Prepend
59. Images (multimodal)
60. Timeout

---

### Category 11 — Memory Guardrails (6)
*Domain: Session Governance · Per-tenant isolated*

61. LG Timeout
62. Context Turns (conversation depth)
63. Session TTL
64. User TTL (per-tenant isolated)
65. Context Detect
66. Force Context

---

### Category 12 — Multi-Language Guardrails (2)
*Domain: Localization · Auto-detect any language*

67. Cross Language toggle
68. Default Language

---

### Category 13 — Output Rendering Guardrails (8)
*Domain: Channel Delivery · Chat-widget, voice, telephony-ready*

69. Relax Filters
70. Stream Plan
71. Log Alt
72. VA Format (voice-agent / telephony)
73. Embed Links
74. Unique Links
75. Stopwords
76. HTML Clean

---

### Category 14 — Audit & Compliance Guardrails (10)
*Domain: Governance · Every change versioned, attributed, exportable*

77. Corp Filter
78. Corp Logging
79. Logger Type
80. Endpoint
81. Prompt Logging
82. Hide Keys (auto-redaction)
83. **Configuration Version Control — Git-style versioning of every config change** *(NEW)*
84. **Configuration Diff & Rollback — visual redline diffs, point-in-time rollback** *(NEW)*
85. **Cache Savings Tracking & ROI Reporting — quantifies prevented spend** *(NEW)*
86. **ISO 42001 / NIST AI RMF Compliance Mapping** *(NEW)*

---

### Category 15 — Prompt Engineering Guardrails (3)
*Domain: Authoring · Template-level, per-intent, per-agent*

87. Custom Prompt builder (secrets + variables + system vars)
88. Instructions
89. Regex Rules (applied input AND output)

---

### Category 16 — Secrets & Credential Guardrails (2)
*Domain: Security · 6 vault back-ends, BYOK/HYOK*

90. Secret Name
91. Secret Value (with vault-backed runtime resolution)

---

### Category 17 — Model-Agnostic Guardrails (13)
*Domain: Orchestration · API / Workflow / Platform-level swap + bake-off*

92. API-level model swap (single parameter)
93. Workflow-node-level model selection
94. Platform-level default LLM
95. Built-in LLM bake-off (any number of LLMs side-by-side)
96. Accuracy comparison metric
97. Latency comparison metric
98. Cost-per-call comparison metric
99. Hallucination rate comparison metric
100. Confidence comparison metric
101. Token usage comparison metric
102. Workflow A/B comparison
103. Cost projection (savings quantification)
104. Exportable comparison reports

---

### Category 18 — Red Team & Rogue AI Guardrails (14)
*Domain: Adversarial Defense · Built-in suite, continuously updated*

105. Built-in adversarial test suite
106. Prompt Injection test bucket
107. Data Exfiltration test bucket
108. SQL Injection test bucket
109. Unauthorized Access test bucket
110. Service Disruption test bucket
111. Continuous threat-intel updates
112. Self-serve on-demand execution
113. Pass/fail scoring report (per agent)
114. AI-generated remediation guidance
115. Runtime attack detection
116. Rate limiting
117. Abuse detection
118. DDoS protection

---

## What changed from the 112 count

Six guardrails were broken out as line items in this revision — they were implicit in earlier work but never enumerated. All six are marked **(NEW)** above. They are:

| # | New Line Item | Category | Source |
|---:|---|---|---|
| 17 | Hallucinated Term Allowlist — closed-loop remediation | Hallucination Prevention | Surfaced in Seek Governance / Semantic Insights analysis |
| 22 | Indirect Prompt Injection Protection | Prompt Injection | Previously buried under Red Team #11 |
| 83 | Configuration Version Control | Audit & Compliance | Surfaced in Configuration Insights analysis |
| 84 | Configuration Diff & Rollback | Audit & Compliance | Surfaced in Configuration Insights analysis |
| 85 | Cache Savings Tracking & ROI Reporting | Audit & Compliance | Surfaced in mAIstro Token Insights analysis |
| 86 | ISO 42001 / NIST AI RMF Compliance Mapping | Audit & Compliance | Surfaced in your earlier compliance answer |

---

## Headline stats (for marketing use)

| Stat | Number |
|---|---|
| **Total AI guardrails** | **118** |
| **Guardrail categories** | **18** |
| **LLMs supported** | **120+** |
| **LLM providers** | **9** |
| **PII detector categories** | **13** |
| **PII enforcement actions** | **5** |
| **Compliance frameworks supported** | **5** (HIPAA, CCPA, SOC 2, ISO 42001, NIST AI RMF) |
| **Adversarial attack buckets red-teamed** | **5** |
| **Vault back-ends supported** | **6** |
| **Log export destinations** | **4+** (S3, Splunk, Datadog, customer SIEM) |
| **Languages supported** | **All** (auto-detect) |
| **Audit attribution coverage** | **100%** |

---

## Headline copy options

- **"118 AI Guardrails. 18 Categories. Every One Auditable."**
- **"The AI Guardrail Suite Enterprise Buyers Actually Demand."**
- **"Built from thousands of regulated-sector go-lives."**

---

## To validate

The 6 additions are my best-judgment line items from our earlier conversations. Quick yes/no on each:

1. **Hallucinated Term Allowlist** as a Hallucination Prevention guardrail — yes/no?
2. **Indirect Prompt Injection Protection** as its own line under Prompt Injection (vs. only under Red Team) — yes/no?
3. **Configuration Version Control** as an Audit guardrail — yes/no?
4. **Configuration Diff & Rollback** as an Audit guardrail — yes/no?
5. **Cache Savings Tracking & ROI Reporting** as an Audit guardrail — yes/no?
6. **ISO 42001 / NIST AI RMF Compliance Mapping** as an Audit guardrail — yes/no?

If you wanted different additions to hit 118, send me the list and I'll re-slot them.
