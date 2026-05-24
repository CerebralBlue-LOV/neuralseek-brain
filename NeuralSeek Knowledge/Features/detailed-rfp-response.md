---
title: Detailed RFP Response
summary: >-
  NeuralSeek's response to a detailed RFP — covers LLM-agnostic orchestration, integrations (OpenAI Enterprise, Azure GPT-4.5, Claude, Gemini), policy enforcement, semantic scoring, token tracking, and frontend flexibility (ChatGPT, Copilot, custom web apps, Slack).
tags: [features, rfp, integrations, openai, azure, claude, gemini, orchestration]
source: Detailed RFP Response.pdf
---

                             NeuralSeek Alignment to Project Scope & Specifications

Core Integrations              NeuralSeek is an LLM-agnostic orchestration platform that serves as the governance and control layer
                               between any frontend experience (such as ChatGPT, Azure Copilot, custom web applications, or even
Does your platform support     enterprise messaging platforms like Slack) and backend LLMs including OpenAI Enterprise, Azure-hosted
integration with OpenAI        GPT-4.5, Claude, Gemini, and others. This flexibility allows organizations to deliver ChatGPT-style or
(Enterprise) and Azure         other conversational AI experiences through virtually any user interface, while maintaining centralized
Copilot?                       governance and operational control.

                               The platform’s architecture enables seamless model routing, policy enforcement, and semantic scoring
                               regardless of the UI or model in use. NeuralSeek allows AI agents to dynamically interact with multiple
                               LLMs within a single workflow, track token-level usage for cost and performance optimization, and
                               enforce strict guardrails to ensure responsible AI deployment. NeuralSeek integrates, powers, and governs
                               these end-to-end AI experiences across the enterprise, connecting any chosen interface to any underlying
                               model with full security, compliance, and observability.




                                                                                                                                 9
Core Integrations              Yes. NeuralSeek supports integration with Salesforce Agentforce through API-based orchestration. Our
                               platform enables agents to read from and write to Salesforce objects, trigger automations, and interact with
Can your solution integrate    Apex APIs as part of broader Retrieval-Augmented Generation (RAG) or multi-step task workflows. With
with Salesforce Agentforce?    the ability to integrate, we do have a strong competitive advantage over agentforce (per customer
                               feedback):

                               NeuralSeek was chosen over Agentforce in recent head-to-head evaluations due to several architectural and
                               performance advantages:
                               • Latency & Performance: While Agentforce knowledge queries often exceed 18 seconds, NeuralSeek
                               consistently delivers sub-3 second responses, ensuring a fast, seamless user experience that scales under
                               enterprise load.
                               • Retriever Efficiency: Unlike Agentforce’s slow, two-step retriever (DataCloud → database), NeuralSeek
                               uses direct, high-performance vector and semantic retrieval pipelines, eliminating unnecessary delay and
                               reducing failure points.
                               • Modular Transparency: Agentforce lacks workflow visibility, making customization difficult. In contrast,
                               NeuralSeek provides drag-and-drop orchestration, real-time tracing, and semantic scoring dashboards,
                               giving business and technical users full control over every step of the agent’s behavior.
                               • Agent-to-Agent Collaboration: Agentforce is still struggling with basic agent-to-agent communication and
                               is attempting to redesign this with Google’s support. NeuralSeek, by contrast, has native multi-agent
                               orchestration via ProPacks, allowing for parallelism, decision handoff, and dynamic logic without code.

                               NeuralSeek’s design is faster, more transparent, and significantly more flexible; making it a superior choice
                               for organizations seeking agility, performance, and governance in AI-driven Salesforce integrations.
Core Integrations              Yes. NeuralSeek supports SSO integration with Okta, Active Directory, and LDAP via SAML 2.0.
                               Role-based access and group-based policy controls are supported.
Does your platform support
Active Directory
(AD)/LDAP and Okta for
identity and access
management?
Core Integrations              Yes. AD/LDAP groupings can be used to enforce Guardrail policies, prompt filters, and workflow access
                               by syncing directory groups with NeuralSeek roles or categories.
Can your platform reflect
### Bank’s AD/LDAP
groupings for prompt policy
enforcement?
Core Integrations           Yes. NeuralSeek supports integration with custom or fine-tuned models hosted on OpenAI, Azure, AWS
                            Bedrock, or any third-party endpoint. This also includes self hosted models. This flexibility enables
Can your platform integrate organizations to tailor AI models to their specific needs, enhancing output relevance, accuracy, and domain
with custom LLMs or         alignment. NeuralSeek also allows agents to toggle between different LLMs to optimize for performance,
fine-tuned models hosted on speed, quality, or cost, while supporting model specific orchestration, validation, and fallback logic to
Open AI or any other Gen    ensure reliable, high quality results across use cases.
AI?
Core Integrations            Yes. In NeuralSeek, the full prompt, response, and all associated metadata can be exported and imported in
                             structured formats, allowing institutions to either use NeuralSeek as the system of record for all AI-driven
Do you support API-based     interactions or feed this data into other enterprise systems. For banking environments, this capability is
integration with third-party particularly valuable for meeting stringent regulatory, audit, and compliance requirements.
policy engines or governance
tools? The prompt or other By retaining a complete lineage of every AI transaction, including the original input, model routing, applied
policies can be exported or  guardrails, retrieved source materials, and the final output; banks can demonstrate accountability and
imported?                    transparency to regulators such as the OCC, FINRA, and the CFPB. This audit-ready data can be integrated



                                                                                                                                   10
                                into core banking systems, case management tools, or compliance platforms to support risk reviews, dispute
                                resolution, and customer service investigations.

                                Furthermore, the ability to import historical interaction data enables financial institutions to train or
                                fine-tune AI agents on domain-specific workflows, ensuring that responses remain accurate, compliant, and
                                aligned with institutional policies. Whether the goal is to preserve records for a mandated retention period,
                                conduct forensic analysis on a disputed interaction, or enrich enterprise data lakes for analytics, NeuralSeek
                                ensures that all AI interactions are captured, portable, and securely managed in accordance with banking
                                industry standards.


                                For the integration with “third-party policy engines or governance tools”, could you share any specific tools
                                you are referring to, or examples that reflect the intended use case?
                                The example is Microsoft Entra (our preference). Another example is SailPoint.
                                If these policies can be access through APIs for the identity flow in future, including Agentic AI (for
                                different departments that introduces new applications with agentic AI capabilities).
                                Policy import/export in formats such as JSON, PAML, YAML, or XML for integration with compliance,
                                risk, or policy automation, in case ### decide to centralize identity governance, including for GenAI and
                                Agentic AI.
Access & Permissions        Yes. NeuralSeek is a multi-agent, agentic AI platform that organizes and directs responses based on query
                            context, ensuring that every interaction is handled by the most appropriate agent or workflow. Each routing
Do you offer automated      pathway can be customized with banking-specific rules, regulatory safeguards, internal compliance
policy enforcement based on policies, and approved data sources; enabling precise control over how information is retrieved, processed,
prompt content              and delivered.
classification?
                            For financial institutions, this means customer inquiries, internal risk assessments, fraud investigations, and
                            compliance checks can be routed through tailored, policy-aligned AI agents that meet OCC, FINRA, FDIC,
                            and FFIEC requirements. Sensitive processes such as loan underwriting, transaction monitoring, and
                            KYC/AML verifications can be bound to dedicated agents with strict access controls, auditable
                            decision-making, and built-in guardrails to prevent policy breaches. By aligning AI agent routing with
                            banking governance frameworks, NeuralSeek ensures both operational efficiency and regulatory
                            compliance at scale.
Access & Permissions            Yes. NeuralSeek can enforce real-time access control for Confluence content when used in Generative AI
                                or Agentic AI prompts, ensuring that users can only access and analyze documents they are authorized to
Does your platform support      view. When Confluence is used as a ground truth source for LLM calls, NeuralSeek can connect to an
role-based access to            external rules engine, or leverage its own RBAC and data source permission controls, to perform a final,
Confluence documents?           real-time permissions check before any document is passed to the LLM.

                                If documents are queried directly by AI agents, NeuralSeek supports structuring calls so that the user’s
                                identity, role, and permissions are passed with the query, ensuring responses are generated only from
                                content the user is entitled to access. This approach aligns with ###’s stringent security policies, mitigates
                                unauthorized access risks, and supports licensed tool governance. While ### is not currently using
                                Atlassian Intelligence, NeuralSeek’s architecture allows for future integration if desired, without
                                compromising existing security enforcement.




                                                                                                                                       11
Access & Permissions        Yes. NeuralSeek integrates with Confluence through API calls, enabling direct access to documents. It can
                            retrieve and return information from these documents and provide a secure link to the source document,
Can users access Confluence supporting user queries or intelligent search.
documents through secure
links rather than uploads?




Access & Permissions          NeuralSeek enables administrators in financial institutions to control access to Agentic AI platforms (such
                              as Lattice, Salesforce Einstein, Azure Copilot, and others) based on user roles, prompt content, or
Can your platform restrict    integration policies, ensuring compliance with strict banking governance and security requirements.
or allow access to specific   Administrators can configure guardrails to allow or block specific AI platforms depending on the
Agentic AI platforms (e.g.,   sensitivity of the prompt or the permissions associated with the requesting user. Each AI agent can be
Lattice Agentic AI)?          directed to interact only with approved systems, such as allowing access to AWS Bedrock while blocking
                              non-compliant platforms like Lattice, aligning AI usage with institutional policy and vendor risk
                              frameworks. Access can also be restricted by department or tenant, limiting certain AI endpoints to
                              authorized banking functions such as compliance, risk management, or fraud detection. All access attempts
                              to restricted platforms are fully logged for audit purposes, with optional alerts or human-in-the-loop
                              reviews for exceptions. Through its API, NeuralSeek supports advanced enforcement measures such as
                              token-based access control and endpoint whitelisting or blacklisting, providing banks with secure,
                              compliant, and controlled AI platform connectivity.




Access & Permissions          NeuralSeek is purpose-built for extensibility across departments, systems, and workflows, enabling
                              organizations to easily expand its capabilities to support internal, third-party, or hybrid agentic AI systems
Can the platform be           tailored to specific departmental needs. Its modular agent design allows for the creation of
extended for the other        department-specific agents grouped into collections aligned to distinct business functions (such as Legal,
agentic AI for specific       Finance, HR, or IT) that can operate independently or collaborate with other agents. Each agent can
department or the software    integrate with the software ecosystem unique to its department, whether that means connecting to Workday
with specific departmental    for HR, Salesforce for Sales, ServiceNow for ITSM, or custom in-house platforms. Access to knowledge,
purposes?                     model types, prompt templates, and policies can be restricted or customized by department, ensuring, for
                              example, that the Legal department enforces stricter semantic match thresholds and audit requirements than
                              Marketing. NeuralSeek’s open APIs and webhooks make it possible to integrate with other departmental AI
                              systems like Lattice, Azure Copilot, or Salesforce Einstein while maintaining centralized governance. The
                              platform’s role-based access control (RBAC) and multi-tenancy capabilities enable the creation of isolated
                              environments or tightly controlled access across departments, all managed from a unified administrative
                              interface. Additionally, department-specific dashboards and monitoring tools allow each team to track agent
                              performance, usage, and analytics separately, with full audit trails and system-wide observability.

                              In banking environments, this architecture supports precise segmentation of AI capabilities across critical
                              areas such as compliance, risk management, fraud detection, customer service, and lending operations. By
                              isolating data sources, enforcing department-specific guardrails, and integrating only with approved
                              banking systems, NeuralSeek ensures that each department operates within regulatory guidelines while
                              enabling enterprise-wide coordination, security, and governance.

Access & Permissions          Yes. NeuralSeek includes role-restrictions on the ability to view or modify prompts in the system.
                              Generally prompt/policy workflow is structured thru tiered environments, so changes are tested in a lower
Is there a role-based         environment before being approved and migrated up into a production environment.
approval workflow for
prompt policy changes?




                                                                                                                                  12
Security & Compliance          Yes. NeuralSeek fully supports Okta-based Single Sign-On (SSO) and user identity verification using
                               industry-standard protocols, including SAML 2.0 and OpenID Connect (OIDC). The platform integrates
Does your platform support     seamlessly with Okta Identity Cloud, enabling users to authenticate with their existing enterprise
Okta-based SSO and user        credentials. In addition to Okta, NeuralSeek’s SAML 2.0 and OIDC support ensures compatibility with a
verification?                  wide range of identity providers, such as Microsoft Entra ID (Azure AD), Ping Identity, and custom IdPs,
                               providing flexibility for diverse enterprise environments.




Security & Compliance         Prompt Interaction Logs
                              NeuralSeek logs every prompt submitted (whether via user interface, API, or embedded agent) capturing
