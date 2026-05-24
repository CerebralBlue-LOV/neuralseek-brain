---
title: Itochu — Hybrid RAG Financial Intelligence with 107 Agents
summary: >-
  Itochu International (Japan's big-5 sogo shosha, ~$90B revenue) deployed NeuralSeek-built hybrid RAG financial intelligence: 107 specialized agents combining SEC EDGAR filings, live web research, and private documents — orchestrated inside Itochu's environment with Microsoft Entra SSO, JWT validation, and per-tenant document isolation.
tags: [client-story, itochu, japan, trading, sogo-shosha, financial-services, hybrid-rag, multi-agent, deep-dive]
source: itochu.pdf
---

NEURALSEEK × ITOCHU INTERNATIONAL




 TRADING / SOGO SHOSHA


       ITOCHU INSIGHT — HYBRID RAG FINANCIAL INTELLIGENCE WITH 107 SPECIALIZED
       AGENTS


107 agents. One intelligence platform for Itochu — built
on NeuralSeek.
Hybrid RAG-powered financial intelligence combining SEC EDGAR filings, live web research, and
private documents — orchestrated through a graph of 107 specialized agents. Deployed inside
Itochu's environment with Microsoft Entra single sign-on, JWT-validated sessions, and per-tenant
document isolation.



   ANNUAL REVENUE

   ~$90 B
   Approx. FY revenue (~¥14T) — one of Japan's largest corporations by sales.



   EMPLOYEES

   120,000 +
   Across the global Itochu group and subsidiaries.



   MARKET POSITION

   Big 5
   Fortune Global 500 member and one of Japan's "big-5" sogo shosha general trading houses.




       VOICE OF THE CLIENT
In Tony's words — a conversation with our partner at Itochu
International.
A short Q&A with Tony Chang on working with NeuralSeek through this engagement.




   DIRECTOR, IT STRATEGY DIVISION

   Tony Chang
   Tony directs IT strategy at Itochu International and runs the Itochu Insight engagement with NeuralSeek — a
   107-agent financial intelligence platform deployed inside Itochu's Azure environment.

        VIEW LINKEDIN
Q1   What parts of NeuralSeek impress you?
The speed and flexibility of their low-code, no-code development platform stand out. We were able
to leverage our Azure cloud infrastructure effectively, and the deep research in full mode is quite
fast. They accommodated our use case well, and the ability to make quick fine-tuning changes has
been especially helpful for the project.



Q2   Thoughts on NeuralSeek having an implementation arm and experience doing
     enterprise go-lives.
The implementation team for the POC has been excellent. They were highly responsive in making
changes and resolving bugs. The onboarding process and project management helped accelerate
the project's kickoff. The team also demonstrated a forward-thinking approach, developing the
application with scalability in mind.



Q3   General feedback on our team.
Overall, it has been a positive experience, and we're glad we started this engagement.




ABOUT ITOCHU INTERNATIONAL


  Sogo Shosha                                        Azure Cloud
  DIVERSIFIED GENERAL TRADING COMPANY                DEPLOYMENT — IN ITOCHU'S EXISTING AZURE
                                                     TENANT



  Est. 1858                                          Tokyo, Japan
  OVER 165 YEARS OF TRADING HISTORY                  HQ; OPERATIONS ACROSS 60+ COUNTRIES



  Public (TYO: 8001)                                 Fortune Global 500
  LISTED ON THE TOKYO STOCK EXCHANGE                 AMONG THE WORLD'S LARGEST COMPANIES
  "Overall, it has been a positive experience, and we're glad we started
  this engagement."
  DIRECTOR, IT STRATEGY DIVISION            Tony Chang · Itochu International




        WHAT'S INSIDE THE ENGAGEMENT                                                                      5 CASES


Use cases delivered for Itochu International.

   01   Hybrid RAG financial intelligence
  A unified retrieval layer that blends SEC EDGAR filings, live web research, and Itochu's private documents —
  with BM25 plus dense vectors so answers stay precise whether the source is a 10-K footnote or an uploaded
  PDF.

   BM25 + VECTOR        SEC EDGAR       PRIVATE DOCS




   02   107-agent orchestration
  Two LangGraph workflows — a Main Orchestrator that resolves a company and fans out to ingestion,
  search, and analysis sub-agents, and a Reports Orchestrator that drives the Summary, Longitudinal, Risk,
  and Peer Comparison decks through parallel section agents with a shared variable store.

   LANGGRAPH       107 AGENTS       SHARED STORE




   03   5-year XBRL financial dashboard
  Revenue, margins, EBITDA, and ROE pulled directly from SEC EDGAR XBRL, with YoY deltas and per-metric
  trend charts. Every metric documents its source filing (10-K / 20-F / 40-F / 10-Q / 6-K) and whether it was
  reported or derived.

   XBRL      YOY DELTAS       CITED FILINGS
 04   Cited, multi-source agent chat
Analysts toggle between Quick Scan and Deep Research modes. Every response blends SEC filings, web
research, and uploaded documents — with inline source attribution so reasoning is auditable back to the
original artifact.

 QUICK + DEEP       INLINE CITATIONS        AUDITABLE




 05   Report generation — PDF & editable PPTX
On demand, the Reports Orchestrator assembles four deck types and deterministically stitches them into
polished PDFs and editable PowerPoint files — ready to drop into an Itochu analyst workflow without post-
processing.

 PDF + PPTX       4 DECK TYPES       DROP-IN READY




107                         8                            5 yrs                        4
SPECIALIZED                 AGENT                        XBRL FINANCIAL               REPORT DECKS ON
AGENTS                      CATEGORIES                   HISTORY                      DEMAND




                       NS · BRAND SYSTEM · 2026.05            Quietly engineered.       V 2.0 — REGULATED