Is there logging and activity key details including user ID and role, timestamp, input prompt, model response, model used (e.g., OpenAI,
monitoring for prompt usage Claude, custom endpoint), semantic match percentage, token usage, and latency. This ensures every
and model interactions?       interaction is traceable and auditable.

                               Model Interaction Tracing
                               The platform records all LLM invocations, allowing teams to monitor model selection, performance
                               metrics, token consumption, and fallback behavior. This visibility enables optimization of cost, efficiency,
                               and accuracy across all AI interactions.

                               Governance Dashboard
                               A centralized, role-based governance dashboard provides real-time monitoring of system performance,
                               semantic confidence trends, guardrail violations, and intent analytics. It also surfaces prompt classification
                               trends, giving administrators a complete picture of how AI is being used throughout the enterprise.

                               Audit Trail Export
                               All logs can be exported in JSON or CSV format and integrated with external SIEM tools such as Splunk
                               via webhook or API. This supports centralized monitoring and correlation with other enterprise security and
                               operational data.

                               Search & Filtering
                               Administrators can filter logs by user, date, intent, or agent, enabling targeted troubleshooting, forensic
                               investigations, or compliance validation. This makes it easy to pinpoint specific interactions or patterns for
                               review.

                               Relevancy for Banking
                               For banking institutions, these capabilities provide the rigorous logging, monitoring, and governance
                               required to meet OCC, FINRA, FDIC, and FFIEC compliance standards. Detailed prompt and model
                               tracking supports regulatory audits, risk management processes, and internal oversight, ensuring all AI
                               activity is transparent, controlled, and defensible.




                                                                                                                                     13
Security & Compliance         Live Prompt Activity Feed
                              NeuralSeek’s real-time monitoring dashboard displays incoming prompts and AI responses as they occur,
Can you provide real-time     including prompt text, user ID or source system, agent used, model invoked (e.g., OpenAI, Claude,
monitoring dashboards for     LLaMA), semantic match percentage, response latency in milliseconds, confidence scores, and any
prompt activity?              guardrail triggers. This immediate visibility allows teams to observe AI activity as it happens and quickly
                              detect anomalies or unusual usage patterns.

                              Semantic Insights Panel
                              The Semantic Insights panel provides trend analysis on semantic scoring, allowing organizations to
                              evaluate the quality and relevance of responses over time. It highlights high, low, and average semantic
                              match scores, identifies top-performing intents and agents, and categorizes prompts to reveal usage trends.

                              Governance Dashboard
                              A centralized governance tab offers full visibility into prompt volume by category or department, policy
                              violations, blocked responses, model utilization, token consumption, and performance outliers. This enables
                              authorized users to track KPIs and monitor system health from a single interface.

                              Filtering and Drill-Down
                              Administrators can filter data by date, agent, user, intent, category, or outcome, supporting both high-level
                              reporting and deep forensic investigations. This flexibility allows targeted analysis for compliance, security,
                              and performance tuning.

                              Integration Ready
                              The monitoring dashboard can push data to external systems through webhooks, APIs, or export in
                              CSV/JSON format for integration with enterprise tools such as Splunk, Power BI, or Cognos. This ensures
                              that AI activity data fits seamlessly into existing enterprise monitoring and analytics workflows.

                              Relevancy for Banking
                              In banking environments, this real-time monitoring capability is critical for ensuring compliance with
                              regulatory mandates from bodies such as OCC, FINRA, FDIC, and FFIEC. Banks can use the dashboard to
                              track AI usage by business unit, identify policy violations instantly, monitor model usage for cost control,
                              and maintain an auditable record of all AI interactions; supporting both operational efficiency and stringent
                              regulatory oversight.
Security & Compliance        Versioned Change Logs
                             NeuralSeek automatically versions and logs every change to model configurations, whether switching from
Can you provide audit trails OpenAI to Claude, updating a model endpoint, or modifying model selection logic. This creates a complete
for model changes (who,      historical record of all configuration adjustments.
what, when)?
                             Detailed Metadata
                             Each logged change captures who made the change (user ID and role), what was changed (e.g., model
                             name, API key, fallback order), when it was made (with timestamp and time zone), and where it was
                             applied (specific agent or global settings). This ensures complete traceability across the platform.

                              Rollback Capability
                              Administrators can roll back model configurations to any previous state using version history, minimizing
                              operational risk and enabling safe experimentation with different model setups.

                              Centralized Audit Log Access
                              All model change logs are accessible in the Governance tab, with filtering options by user, date range, and
                              change type, making it easy to review and validate configuration history.

                              Exportable for Compliance
                              Audit logs can be exported in CSV or JSON format for use by auditors, internal IT teams, or external



                                                                                                                                   14
                                regulators, ensuring smooth compliance reporting.

                                Integration Support
                                Audit events can be forwarded to third-party systems such as Splunk, SIEM tools, or GRC platforms via
                                webhook or API, allowing seamless inclusion in enterprise compliance and monitoring workflows.
Security & Compliance        Guardrail Violation Alerts
                             NeuralSeek’s Guardrails Framework can automatically trigger alerts in real time when prompts or
Are there notification and   responses contain PII, profanity, or other sensitive content, fall below a configured semantic confidence
alerting capabilities based  threshold, trigger prompt injection or attribute protection filters, or violate role-based access policies and
on prompt policy violations? department-specific restrictions.

                                Configurable Alert Channels
                                Alerts can be delivered through multiple channels, including email distributions (e.g.,
                                compliance@company.com), Slack, Microsoft Teams, webhooks, custom API endpoints, and SIEM
                                platforms such as Splunk, LogRhythm, or Securonix, ensuring they reach the right stakeholders
                                immediately.

                                Severity & Action Mapping
                                Each violation can be tagged by severity level, allowing differentiated responses such as blocking the
                                output, escalating to human review, logging silently for later audit, or notifying the relevant departmental
                                lead or compliance officer.

                                Governance Dashboard Visibility
                                All violations are also displayed in the Governance tab, where authorized users can filter by date, user,
                                intent, category, or action taken, providing a centralized view of compliance-related incidents.

                                Audit Logging of Alerts
                                Every alert is timestamped, fully traceable, and exportable in CSV or JSON, supporting internal reviews
                                and meeting regulatory audit requirements.

                                Relevancy for Banking
                                In banking environments, this capability enables proactive enforcement of OCC, FINRA, FDIC, and FFIEC
                                compliance by ensuring any policy breaches or high-risk AI interactions are immediately detected, properly
                                escalated, and fully documented for regulatory examination.




                                                                                                                                     15
Security & Compliance         Semantic & Behavioral Anomalies
                              NeuralSeek’s AI agents continuously monitor for irregularities in AI activity, detecting issues such as
Does your platform support    unexpected spikes in prompt volume, sudden drops in semantic match confidence, repeated guardrail
anomaly detection and         violations, use of unapproved prompt intents or agents, and latency or cost outliers in LLM usage. This
incident response             proactive monitoring helps identify potential misuse, performance degradation, or security risks in real
workflows?                    time.

                              Configurable Thresholds & Alerts
                              Administrators can define custom thresholds (such as more than five failed prompts within one minute or a
                              semantic score falling below 50%) to trigger immediate alerts and automated workflow actions. This
                              flexibility allows organizations to tailor anomaly detection to their operational and compliance
                              requirements.

                              Incident Response Workflow Support
                              Through webhook and API integration, NeuralSeek connects with enterprise ITSM tools like ServiceNow,
                              Jira, PagerDuty, and custom SOAR platforms to initiate ticket creation, escalate issues to security or
                              compliance teams, and even quarantine specific agents or prompts. This ensures rapid and coordinated
                              responses to detected anomalies.

                              Auto-Mitigation Options
                              NeuralSeek can automatically block or pause agent activity, route flagged interactions to a
                              human-in-the-loop review process, or log anomalies for later post-mortem analysis. These capabilities
                              reduce the risk of ongoing impact while ensuring incident containment.

                              Audit & Post-Incident Logging
                              Every anomaly and corresponding response action is logged with complete metadata, supporting root cause
                              analysis, internal reporting, and regulatory compliance documentation.




Security & Compliance         Yes. NeuralSeek integrates seamlessly with Splunk to share logs through three straightforward methods,
                              making it easy to monitor user activities and system performance. Using the HTTP Event Collector,
Is there Splunk integration   NeuralSeek can send logs (such as user questions, system responses, and activity details) directly to Splunk
for centralized logging?      over a secure internet connection. For on-premise deployments, the platform can save logs as files, similar
                              to a spreadsheet of activity records, which Splunk can automatically collect and forward to a central
                              dashboard for review. Additionally, NeuralSeek supports direct API-based connections, allowing Splunk to
                              pull specific logs on demand, giving administrators precise control over which data is shared for monitoring
                              and analysis.




                                                                                                                                 16
Security & Compliance        Custom Retention Policies
                             NeuralSeek allows administrators to define tailored retention periods for prompt and response history,
Are backup and retention     model interaction logs, audit trails, and KnowledgeBase indexing or source content. Retention rules can be
policies configurable?       scoped by deployment type (SaaS vs. on-premise), user role, or data category, such as PII, financial data, or
                             internal-only content, ensuring alignment with internal governance and compliance mandates.

                             Automated Backups
                             The platform supports automated, scheduled backups of agent configurations, workflows, guardrail and
                             policy settings, KnowledgeBase content, and system metadata or audit logs. These backups can be securely
                             exported or stored in customer-controlled environments, including cloud storage, secure file systems, or
                             on-premise infrastructure.

                             Data Deletion & Archiving
                             NeuralSeek includes built-in tools to delete prompt history and logs manually or automatically after the
                             retention period expires, archive data to external systems for long-term storage or regulatory hold, and
                             anonymize or mask sensitive content prior to retention for privacy compliance.

                             Deployment-Specific Configuration
                             SaaS deployments come with default retention periods that can be customized, while on-premise
                             deployments provide customers with full control over data lifecycle management, from retention to
                             deletion.

                             Compliance Alignment
                             Retention and backup policies can be configured to meet GDPR, HIPAA, SOC 2, and industry-specific
                             regulations through custom policy profiles, ensuring that data governance aligns with both enterprise
                             policies and regulatory requirements.

Security & Compliance        Yes, NeuralSeek gives administrators complete control over managing prompt history with flexible options
                             for data retention. By default, prompts are deleted after 30 days, but admins can customize this from 1 day
Can administrators delete,   to 10 years to match company policies or regulations. Admins can manually delete specific logs, remove
clean, and archive prompt    multiple logs by date or category, or set up automatic deletion rules. For compliance or long-term storage,
history?                     prompt history can be securely archived in NeuralSeek or exported to systems like cloud storage, data
                             lakes, or SIEM tools. This ensures data privacy, compliance with regulations like GDPR or HIPAA, and
                             keeps only necessary data.




                                                                                                                                 17
Security & Compliance        Role-Based Access Control (RBAC)
                             NeuralSeek enforces fine-grained user permissions across all Gen AI and agentic AI operations, including
How does your platform       access to agents, prompt templates, guardrails, knowledge bases, and model configurations. Administrators
ensure Gen AI or Agentic     can assign roles such as Viewer, Editor, Approver, or Admin, mapped directly to internal identity providers
model security (permissions, like Okta, LDAP, or Active Directory, ensuring alignment with existing enterprise identity management
audit logs, alerts)?         policies.

                               Guardrail Enforcement & Prompt Filtering
                               The platform’s built-in guardrails automatically block or modify prompts and responses to prevent unsafe
                               or non-compliant model usage. Protections include PII detection, prompt injection prevention, semantic
                               confidence thresholds, inappropriate language or category filtering, and enforcement of policy restrictions
                               by user role or department.

                               Audit Logging & Change History
                               Every interaction with a model (from prompt submissions and model invocations to configuration changes)
                               is fully logged with details on who initiated the action (user or API key), what was changed or queried,
                               when it occurred (timestamped), and which agent or model was involved. Logs are tamper-proof,
                               exportable, and suitable for both regulatory and legal audit purposes.

                               Alerting & Notification System
                               NeuralSeek delivers real-time alerts for policy or guardrail violations, anomalous prompt activity such as
                               sudden spikes or misuse, and high-risk behavior or failed model calls. Alerts can be sent via email, Slack,
                               Microsoft Teams, or integrated into SIEM tools like Splunk for centralized monitoring.

                               Deployment Security Options
                               The platform supports on-premise, network-isolated, and SaaS deployments with strict access and
                               encryption controls, including TLS 1.2+ for data in transit, encryption for data at rest, and optional
                               customer-managed encryption keys.

Security & Compliance          Prompt Content Guardrails
                               NeuralSeek’s Guardrails Framework automatically detects and manages sensitive prompt content, including
Does your platform support     personally identifiable information (PII), protected health information (PHI), and financial or regulated
data privacy policies for      entity references. Detected content can be blocked, masked, or rerouted according to organizational
prompt content?                policies, ensuring compliance with internal governance and external regulations.

                               Data Classification & Filtering
                               Prompts and responses can be tagged with sensitivity labels (such as confidential, internal, or public) and
                               routed through custom workflows or excluded from logs and dashboards based on classification. This
                               supports precise data handling and segregation.

                               Retention Policy Controls
                               Administrators can define custom retention periods for prompt history and audit logs, automatically
                               deleting or archiving content after the designated time frame to minimize unnecessary data exposure.

                               Anonymization & Redaction
                               Prompt content can be anonymized or redacted before it is logged, archived, or shared, preserving privacy
                               while still maintaining analytical value for monitoring and reporting purposes.

                               Access Controls
                               Role-based access control ensures that only authorized users or departments can view prompt content, edit
                               templates, or retrieve prompt history, preventing unauthorized exposure of sensitive information.

                               End-to-End Encryption
                               All prompt content is encrypted both in transit (TLS 1.2+) and at rest. Optional on-premise or private-cloud



                                                                                                                                        18
                               deployments give organizations full control over data residency and access, supporting enterprise-grade
                               privacy requirements.
Security & Compliance          Real-Time Prompt Injection Detection
                               NeuralSeek leverages a dedicated Guardrail rule to scan all incoming prompts for known injection patterns,
Is secure input validation in  manipulation attempts, and adversarial tokens intended to bypass system instructions or alter model
place to detect injection or   behavior. This proactive check helps stop malicious activity before it reaches the model.
malicious inputs? How does
your platform handle          Injection Risk Classification
prompt injection attacks and Prompts are evaluated for attempts to override prior instructions (e.g., “Ignore the above and do X”), use of
context leakage?              delimiters or encoded instructions, and jailbreak phrasing such as “as an AI, you must…”. Flagged prompts
                              can be blocked, rerouted for human review, or automatically rephrased based on configuration settings.

                               Context Isolation per Session
                               The agentic execution architecture enforces strict session-level context boundaries, ensuring prompt
                               memory is cleared or scoped per interaction. This prevents context bleed or unintended data leakage
                               between users or agents.

                               Role-Aware Prompt Scoping
                               Access to sensitive prompts, documents, or system commands is managed through role-based filters,
                               preventing privilege escalation via prompt engineering techniques.

                               Output Guardrails to Prevent Leakage
                               Even if a malicious input passes initial checks, NeuralSeek applies semantic output validation to block or
                               sanitize responses containing sensitive information, PII or PHI, policy violations, or banned topics.

                               Continuous Monitoring & Alerting
                               All injection attempts are logged and can trigger real-time alerts to administrators or security teams. These
                               logs provide the foundation for incident response, root cause analysis, and regulatory audits.

                               In short, NeuralSeek combines preventive input validation, semantic risk scoring, and post-response
                               filtering to create a robust, multi-layered defense against prompt injection attacks and context leakage.




                                                                                                                                    19
Security & Compliance          Semantic Match Scoring
                               Every LLM response in NeuralSeek is evaluated using a Semantic Match percentage, which measures how
How is data integrity          closely the output aligns with the original source material in the connected KnowledgeBase. This provides
maintained (accuracy,          a real-time confidence score and flags potential inaccuracies or hallucinations.
cleanliness)?
                               KnowledgeBase Confidence & Coverage Metrics
                               NeuralSeek tracks two critical indicators to assess data completeness and relevance: KnowledgeBase
                               Confidence %, which measures how relevant retrieved documents are to the prompt, and Coverage %,
                               which gauges how comprehensive the supporting evidence is. These metrics help identify gaps, outdated
                               information, or insufficient source material.

                               Source-Backed Retrieval-Augmented Generation (RAG)
                               All responses can be traced directly back to their originating sources, ensuring outputs are grounded in
                               validated enterprise content such as Confluence, SharePoint, Salesforce, or internal file systems. This
                               approach minimizes hallucinations and strengthens factual accuracy.

                               Automated Document Cleanliness Tools
                               When ingesting content into the KnowledgeBase, NeuralSeek applies preprocessing techniques including
                               OCR correction, noise and formatting cleanup, HTML/text normalization, and chunking/token
                               optimization. These processes ensure the stored data is clean, consistent, and optimized for AI retrieval.

                               Change Tracking & Version Control
                               All updates to agent logic, prompt templates, and KnowledgeBase content are version-controlled with
                               detailed metadata on who made the change, when it occurred, and what was modified. This maintains
                               integrity and accountability over time.

                               Guardrails & Output Validation
                               Guardrails enforce organizational accuracy thresholds and confidence score requirements. Outputs that fall
                               below these levels can be blocked or rerouted for review, ensuring that only reliable, policy-compliant
                               results are delivered.
Security & Compliance      Target SLA
                           NeuralSeek’s standard SaaS deployment offers a 99.9% uptime guarantee, excluding scheduled
What is your SaaS platform maintenance windows, ensuring continuous service availability for business-critical AI operations. Custom
uptime (availability       SLAs are available for enterprise and regulated environments that require higher assurance levels.
guarantees)?
                           Multi-Cloud Hosting
                           The platform is hosted across multiple major cloud providers, including AWS (primary SaaS environment
                           with multi-availability zone redundancy), Azure (available upon request for Microsoft-centric clients), and
                           IBM Cloud (commonly used for financial services or hybrid enterprise environments). This multi-cloud
                           approach ensures flexibility, resilience, and alignment with client infrastructure preferences.

                               Global Deployment Options
                               NeuralSeek supports regional hosting to meet data residency and latency requirements in jurisdictions such
                               as the US, EU, Canada, Asia-Pacific, and Latin America. This allows organizations to comply with local
                               regulations while optimizing performance for their user base.

                               High Availability Architecture
                               The platform’s architecture is designed for resiliency, featuring load-balanced clusters across multiple
                               availability zones, auto-scaling services to handle unexpected traffic spikes, redundant infrastructure for
                               database, storage, and AI inference layers, and continuous health checks with automated failover
                               mechanisms.

                               Monitoring & Alerting



                                                                                                                                    20
                               NeuralSeek maintains 24/7 infrastructure monitoring across all environments, with integrated alerting
                               systems tied to DevOps pipelines. This enables proactive incident detection and rapid response to maintain
                               service continuity.
Security & Compliance         Yes. All data transmitted through NeuralSeek is encrypted in transit using TLS 1.2 or higher, ensuring that
                              sensitive prompt content, model responses, and system interactions remain secure from interception or
Is data encrypted in transit? tampering.
Security & Compliance          Yes. NeuralSeek provides comprehensive DDoS protection as part of its SaaS platform, leveraging the
                               native defense capabilities of its cloud hosting providers, AWS Shield, Azure DDoS Protection, and IBM
Do you provide DDoS            Cloud Internet Services, depending on deployment. These protections are designed to automatically detect
protection?                    and mitigate large-scale volumetric, protocol, and application-layer attacks. In addition, NeuralSeek
                               implements its own rate limiting, API throttling, and traffic shaping controls to prevent abuse or system
                               overload. The platform supports integration with Web Application Firewalls (WAF) for further inspection
                               and blocking of malicious requests, and uses load balancing with auto-scaling to absorb legitimate traffic
                               spikes without compromising performance. All incoming traffic is monitored in real time, and alerts can be
                               routed to NeuralSeek’s operations team or the client’s security personnel for coordinated incident response.
                               Together, these layers of protection ensure the platform remains stable, secure, and available; even during
                               attempted denial-of-service attacks.
Security & Compliance          Yes. NeuralSeek maintains a valid SOC 2 Type II certification, underscoring its commitment to security,
                               availability, and confidentiality across all platform operations. The certification covers key Trust Service
Do you have a valid SOC 2      Criteria (TSC), including Security, with controls to protect against both physical and logical unauthorized
Type II certification?         access; Availability, ensuring systems are designed for reliability, resilience, and uptime in accordance with
                               defined SLAs; and Confidentiality, safeguarding sensitive data such as prompt history, user information,
                               and knowledge content through encryption, strict access controls, and comprehensive audit capabilities.


Security & Compliance          Yes, and we have current SOC-2 certification thru Drata. We have also had a penetration test conducted by
                               the Cybersecurity and Infrastructure Security Agency (CISA) of the U.S. Department of Homeland
Was a penetration test         Security. This independent security assessment evaluated the target environment’s resilience against
conducted in the last 12       real-world cyber threats, using a combination of automated scanning and manual exploitation techniques.
months?
                               Scope and Objectives
                               CISA performed a comprehensive review of the system’s security posture, including reconnaissance,
                               vulnerability identification, exploitation attempts, and post-exploitation analysis. The goal was to identify
                               weaknesses that could be leveraged by malicious actors and to assess the system’s overall defensive
                               capabilities.

                               Key Findings
                               The CISA Cyber Hygiene assessment found no vulnerabilities or security risks across the evaluated assets.
                               Specifically:
                               • 0 hosts were running unsupported software.
                               • 0 potentially risky open services were detected, including RDP, Telnet, SMB, FTP, SQL, and others.
                               • 0% of hosts were vulnerable, with no critical, high, medium, or low severity vulnerabilities identified.
                               • All assets (100%) were scanned, and no new vulnerabilities or risks were introduced.
                               • The maximum age of active critical and high vulnerabilities was 0 days, indicating that all findings are
                               addressed immediately upon detection.

                               This clean security profile reflects a strong security posture with no outstanding risks at the time of testing
                               (February 26, 2025), as verified by the U.S. Department of Homeland Security’s Cybersecurity and
                               Infrastructure Security Agency (CISA).

                               Remediation Guidance
                               CISA outlined zero specific corrective actions, including patch management, system hardening, access
                               control improvements, and to keep conducting ongoing monitoring practices.



                                                                                                                                      21
                               Conclusion
                               The CISA penetration test delivers a clear, authoritative evaluation of the NeuralSeek's security health and
                               provides a practical roadmap for addressing identified risks. This federally conducted assessment
                               underscores our commitment to maintaining a secure, resilient environment aligned with national
                               cybersecurity standards.
Security & Compliance          Code Security Audit (CerebralBlue dba NeuralSeek, August 2025)

Can you share a code testing This Code Security Audit was conducted by Aikido Security on behalf of CerebralBlue dba NeuralSeek to
report from the past year?   provide transparency and demonstrate secure software development practices from developer workstations
                             through to production infrastructure. The audit is based on real-time monitoring of code and infrastructure,
                             evaluating adherence to security best practices and identifying any potential vulnerabilities.

                               OWASP Top 10 Compliance
                               CerebralBlue maintains active security measures across most OWASP Top 10 risks, including:
                               - Broken Access Control, Cryptographic Failures, Injection, Security Misconfiguration, and Server-Side
                               Request Forgery – fully addressed with robust configuration, encryption enforcement, vulnerability
                               scanning, and preventive measures.
                               - Insecure Design, Vulnerable/Outdated Components, and Identification/Authentication Failures – actively
                               monitored, though not yet fully compliant.
                               - Software/Data Integrity Failures – mitigated via dependency lockfiles, controlled deserialization, and
                               secure code repositories.
                               - Security Logging/Monitoring Failures – mitigated with active email notification systems.

                               Security Scanning & Monitoring
                               CerebralBlue employs continuous security scanning across the following:
                               - Open-source dependencies: 2,484 JavaScript, 90 Java, 25 Go, and 31 Python packages monitored daily.
                               - OSS license compliance: 2,630 monitored weekly.
                               - Static application security testing (SAST), Infrastructure-as-Code scanning, and exposed secret detection
                               are all performed daily.

                               Findings (Past 3 Months)
                               - Open-source dependencies: 77 new findings, with 45 false positives and 9 resolved.
                               - Secrets in source code history: 137 new findings, with 85 resolved.
                               - Static App Security Testing: 141 new findings, with 70 resolved.
                               - Infrastructure-as-Code: 9 new findings, with 1 false positive.
                               - No new findings in container images, cloud configurations, VMs, mobile, malware, access controls, or
                               licenses.

                               Conclusion
                               The Aikido Security audit confirms that CerebralBlue dba NeuralSeek maintains strong foundational
                               security controls, robust monitoring across development and infrastructure, and active remediation
                               processes. While certain OWASP risk areas are still under monitoring rather than fully compliant, the
                               organization demonstrates a mature and proactive security posture suitable for enterprise and regulated
                               environments.




                                                                                                                                   22
Testing & Validation           Yes. NeuralSeek includes a built-in policy simulation environment that enables administrators and builders
                               to test prompt scenarios against configured guardrails and policy settings before deploying them into
Can you simulate prompt        production.
scenarios to test policy
enforcement before             “Try It Out” Sandbox Mode
deployment?                    Accessible from the Governance tab, this mode allows users to submit test prompts and see how guardrails,
                               semantic scoring thresholds, PII filters, and other policies would respond, without affecting live users or
                               production logs.

                               Policy Behavior Preview
                               The simulation clearly indicates whether a prompt would be allowed, blocked, or flagged for review,
                               whether it would trigger semantic confidence failures, violate profanity or attribute tolerance filters, or
                               require routing to a human-in-the-loop (HITL) process.

                               Version-Aware Testing
                               Teams can run simulations against draft or in-review configurations, ensuring that policy and guardrail
                               changes are validated before being applied to production agents.

                               Traceable Testing Logs
                               All simulations are timestamped and can be stored for documentation, training, or internal review, creating
                               a clear record of testing outcomes.
Testing & Validation         Yes. NeuralSeek provides dedicated sandbox environments that allow organizations to safely test
                             integrations, prompt logic, AI agent workflows, and policy configurations without affecting production data
Is there support for sandbox or users. These sandbox instances mirror the full functionality of the production environment (including
environments for testing     access to Guardrails, KnowledgeBases, multi-agent orchestration, and LLM integrations) enabling thorough
integrations and policies?   end-to-end testing of custom configurations, external APIs, and data sources. Teams can simulate prompt
                             behavior, validate access controls, and evaluate policy enforcement outcomes in a controlled setting. This
                             ensures that deployments are secure, reliable, and compliant before going live, and provides a safe space for
                             experimentation, onboarding, and continuous improvement.
Testing & Validation          Yes. NeuralSeek offers automated regression testing capabilities to ensure consistent prompt behavior
                              across different model versions and configurations. When organizations switch or upgrade LLMs (such as
Do you offer automated        moving from GPT-4 to Claude, LLaMA, or a fine-tuned internal model) NeuralSeek allows teams to rerun
regression testing for prompt historical prompts against the new model setup. The platform then compares outputs using semantic match
behavior across model         scoring, confidence thresholds, and policy compliance to identify any unexpected changes, hallucinations,
versions?                     or drops in response quality. This allows enterprises to validate that new models perform within acceptable
                              bounds before deployment. These tests can be conducted in sandbox environments and logged for audit,
                              review, or regulatory reporting; ensuring safe, reliable model evolution without risking production
                              instability.
Operational Scalability        NeuralSeek is built for high concurrency and enterprise scalability, capable of supporting thousands of
                               concurrent users and prompt executions in both SaaS and on-premise deployments. In SaaS environments,
What is the maximum            NeuralSeek runs on auto-scaling containerized infrastructure across AWS, Azure, and IBM Cloud, allowing
number of concurrent users     it to dynamically handle large volumes of simultaneous prompt traffic across multiple agents and
or prompts your platform       departments. The backend is designed to scale horizontally; ensuring low-latency responses even during
can support (SaaS or           traffic spikes or high-throughput events.
On-premise)?
                               For on-premise or network-isolated deployments, the platform’s concurrency limits are determined by the
                               customer’s infrastructure capacity. However, NeuralSeek supports multi-node and multi-region clustering,
                               allowing organizations to scale performance as needed based on available compute, network, and storage
                               resources. In real-world production scenarios, NeuralSeek has supported enterprise-scale deployments
                               involving 10,000+ users, with no degradation in performance when properly resourced. Detailed sizing
                               recommendations and performance tuning guidance are provided during implementation based on expected
                               usage patterns.




                                                                                                                                      23
Operational Scalability       Yes. NeuralSeek is designed to scale horizontally across regions, business units, and deployment zones,
                              supporting both centralized governance and localized autonomy. Whether deployed in the cloud or
Can you scale horizontally    on-premise, the platform supports multi-region clustering and multi-tenant architecture, enabling
across regions or business    enterprises to isolate or share agents, data sources, policies, and infrastructure as needed.
units?
                              For global organizations, NeuralSeek can be deployed in multiple geographic regions (e.g., US, EU, APAC)
                              to meet data residency, latency, or compliance requirements. Each regional deployment can be managed
                              independently or connected through federated administration.

                              Across business units, NeuralSeek allows different teams or departments to operate their own AI agents,
                              Guardrails, KnowledgeBases, and prompt policies, while still reporting into a centralized monitoring and
                              governance layer. This structure supports large-scale rollouts where different units require tailored
                              functionality but with enterprise-wide control, auditability, and performance consistency.
Operational Scalability       Yes. NeuralSeek fully supports multi-tenancy with isolated data, policies, and agent configurations, making
                              it ideal for large enterprises, managed service providers, or any organization that needs to serve multiple
Is there support for          departments, clients, or environments from a single platform instance.
multi-tenancy with isolated
data and policies?            Each tenant within NeuralSeek can be configured with:
                              - Isolated KnowledgeBases – ensuring no data leakage across tenants
                              - Dedicated AI Agents and ProPacks – customized per use case or department
                              - Independent Guardrails and prompt policies – tailored to unique compliance or operational needs
                              - Role-based access control (RBAC) – enforcing strict permissions by tenant, role, or group
                              - Usage tracking and audit logs scoped to each tenant – enabling full transparency and chargeback reporting

                              Tenants can be deployed as logical partitions within a shared infrastructure or as physically isolated
                              deployments (e.g., across different regions or cloud accounts), depending on your security and regulatory
                              requirements.

                              This multi-tenant architecture enables NeuralSeek to serve multiple teams or clients concurrently, while
                              preserving strict data privacy, governance, and operational independence for each environment.
Integration &                 Yes. NeuralSeek supports integration with Salesforce’s AI-based chat and NLP systems, including
Interoperability              Salesforce Agentforce and Einstein GPT, through API-based orchestration and direct agent communication.
                              The platform can be embedded into Salesforce workflows to enhance chat experiences with real-time,
Does your platform support    context-aware responses grounded in enterprise knowledge, integrate with Salesforce Service Cloud or
Salesforce’s AI-based         Agentforce by reading and writing to Salesforce objects such as Cases, Contacts, and Opportunities, and
chat/NLP integration?         trigger actions or automations inside Salesforce based on AI-driven intent detection and guardrail-enforced
                              decisions. NeuralSeek can also use Salesforce data as a KnowledgeBase source, enabling AI agents to
                              generate accurate responses using the most up-to-date customer or product information, and embed directly
                              into Salesforce bots or digital experiences to improve self-service outcomes and reduce agent workload.
                              Additionally, Salesforce administrators can configure NeuralSeek workflows to align with existing CRM
                              logic, security roles, and field-level access controls, ensuring seamless interoperability and AI
                              augmentation within the Salesforce ecosystem without compromising governance or performance.




                                                                                                                                 24
Integration &                 Integration with Enterprise Data Lakes and Warehouses
Interoperability              NeuralSeek integrates with enterprise data lakes and data warehouses through both built-in connectors and
                              API-based integrations, supporting custom environments as needed. This allows AI agents to retrieve,
Can your platform integrate analyze, and generate responses based on real-time structured or unstructured enterprise data.
with enterprise data lakes or
warehouses?                   Supported Platforms
                              The platform supports native or API-based access to systems like Snowflake, Amazon Redshift, Google
                              BigQuery, and Azure Synapse for real-time querying. It also integrates with cloud data lakes such as
                              Amazon S3, Azure Data Lake Storage (ADLS), Google Cloud Storage, and Hadoop-based systems, as well
                              as relational databases like PostgreSQL, MySQL, Oracle, and SQL Server via direct queries or RESTful
                              API intermediaries.

                               AI Querying and Response Generation
                               AI agents can be configured to query live data, execute parameterized or semantic SQL, and interpret
                               results into natural language responses. If a direct integration is not available, NeuralSeek can connect via
                               custom APIs, webhooks, or middleware to ensure interoperability.

                               Governance and Access Control
                               Role-based guardrails and policy enforcement ensure that AI agents only access approved datasets and
                               adhere to governance frameworks. Different agents can be configured per department or business unit to
                               leverage unique data sources and generate domain-specific insights.

                               Intelligent Data Layer
                               With these capabilities, NeuralSeek serves as an intelligent conversational layer over enterprise data
                               infrastructure, bridging AI-driven interactions with trusted analytics systems via both native connectors and
                               open API integration pathways.
Integration &                  Guardrail-Based URL Filtering
Interoperability               NeuralSeek’s Guardrails Framework allows administrators to define blacklists or whitelists of URLs and
                               domains, ensuring agents never access or reference content from unauthorized or non-compliant sources
Can the platform block         during retrieval-augmented generation (RAG) workflows.
specific websites or IP
addresses from being           Input Sanitization & Response Scrubbing
accessed or used to generate   Prompt inputs containing blacklisted URLs or IP addresses can be automatically blocked, flagged, or
prompt responses across the    sanitized before reaching the LLM. Similarly, AI-generated responses can be filtered to remove or prevent
enterprise?                    references to banned sources.

                               Custom API-Based Logic
                               For more advanced enforcement, NeuralSeek supports API-based Guardrail extensions, allowing
                               integration with external threat intelligence or compliance feeds. This enables organizations to enforce
                               dynamic, centralized restriction rulesets.

                               LLM Input Routing Control
                               In use cases involving external document scraping or API augmentation, NeuralSeek can restrict which
                               endpoints agents are permitted to query or integrate with, ensuring LLM prompts do not rely on untrusted
                               or unverified third-party data.




                                                                                                                                     25
Integration &                   URL Blacklisting & Whitelisting via Guardrails
Interoperability                NeuralSeek’s Guardrails Framework enables administrators to define explicit allowlists or blocklists of
                                URLs, domains, or IP ranges. These rules can be applied at the category, intent, or agent level, providing
Can you enforce                 fine-grained control over what the AI can reference or link to during prompt processing and response
blacklist/whitelist rules for   generation.
websites or IPs used in
prompt responses?               Prompt & Response Filtering
                                If a prompt contains a blacklisted URL or references a blocked source, NeuralSeek can automatically block,
                                mask, or reroute the interaction. Likewise, if an LLM-generated response includes a link to a prohibited
                                site, the system can scrub, replace, or reject the response in real time.

                                Dynamic Rule Enforcement via API
                                For advanced governance requirements, NeuralSeek can integrate with external security or policy engines
                                via API to dynamically update and enforce blacklist/whitelist rules. This ensures continuous alignment with
                                evolving compliance mandates or threat intelligence feeds.

                                Audit & Monitoring
                                All blacklist and whitelist enforcement actions are fully logged with metadata capturing the violating
                                content, the triggering rule, and the action taken. These logs provide complete transparency and support
                                audit readiness for internal and regulatory reviews.
Model Management &              Yes. NeuralSeek provides robust support for model versioning, allowing organizations to manage, compare,
Transparency                    and roll back AI model configurations as needed. Administrators can track every change to model settings
                                (including provider, version, endpoint, and fallback logic) through detailed version histories that are fully
Can you manage model            auditable. When switching between LLM providers (e.g., OpenAI GPT-4, Claude, or fine-tuned internal
versioning (e.g., rollback,     models), NeuralSeek enables teams to run side-by-side comparisons using historical prompt data, supported
comparison)?                    by semantic match scoring and performance metrics. If a newer model version introduces regressions,
                                administrators can easily roll back to a previous configuration without downtime. This flexibility ensures
                                operational stability, supports testing and continuous improvement, and gives teams the control needed to
                                evolve their model strategy safely within production environments.
Model Management &             Yes. NeuralSeek provides detailed visibility into model metadata and performance metrics, enabling
Transparency                   organizations to monitor, compare, and evaluate the behavior of different language models used within the
                               platform. While access to the underlying training data depends on the model provider (e.g., OpenAI,
Is there visibility into model Claude, LLaMA), NeuralSeek delivers comprehensive operational insights into each model’s real-world
metadata (training data,       performance.
performance metrics)?
                               Semantic Match %
                               Measures how closely a model’s response aligns with the source data, offering a direct indicator of factual
                               accuracy.

                                KnowledgeBase Confidence & Coverage
                                Shows how well retrieved enterprise content supports the model’s answer, highlighting both relevance and
                                completeness.

                                Latency Metrics
                                Tracks average and outlier response times per model and agent, enabling teams to identify performance
                                bottlenecks.

                                Token Usage & Cost Metrics
                                Monitors consumption patterns and provides cost estimates for model usage across different workflows and
                                departments.

                                Prompt History & Model Selection Logs
                                Records which model was used for each interaction, along with any fallback paths taken when a model



                                                                                                                                    26
                             failed or underperformed.

                             Additionally, NeuralSeek logs all model interactions in a fully auditable format, supporting historical
                             comparisons across versions and configurations. This level of visibility empowers teams to make
                             data-driven decisions about model selection, optimization, and performance tuning; even when the model
                             itself is externally hosted and treated as a black box.
Model Management &           Yes. NeuralSeek includes multiple features that enhance model explainability and interpretability, enabling
Transparency                 users and administrators to understand why a particular response was generated and how confident the
                             system was in its accuracy. While NeuralSeek functions as a model-agnostic orchestration layer (often
Is there support for model   treating the LLM as a black box) it overlays semantic and contextual scoring tools that bring transparency
explainability or            to model behavior.
interpretability features?
                             Semantic Match %
                             Measures how closely the model’s response aligns with retrieved enterprise knowledge, providing a
                             quantifiable metric for truth alignment.

                             KnowledgeBase Confidence & Coverage Scores
                             Indicate how well the input prompt is supported by underlying enterprise content, clarifying whether
                             sufficient evidence existed to generate a reliable answer.

                             Semantic Analysis Panel
                             Available in the Governance dashboard, this feature breaks down the factors that influenced the Semantic
                             Match score, making it clear why a response was considered valid or not.

                             Source Referencing
                             Displays the specific knowledge chunks or documents used to generate a response, ensuring traceability
                             and reducing the risk of hallucinations.

                             Prompt/Response Auditing
                             Logs every interaction with metadata on model selection, confidence thresholds, policy enforcement, and
                             fallback paths, offering visibility into system behavior and decision-making logic.

                             Together, these capabilities make NeuralSeek explainable at both the prompt level for business users (and
                             the system level) for technical and compliance teams, bridging the gap between powerful LLMs and
                             trustworthy enterprise AI adoption.




                                                                                                                                27
Model Management &            NeuralSeek introduces a semantic safety layer between the user and the model, ensuring that every LLM
Transparency                  response is validated, scored, and governed before reaching the end user. This approach provides a
                              measurable and enforceable safeguard against hallucinations, compliance risks, and unverified content.
Can your platform detect
and flag hallucinations or    Semantic Match Scoring (Ground Truth Validation)
misinformation in             Every response from the model is evaluated against content retrieved from NeuralSeek’s
responses?                    enterprise-connected KnowledgeBase. High Semantic Match scores indicate strong alignment with factual
                              content, while low scores signal speculative or unsupported answers. This scoring is objective, based on
                              reality matching rather than token probabilities.

                              Knowledge Coverage and Confidence Metrics
                              NeuralSeek measures whether the system retrieved sufficient and relevant source material (Coverage) and
                              whether that material is trustworthy (Confidence). These indicators assess hallucination risk before it
                              occurs, allowing proactive intervention.

                              Configurable Guardrails for Enforcement
                              Administrators can set precise rules such as rejecting responses below a defined Semantic Match threshold,
                              routing unknown answers to human review, or restricting responses to those sourced from internal systems.
                              This enables governance teams to enforce trust-based standards rather than relying on model guesswork.

                              Traceability
                              NeuralSeek can display exactly which documents or data chunks informed a given response, making it
                              clear when a claim lacks a verifiable source and enabling it to be flagged, blocked, or annotated for
                              transparency.

                              Logging and Alerting for Continuous Oversight
                              All hallucination risks (whether blocked or allowed) are logged with full metadata, exportable for audits,
                              and integrable with compliance dashboards or SIEM tools like Splunk. This continuous monitoring ensures
                              operational transparency and regulatory readiness.




Platform Scalability &        NeuralSeek provides robust administrative controls to manage and limit resource usage in shared SaaS
Configuration                 environments, ensuring fair access, predictable costs, and system stability. These controls include
                              configurable throttling, usage quotas, and rate-limiting policies that can be tailored to organizational or
Can you limit resources for   departmental needs.
shared SaaS environments
(e.g., throttling, quotas)?   Rate Limiting allows administrators to cap the number of prompts per user, agent, or organization within a
                              set timeframe (e.g., 100 prompts per hour), helping prevent abuse, overconsumption, or spikes in traffic.
                              Token and Cost Quotas track usage across all connected model providers, enabling quota enforcement by
                              team, department, or tenant, which is critical for accurate cost allocation and governance. Concurrent
                              Execution Limits ensure fair distribution of processing power by restricting the number of prompts running
                              simultaneously, avoiding noisy-neighbor issues in shared infrastructures.

                              When multiple language models are configured, LLM Fallback Throttling can be applied to control how
                              often premium or latency-sensitive models are invoked, preserving performance and cost efficiency. Quota
                              Monitoring and Alerts provide real-time visibility into consumption, with configurable notifications to warn
                              administrators as thresholds are approached or exceeded. Together, these capabilities give organizations
                              granular control over AI usage while maintaining operational fairness and budget predictability.




                                                                                                                                     28
Platform Scalability &       Yes. NeuralSeek fully supports the creation and management of custom prompt templates tailored to
Configuration                specific departments, teams, or use cases. Administrators and authorized users can define structured
                             prompts that guide AI behavior based on the unique needs of each business unit whether it’s Legal, HR,
Do you support custom        Finance, Customer Support, or Engineering. These templates can include fixed text, variable fields, sliders,
prompt templates for         dropdowns, and toggles, all of which are exposed to the end user through an intuitive UI or API. Prompt
different departments or use templates are tied to specific AI Agents and can be governed using role-based access control, ensuring that
cases?                       only authorized users can modify or use them. Additionally, departments can operate in isolated or shared
                             environments, allowing for independent iteration without impacting other teams. This flexibility enables
                             organizations to safely scale their Gen AI usage while aligning AI outputs with department-specific
                             language, logic, and compliance requirements.
Governance, Compliance &       NeuralSeek was built with governance at its core, maintaining default governance dashboards that provide a
Reporting                      centralized executive and management view of AI risks. Structured processes align with the framework’s
                               four core functions (Govern, Map, Measure, and Manage) ensuring comprehensive oversight and control.
Is your platform aligned
with NIST AI Risk              In the Govern function, the platform supports default roles for developers, deployers, operators, and
Management Framework           auditors, enabling appropriate segregation of duties. Centralized baseline policies can be established across
(AI RMF)?                      the enterprise, and a marketplace portal facilitates enterprise-wide collaboration, including sharing best
                               practices, security, compliance, and privacy requirements, training resources, and reusable agents,
                               workflows, and code.

                               For the Map function, NeuralSeek enables complete inventorying of all Agents and Agentic AI workflows.
                               Standard dashboards and reports display each agent’s or workflow’s configuration, including API
                               integrations, usage, and user distribution. Risk levels (such as high, medium, and low) can be assigned to
                               agents and workflows, with templates enforced based on risk. Features also capture use cases, operational
                               context, and stakeholder impacts, all easily integrated into standard dashboards. The platform is built with
                               full data lineage capabilities and includes agents for data quality management.

                               In the Measure function, the platform undergoes rigorous testing and maintains security, privacy, usage, and
                               reliability features by default. These include prompt injection protection and PII filtering, semantic scoring
                               for truth validation and hallucination prevention, confidence gating and token cost tracking, and real-time
                               dashboards for data usage and algorithmic decision documentation. Accountability is reinforced through
                               comprehensive audit trails, system- and decision-level transparency, and natural language, contextual, and
                               technical explainability.

                               Under the Manage function, NeuralSeek maintains full version control and audit trails, automated audit and
                               control agents tailored to specific scenarios and use cases, and continuous monitoring capabilities. For
                               organizations seeking NIST AI RMF compliance, NeuralSeek offers inherent flexibility and customization
                               through AI RMF profiles that align with specific industry requirements, organizational risk tolerance, and
                               regulatory obligations, providing the adaptability needed to meet all industry and regulatory mandates.
Governance, Compliance &      Yes. NeuralSeek can generate detailed compliance reports to support internal audits, regulatory reviews,
Reporting                     and ongoing governance activities. The platform logs all prompt interactions, model responses, policy
                              enforcement actions, semantic scores, and user access events in a structured, exportable format (JSON or
Can your platform generate CSV). These logs can be filtered by user, department, time range, intent, or violation type, making it easy to
compliance reports for        produce audit-ready documentation on-demand. Additionally, NeuralSeek integrates seamlessly with
internal audits or regulatory enterprise analytics tools such as Power BI, IBM Cognos, and other BI platforms via API or scheduled data
reviews and integrate with    exports, enabling compliance, security, and audit teams to build dashboards, monitor trends, and visualize
tools such as Power BI and AI usage and risk across the organization. This ensures that enterprises can maintain continuous oversight
Cognos?                       of their AI deployments while meeting internal controls and external regulatory expectations.




                                                                                                                                    29
Governance, Compliance &      Yes. NeuralSeek offers legal hold capabilities for prompt history, allowing organizations to preserve
Reporting                     specific prompt interactions and related metadata in a tamper-proof state for legal, compliance, or
                              investigative purposes. When a legal hold is initiated, the affected prompt records (including input prompts,
Do you offer legal hold       AI responses, user identifiers, timestamps, semantic scoring, and policy enforcement outcomes) are
capabilities for prompt       excluded from automated deletion or archiving processes, ensuring they remain intact and accessible for the
history?                      duration of the hold. Legal holds can be applied to individual users, departments, intents, or time ranges,
                              and can be managed through the administrative interface or via API for automated enforcement.
                              Additionally, held data can be exported in secure, audit-ready formats (e.g., CSV, JSON) and integrated into
                              eDiscovery workflows or compliance systems. This capability ensures NeuralSeek aligns with litigation
                              readiness, regulatory auditability, and corporate data governance frameworks, helping enterprises meet their
                              legal obligations with confidence.
Governance, Compliance &      Yes. NeuralSeek provides comprehensive audit logs that are fully suitable for regulatory submission in
Reporting                     industries such as finance, healthcare, government, and enterprise IT. Every system interaction (whether it’s
                              a user submitting a prompt, an AI agent generating a response, a policy enforcement action, or a
Can you provide audit logs    configuration change) is immutably logged with timestamped metadata, including user ID, role, IP address,
suitable for regulatory       semantic match score, model used, and knowledge sources referenced. These logs are exportable in
submission?                   standard formats such as CSV and JSON, making them compatible with most regulatory reporting systems
                              and audit workflows. NeuralSeek’s audit logging also tracks version history of AI Agents, Guardrails,
                              prompt templates, and model configurations, providing full transparency into who made changes, when
                              they were made, and what was modified. For added assurance, audit logs can be streamed into SIEM
                              platforms like Splunk, or accessed via API for automated ingestion into compliance dashboards,
                              eDiscovery tools, or internal audit systems. This level of traceability ensures NeuralSeek meets the
                              stringent documentation and accountability standards required by frameworks such as SOC 2, HIPAA,
                              GDPR, NIST, and FINRA.
Security & Privacy            Yes. NeuralSeek includes built-in capabilities to detect and mask personal data in both prompts and
                              AI-generated responses, helping organizations meet strict data privacy and compliance requirements such
Can your platform mask        as GDPR, HIPAA, and CCPA.
personal data in prompts
and responses?                Using its Guardrails Framework, NeuralSeek automatically identifies personally identifiable information
                              (PII) and sensitive data (such as names, addresses, phone numbers, email addresses, Social Security
                              Numbers, and more) within user inputs or LLM responses. Once detected, this information can be
                              configured to be:
                              - Masked (e.g., replacing with symbols like **** or [REDACTED])
                              - Blocked entirely (preventing further processing)
                              - Routed for human review (in human-in-the-loop workflows)
                              - Logged with obfuscation to preserve analytical context while ensuring privacy

                              These protections apply at both the input and output stages, ensuring sensitive content is never exposed
                              unnecessarily either in logs, audit trails, or downstream applications. Additionally, privacy filters are
                              customizable, so organizations can define what constitutes sensitive content based on their regulatory
                              obligations and internal data governance standards.
Security & Privacy            Yes. NeuralSeek supports both prompt redaction and data minimization as part of its enterprise-grade
                              privacy and compliance framework. Through its configurable Guardrails, the platform can automatically
Is there support for prompt   scan and redact sensitive content (such as PII, confidential terms, or user-defined keywords) before prompts
redaction or data             are processed by the LLM or recorded in logs. This ensures that only the minimum necessary information is
minimization?                 retained or transmitted, reducing exposure risk and aligning with data protection regulations like GDPR and
                              HIPAA. Redaction rules can be applied at multiple levels, including by user role, department, or data
                              category, and can be extended via API for integration with external data classification tools. Additionally,
                              organizations can choose to minimize logged data, disabling storage of raw prompt content while still
                              capturing essential metadata for auditing and performance monitoring. This layered approach to redaction
                              and minimization helps organizations enforce least-privilege principles and ensures AI interactions are
                              privacy-conscious by design.




                                                                                                                                  30
Security & Privacy          Yes. NeuralSeek can integrate with external data classification tools to detect and tag sensitive content in
                            both prompts and AI-generated responses, enabling more advanced data governance and privacy
Can you integrate with data enforcement.
classification tools to tag
sensitive content?          Through its open API architecture and webhook support, NeuralSeek can route input or output text to
                            external classification engines (such as Microsoft Purview, BigID, Varonis, or custom-built classifiers) for
                            real-time content tagging. Once tagged, NeuralSeek can apply corresponding Guardrail actions, such as
                            redacting sensitive terms, routing the interaction for human review, or blocking it entirely based on policy.

                               In addition to third-party integration, NeuralSeek also includes native content classification features for
                               detecting common categories like PII, PHI, financial data, and regulated keywords. These can be used alone
                               or alongside external classifiers to enrich AI oversight and build layered defense strategies.

                               This capability allows organizations to extend their existing data classification ecosystem into the world of
                               AI ensuring that sensitive or regulated content is handled according to corporate policy, even as it flows
                               through generative models.
Ethics & Responsible AI        Neuralseek along with its consulting partners have extensive experience building AI governance programs
                               at Banks and maintain policy templates that can be used to build an ethical AI program from scratch. Our
Do you offer policy            collective knowledge and experience has enabled many financial institutions to quickly stand up AI
templates or best practices    programs that meet the expectations of all key stakeholders.
for ethical AI use?
Ethics & Responsible AI     NeuralSeek includes built-in mechanisms to validate AI responses for fairness and harmfulness, ensuring
                            that biased, offensive, or unsafe outputs are identified and addressed before reaching end users. Leveraging
Does your platform validate its Guardrails Framework, the platform can automatically evaluate responses from language models for
response fairness and       toxicity, offensive language, bias or discriminatory phrasing, misinformation, unsubstantiated claims, and
harmfulness?                violations of organizational or regulatory fairness guidelines.

                               This validation process uses real-time semantic classification and risk scoring to assess potential harm or
                               unfairness. When a response is flagged, it can be automatically blocked, rerouted to human-in-the-loop
                               (HITL) review, sanitized or rephrased before delivery, or logged for compliance auditing. NeuralSeek also
                               supports fully customizable fairness policies tailored to organizational values, regional legal requirements,
                               and industry-specific standards; for example, avoiding gendered language in HR-related agents or ensuring
                               neutral, fact-based tone in financial advisory applications. These capabilities help organizations enforce
                               consistent ethical standards and mitigate reputational and regulatory risks.




                                                                                                                                    31
Ethics & Responsible AI      NeuralSeek has contributed to Ethical AI Policy Toolkits for clients on a case-by-case basis through its
                             consulting services arm. These toolkits include a customizable AI Acceptable Use Policy (AUP) template,
Do you provide               bias mitigation guidelines and examples, a Data Protection Impact Assessment (DPIA) worksheet, and
documentation or tooling for reference guides aligned to frameworks such as the NIST AI Risk Management Framework, OECD AI
ethical AI usage policies?   Principles, and emerging regulations like the EU AI Act. Designed to support internal governance teams
                             (legal, risk, compliance, and IT) these materials help codify responsible AI use policies that are both
                             actionable and audit-ready. Complementing these resources, NeuralSeek’s platform provides technical
                             enforcement layers that operationalize ethical policies, including guardrails to block unsafe, biased, or
                             non-compliant content, semantic scoring to validate the truthfulness and tone of AI outputs, prompt
                             injection protection and PII filtering, role-based access controls, content redaction, policy-driven prompt
                             routing, and logging and monitoring dashboards for transparency and continuous oversight.




Ethics & Responsible AI        NeuralSeek includes multiple built-in mechanisms to route, flag, or pause AI-generated outputs for human
                               review based on configurable criteria. Key capabilities include:
Is there support for
human-in-the-loop review       Confidence Threshold Routing
for sensitive prompts?         NeuralSeek can automatically flag or withhold responses that fall below a configurable semantic match or
                               confidence score. This ensures that only high-quality, well-grounded answers are released without manual
                               review.

                               Guardrail Triggers
                               The platform detects categories such as Personally Identifiable Information (PII), profanity, or custom
                               prompt injection attempts, routing flagged outputs to a human reviewer before delivery.

                               Workflow Orchestration
                               Using NeuralSeek’s multi-agent framework, organizations can insert human-in-the-loop (HITL) review
                               agents or trigger external API calls (such as Slack alerts, email notifications, or internal ticket creation) at
                               specific decision points.

                               Audit & Traceability
                               All routed interactions are logged with full context, enabling compliance teams to review, validate, and
                               audit outputs as part of governance and regulatory processes.

                               Integration Flexibility
                               HITL checkpoints can be triggered programmatically or manually, and can integrate with existing business
                               tools via API, ensuring seamless fit within enterprise workflows.




                                                                                                                                        32
Lifecycle Security Coverage - The Data Ingestion & Processing Safeguards
proposal will document the
breadth of safeguards- all types of NeuralSeek uses secure, API-based integrations to connect with customer knowledge bases and
Gen AI and Agentic AI               content repositories. All data is encrypted in transit and at rest, and undergoes automated filtering and
(including, data ingestion to       validation to ensure quality and compliance. Customer data is never stored or retained after processing,
model training, deployment, and with strict access controls and authentication in place to prevent unauthorized use.
retirement.

                                     Model Training & Development

                                     Models are trained on carefully curated datasets to maintain high accuracy and relevance. NeuralSeek
                                     regularly evaluates models for bias, accuracy, and performance drift, documenting all iterations
                                     through version control. All development follows responsible AI practices to ensure ethical and
                                     compliant outcomes.


                                     Deployment Safeguards

                                     During operation, NeuralSeek applies real-time accuracy scoring and source attribution to every
                                     AI-generated response. Factuality checks and hallucination prevention are built in, supported by
                                     automated moderation to filter inappropriate content. Regular security audits and vulnerability
                                     assessments help maintain a secure deployment environment.


                                     Operational Controls

                                     Role-based access control (RBAC) governs user permissions, while all system activity is captured in
                                     detailed audit logs. Regular backups and recovery procedures safeguard against data loss, and SOC 2
                                     Type 2 compliance ensures enterprise-grade governance. Continuous system performance monitoring
                                     maintains reliability and uptime.


                                     Model Retirement

                                     When models are deprecated, NeuralSeek follows a structured retirement process, including secure
                                     deletion of training data where required. All lifecycle changes are fully documented and
                                     communicated to customers in advance. This process ensures transparency and eliminates risks from
                                     outdated models.


                                     Additional Safety Features

                                     NeuralSeek supports human-in-the-loop oversight to review sensitive or high-impact outputs.
                                     Administrators can configure content filters, safety parameters, and incident response protocols, which
                                     are regularly updated. Ongoing staff training reinforces AI safety, ethics, and evolving best practices.




                                                                                                                                   33
Extendibility to Multiple AI          Yes. NeuralSeek is purpose-built to support extensibility across all types of AI Agents and future
Agents (or Agentic AI) - Can the      Agentic AI architectures, making it a future-proof platform for enterprises looking to scale across
tool can be extended for all types    multiple AI use cases and models. The platform’s modular, no-code agent framework allows users to
of future Agents and whether the      create, chain, and orchestrate multiple specialized agents, each with its own logic, model, data source,
license supports all types of         and policy layer. These agents can be grouped into ProPacks, which enable multi-agent collaboration,
Agentic AI and Gen AI?                handoff, and decision-making; mirroring real-world workflows across departments or systems.

                                      Critically, NeuralSeek is LLM-agnostic and integration-flexible. It supports a wide range of current
                                      and emerging models; including OpenAI (GPT), Claude, LLaMA, Gemini, Bedrock, and fine-tuned
                                      custom models via API. This ensures that any future agent built on top of a new Gen AI backend can
                                      be quickly adopted without vendor lock-in.

                                      From a licensing perspective, NeuralSeek’s standard enterprise license supports unlimited agent
                                      creation, including support for Agentic AI architectures, task-specific agents, and multi-step decision
                                      trees. It also includes the ability to govern these agents with centralized Guardrails, semantic scoring,
                                      and audit logging, ensuring control and compliance at scale.
SBOM Assurance - The proposal         NeuralSeek integrates seamlessly with existing banking knowledge base systems such as Salesforce,
will speak to the tool’s ability to   ServiceNow, and Zendesk, leveraging secure API connections to eliminate the need for additional
inventory, version, and scan          plugin or version management. The platform automatically scans and indexes content for AI use
third‑party models, data sets, and    without storing third-party datasets, ensuring sensitive financial information remains under the bank’s
plugins.                              control. All AI-generated responses are tracked, logged, and linked to their source content for full
                                      auditability, supporting regulatory compliance and internal governance. While NeuralSeek utilizes
                                      enterprise-grade LLMs, banks are not required to manage or version control these models, reducing
                                      operational overhead. This architecture is purpose-built to complement and enhance existing financial
                                      systems, enabling advanced AI capabilities without introducing new inventory, versioning burdens, or
                                      data residency risks.
Runtime Guardrails & Policy           Yes. NeuralSeek includes a comprehensive Runtime Guardrails and Policy Enforcement framework,
Enforcement - Controls for            giving enterprises full control over prompt execution, tool usage, and response generation. This
prompt injection, jailbreaks,         ensures that all AI activity (whether initiated by users or autonomous agents) remains secure,
tool‑use limits, and output           policy-compliant, and aligned with governance standards.
filtering.

                                      Prompt Injection and Jailbreak Protection

                                      NeuralSeek proactively detects and blocks prompt injection or jailbreak attempts before they reach the
                                      model. This includes detecting override phrases (e.g., “Ignore previous instructions…”),
                                      pattern-matching against known adversarial structures, and using semantic evaluation to assess
                                      manipulation attempts in context. Administrators can set thresholds to block, reroute, or flag
                                      suspicious prompts for human-in-the-loop (HITL) review, ensuring model integrity at runtime.


                                      Tool-Use Limits and API Access Control

                                      NeuralSeek allows precise control over what tools, APIs, and functions an agent can access.
                                      Administrators can enforce role-based or intent-based restrictions, set rate limits, define concurrency
                                      caps for high-cost operations, and block unauthorized data access in real time. These safeguards
                                      prevent misuse of external systems, protect sensitive integrations, and enforce operational boundaries
                                      for AI agent behavior.


                                      Output Filtering and Response Sanitization

                                      NeuralSeek applies strong output controls to keep responses safe, accurate, and compliant. Capabilities



                                                                                                                                       34
                                    include profanity and toxic language filtering, automatic PII/PHI redaction, semantic match scoring to
                                    measure truth alignment, and the ability to block or reroute low-confidence answers. Custom rules can
                                    also enforce tone, format, and language restrictions, with options to suppress responses, trigger alerts,
                                    or escalate to human review when necessary.
RBAC Configurability -              NeuralSeek provides comprehensive role-based access control (RBAC) capabilities that allow
Administrative access for           administrators to manage user permissions and access levels within the system. The administrative
role-based access to generate the   features include:
response (internal data and
external resources.)                User Role Management:
                                    Admin roles with full system access and configuration capabilities
                                    Standard user roles with customizable permissions
                                    Read-only roles for viewing responses without editing capabilities

                                    Access Control Features:
                                    Granular permission settings for different functionalities
                                    Ability to restrict access to specific data sources and content
                                    Control over response generation and editing capabilities
                                    User activity monitoring and audit logs

                                    Security Measures:
                                    Secure authentication protocols
                                    Single Sign-On (SSO) integration options
                                    Activity logging and tracking
                                    Compliance with security standards and protocols

                                    Resource Management:
                                    Control over internal knowledge base access
                                    Management of external resource connections
                                    Configuration of AI response parameters
                                    Data source permission settings

                                    Administrators can easily manage these settings through NeuralSeek's intuitive administrative
                                    interface, ensuring proper access control while maintaining security and compliance requirements.




                                                                                                                                    35
Data‑Privacy & Token‑Level         Yes. NeuralSeek offers a comprehensive Data Privacy and Token-Level Protection framework that
Protection - Pseudonymisation,     addresses enterprise-grade privacy requirements, including pseudonymisation, masking,
masking, re‑identification risk,   re-identification risk mitigation, and data-in-use protection during AI prompt and response handling.
data‑in‑use encryption.
                                   Pseudonymisation and Masking

                                   NeuralSeek can automatically detect and pseudonymize sensitive data (such as names, email
                                   addresses, phone numbers, or unique identifiers) in both prompts and model responses. This is done
                                   using real-time Guardrails that scan input and output content for PII, PHI, and other regulated data
                                   types, replacing them with consistent, non-identifiable tokens (e.g., [USER_ID_123] or ****). This
                                   allows teams to preserve context for AI processing while protecting individual identities from
                                   exposure.

                                   Re-identification Risk Mitigation

                                   NeuralSeek includes built-in safeguards to minimize the risk of downstream re-identification.
                                   Role-based access controls ensure that only authorized users can view or handle sensitive prompt
                                   content, while configurable logging controls allow administrators to redact or omit personal data from
                                   histories, audit trails, and reports. In addition, context-aware filtering prevents AI agents from
                                   aggregating or inferring identities across multiple prompts or sessions. Together, these measures help
                                   organizations meet GDPR, HIPAA, CCPA, and other data protection requirements while reducing the
                                   likelihood of unintended identity exposure.

                                   Token-Level Data-in-Use Encryption

                                   During active processing, all data transmitted through NeuralSeek (whether between user interfaces,
                                   AI agents, or LLM endpoints) is encrypted in transit using TLS 1.2+ and, where supported, at the
                                   token level through secure API payload handling. For on-premise deployments, organizations can
                                   implement zero-trust controls and containerized isolation to further safeguard data-in-use within their
                                   infrastructure.

                                   Additionally, NeuralSeek does not cache or store prompt data unnecessarily and allows organizations
                                   to configure retention policies to automatically delete or anonymize sensitive content after a defined
                                   window.
Data Retention and Disposal        NeuralSeek’s SaaS deployment retains data for 30 days by default, ensuring a balance between
Policy Management - Ability to     operational visibility and privacy. This retention policy helps minimize long-term storage of sensitive
securely retain and dispose data   information while still allowing for monitoring, troubleshooting, and compliance review.
(at the user level and corporate
level)                             For on-premise deployments, data retention settings are fully configurable, enabling organizations to
                                   define storage durations that align with their internal policies, regulatory requirements, or
                                   industry-specific standards. This gives customers, particularly in highly regulated sectors like banking,
                                   complete control over how long records, logs, and AI interaction data are preserved.




                                                                                                                                  36
Autonomous‑Agent Containment NeuralSeek implements robust agent containment through its Agent Registry system, which provides
- Sandboxing and privilege   secure sandboxing and well-defined privilege boundaries for agent actions. Key features include:
boundaries for agent actions
(tools, API calls)           Agent Registry Isolation
                             Agents can be grouped into separate Agent Registries that act as isolated sandboxes
                             Each Registry maintains its own permission set and access controls
                             Agents within a Registry can only interact with approved resources and APIs defined for that Registry

                                   Privilege Management
                                   Granular control over which tools and API calls each Agent Registry can access
                                   Ability to restrict agent actions to specific domains and capabilities
                                   Clear boundaries between different agent groups through Registry separation

                                   Security Controls
                                   Agents operate within their designated Registry sandbox with no ability to escape those boundaries
                                   API access is strictly controlled through Registry-level permissions
                                   Actions are limited to pre-approved tools and capabilities defined for each Registry

                                   Compliance & Governance
                                   Registry-based isolation enables compliance with security policies
                                   Audit trails of agent actions within each sandbox
                                   Ability to create separate Registries for different business units or security requirements

                                   This containment architecture ensures agents operate safely within defined boundaries while
                                   maintaining necessary access to authorized tools and APIs.
Continuous Attack Simulation       NeuralSeek employs a comprehensive approach to LLM security testing and red teaming through its
(LLM Red Team) - Frequency         built-in agent scheduler system. The platform conducts regular automated adversarial testing in the
and depth of automated             following ways:
adversarial testing
                                   Continuous Security Testing

                                   NeuralSeek integrates automated adversarial testing directly into its operational workflow, ensuring
                                   constant monitoring for vulnerabilities. This includes real-time exploit detection and ongoing
                                   validation without interrupting normal AI operations.

                                   Scheduled Deep Scans

                                   Daily security scans are executed via the built-in agent scheduler, performing comprehensive,
                                   multi-layer tests to identify potential weaknesses. Customers can configure additional ad-hoc scans to
                                   meet unique compliance or threat scenarios.

                                   Multi-Layer Threat Evaluation

                                   Testing covers input validation, prompt injection detection, output filtering, response consistency,
                                   model boundary testing, and jailbreak prevention. Automated agents simulate diverse attack vectors to
                                   uncover and address risks across both content generation and knowledge retrieval functions.

                                   Flexible Configuration & Compliance Alignment

                                   Security testing frequency, depth, and scope can be tailored to align with industry-specific
                                   requirements, including banking regulations and internal security policies. This flexibility ensures
                                   proactive risk management while meeting compliance standards.




                                                                                                                                  37
                                    Comprehensive Logging & Continuous Improvement

                                    All testing results are recorded, analyzed, and fed into NeuralSeek’s continuous improvement cycle.
                                    This enables rapid remediation, informed governance decisions, and evolving defense strategies
                                    against emerging threats.
Observability & Explainability -    Yes. NeuralSeek provides industry-leading observability and explainability features that give
Trace logs, prompt lineage,         enterprises full transparency into every AI interaction; enabling traceability, accountability, and
attribution of policy violations,   real-time governance across agents, models, prompts, and users. This level of insight is critical for
explainable risk scoring            regulated industries and enterprise deployments where understanding why a decision was made is just
                                    as important as the result itself.

                                    Full Observability & Explainability

                                    NeuralSeek delivers complete transparency into every AI interaction, ensuring traceability,
                                    accountability, and governance across agents, models, prompts, and users. This enables regulated
                                    industries like banking to validate not just the outcome of AI-driven decisions, but the reasoning and
                                    data behind them.

                                    Trace Logs & Prompt Lineage

                                    Every prompt is logged end-to-end, capturing the original input, user identity, AI Agent or ProPack
                                    used, models invoked, source documents retrieved, Guardrail checkpoints, and final outputs. This
                                    comprehensive lineage enables rapid troubleshooting, compliance audits, and historical usage reviews.

                                    Attribution of Policy Violations

                                    All Guardrail enforcement actions are logged with full context, including the violated policy, the
                                    enforcement action taken, and the user or system involved. Risk and compliance teams can filter and
                                    export violation data by user, intent, agent, or category for precise monitoring and reporting.

                                    Explainable Risk Scoring

                                    NeuralSeek calculates and displays key trust metrics for each AI response, including Semantic Match
                                    %, KnowledgeBase Confidence %, Coverage %, and Guardrail Risk Scores. These insights make it
                                    clear why a response was accepted, blocked, or flagged, enabling policy enforcement based on
                                    measurable thresholds.
Compliance Posture Management NeuralSeek maintains platform-level controls, customizable features, and AI agents that allow
- Built‑in control libraries for institutions to meet the most stringent security, privacy, and compliance standards and global
SOX, GDPR, PSD2, FINRA,          requirements. The platform is designed with flexibility in mind, recognizing that needs vary greatly
NYDFS, and OCC bulletins         depending on the use case (such as internal versus external deployments or PII versus non-PII data)
                                 and is built to adapt to changing requirements and business needs.

                                    Organizational and default platform-level controls ensure security and regulatory compliance with
                                    standards such as NYDFS and FFIEC, as well as industry expectations. These include the designation
                                    of a CISO and DPO, comprehensive policies, standards, and procedures, continuous risk assessments,
                                    rigorous third- and fourth-party due diligence, cybersecurity awareness training, vulnerability and
                                    penetration testing programs, and SOC 2 certification processes. Platform controls include user access
                                    management with role-based access control and Single Sign-On (SSO) capabilities; multi-factor
                                    authentication (MFA) with Active Directory, external MFA integration, and zero-trust access controls;
                                    unique user identification for each system user; encryption of sensitive data in transit and at rest using
                                    industry-standard algorithms; data classification and labeling features across the data lifecycle; secure
                                    data disposal; data loss prevention measures; and audit trails with full user and privileged account
                                    activity logging and SIEM integration.



                                                                                                                                     38
In alignment with GDPR and other privacy regulations, NeuralSeek offers default and customizable
processes and controls such as intelligent legal basis and consent management with dynamic consent
flows; automated transparency through privacy notice generation, real-time processing dashboards,
and plain-language algorithmic decision documentation; data minimization and purpose control;
advanced security features like automated key management, pseudonymization, data masking, and
zero-trust access; and comprehensive user rights automation for subject access requests, “right to be
forgotten” actions, consent withdrawal, and objection management.

For SOX compliance, NeuralSeek emphasizes organizational and technical safeguards that protect data
integrity, security, and auditability. This includes annual SOC 2 audits, penetration testing, disaster
recovery planning, vendor risk management, robust access controls with automated segregation of
duties, encryption protocols, monitoring systems, detailed audit trails, and Records of Processing
Activities (ROPA). Software exploitation policies and network protections are in place to mitigate
vulnerabilities and ensure continuous compliance.




                                                                                             39
Integration & Deployment Model   Yes. NeuralSeek offers a highly flexible integration and deployment model, supporting a range of
- SaaS vs. VPC vs. on‑prem;      enterprise infrastructure requirements including SaaS, Virtual Private Cloud (VPC), and fully
API/SDK maturity; Kubernetes     on-premise deployments. This flexibility allows organizations to align AI adoption with their existing
& SIEM connectors                security, compliance, and data residency strategies whether operating in regulated environments,
                                 air-gapped networks, or modern cloud-native stacks.

                                 Flexible Deployment Models

                                 NeuralSeek supports SaaS, Virtual Private Cloud (VPC), and fully on-premise deployments, enabling
                                 organizations to align AI adoption with existing security, compliance, and data residency requirements.
                                 Whether operating in regulated banking environments, air-gapped networks, or cloud-native
                                 architectures, NeuralSeek ensures secure and scalable integration.

                                 SaaS Deployment

                                 Hosted in secure, multi-tenant environments on AWS, Azure, or IBM Cloud, the SaaS model includes
                                 encryption, tenant isolation, and elastic scaling; ideal for rapid deployment without infrastructure
                                 overhead.

                                 VPC Deployment

                                 For institutions requiring stricter control, NeuralSeek can run in a customer-managed VPC, allowing
                                 network isolation while retaining the scalability and reliability of cloud-native infrastructure.

                                 On-Premise Deployment

                                 For highly regulated industries such as banking and government, NeuralSeek supports complete
                                 on-premise deployment, including containerized and Kubernetes-based rollouts, with no reliance on
                                 external internet or public APIs.

                                 Integration & API/SDK Maturity

                                 NeuralSeek provides a robust REST API with capabilities for agent management, prompt execution,
                                 Guardrail configuration, analytics, and real-time event streaming. SDKs, CLI tools, and
                                 low-code/no-code UI options enable seamless integration into enterprise workflows and DevOps
                                 pipelines.

                                 Kubernetes & CI/CD Support

                                 Built for containerized deployment, NeuralSeek includes native support for Kubernetes, Helm charts,
                                 and CI/CD pipelines. This allows for horizontal scaling, multi-region deployments, and easy
                                 integration into microservice architectures.

                                 SIEM & Security Monitoring Integration

                                 NeuralSeek integrates with SIEM platforms such as Splunk, IBM QRadar, and Azure Sentinel,
                                 streaming real-time logs of prompt activity, Guardrail triggers, and access events. This enables
                                 proactive security monitoring, anomaly detection, and policy enforcement.




                                                                                                                               40
Performance Overhead &              NeuralSeek is optimized for low-latency, high-throughput performance at enterprise scale, adding
Scalability - Added latency,        minimal overhead while enabling deep control, observability, and policy enforcement across AI
throughput ceilings, cost per       workflows. The platform is designed to sit between users and LLMs with near real-time processing,
million tokens                      making it suitable for both high-speed chat interfaces and mission-critical automation pipelines.

                                    Low-Latency Enterprise Performance
                                    NeuralSeek is engineered for near real-time processing, adding only 2–3 seconds of total end-to-end
                                    latency. This includes semantic scoring, Guardrail checks, KnowledgeBase retrieval, and model
                                    post-processing; making it fast enough for both high-speed chat interfaces and mission-critical
                                    automation.

                                    Competitive Response Times
                                    Unlike orchestration platforms that can exceed 15–20 seconds per knowledge-grounded response,
                                    NeuralSeek consistently remains within enterprise SLA thresholds while delivering full observability,
                                    risk scoring, and filtering not available in raw LLM calls.

                                    High Throughput & Scalability
                                    Built for horizontal scalability, NeuralSeek supports SaaS, VPC, and on-premise deployments with
                                    auto-scaling Kubernetes infrastructure, multi-node clustering, and multi-region rollout. It has been
                                    proven to handle 10,000+ concurrent users and thousands of prompts per minute without bottlenecks.

                                    Efficient Cost Management
                                    NeuralSeek passes through LLM token costs transparently while providing tools to track usage per
                                    prompt, agent, or department, compare model efficiency, and set alerts or limits. Its fine-grained
                                    control reduces unnecessary token spend by eliminating retries, hallucinations, and irrelevant outputs.
Data Security/Destruction - The     SaaS Deployment
Vendor will provide a description   In NeuralSeek’s SaaS environment, all customer data is automatically deleted by default every 30
of methodology used for             days, ensuring minimal data retention and reducing regulatory exposure. For financial institutions
electronic and physical data        requiring continuous oversight, the platform supports integration with Security Information and Event
security and destruction            Management (SIEM) systems, enabling real-time monitoring, alerting, and compliance tracking.
practices.
                                    On-Premise Deployment
                                    For on-site or private cloud deployments, the customer maintains 100 percent control over data
                                    storage, retention policies, and security configurations. This allows banks to align AI operations with
                                    strict internal governance standards, data residency requirements, and regulatory frameworks such as
                                    GLBA, FFIEC, and OCC guidelines.




                                                                                                                                   41
                                           NeuralSeek Company Background


1. Company Name(s)                                      Cerebral Blue dba NeuralSeek
2. Company Address                                      50 Biscayne Blvd, Unit 4902, Miami Florida, 33132
3. Company Contact Information (and preferred           Lawrence Patrizio, Partner, lawrence@neuralseek.com, 914-355-8352
method of communication                                 Marc Martina, Co-Founder, marc@neuralseek.com
                                                        Garrett Rowe, Co-Founder, garrett@neuralseek.com
4. Legal Formation of Company (e.g. sole proprietor,    LLC
partnership, corporation)
5. Description of Company in terms of size, range and A US Veteran owned business, NeuralSeek is a privately held enterprise AI
types of services offered and clientele.              software company specializing in no-code AI orchestration, governance, and
                                                      decision automation for regulated industries. The company serves a global client
                                                      base across Banking, Financial Services, Healthcare, Telecommunications,
                                                      Higher Education, and Government sectors, with deployments in over 19
                                                      countries. NeuralSeek’s platform enables organizations to rapidly build, deploy,
                                                      and govern AI agents that integrate seamlessly with existing systems, leveraging
                                                      Retrieval-Augmented Generation (RAG), semantic confidence scoring, and
                                                      multi-agent orchestration to deliver accurate, policy-compliant outputs. The
                                                      company offers both SaaS and on-premise deployment models, with full support
                                                      for HIPAA, SOC 2, and other regulatory compliance standards. Its client roster
                                                      ranges from Fortune 100 enterprises to government agencies, all of which require
                                                      AI solutions that are secure, auditable, and adaptable to complex workflows.
                                                      NeuralSeek’s services include AI solution design, integration with enterprise
                                                      systems, governance configuration, and ongoing operational support,
                                                      empowering clients to safely scale AI adoption while maintaining full control
                                                      over data, compliance, and business logic.
6. Evidence of established track record for providing   200+ clients over 21+ countries
services and/or deliverables that are specific to the
subject matter and objective of this proposal.
7. Confirmation that no conflict of interest exists that Confirmed, no conflicts
would prohibit your firm from engaging with
######## for this project.
8. Supply a minimum of 3 customer references and        Has been provided in the Client Story Section
contact information, preferably in the banking /
financial industry for whom Company has provided
the same or similar consultation.
State whether the Company or its parent company (if NeuralSeek has never filed for bankruptcy protection.
any) has ever filed for bankruptcy or any form of
reorganization under the bankruptcy code.
State whether the Bidder or its parent company (if      We have never received sanctions.
any) has ever received any sanctions or is currently
under investigation by any regulatory or
governmental body.




                                                                                                                             46
Confirmation that the Company’s contractual terms Our terms will be in accordance of Section 1.25
and conditions in any resulting agreement between
the Vendor and ### in connection with this proposal
will be in accordance with the key legal provisions set
forth in Section 1.25 above, and if not, detail the
Company’s proposed contractual terms and
conditions with respect to such specific provisions.
Commitment to Diversity                              NeuralSeek is committed to supporting diversity, equity, and inclusion in all
                                                     aspects of our operations, including our vendor relationships. While we do not
                                                     currently maintain a formal Vendor Diversity Program, we actively seek
                                                     opportunities to work with diverse business enterprises (DBEs) and are willing to
                                                     align with ### Bank’s goals for inclusion under this contract. We are open to
                                                     committing to a mutually agreed-upon participation level of DBEs and will
                                                     provide regular reporting on the use of DBE subcontractors as part of our
                                                     engagement. Additionally, we welcome and will consider recommendations of
                                                     potential DBE partners to ensure that our work under this contract reflects the
                                                     values of diversity, inclusion, and equitable economic opportunity.
Sustainability                                       NeuralSeek is committed to conducting business in a manner that supports
                                                     environmental sustainability and aligns with ### Bank’s goals. We will use
                                                     commercially reasonable efforts to perform our obligations under this agreement
                                                     in a way that gives appropriate regard to the protection of the natural
                                                     environment. We continuously seek to operate in an environmentally sustainable
                                                     manner, working to improve our business processes to reflect current industry
                                                     practices and advancements in sustainability. Additionally, we are willing to
                                                     provide information, upon reasonable request, regarding our sustainability
                                                     initiatives and activities to ensure transparency and alignment with ### Bank’s
                                                     environmental objectives.
Financials                                           Available upon request. Here is NeuralSeek’s accountant contact information:

                                                     Robert L. Parker, CPA, Partner
                                                     Siana Carr O'Connor & Lynam, LLP
                                                     1500 E. Lancaster Avenue, Ste 202
                                                     Paoli, PA 19301
                                                     t. 610-296-4205
                                                     www.scolcpa.com




                                                                                                                             47
                                        Training, Community, & Support

NeuralSeek provides a comprehensive suite of integration, training, and post-sales support services designed to
ensure successful deployment, adoption, and long-term value realization across global enterprise environments. Our
approach emphasizes speed, enablement, and self-sufficiency, backed by dedicated technical and customer success
teams, global support channels, and detailed onboarding pathways.


 Integration & Deployment Support
 NeuralSeek’s dedicated integration team ensures smooth and secure deployments across SaaS, VPC, and on-premise
 environments using containerized infrastructure and Kubernetes. Services include instance provisioning, model configuration,
 knowledge source setup, API integrations with enterprise systems, and custom agent development for unique workflows.
 Integration Accelerators; prebuilt toolkits for platforms like Salesforce, ServiceNow, SharePoint, and Snowflake, help reduce
 time-to-value.

 Training & Enablement
 Role-based training programs, including Level 1–3 certification tracks, equip builders, administrators, and AI governance
 professionals with the skills needed for success. Delivery options include instructor-led sessions, on-demand video modules,
 live office hours, and train-the-trainer programs. Customers also gain access to the NeuralSeek Community Hub and
 labs.neuralseek.com for sandbox experimentation, supported by a structured 30–60–90 day success plan.

 Global Support Coverage
 NeuralSeek provides 24/7 customer support through a global portal and ticketing system, with same-day technical assistance
 for critical issues. Enterprise clients receive dedicated Technical Account Managers and access to solution engineers
 specializing in AI agent design, governance compliance, infrastructure scaling, and RAG optimization. Support resources span
 the US, EMEA, and APAC regions to meet international demand.

 Enterprise Support Options
 For organizations with specialized needs, NeuralSeek offers custom SLAs that include onsite engineer dispatch, technical
 workshops, and white-glove onboarding services. These agreements are designed to meet the highest levels of enterprise
 service expectations.




                                                                                                                                48
                                              NeuralSeek Learning Labs
                                                 https://labs.neuralseek.com/

The NeuralSeek Learning Labs is more than just a training program, it’s an immersive, hands-on gateway into the future of AI
deployment. Designed as a self-paced, no-code experience, the program empowers participants to seamlessly connect NeuralSeek
with their chosen KnowledgeBase and Virtual Agent, unlocking the platform’s enterprise-grade AI capabilities for precise,
scalable, and human-supervised natural language generation. Whether you’re a business leader, solution architect, or innovation
strategist, the Learning Labs transform you from a casual user into a confident builder of intelligent, decision-making AI systems.

Getting Started
The journey begins with an introduction to NeuralSeek and guided setup instructions for AWS, IBM Cloud, or Azure. Even for
those new to enterprise AI, the program provides step-by-step direction for free trials, recommended configurations, and
best-practice deployment paths tailored to your environment.

          Seeking Answers
          In the first challenge, participants learn to master accuracy and trust in AI outputs. This stage covers implementing
          Semantic Scoring to validate responses, training Virtual Agents for tailored interactions, and applying PII filtering to
          safeguard sensitive information; all through an intuitive, no-code interface.

          mAIstro Essentials
          The second challenge takes a deeper dive into NeuralSeek’s content creation and retrieval capabilities. Participants
          explore how to integrate with connectors for seamless data access, improve data quality for large language model
          interactions, and harness the platform’s retrieval features for fast, context-rich results.

          Mastering mAIstro
          The final challenge is where participants evolve from user to AI architect. Here, they learn to build and scale custom AI
          Agents with the Auto-Builder, design enterprise-ready performance workflows, and orchestrate multi-agent logic for
          dynamic decision-making at scale.

By the end of the Learning Labs, participants experience NeuralSeek’s philosophy of speed, security, and simplicity in action.
They emerge with not only a fully functional NeuralSeek deployment but also the skills and confidence to innovate faster,
eliminate operational bottlenecks, and deliver transformative AI solutions; all without writing a single line of code. Completion
of the program earns the NeuralSeek Certification, an official recognition of mastery over one of the most advanced AI platforms
available today.




                                                                                                                                 49
                                             NeuralSeek Documentation
                                           https://documentation.neuralseek.com/

NeuralSeek’s online documentation is a comprehensive, enterprise-grade resource designed to guide users through every stage of
deployment, integration, and optimization. It offers robust coverage of platform features, no-code tools, governance controls,
integrations, and advanced AI agent orchestration, ensuring both technical and non-technical users can maximize value. The
documentation is structured for clarity, with detailed guides, walkthroughs, and configuration instructions that support rapid
learning and scalable implementation. Here is everything available online:
 Getting Started                                                Integrations
 Introduction and onboarding into NeuralSeek.                        ● AWS S3
                                                                     ● Databases
 Explore the Interface                                               ● GitHub
     ● Home                                                          ● Google Drive
     ● Configure                                                     ● Jira
                                                                     ● KnowledgeBases
 Integrate                                                           ● SharePoint
      ● Platform Integrations                                        ● Slack
      ● KnowledgeBases                                               ● Trello
      ● Supported LLMs                                               ● Watsonx.governance
      ● Supported Virtual Agents                                     ● Web Searches

 Extract - pulling data into NeuralSeek.                        Guides & Walkthroughs
                                                                    ● Data
 Load - data ingestion and preparation.                             ● Proposals
                                                                    ● Tuning Guide
 mAIstro                                                            ● Dynamic Filters
     ●     NTL Functions                                            ● VirtualKB
     ●     Get Data                                                 ● Document Ingestion
     ●     Upload Data                                              ● Replay
     ●     Generate Data                                            ● Integration
     ●     Local Cache                                              ● Chat SDK
     ●     Extract Data                                             ● Training Virtual Agents
     ●     Multi-Agent                                              ● Backup and Restore
     ●     Control Flow                                             ● ElasticSearch Vector Model
     ●     RAG Tools                                                ● Pinecone Configuration
     ●     GuardRails                                               ● Passing Conversational Context
     ●     System Variables                                         ● mAIstro Streaming Endpoint with Watsonx
     ●     Sandboxes                                                ● Implementing Feedback
                                                                    ● Models
 Modify Data                                                        ● Multimodal LLM Configuration
     ● Code Toolbox                                                 ● Semantic Model Tuning
     ● JSON Toolbox
     ● String Toolbox                                           More About NeuralSeek
     ● Transform                                                    ● NeuralSeek Partnerships
     ● XML Toolbox                                                  ● Available NeuralSeek Plans
                                                                    ● Data Security and Privacy

 Send Data - data output workflows.                             Curate - managing and refining content or datasets for Chat

 Seek - search and retrieval functions.                         Governance- AI governance and compliance controls.

 Chat - conversational interface capabilities.                  Changelog - updates to the platform




                                                                                                                           51
                                                NeuralSeek Community
                                            https://community.neuralseek.com/

The NeuralSeek Community is an interactive hub where users can stay informed, share ideas, and get support. It includes
Announcements for news and updates, Feature Requests for suggesting improvements, General Discussion for open
conversations and tips, and Product Q/A Discussion with verified answers and official resources to ensure accuracy. This space
fosters collaboration, knowledge sharing, and engagement among NeuralSeek users.




NeuralSeek Cohort Training & Certification Program -NeuralSeek offers a comprehensive AI Reskill and Internship Program
designed to produce NeuralSeek Certified AI Agent Builders; a vetted talent pool available for hire by NeuralSeek clients. Each
cohort attracts significant interest, with 700+ applications from both students and experienced professionals seeking to pivot into
AI, reflecting the strong market demand for AI skill development. The program provides participants with a structured,
multi-stage curriculum:

     ●    AI Agent Foundations – Establishes core understanding of AI Agents and hands-on proficiency with NeuralSeek’s
          platform.
     ●    Agentic AI for Business – Applies AI Agent capabilities to real-world enterprise use cases, enabling participants to
          design impactful business solutions.
     ●    Multi-Tier AI Agent Architecture – Develops advanced skills in designing, deploying, and managing multi-agent
          systems at scale.

Many participants enter the program with an entrepreneurial vision, aiming to build solutions on top of NeuralSeek’s technology.
Graduates emerge with proven technical expertise, practical experience, and an understanding of enterprise-grade AI
deployments; making them immediately valuable to organizations seeking to accelerate AI adoption. This program not only
advances AI education but also creates a direct talent pipeline for NeuralSeek clients, ensuring access to certified professionals
capable of delivering high-quality AI solutions from day one.




                                                                                                                                 52
                                            General Pricing Information
                                              https://neuralseek.com/pricing

NeuralSeek offers flexible pricing models: Cloud SaaS and Containerized (On-Premise or Private Cloud) Licensing. The Cloud
SaaS model is usage-based, with fees charged per instance hour plus a per-Seek rate, varying by provider (AWS, IBM, Azure)
and whether the customer brings their own LLM or uses one provided. The Containerized model typically involves a one-time
upfront perpetual license fee for unlimited usage rights, plus an annual Support and Maintenance (S&M) fee starting at 20% of
the license cost, increasing by 5% each year. We do offer a special containerized subscription license to only select clients. No
standard incentive or penalty fees are listed. Professional services, if required for implementation or customization, are billed
separately per Statement of Work. Discounts may be available for enterprise-wide or multi-year agreements. If travel is required,
Travel & Expenses are billed at cost. All models include software updates, patches, and technical support under the applicable
support arrangement.




         We maintain our pricing publicly for SaaS and deliver custom pricing for Enterprise wide licensing.




                                                                                                                              58
