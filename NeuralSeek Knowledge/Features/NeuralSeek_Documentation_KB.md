# NeuralSeek Documentation — Knowledge Base

_This document is a consolidated snapshot of the NeuralSeek wiki at https://draft-wiki.neuralseek.com/, assembled for use as a chatbot knowledge base. Each page below is preceded by its source URL so the bot can cite the original documentation._

---

## Table of Contents

- [Home](#home)
  - [NeuralSeek Documentation — Home](#neuralseek-documentation-home)
- [About NeuralSeek](#about-neuralseek)
  - [Data Security and Privacy](#data-security-and-privacy)
  - [Partnerships](#partnerships)
  - [Plans and Pricing](#plans-and-pricing)
- [Guides — Data](#guides-data)
  - [Data Guides Overview](#data-guides-overview)
  - [Proposals](#proposals)
  - [Tuning Guide](#tuning-guide)
  - [Dynamic Filters](#dynamic-filters)
  - [VirtualKB](#virtualkb)
  - [Document Ingestion](#document-ingestion)
  - [Replay Guide](#replay-guide)
- [Guides — Integration](#guides-integration)
  - [Integration Guides Overview](#integration-guides-overview)
  - [Chat SDK Integration](#chat-sdk-integration)
  - [Training Virtual Agents](#training-virtual-agents)
  - [Backup and Restore](#backup-and-restore)
  - [ElasticSearch Vector Model](#elasticsearch-vector-model)
  - [Pinecone Configuration](#pinecone-configuration)
  - [Providing Context](#providing-context)
  - [Watsonx Streaming Context Guide](#watsonx-streaming-context-guide)
  - [Implementing Feedback](#implementing-feedback)
  - [NICE CXone Integration](#nice-cxone-integration)
- [Guides — Models](#guides-models)
  - [Model Guides Overview](#model-guides-overview)
  - [Multimodal LLM Configuration](#multimodal-llm-configuration)
  - [Semantic Model Tuning](#semantic-model-tuning)
- [Features](#features)
  - [Answer Curation](#answer-curation)
  - [Auto Data Cleanse](#auto-data-cleanse)
  - [Caching](#caching)
  - [Content Analytics](#content-analytics)
  - [Conversational Context](#conversational-context)
  - [Dynamic Personalization](#dynamic-personalization)
  - [Entity Extraction](#entity-extraction)
  - [Intent Categorization](#intent-categorization)
  - [Language Support](#language-support)
  - [Language Identification](#language-identification)
  - [Multi-LLM Orchestration](#multi-llm-orchestration)
  - [PII Detection](#pii-detection)
  - [Replay Feature](#replay-feature)
  - [Real-time Logging](#real-time-logging)
  - [Semantic Analytics](#semantic-analytics)
  - [Sentiment Analysis](#sentiment-analysis)
  - [Table Understanding](#table-understanding)
- [Reference — Integrate / Interface](#reference-integrate-interface)
  - [Integrate Tab Overview](#integrate-tab-overview)
  - [Supported KnowledgeBases](#supported-knowledgebases)
  - [Supported LLMs](#supported-llms)
  - [Supported Virtual Agents](#supported-virtual-agents)
- [Changelog](#changelog)
  - [Changelog](#changelog)

---

## Home

### NeuralSeek Documentation — Home

**Source:** <https://draft-wiki.neuralseek.com/en/home>

Welcome to the official NeuralSeek documentation. Your central hub for learning, integrating, and building with NeuralSeek.
Here you'll find step‑by‑step guides, API references, integration walkthroughs, and feature overviews to help you succeed.

##### Get Started

NeuralSeek connects your data, models, and integrations to deliver accurate, meaningful AI answers and workflows.

- Data Guides
- Integration Guides
- Model Guides
- Reference & API
- Changelog

##### About NeuralSeek

NeuralSeek brings advanced retrieval, grounding, and reasoning together in one platform.

- Security & Privacy
- Partnerships
- Plans & Pricing

---

## About NeuralSeek

### Data Security and Privacy

**Source:** <https://draft-wiki.neuralseek.com/documentation/about/data_security_and_privacy>

NeuralSeek is both a UI and a (REST) API. All data that flows to or thru us is encrypted SSL/TLS. All data stored is also encrypted.

- Neither NeuralSeek nor any of our sub processors use any customer data to learn/train models or systems. All user data and generated answers are owned by and for the sole use of the customer.
- Data processing locations for our Pay-per-answer plan:
  * Dallas: US-based LLM's.
  * Frankfurt: EU-based LLM's
  * Sydney: Australia-based LLM's
- Data is stored within a datacenter. So data storage can be localized to a region. (Eg within the EU)
- We do not generate any data that is personally identifiable while delivering the service. We utilize optional session tokens, decided on and provided by the customer's calling service to maintain an optional state. We have an option on our API to generate "Personalized" answers, where the customer passes us personal data on a defined option on our endpoint. This flags the result as potentially containing PII, and will be treated the same as any content the system automatically flags as containing PII. (Flag, Mask, Hide, Delete)
- Data is retained on our service for a minimum of 30 days before it is automatically deleted. A customer may delete their generated data from their account at any time, however if using our plans with a curated LLM the curated LLM provider may retain the data for up to 30 days for purpose of monitoring abuse. BYO-LLM plans have no minimum data hold requirements.
- In terms of specifics on which LLM's and sub-processors we use, we can have those conversations as needed under NDA with enterprise customers. The short answer is we use multiple, some internally developed, some provided by third part sub-processors.
- For enterprise customers NeuralSeek is available as a containerized platform that can be deployed anywhere, on top of kubernetes or openshift.

For more information, please visit <https://neuralseek.com/eula>

---

### Partnerships

**Source:** <https://draft-wiki.neuralseek.com/documentation/about/partners>

We make the hype around Generative AI real for businesses.
Click the logo icons below to discover how you can build and manage multiple agentic generative AI solutions from a single platform.

###### NeuralSeek on AWS MarketPlace

[![NeuralSeek on AWS](https://draft-wiki.neuralseek.com/assets/more_about_NS/AWS_logo.png)](https://neuralseek.com/generative-ai-aws-solutions "Click Here for AWS Partnership")

###### NeuralSeek on Azure MarketPlace

[![NeuralSeek on Azure](https://draft-wiki.neuralseek.com/assets/more_about_NS/Azure_logo.png)](https://neuralseek.com/generative-ai-azure-solutions "Click Here for Azure Partnership")

###### NeuralSeek on IBM Cloud

[![NeuralSeek on IBM](https://draft-wiki.neuralseek.com/assets/more_about_NS/IBM_logo.png)](https://neuralseek.com/generative-ai-ibm-solutions "Click Here for IBM Partnership")

---

### Plans and Pricing

**Source:** <https://draft-wiki.neuralseek.com/documentation/about/plans>

##### Pay-per-answer

Create natural language answers to user questions based on your raw Corporate KnowledgeBase. This plan uses our curated LLM and does not offer connectivity to other LLMs. All other features are available with this plan. The NeuralSeek Curated LLM is kept pinned to the industry's highest price-performing LLM. Specifics such as exact LLM used for the curated LLM are discussable only under NDA with Cerebral Blue. We automatically update the underlying minor version of the LLM, and major version changes are controllable by the end user. The BYOLLM (Bring your own LLM) plan is available if you require a specific LLM.

This plan's features include, but are not limited to:

- Automatic catalog, curation and grouping of questions and answers
- Export to a Virtual Agent
- Round-trip monitoring to a Virtual Agent
- Sentiment scoring
- Automatic language detection
- Translate text into other languages
- Extract Entities from text
- Categorize text by matching categories and matching or creating Intents
- Connect to any supported KnowledgeBase, including Watson Discovery, Watsonx Discovery, Elastic, Kendra, pinecone, Milvus, or a Virtual KB based on any connection in mAIstro...

##### Flex

The NeuralSeek Flex plan is a bring-your-own LLM plan featuring unlimited usage, and a flex license allowing you to optionally and additionally install NeuralSeek components on your hardware, behind your firewall as needed to meet your security requirements while you are subscribed to this flex plan. All NeuralSeek features are supported on this plan.

This plan's features include, but are not limited to:

- Automatic catalog, curation and grouping of questions and answers
- Export to a Virtual Agent
- Round-trip monitoring to a Virtual Agent
- Sentiment scoring
- Automatic language detection
- Translate text into other languages
- Extract Entities from text
- Categorize text by matching categories and matching or creating Intents
- Unlimited instances within a deployment to allow for logical separation of usecases
- Connect to any supported LLM
- Connect to any supported KnowledgeBase, including Watson Discovery, Watsonx Discovery, Elastic, Kendra, pinecone, Milvus, or a Virtual KB based on any connection in mAIstro

Each base instance (or install) is licensed for 10,000 users. Additional users may be added in blocks of 10,000.
> **Note**
> Upon Flex plan purchase, we provide a free working session (up to 1 hour) designed to guide users live through the installation process and grant access to the docker repository. This is generally sufficient time to complete product installation with basic authentication. Integrating Single Sign-on (SSO) may take additional time.

###### On-Premise Details

The Flex plan grants license for you to install NeuralSeek on-premise or on your cloud provider of choice, on your your hardware, behind your firewall to meet security requirements. The flex plan allows for complete network isolation, as well as projects that require compliance with FedRamp, GovCloud, and HIPAA regulations. Neuralseek on-premise runs as containers on top of OpenShift (OCP) or Kubernetes.

###### Installation Requirements

Minimum sizing requirements for on-prem installation include:

- 12 Core CPU
- 64 GB RAM/Memory
- 100 GB Available Disc Space
- If self-hosting an LLM (not using [watsonx.ai](http://watsonx.ai) or sagemaker) your self-hosted LLM will require a GPU VM that is equivalent or better to a single NVIDIA A10G

###### Installation Steps

1. Log onto Red Hat OpenShift console with appropriate domain.
2. Modify the appropriate .yml file with the corresponding hostname OpenShift external URL.
  - .yml files are provided during consultation meeting.
3. Verify connectivity to the Cerebral Blue docker in .yml files.
  - Permission access will be granted during consultation meeting. Provide the appropriate username.
4. Copy the contents of the .yml files into your OpenShift console by clicking the plus icon, then click create.
5. Route will be created manually by navigating to **Networking → Routes → Create Route**.
  - Add a unique name.
  - Select the service to route to.
  - Select the target port for traffic.
  - Optionally, provide a TLS certificate. Default will set to HTTP.
6. Click the link to the route to open the NeuralSeek User Interface.

> **Note**
> It will take approximately 15 minutes for the pods to run. View their status in the OpenShift console under **Workloads → Pods**.

##### Bring-your-own-LLM

Leverage all of NeuralSeek's features, but instead of using our curated LLM, you can connect via our no-code connectors to leading commercial and open-source LLM's. This enables you to run within a single datacenter or country, or choose the commercial LLM that best fits your business and pricing needs.

**Refer to our Integrations documentation for a list of supported LLM's.**

This plan's features include, but are not limited to:

- Automatic catalog, curation and grouping of questions and answers
- Export to a Virtual Agent
- Round-trip monitoring to a Virtual Agent
- Sentiment scoring
- Automatic language detection
- Translate text into other languages
- Extract Entities from text
- Categorize text by matching categories and matching or creating Intents
- Connect to any supported LLM
- Connect to any supported KnowledgeBase, including Watson Discovery, Watsonx Discovery, Elastic, Kendra, pinecone, Milvus, or a Virtual KB based on any connection in mAIstro

##### Search

The Search Plan is for use cases not requiring a Virtual Agent. NeuralSeek provides a search interface to supported KnowledgeBases, and will provide search responses plus generative AI summaries. Any generated AI summary incurs a per-call usage fee. Cache responses are included at no additional cost. This plan uses our curated LLM and does not offer connectivity to other LLMs. The NeuralSeek Curated LLM is kept pinned to the industry's highest price-performing LLM. Specifics such as exact LLM used for the curated LLM are discussable only under NDA with Cerebral Blue.

This plan's features are identical to the pay-per-answer plans EXCEPT:

- No export to a Virtual Agent is allowed
- No round-trip monitoring to a Virtual Agent is allowed
- No sentiment scoring
- No automatic language detection

##### Small Business

The Small Business plan is the easiest plan to get NeuralSeek running in minutes with no experience required. This plan is pre-connected to both our curated LLM and a KnowledgeBase, and you cannot swap these out. Simply point NeuralSeek at your website or upload documents, connect to a Virtual Agent, and go-live! This plan uses our curated LLM and does not offer connectivity to other LLMs. All other features are available with this plan. The NeuralSeek Curated LLM is kept pinned to the industry's highest price-performing LLM. Specifics such as exact LLM used for the curated LLM are discussable only under NDA with Cerebral Blue.

This plan's features include, but are not limited to:

- Automatic catalog, curation and grouping of questions and answers
- Export to a Virtual Agent
- Round-trip monitoring to a Virtual Agent
- Sentiment scoring
- Automatic language detection
- Translate text into other languages
- Extract Entities from text
- Categorize text by matching categories and matching or creating Intents

**For cloud-specific available plans, see cloud provider for up-to-date cost information.**

---

## Guides — Data

### Data Guides Overview

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/index>

##### Data

- [Proposals](https://draft-wiki.neuralseek.com/documentation/guides/data/proposals/index)
- [Tuning Guide](https://draft-wiki.neuralseek.com/documentation/guides/data/tuning_guide/index)
- [Dynamic Filters](https://draft-wiki.neuralseek.com/documentation/guides/data/dynamic_filters/index)
- [VirtualKB](https://draft-wiki.neuralseek.com/documentation/guides/data/virtual_kb/index)
- [Document Ingestion](https://draft-wiki.neuralseek.com/documentation/guides/data/doc_ingestion/index)
- [Replay](https://draft-wiki.neuralseek.com/documentation/guides/data/replay_guide/index)

---

### Proposals

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/proposals/index>

##### Overview

NeuralSeek offers a flexible and dynamic way to manage configurations through the use of "Proposals." This feature allows administrators and Subject Matter Experts (SMEs) to test proposed changes separately from the main configuration, enabling multiple configurations to run concurrently. This guide will walk you through the common issues, steps to configure this feature, and provide answers to frequently asked questions.

###### Common use cases

- **Running Multiple Configurations**: Users often need to run different versions of NeuralSeek simultaneously, especially when making backend changes without affecting existing extensions or integrations.
- **Overriding Default Settings**: Users may want to override default settings like "Max Verbosity" for specific API calls without changing the global configuration.
- **Managing Multiple KBs/Projects**: Integrating multiple projects from Watson Discovery into a single NeuralSeek instance can be challenging.

###### How to use Proposals

![image](https://draft-wiki.neuralseek.com/assets/guides/data/changelog-button.png)![image](https://draft-wiki.neuralseek.com/assets/guides/data/changelog-example.png)

- **Save Your Configuration as a Proposal**:

  * Navigate to the configuration tab in NeuralSeek.
  * Adjust your settings to the desired state.
  * Instead of clicking "Save," click on "Propose Changes."
  * Name the proposal (optional) and save within the popup. This will show "Proposal Saved".
  * Find your **Proposal ID (green arrow)** within the "Change Logs" menu. An ID number will be shown in the Date column. This will be used to reference the proposal configuration.

- **Managing Configurations/Proposals**:

  * For each unique configuration needed, save it as a separate proposal.
  * Reference the appropriate proposal ID when making API calls to apply the desired configuration.
  * Using the Change Log menu, you are able to **"Activate" (purple arrow)** or **"Delete" (red arrow)** proposals.
  * Activating a proposal will apply that change to the current/live configuration.

- **Using Proposals in API Calls**:

  * When making an API call to NeuralSeek, pass the `proposalID` as a parameter.
  * This allows you to use the specific configuration associated with the proposal ID without affecting the main configuration.

- **Accessing Proposals from Different Tabs**:

  * Proposals can be accessed and called dynamically from the API, the Seek tab, or the Home tabs.

###### Frequently Asked Questions (FAQs)

- **Q: Can I have two versions of NeuralSeek running at the same time?**

  * A: Yes, you can use the proposals feature to run multiple configurations simultaneously.

- **Q: Is it possible to use multiple projects from Watson Discovery in the same NeuralSeek instance?**

  * A: Yes, save each project configuration as a different proposal and call them via the API using the respective proposal IDs.

- **Q: Can I override settings like "Max Verbosity" at the API call level?**

  * A: Yes, save a configuration with your preferred settings as a proposal and use its ID in the API call to override default settings.
> **Note: By following this guide, you should be able to effectively utilize NeuralSeek's proposals feature to manage various configurations and enhance your instance's flexibility and efficiency.**

---

### Tuning Guide

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/tuning_guide/index>

##### Overview

This guide provides information on improving answers from the connected KnowledgeBase - Your **ground truth**.

Use this guide to help get started, improve answers, and learn about some best practices.

##### Bootstrapping your Agent

NeuralSeek aims to make bulk-tuning easy, offering different methods for Subject-Matter Experts (SMEs) to collaborate and curate answers.

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/ns-home.png)

To bootstrap your agent, you may find these options on the home screen.

- Auto-Generate Questions: This will run a query against your connected KnowledgeBase and attempt to generate a list of relevant questions to your subject matter, and then mimics the below option
- Manually Input Questions: Accepts a list of newline-separated questions, and will perform a Seek action with each question. This populates the Curate tab, while also generating a report spreadsheet that can be distributed among SMEs to weigh in on answers and make edits. (you can also export a similar spreadsheet from the Curate tab)

Finally, you can upload the resulting edits via the "Upload Curated Q&A" option. Congratulations! You've quick-tuned your agent to your most important or relevant subjects.

##### Improving Answers

There are many ways to improve generated answers. This can include:

- Utilizing Semantic Scores to monitor or block low-quality answers
- Updating or improving documentation - Answers are only as good as the ground truth!
- Controlling the amount of information sent to the LLM and "force" answers from the KnowledgeBase
- Choosing Lucene VS Vector search (we also support a Hybrid mode!)

###### Understanding Generated Answers

A common issue with LLMs: giving answers that are irrelevant or inaccurate. NeuralSeek makes it easier to handle these cases.

To reduce low quality answers, start on the Seek tab: Ask a question.

To help analyze your answers, take a look at the following:

**Review the Semantic Score**

- Is it low? (below 20%) - Perhaps your documentation does not compare well to the question posed, or there is many source jumps / unattributed terms
- Is it high? (above 60%) - If the answer is low quality - does your documentation have conflicting answers, or very similar terminology to the given query?

**Understand the Semantic Analysis text**

- This is meant to offer insight into the scores given - e.g. a lot of terms from many documents, or primarily one source of documentation.

**Review the KB scores**

- Low Coverage - There is not many documents matching the query
- High Coverage - There are many documents matching the query, or few documents that match exactly
- Low Confidence - The source KB thinks we do not have good matches to the query
- High Confidence - The source KB has found good query matches, but may not answer the query directly

**Review the documentation sources**

- Expand the accordions below to see the actual source documentation provided by the KnowledgeBase. This is what is sent to the LLM for language generation.
- Improve the documentation: If the source documentation does not directly answer the question, updating the source content will almost always help.
- Adjust the Document Score Range: This widens, or shrinks, the top % of documents that will be considered.
- Adjust the Snippet Size: This can help narrow passages out of blocks of unrelated text, or widen the scope for large paragraphs that only mention the subject of your query once.
- Narrow the Max Documents per Seek: This can help target only the best scoring/matching documents, and avoid confusing some LLMs with a slew of information.

To give some examples: Here, we've set the maximum allowed documents to one with snippet size set to 2000 (the largest):

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/1_doc_2000_snippet_size.png)
![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/seek_with_1_doc_max.png)

Some things to notice:

- There is only one document result
- The semantic score is high
- If you expand the document accordion - there is a lot of text returned in this passage

In the next example, we've set the maximum allowed documents to three with snippet size set to 400 (relatively small):

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/3_doc_400_snippet_size.png)
![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/seek_with_2_doc_max.png)

We now have:

- One additional document (total of 2)
- A lower semantic score
- More source jumps in the answer

Generally speaking, and for most use cases, it is better to provide a few top quality documents, versus many low quality or unrelated documents, to the LLM for answer generation. Using these settings can help focus or widen the documentation as needed per use-case.

**Replay a Seek**

Users can also go into Logs and pull previous answers by using our Replay feature. This requires enabling Corporate Logging with an instance of Elasticsearch. For more information, refer to our [Replay article](https://draft-wiki.neuralseek.com/documentation/guides/data/replay_guide/index) section.

###### Optimal Settings

For most use-cases, the combination of settings that we get the best results with are close to:

**In KB Tuning:**

- Document Score Range: `0.6 - 0.8`
- Max Documents per Seek: `4 - 5`
- Snippet Size: If your documents are mostly filled with unrelated small paragraphs (2-3 sentences) - like an faq document - then `400 - 600` is appropriate. Note it is always best to break up documents containing unrelated information into multiple documents. If your documents are large reference manuals that contain long passages - use the max snippet size available to you.

**In Answer Engineering:**

- `Answer Verbosity` slider favoring the "Very Concise" side
- Enable `Force Answers from the KnowledgeBase`

**In Governance and Guardrails:**

- `Warning Confidence` around +/- 20%
- `Minimum Confidence` around +/- 10-20%
- `Minimum Text` around 1-3 words
- `Maximum Length` around 20 words

###### Improving Source Documentation

One of the best ways to directly improve answer generation! Here's an example:

- A customer had a very large document, with an Acronym and a definition that was near the top of the document. The acronym was used hundreds of times across many pages. The source KB typically returned the paragraph with the most uses (matches) of the acronym, despite the overall snippet not answering the question directly. To improve the results, we split the document by pages, increased the score range and lowered the snippet size, allowing the KB to effortlessly bring back the relevant document passages while enabling the customer to control the amount of documentation fed to the LLM.

Generally speaking, the best practice for source documentation formatting is to have **individual documents that speak directly to the subject you want to answer**.

###### Hybrid and Vector Search

NeuralSeek supports Vector searching on some KnowledgeBase platforms. (see the Supported KnowledgeBases page for details)

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/hybrid_vector.png)

Vector Similarity searching is finding "similar" words, where Lucene is "exact matching" terms. For example, if you search for `Animal` you could also get results like `Cat, Dog, Mouse, Lizard`. It's not recommended to use only vector search for corporate-based RAG, as the chance of hallucination is incredibly high. For example - a user searches for `8.1.0`. Lucene will bring back only results with the exact term, where vector similarity may also return `8.0.1`, `8.10`, or similar.

Choosing the Hybrid implementation is recommended if using vector similarity - NeuralSeek will boost the Lucene results, offering Vector results as a sort of "fallback". This can help some use cases. Pure vector serach is not reccomended in any RAG pattern as any vector search increases the likelihood of halucinations.

###### Answer Variations

Generative AI often times will generate small variations for the same query.

Two ways to combat this:

- Set the "edited" answer cache setting to 1, and edit the answer on the curate tab.
- Set the "normal" answer cache setting to 1.

Both of these options will cause NeuralSeek to output consistent, identical answers. This also reduces the amount of language generation calls.
> **Note**
> Edited answers always return a Semantic Score of 100%.

##### Filtering Documentation

Many times there is a large amount of documents, or many data sources / types, to manage. Filtering can narrow down results in a large pool of data.

You may filter on any metadata field available from the KB. Simply set the desired field in the KnowledgeBase Connection settings, and pass a value for which to filter in the Seek call.

For example - Using `metadata.document_type` as the field, and `PDF` as the value, will return only documents with this field set to PDF. Use comma-separated values for an `OR` filter.
> **Note: Watson Discovery users**
> To filter by Collection ID: Under KnowledgeBase Connection, enable the Advanced Schema, and manually input `collection_id` in the filter field
>
> DQL_Pushdown is also an option for Discovery users - Select this option, and pass [DQL syntax](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-query-dql-overview) in the filter value on Seek calls.

Another tool to help target the best quality documentation available is to utilize the "Re-Sort values list" option. This allows you to prioritize certain documents over others - maybe use a collection ID to prioritize internal uploaded documentation over a general company website scrape, or perhaps PDFs have more concise data than your DOCX files. **This allows you to prioritize values without entirely excluding other values.**

##### Avoiding Timeouts

NeuralSeek has a limited amount of time to generate a response, as well as a context window that the LLM dictates. Sometimes, the LLM generates large answers and cannot finish its thought before the space runs out, we exceed the chatbot platform timeout, or we exceed the KB's timeout. This will occasionally cause the generated answer to have a dangling sentence near the end - NeuralSeek looks for these dangling responses and trims them back to a logical sentence.

Contributing factors can include:

- KnowledgeBase retrieval speed
- LLM generation speed
- Chatbot settings - timeout settings, etc
- Network latency

Some settings that may help:

- Reducing the maximum number of documents returned from the KB
- Using a faster LLM
- Reducing LLM verbosity in the NeuralSeek Configuration
- Increasing the chatbot timeout threshold
- Provisioning services in the same regions

> **Note**
> When adjusting the verbosity setting, for shorter answers change the verbosity setting to "more concise". For longer/more descriptive answers change the verbosity setting to "more verbose".

##### KnowledgeBase Translation

It can be challenging to work with multiple languages. For example - you want the LLM to respond in Spanish, but the source documentation is in English. NeuralSeek can solve this: In the Platform Preferences configuration, enable `Translate into KB Language`, and set the desired output language.

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/platform_preferences.png)

This allows NeuralSeek to:

- Accept a question in Spanish (for example)
- Translate to English (source documentation language)
- Perform a KB search in English
- Generate an Answer in English
- Translate the Answer to Spanish

> **Warning: For Bring-your-own LLM users**
> When using the cross-language feature of NeuralSeek, some LLMs will not excel at this. You will need to use a powerful model like GPT, Llama 70b, or Mixtral.

You can set NeuralSeek's output language to "Match Input" to respond in the same language as the query. Another choice is to have the chatbot control the language returned. Some chatbots support passing the language dynamically as a context variable to the NeuralSeek API. The source of the context variable can be the web browser language or part of the chatbot's URL that tells you the user's language.

Example from watsonx Assistant:

![Click_to_insert](https://draft-wiki.neuralseek.com/assets/guides/data/extension_config.png)

##### Using Multiple Data Sources

NeuralSeek allows you to use multiple configurations on-demand, effectively overriding any settings currently in the Configure tab. This is useful if you want to use multiple KB sources, project IDs, or similarly exceed the UI limitations.

![download settings](https://draft-wiki.neuralseek.com/assets/guides/data/download_settings.png)

Simply configure NeuralSeek with the desired parameters, save, and then "Download Settings" as pictured.

This will download a `.dat` file, containing an encoded string of all current settings - including KB details, project IDs, LLMs, etc.

On Seek API calls, set `options.override` to this encoded string - Effectively using these saved settings for this Seek call, ignoring "current" settings in the UI.

---

### Dynamic Filters

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/dynamic_filters/index>

##### Overview

**What is it?**

- Dynamic Query Language (DQL) is a system for defining flexible, operator and rule-based filters that refine document results based on specific criteria. This interprets filter expressions, enabling real-time adjustments to document queries without modifying the core dataset.

**Why is it important?**

- Dynamic filters empower users to refine document searches using DQL operators. This allows for more precise queries by narrowing document results to specific groups or areas without being limited to filtering by one singular metadata property in a very rigid manner (exact matches). DQL allows you to filter by many or few facets as needed.

**How does it work?**

- NeuralSeek converts DQL into the correct query format for the connected KnowledgeBase (KB), allowing support for DQL even on KBs that do not natively support it.

---

##### Setting up Dynamic Filters

To use dynamic filter capabilities within NeuralSeek, we need to configure `DQL_Pushdown` as follows:

1. Navigate to the **Configuration** tab in the **KnowledgeBase Connection** section.

    ![Configuration Knowledge Base](https://draft-wiki.neuralseek.com/assets/guides/data/config_knowledge.png)

2. In the **Filter Field** drop-down, select the `DQL_Pushdown` option. This enables queries to include dynamic filters.

    ![DQL Pushdown](https://draft-wiki.neuralseek.com/assets/guides/data/dql_pushdown.png)

You can now pass dynamic filter language through the filter parameters available.
> **Warning: Elasticsearch and watsonx Discovery users**
> Please note that due to the tokenization method that Elasticsearch uses, dynamic filters will not always work as expected on properties that are not of type `keyword`. For best results, set up your index to either have important types as `keyword` or have a duplicate nested property that is type `keyword` for use with dynamic filters.

###### Applying filters in Seek

1. Navigate to the Seek tab.

2. Find the "filters" button (highlighted by the red arrow)

3. Input your DQL filter string.

![seek filters](https://draft-wiki.neuralseek.com/assets/guides/data/seek_filters.png)

###### Applying filters in mAIstro

1. Locate the `KB Search` node in mAIstro.

2. You can now begin adding filters to query the KnowledgeBase effectively.

![KB Search Example](https://draft-wiki.neuralseek.com/assets/guides/data/kb_search_example.png)

###### Applying filters via the API

Simply pass the regular or DQL filter string as the `filter` parameter of the Seek API call.

![api filter](https://draft-wiki.neuralseek.com/assets/guides/data/api_filter.png)
> **Tip**
> NeuralSeek's DQL parser is able to distinguish between numbers, booleans, and strings. It also allows for intentionally blank values.
>
> For example:
>
> - `age::25` is a **number**, where `age::"25"` is a **string**.
> - `available::true` is a **boolean**, where `available::"true"` is a **string**.
> - `value::""` is an intentionally blank value.
---

##### Query Filtering Examples

Here are some examples of how to filter the KnowledgeBase in NeuralSeek using dynamic filters, given this example document that we want to highlight using filters:

    {
      "document_id": "doc_001",
      "section_name": "Overview",
      "content": {
        "title": "NeuralSeek Use Cases Overview",
        "text": "An introductory guide to NeuralSeek use cases, focusing on application and benefits.",
        "date_created": "2023-02-15"
      },
      "author": "NeuralSeek Bot"
    }

- **Exact Match Filter**: To retrieve only documents that are exactly matched with the term `"Overview"`, apply the filter as follows. This will return documents related to 'neuralseek use cases' with "Overview" specifically in the `section_name` property.

    section_name::"Overview"

- **Delimiter and Date Comparison Filter**: To retrieve only documents that are greater or equal `"2023-01-01"`, apply the filter as follows. This will return documents in that range specifically in the `content.date_created` property.

    content.date_created >= "2023-01-01"

- **Wildcard Filter**: To retrieve documents where the `title` within `content` begins with "neu" and is followed by any characters, use the wildcard filter as shown below. This filter will return all documents with a `content.title` that starts with "neu" (e.g., "NeuralSeek," "neurobiology").

    content.title:neu*

---

##### Operator reference

###### Delimiter `.` (JSON hierarchy delimiter)

**Description**:
The `.` operator is used to access fields within a nested JSON structure. It allows you to specify subfields within a field, making it easy to search within specific sections of hierarchical data.

`title.subsection:"AI"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Phrase Query `""`

**Description**:
Placing terms within quotation marks `" "` searches for an exact phrase match within the specified field, preserving the word order. This is useful for finding specific phrases instead of individual terms. Please note that Phrase Query converts all values to strings, even in KnowledgeBases that support native data types such as numbers, booleans, or dates.

`url:"neuralseek"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Exact Match `::`

**Description**:
The `::` operator performs an exact match, ensuring that the field content matches the specified term or phrase exactly. It is stricter than `:` and `""`, as it does not allow partial or flexible matches.

`content::"AI"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Not an Exact Match `::!`

**Description**:
The `::!` operator excludes documents that exactly match a specified term or phrase. It is the negation of the `::` operator and can be useful for filtering out precise phrases.

`content::!"large models"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Nested Grouping `()`

**Description**:
Parentheses `()` are used to group queries, allowing for more complex expressions with combined operators. They let you control the order of operations in a query, much like in mathematical expressions.

`(title:"AI" | title:"ML") , content:"deep learning"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### OR `|`

**Description**:
The `|` operator allows you to perform an OR operation between two or more terms. It returns documents that contain at least one of the specified terms, making it useful for broad searches.

`title:"AI" | title:"machine learning"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### AND `,`

**Description**:
The `,` operator performs an AND operation, requiring that both terms appear within the specified fields. This is useful when you need to find documents containing multiple specific terms.

`title:"AI", content:"neural networks"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Numerical and Date Comparisons `>, <, >=, <=`

**Description**:
These operators allow for numerical or date comparisons within fields. Use them to search for records within a specific range or threshold of values.

`publish_date>=2023-01-01`
`revision>5, revision<10`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch
- Kendra

---

###### Includes `:`

**Description**:
The `:` operator performs a search to see if the specified field includes the given term or phrase. This is a broad match that will return results containing the specified term anywhere within the field.

`title:"LLMs"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch

---

###### Does Not Include `:!`

**Description**:
The `:!` operator is used to exclude documents that contain a specified term within a field. It is the negation of the `:` operator and helps filter out unwanted terms.

`content:!"profanity"`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch

---

###### Field Exists `:*`

**Description**:
The `:*` operator checks if a field is present in a document, regardless of its content. It's useful for filtering records based on the existence of specific fields.

`author:*`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch

---

###### Field Does Not Exist `:*!`

**Description**:
The `:*!` operator checks if a field is absent in a document. It's useful for finding records missing a specific field.

`author:*!`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch

---

###### Wildcard Operator `:*`

**Description**:
The `:*` operator is used to match any value within a specified field, acting as a wildcard. This operator is helpful for locating records where a field contains any value, rather than a specific one.

`author:*`

**Supported By**:

- Watson Discovery
- watsonx Discovery
- ElasticSearch

---

### VirtualKB

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/virtual_kb/index>

##### Overview

**What is it?**

- Virtual KB is a feature in mAIstro that allows you to define a flow and use it as a virtual knowledge base. This feature enables you to combine multiple knowledge sources into a single, unified knowledge base, providing a more comprehensive and flexible solution for your information retrieval needs.

**Why is it important?**

- A Virtual KB enhances your application's search and discovery by integrating multiple knowledge sources, delivering more comprehensive and relevant results. It offers flexibility and scalability, allowing you to easily adjust the knowledge sources as your needs change.

**How does it work?**

- Virtual KB allows you to connect and integrate various knowledge sources, such as databases, content management systems, and external APIs, into a single virtual knowledge base. Begin by building a flow in mAIstro utilizing our variety of native functions and connectors or reference our Virtual KB example template for an easy guide on configuring a Virtual KB.

##### Example Template in mAIstro

1. Navigate to the mAIstro tab in your NeuralSeek instance.
2. Click on Example Templates, and search for the template titled **Virtual KB**.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_selectExTemp.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_selectVirtualKBtemplate.png)

This flow utilizes the **Virtual In** and **Virtual Out** nodes, located underneath RAG Tools on the sidebar menu. It passes a DuckDuckGo Search connector and a Rest API connector with a Wikipedia URL to the Large Language Model for answer generation within the Seek tab. We are now able to utilize the World Wide Web as a knowledge source for answer generation.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_mAIstroVisual.png)

    {{ virtualKbIn  }}
    {{ duckSearch  | query: "<< name: virtualKbIn.contextQuery>>" }}=>{{ variable  | name: "parallelDuckRaw" }}
    {{ post  | url: "https://en.wikipedia.org/w/api.php?action=query&format=json&list=search&srsearch=<< name: virtualKbIn.contextQuery, prompt: true >>" | body: "" | headers: "" | username: "" | password: "" | apikey: "" | operation: "POST" | jsonToVars: "true" }}=>{{ varsToJSON  | path: "query.search" | variable: "s1" | includePath: "false" | output: "true" }}=>{{ arrayFilter  | filter: "0-3" | filterType: "IndexRange" }}=>{{ reMapJSON  | match: "title" | replace: "document" }}=>{{ reMapJSON  | match: "snippet" | replace: "passage" }}=>{{ regex  | match: "/(\"document\":\")([^\"]+)/g" | replace: "$1$2\",\"url\":\"https://en.wikipedia.org/wiki/$2" | group: "" }}=>{{ regex  | match: "/^\[/" | replace: "" | group: "" }}=>{{ regex  | match: "/<\/?span.*?>/g" | replace: "" | group: "" }}=>{{ variable  | name: "wikipedia" }}
    << name: parallelDuckRaw, prompt: false >>=>{{ jsonEscape  }}=>{{ variable  | name: "duck" }}=>
    << name: duck, prompt: false >>=>{{ regex  | match: "/https?:\/\/[^\s)]+/g" | replace: "" | group: "0" }}=>{{ variable  | name: "url" }}
    {{ virtualKbOut  | context: "[{
    \"document\": \"DuckDuckGo Search\",
    \"url\": \"<< name: url >>\",
    \"passage\": \"<< name: duck, prompt: false >>\"
    },<< name: wikipedia, prompt: false >>" | kbCoverage: 0 | kbScore: 0 | url: "<< name: url >>" | document: "" }}

##### Selecting a Virtual KB

1. Navigate to the Configure tab in your NeuralSeek instance.
2. Expand the **KnowledgeBase Connection** accordion.
3. For KnowledgeBase Type, select the **Virtual KB** option.
4. For mAIstro Virtual KB template, select the **ex_Virtual_KB** option.
5. Click the red Save icon at the bottom of the screen to save your configuration.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_selectKB.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_selectTemplate.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_saveConfig.png)

##### Seek With a Virtual KB

1. Navigate to the Seek tab in your NeuralSeek instance.
2. Type in any question. For example, **Who is Taylor Swift?**
3. Click the Seek button to generate an answer.

As we review the answer generated, we can highlight over the statistical details and source brought back by NeuralSeek. The response is synthesized from a combination of DuckDuckGo and Wikipedia searches related to the singer. Our semantic analysis tells us about the varying jumps between source articles. Considering there is vast information on Wikipedia about Taylor Swift, we also receive a 99% KB Coverage score back.

By expanding the sources below, we can examine each one in detail. The provenance highlights indicate the specific keywords and phrases drawn from each source to form the final response.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_seek.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_seekStats.png)

##### Expanding Your KnowledgeBase

Ultimately, you can connect virtually any knowledge source to your NeuralSeek instance for answer generation via the Virtual KB connectors in mAIstro. You can choose from a variety of built-in database connectors, KnowelgeBase connectors, or Web Search connectors. Or, connect to any additional source via our Rest API connector node.

###### Building a Flow

1. Navigate to mAIstro in your NeuralSeek Instance.
2. Select the **Virtual KB - In** node from the sidebar menu under RAG Tools.

This node gives you several variables to use inside of your flow.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addKBin.png)

3. Select the **Website Data** node from the sidebar menu under Get Data. This will automatically link below your first node.
4. Click the gear icon to input any valid URL. In this example, we are connecting to a Google search: `https://www.google.com/search?gfns=1&q=<< name: virtualKbIn.contextQuery>>`
5. Select the **Set Variable** node from the sidebar menu under Control Flow.
6. Click and drag the Set Variable node to the right of the Website Data node to chain it.
7. Click the gear icon to set the variable name. In this example, the variable name is `google`.

The addition of the variable **virtualKbIn.contextQuery** allows the context of the user's query to be dynamically carried forward in the Google search.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addWeb1.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addVar1.png)

8. Select a second **Website Data** node.
9. Click the gear icon to input any additional URL. In this example, we are connecting to NeuralSeek's documentation page: `https://documentation.neuralseek.com/`
10. Select the **Set Variable** node from the sidebar menu under Control Flow.
11. Click and drag the Set Variable node to the right of the second Website Data node to chain it.
12. Click the gear icon to set the variable name. In this example, the variable name is `docs`.

We have added the NeuralSeek documentation as a second source of reference for our KnowledgeBase and are performing a static pull of the website's information.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addWeb2.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addVar2.png)

13. Select the **Virtual KB - Out** node from the sidebar menu under RAG Tools.
14. Click the gear icon to configure the information to be piped back into Seek. In this example, we want to define the passage by including the variable names: `<< name: google >>\n<< name: docs >>`.
15. Additionally, we can preset the kbCoverage, kbScore, url, and document name. In this example, we define the document name as `Virtual KB`.
16. Save your mAIstro flow with a unique name and optional description. In this example, the name is `websiteKB`.

Both of the websites will now be pulled live every time a Seek comes in. The information scraped from the sites will come out dynamically and in parallel, then plugged back into the Seek process for answer generation.
> **Note**
> While we use a single, concatenated document here for the sake of simplicity, it is possible to split this into multiple documents. Simply build a JSON object with an array of document objects containing properties: document (title), url, score, and passage.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_addKBout.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_finalBuild.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_saveNewFlow.png)

    {{ virtualKbIn  }}
    {{ web  | url: "https://www.google.com/search?gfns=1&q=<< name: virtualKbIn.contextQuery>>" }}=>{{ variable  | name: "google" }}
    {{ web  | url: "https://documentation.neuralseek.com/" }}=>{{ variable  | name: "docs" }}
    {{ virtualKbOut  | context: "<< name: google >>\n<< name: docs >>" | kbCoverage: 0 | kbScore: 0 | url: "" | document: "Virtual KB" }}

###### Configuring a Virtual KB

1. Navigate to the Configure tab in your NeuralSeek instance.
2. Expand the **KnowledgeBase Connection** accordion.
3. For KnowledgeBase Type, select the **Virtual KB** option.
4. For mAIstro Virtual KB template, select the **websiteKB** option.
5. Click the red Save icon at the bottom of the screen to save your configuration.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_saveNewConfig.png)

###### Seek with a Virtual KB

1. Navigate to the Seek tab in your NeuralSeek instance.
2. Type in any question. For example, **Does NeuralSeek provide a Hands-On Lab?**
3. Click the Seek button to generate an answer.

We can expand the Virtual KB source underneath KnowledgeBase Context and view which information was pulled from the Google Search and which was pulled from our NeuralSeek Documentation URL to generate the answer.

![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_seekNewBuild.png)
![image](https://draft-wiki.neuralseek.com/assets/guides/data/virtualKB_seekNewContext.png)

---

### Document Ingestion

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/doc_ingestion/index>

This mini-guide provides a quick overview of how to upload, process, and use PDF files of varying length and content in mAIstro.

##### PDF with text

Text-based PDFs are the most straightforward to work with in mAIstro. These files contain embedded digital text (not scanned images), which allows the AI to directly parse, analyze, and reuse the content.

To process a PDF containing solely text, the user should follow these steps:

1. Upload the PDF as a local document using the Upload Document node under Upload Data.
2. Use a context loop to split the document into smaller, readable sections.
3. Save the content into a variable to be used by the AI agent.
4. End the loop.

EXAMPLE NTL:

    {{ doc  | name: "example.pdf" }}
    {{ contextLoop  | tokens: "3000" | overlap: "10" }}
    {{ variable  | name: "exampleContent" | mode: "append" }}
    {{ endLoop  }}
    << name: exampleContent, prompt: false >>

![imagepdf](https://draft-wiki.neuralseek.com/assets/guides/data/pdftext.png)

##### PDF with images

When a PDF consists of scanned pages or embedded images (ex. from a physical book or printed document), it must be converted into readable text using Optical Character Recognition (OCR).

To process an image-based PDF for use in mAIstro:

1. Upload document using the Upload & OCR node under Upload Data.
2. Once OCR is applied, you can proceed with looping and variable setup just like with a text-based PDF.

For more information on OCR'ing an image, see [Upload & OCR](https://documentation.neuralseek.com/ui/maistro/features/ntl_functions/upload_data/#upload_document).

##### Long PDF with images and text

Complex PDFs such as technical manuals, equipment documentation, or compliance guides often contain both unstructured and structured content (e.g., narrative text, tables, flowcharts).

Processing a long PDF file with images and text in mAIstro can be efficiently managed by following these steps:

1. Set up a PDF loop, which splits a PDF by page and loops through the pages as both text and images.
2. Send contents to the LLM and save as a variable.
3. End the PDF Loop
4. Run context loops on the variable, then end the loop.

EXAMPLE NTL:

    {{ pdfLoop  | file: "longexample.pdf" | pagesPerLoop: "1" }}
    {{ LLM  | prompt: "Your job is to turn everything in this business document into text. \n\nIf there are any images, describe them in detail.\n \nIf there are charts or diagrams, explain all of the data points.\nHere is the text:\n<< name: pdfLoopText0, prompt: false >>\n" | cache: "true" | images: "<< name: pdfLoopImage0, prompt: false >>" }}=>{{ variable  | name: "accumulator" | mode: "append" }}
    {{ endLoop  }}
    << name: accumulator, prompt: false >>
    {{ contextLoop  | tokens: "3000" | overlap: "10" }}
    {{ endLoop  }}

![imagelong](https://draft-wiki.neuralseek.com/assets/guides/data/longpdfloop.png)
> **Tip: Final Tips**
>
> - You can check if your PDF is text-based by trying to highlight/select text. If you can't, it likely needs OCR.
> - Token Overlap is important for preserving sentence continuity across segments.
> - Test small samples first when working with large PDFs to fine-tune your prompts or loop settings.

---

### Replay Guide

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/data/replay_guide/index>

**What is it?**

- The Replay feature in NeuralSeek enables users to revisit previously logged questions and their corresponding answers, semantic analysis, and the KnowledgeBase documentation used to generate the response at that point in time. Replay can also be enabled for mAIstro flows, allowing you to revist the point in time when an AI Agent was evaulated in mAIstro for debugging or other tracking purposes.

**Why is it important?**

- As documentation in our KnowledgeBase gets updated, questions on the Seek tab get updated to account for that new information. As a result, a user could ask a question identical to one asked previously and receive a completely different answer if the documentation has been significantly changed. If one wants to go back to a previous response and notice the changes that occurred in the documentation to see how the answers evolve, the Replay feature is very useful to get some insight. Replay also allows us to track when an AI Agent runs successfully or not. By reviewing the Replay log for the mAIstro agent, then we can inspect the debugger icon at each step to analyze what steps were performed, and what was generated, during the run.

**How does it work?**

- First, check to make sure that you have Corporate Logging enabled with an instance of Elasticsearch. You can find the settings for Corporate Logging underneatch the `Configure` tab.

![corporate-logging](https://draft-wiki.neuralseek.com/assets/guides/data/corporatelogging.jpg)

- Navigate to the `Governance` tab on Neuralseek, and click on the **Seek Logs** page from the sidebar. There, you will find a log of all previously asked questions and answers from the `Seek` tab.
- Notice the small icon underneath the answer that resembles a clock turning backward. By clicking on it, you will be taken to the page as it appeared at that specific point in time.

![location](https://draft-wiki.neuralseek.com/assets/guides/data/seek1.png)

![previous-answer](https://draft-wiki.neuralseek.com/assets/guides/data/seek2.png)
![previous-context](https://draft-wiki.neuralseek.com/assets/guides/data/seek3.png)

- Repeat the above steps for **mAIstro Logs** as well.

![mAIstro-logs](https://draft-wiki.neuralseek.com/assets/guides/data/mAIstro_logs.png)
![mAIstro_replay](https://draft-wiki.neuralseek.com/assets/guides/data/mAIstro_replay.png)

- If the documentation used to answer the question has been updated, you can compare and contrast the results by asking the same question in the `Seek` tab.

![current-answer](https://draft-wiki.neuralseek.com/assets/guides/data/seek4.png)
![current-context](https://draft-wiki.neuralseek.com/assets/guides/data/seek5.png)

---

## Guides — Integration

### Integration Guides Overview

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/index>

##### Integration

- [Chat SDK](https://draft-wiki.neuralseek.com/documentation/guides/integration/chat_sdk_integration/index)
- [Training Virtual Agents](https://draft-wiki.neuralseek.com/documentation/guides/integration/training_virtual_agents/index)
- [Backup and Restore](https://draft-wiki.neuralseek.com/documentation/guides/integration/backup_and_restore/index)
- [ElasticSearch Vector Model](https://draft-wiki.neuralseek.com/documentation/guides/integration/elasticsearch_vector_model/index)
- [Pinecone Configuration](https://draft-wiki.neuralseek.com/documentation/guides/integration/pinecone_configuration/index)
- [Passing Conversational Context](https://draft-wiki.neuralseek.com/documentation/guides/integration/providing_context/index)
- [mAistro Streaming Endpoint with Watsonx](https://draft-wiki.neuralseek.com/documentation/guides/integration/wa_context_guide/index)
- [Implementing Feedback](https://draft-wiki.neuralseek.com/documentation/guides/integration/implementing_feedback/index)
- [NICE CXone](https://draft-wiki.neuralseek.com/documentation/guides/integration/nice_cxone_integration/index)

---

### Chat SDK Integration

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/chat_sdk_integration/index>

##### Overview

**What is it?**

- NeuralSeek's Chat feature enables users to test questions and generate answers using content from their connected KnowledgeBase, similar to Seek. The Chat SDK is easy to integrate, allowing seamless embedding in any website by adding a JavaScript snippet.

**Why is it important?**

- This feature empowers users to integrate NeuralSeek's capabilities with a chat-like interface rapidly. It also allows users to drag and drop documents directly into the chat to inquire about them, enhancing interaction and accessibility.

**How does it work?**

- NeuralSeek's Chat SDK connects to the KnowledgeBase content. Users can ask questions directly through a customizable chat widget, which is embedded on their website. When a user submits a question, the Chat SDK queries the NeuralSeek, processes the information, and delivers a relevant response. The integration supports document uploads, making it possible for users to drop files and ask specific questions based on file content. Additionally, options for welcome messages and styling help personalize the chat experience.

##### Embedding Chat

This is a step-by-step guide to integrating NeuralSeek's Chat SDK into a custom HTML or website.

- Edit the NeuralSeek embedded chat configuration within the NeuralSeek tab. You can preview most of your configuration changes in the chat window to the right of the embed box.

![chat](https://draft-wiki.neuralseek.com/assets/guides/integration/ns-chat.png)

- Copy the embedded chat script from the 'Embed Instructions' box within the NeuralSeek Chat tab.

![chat_config](https://draft-wiki.neuralseek.com/assets/guides/integration/chat_config.png)

- Paste the embedded chat script into your page. Make sure you have HTML elements in your page with IDs that match those defined in your chat config.

![chat_integrated](https://draft-wiki.neuralseek.com/assets/guides/integration/chat_integrated.png)

- At a minimum, you must have an element with an ID matching the `chatElement` configuration property. The embedded chat will be contained within this element.

- If `enableChatHistory` is set to true, you must include an element with an ID matching the `chatHistoryElement` configuration property. The chat history view will be contained within this element.

- If `enableChatOverlayToggleButton` is set to true, you must include an element with an ID matching the `chatOverlayToggleButtonElement` property. The button to toggle show/hide of the chat element will be contained within this element.

- Below is a minimal HTML File which includes the embedded chat, chat history, and chat toggle button:
> **Note: HTML Example**
>
> <!DOCTYPE html>
> <div id="chat"></div>
> <script type="module">
> import { NsChat } from 'http://api.localhost:3004/src/chatSDK.js';
>
> const chatConfig = {
> "userId": "myid",
> "chatElement": "chat",
> "chatHistoryElement": "chathistory",
> "chatOverlayToggleButtonElement": "chat-toggle-btn",
> "enableChatHistory": false,
> "enableChatOverlayToggleButton": false,
> "chatOverlayHeaderTitle": "NeuralSeek",
> "includeUrlInResponse": true,
> "urlDisplayText": "See more here",
> "apiServer": "http://api.localhost:3004",
> "loadingAnimationURL": "http://api.localhost:3004/images/ns-loader-chat.svg",
> "chatTheme": {
> "headerColor": "#4F1FF4",
> "headerTextColor": "#FFFFFF",
> "userMsgColor": "#F8D8FF",
> "userMsgTextColor": "#161616",
> "botMsgColor": "#B7EDFF",
> "botMsgTextColor": "#161616"
> },
> "chatTimeout": 23000,
> "chatPersist": true,
> "instanceId": "my-ns-instance",
> "embedCode": 000000000,
> "streaming": true,
> "maistroLed": false,
> "maistroFlow": "",
> "enableDrop": true,
> "allowedFiles": [
> ".png",
> ".jpg",
> ".jpeg"
> ],
> "welcomeMessage": "Welcome to NeuralSeek!",
> "welcomeBotMessages": [
> "How can we help?"
> ],
> "welcomeButtons": [
> "Tell me about NeuralSeek"
> ],
> "turnHistoryLimit": 1,
> "includeRequired": true
> }
>
> const chat = new NsChat(chatConfig);
> </script>
>
> <body style="background-color: #989898">
> <div id="chat" style="position:fixed; right:20px; bottom:20px; width: 450px; display: none; max-height: 50vh; min-height: max(160px,calc(min(250px, 100vh) - 10px)); height:calc(100vh - 140px);"></div>
> <div id="chat-toggle-btn" style="position: fixed; right: 20px; bottom: 20px;"></div>
> <div id="chathistory"></div>
> </body>
>
> **Note: Notice**
> Please note that for this example we use a test API server and embed code using NeuralSeek's own data. When embedding the NeuralSeek chat feature onto your own servers, make sure to swap the NeuralSeek URL with your own company's name.

##### Chat Config Properties

| Property Name | Type | Description |
| --- | --- | --- |
| chatElement | String | Provide the ID of the element to inject the chat window into |
| chatHistoryElement | String | Provide the ID of the element to inject the chat history into |
| chatOverlayToggleButtonElement | String | Provide the ID of the element to inject the chat toggle button into |
| chatOverlayHeaderTitle | String | Text to display in the header of the chat window |
| includeUrlInResponse | Boolean | True to include the top ranked URL in your knowledge base when providing a response. False to never include URLs in the response |
| apiServer | String | Autopopulated. API server URL corresponding to the instance of NeuralSeek you wish to use for the embedded chat |
| loadingAnimationURL | String | Provide a URL of a loading animation resource (gif, svg, etc.) to display when the chat is waiting on a response back from NeuralSeek. Defaults to the NeuralSeek loading animation |
| chatTheme.headerColor | String | Custom hexedecimal color code to set the header bar color |
| chatTheme.headerTextColor | String | Custom hexedecimal color code to set the header text color |
| chatTheme.userMsgColor | String | Custom hexedecimal color code to set the user message box background color |
| chatTheme.userMsgTextColor | String | Custom hexedecimal color code to set the user message box text color |
| chatTheme.botMsgColor | String | Custom hexedecimal color code to set the bot message box background color |
| chatTheme.botMsgTextColor | String | Custom hexedecimal color code to set the bot message box text color |
| chatTimeout | Integer | Milliseconds to wait for a response from the server before re-enabling interaction for the refresh button and chat input box. Defaults to the timeout specified in the Configure tab within NeuralSeek |
| chatPersist | Boolean | True to enable chat persistence. If you leave the chat page or refresh, the latest chat will be displayed for up to 1 hour after the last interaction. False to disable chat persistence and display a fresh chat every time. |
| instanceId | String | ID identifying the instance of NeuralSeek the embedded chat will use |
| embedCode | Number |  |
| streaming | Boolean | true to use streaming API, false to use non-streaming API |
| maistroLed | Boolean | Controls whether the chat will use regular seek or a specific mAIstro agent. Set to true if you wish to point the chat at a mAIstro agent. Must be used in conjunction with maistroFlow |
| maistroFlow | String | If maistroLed is set to true, provide the name of the mAIstro agent you wish to use here |
| enableDrop | Boolean | True to enable the ability to drag and drop files into the NeuralSeek chat area |
| allowedFiles | Array | Allowlist of file types that can be uploaded to the chat |
| welcomeMessage | String | Message to automatically display at the top when the chat is loaded. |
| welcomeBotMessages | Array | Each string element in the array will display as a bot message on chat load |
| welcomeButtons | Array | Each string element in the array will be displayed as a button on chat load. These act as a set of pre-defined prompts the user can click on to send the associated message in the chat |
| turnHistoryLimit | Integer |  |
| includeRequired | Boolean |  |

---

### Training Virtual Agents

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/training_virtual_agents/index>

##### Overview

**What is it?**

- NeuralSeek will automatically generate IBM Watson Assistant "Actions" or "Dialogs," based on user questions that are asked. Generally, IBM Watson Assistant needs five (5) or more user question examples to train on for a high confidence match to a user query. When user questions are cataloged by the system, NeuralSeek automatically tries to generate similar worded questions to meet the minimum of five (5) user examples. Similar Question generation may take up to one (1) minute to show inside the Curate tab after a new user question is logged.

**Why is it important?**

- Users who develop and maintain Watson Assistant have to work with its Actions and Dialogs, and can quickly get overwhelmed by its vast numbers. Coming up with multiple number of questions for each intent is also very time consuming, but it also quickly becomes burdensome when you have to continuously monitor and update them by yourself.

**How does it work?**

- NeuralSeek provides ways to generate the candiate questions and answers based on the contents inside the KnowledgeBase, and let users download the whole thing or portions of it, so that it could be created either as Watson Assistant Actions, or Watson Assistant Dialogs.

##### Generating Questions and Answers

After you have configured NeuralSeek, in its `Home`, you will see an option to auto-generate questions.

![generate questions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-001.png)

Clicking will let NeuralSeek scan through your KnowledgeBase, and start generating potential questions that would be most commonly used.

![generating questions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-002.png)

The resulting list of questions appear at the bottom. If you do not like the list of questions, you can re-generate them again, or edit them on the spot.

![generation complete](https://draft-wiki.neuralseek.com/assets/guides/integration/image-003.png)

When you feel like you can generate the Answers for those questions, you can click Submit button and those questions will be available on the `curate` tab of the top menu. Usually the most recently entered questions and answers appear at the top:

![loaded answers](https://draft-wiki.neuralseek.com/assets/guides/integration/image-004.png)

##### Testing Questions

During the curation process, usually the user would need to use `Seek` tab to submit questions to see how well the answer is generated. However, this process can be tedious if you have a certain set of questions that you want to ask in bulk and derive the results. In that case, you can use `Upload Test Questions` to upload multiple questions and generate their answers easily.

1. Go to `Home` of NeuralSeek, and click `Upload Test Questions`.
2. In the instructions, you will see a link of `template` file that you can download from. It's a template file in CSV format. click it to download.
3. Use the file to enter the list of questions. For example,

    ID,Question
    1,"What are the main features of NeuralSeek?"
    2,"What are the knowledgebases supported by NeuralSeek?"
    3,"I want to integration NeuralSeek with Watson Assistant. What do I need to do?"
    4,"Where can I see the demo?"

4. Click the upload button to upload the file.
5. Click `Submit` button.
6. NeuralSeek will run through the questions and let you know how many are being processed. When it is finsihed it

![processing](https://draft-wiki.neuralseek.com/assets/guides/integration/image-031.png)

7. When finished, you can either Download the report, Export All Q&A, or Delete the generated report.

![generated report](https://draft-wiki.neuralseek.com/assets/guides/integration/image-032.png)

8. Download the report: it will give you a CSV file that has the following columns:
  - `ID,question,score,semanticScore,kbCoverage,totalCount,url,document,answer,categoryId,category,intent,pii,sentiment` which will give you the answer and score of how well it got generated.
9. Export All Q&A: it will export all the Q&A currently stored in NeuralSeek, in JSON format suitable to be imported as Watson Assistant Actions.
10. Delete Report: it will delete the generated report, and will not be available anymore.

##### Uploading Curated Q/A

This feature is very similar to `Upload Test Questions`, but uses the CSV format that has `ID,Question,Answer`. User can create question and answer pairs to submit it, which will then be populated as `edited answers` in NeuralSeek. This feature is useful when you need to edit and upload answers in bulk fashion. An example format of the CSV is as follows:

    ID,Question,Answer
    1,Tell me about NeralSeek,"NeuralSeek is an AI-powered platform that generates natural-language answers to complex, open-ended, and contextual questions from real customers."

##### Importing Q/A into Watson Assistant

Depending on how your NeuralSeek is setup, it can either product questions and answers into `Action` type or `Dialog` type. That depends on whether your Watson Assistant is enabled with dialog or not.

###### Importing into Watson Assistant as Actions
> **Tip**
> As for importing Q&A into Watson Assistant, you can do it on both Watson Assistant `Classic` mode or new `Dialog` mode.

1. Go to your Watson Assistant, and to go to `Actions`. Click the gear icon on top right to go into the settings.

![gear icon](https://draft-wiki.neuralseek.com/assets/guides/integration/image-021.png)

2. In the global settings, move to the right most tab which is `Upload/Download`, and click `Download` button to download the action's JSON file.

![download json](https://draft-wiki.neuralseek.com/assets/guides/integration/image-022.png)

3. A JSON file should be saved.
4. Go to NeuralSeek, click `Curate` tab.
5. Click `Import Base Watson Assistant Actions`.

![import base wa actions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-019.png)

6. Upload the downloaded JSON file.

![upload json](https://draft-wiki.neuralseek.com/assets/guides/integration/image-023.png)

7. Now, select one or more intents which you want to import into Watson Assistant. You will notice a new button is display which is `Export to Watson Assistant Actions`.

![export to wa actions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-024.png)

8. It will download a JSON file called `actions.json` which will contain the selected intents that you want to convert it into Watson Assistant Actions.
9. Go to Watson Assistant. At the same page where you just downloaded the JSON, click to select a file, and select the `actions.json` and click `Upload` button.

![upload actions.json](https://draft-wiki.neuralseek.com/assets/guides/integration/image-025.png)

10. You will see a warning message. Click `Upload and replace`.

![upload and replace](https://draft-wiki.neuralseek.com/assets/guides/integration/image-026.png)

11. Now, close this page, and you will see the exported actions appear on your actions list.

![exported actions on list](https://draft-wiki.neuralseek.com/assets/guides/integration/image-027.png)

12. Click one of the actions. You should be able to see the list of the quesitons generated by NeuralSeek nicely populated.

![generated questions_1](https://draft-wiki.neuralseek.com/assets/guides/integration/image-028.png)
![generated questions_2](https://draft-wiki.neuralseek.com/assets/guides/integration/image-029.png)

With these, you can easy save time to jump start Watson Assistant to provide better answers to the questions and answers generated by NeuralSeek. One other nice thing about this is that if you find any particular questions and answers that does not yet exist in Watson Assistant, you can easily move them from NeuralSeek.

###### Importing into Watson Assistant as Dialogs
> **Note**
> Unlike importing them as Actions, you first need to export your Watson Assistant's dialogs and set them as `Base Watson Assistant Dialog` into NeuralSeek. That is because Watson Assistant, when uploading a Dialog, would simply override the existing dialog and upload a new one. In order to make sure any existing actions or dialogs are not deleted, NeuralSeek needs to have it first, and then merge the dialogs into it.

1. Go to your Watson Assistant, and to go `Dialog > Options > Upload / Download`:

![downloading](https://draft-wiki.neuralseek.com/assets/guides/integration/image-005.png)

2. Click `Download` tab and click `Doanload` button:

![loaded answers](https://draft-wiki.neuralseek.com/assets/guides/integration/image-006.png)

3. A JSON file should be downloaded.
4. Now go to NeuralSeek, and go to `Curate` tab.
5. Click `Import Base Watson Assistant Dialog` button.

![importing dialog](https://draft-wiki.neuralseek.com/assets/guides/integration/image-007.png)

6. Select the downloaded JSON file. The button will now be turned to `Base Watson Assistant Dialog Uploaded`.

![imported dialog](https://draft-wiki.neuralseek.com/assets/guides/integration/image-008.png)
> **Warning**
> Whenever there is a change of your Watson Assistant Dialog, make sure to delete the older one and upload the recent one in order to not risk losing your most up-to-date dialogs.

7. Now, select the list of questions that you want to load it into. As soon as you select them, a new button `Export to Watson Assistant Dialog` will appear. You can obviously select all the questions by checking the `all` box at top left.

![selecting questions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-009_2.png)

8. Click the button to export these dialogs.
9. Now, a JSON file should be downloaded. Load the file back into Watson Assistant using its upload tab.

![uploading](https://draft-wiki.neuralseek.com/assets/guides/integration/image-010.png)

10. Note that uploading this JSON will overwrite any existing dialog contents. Click `Upload and replace`.

![uploading warning](https://draft-wiki.neuralseek.com/assets/guides/integration/image-011.png)

11. If everything goes well, it will say the skills were uploaded successfully.
12. You now have the curated answer from NeuralSeek populated as a Dialog node in Watson Assistant. Next time when the user asks the same question, Watson Assistant should be able to answer it the same way as NeuralSeek did.

![modified dialog](https://draft-wiki.neuralseek.com/assets/guides/integration/image-012.png)
![Alt text](https://draft-wiki.neuralseek.com/assets/guides/integration/image-030.png)
![search result](https://draft-wiki.neuralseek.com/assets/guides/integration/image-013.png)

This is a great way to effectively manage some of the most frequent questions and answers that you uncover from NeuralSeek to be able to be transferred into the Virtual Agent's dialog, such that it will be able to be trained with better set of answers.

##### Importing into AWS Lex

You can either export NeuralSeek curated questions and answers into a new Lex Bot or merge existing Lex Box intents with curated questions and answers from NeuralSeek into a cloned Lex Bot

###### AWS Lex Bot Merge Import

These directions allow you to merge existing AWS Lex bot intents with curated NeuralSeek questions and answers into a new bot. The NeuralSeek curated questions and answers get converted to Lex intents automatically.

1. Log into AWS Management Console and navigate to AWS Lex > Bots. You should see a list of available bots to merge with NeuraSeek.

![Available Bots](https://draft-wiki.neuralseek.com/assets/guides/integration/available_bots.png)

2. In the Bots list in the main view select the desired bot so it is selected, and click Action > Export. An Export Bot: dialog is shown.

![Export Bot](https://draft-wiki.neuralseek.com/assets/guides/integration/bot_export_dialog.png)

3. From the export dialog leave all the default values and click Export. A blue banner is shown of exporting followed by a green banner of successfully exported/downloaded.
4. Next log into your NeuralSeek instance with a user with permissions to the Curate tab.
5. Click on the Curate tab.
6. Click on the Import Base AWS Lex V2 button in the upper right corner. A File Explorer dialog is shown.

![import base AWS Lex V2](https://draft-wiki.neuralseek.com/assets/guides/integration/import_base_aws_lex.png)
> **Note**
> If the import button says something different than AWS Lex, switch to the NeuralSeek instance that is using the AWS Lex Virtual Agent. Optionally, you can also change the virtual agent type under Configure > Platform Preferences.

7. Navigate to the zipped AWS Lex file you exported from step 3 and click Open. The button will switch to Base AWS Lex V2 Uploaded. After import, intents will not get added to the content list, but duplicates will show an indicator that this intent is already present in the definition file.
8. Now, select the list of questions that you want to export into AWS Lex. As soon as you select them, a new button `Export to AWS Lex V2 Dialog` will appear. You can select all the questions by checking the `all` box at top left.

![selecting questions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-009_2.png)

9. Click the `Export to AWS Lex V2` button to export these questions and answers. A zipped file should be downloaded.
10. From the AWS Management Console Amazon Lex > Bots screen click Actions > Import. A Lex > Bots > Import bot screen is shown.

![Import AWS Lex Bot](https://draft-wiki.neuralseek.com/assets/guides/integration/import_lex_bot_1.png)

11. Fill in the new Bot name, browse for the zip file, set the COPPA yes/no, set the IAM permissions, and then scroll down and click Import. You'll see a blue banner that the bot is being imported followed by a successfully imported banner.

12. Find the imported bot in the bots list and open it by clicking on its name. The details for the merged bot is shown. Notice the Intents section in the left pane has both the original intents and the NeuralSeek intents merged into a single bot.

13. Click the build button. You can now test the new imported intentions.

![Import AWS Lex Bot](https://draft-wiki.neuralseek.com/assets/guides/integration/build_bot.png)

###### AWS Lex Bot Import Only

These directions are for creating a new Amazon Lex bot from curated NeuralSeek questions and answers only. It will not contain existing intents from AWS.

1. Start by logging into your NeuralSeek instance with a user with permissions to the Curate tab.
2. Click on the Curate tab.
3. Select the list of questions that you want to export into AWS Lex. As soon as you select them, a new button `Export to AWS Lex V2 Dialog` will appear. You can select all the questions by checking the `all` box at top left.

![selecting questions](https://draft-wiki.neuralseek.com/assets/guides/integration/image-009_2.png)

4. Click the `Export to AWS Lex V2` button to export these questions and answers. A zipped file should be downloaded.
5. From the AWS Management Console Amazon Lex > Bots screen click Actions > Import. A Lex > Bots > Import bot screen is shown.

![Import AWS Lex Bot](https://draft-wiki.neuralseek.com/assets/guides/integration/import_lex_bot_1.png)

6. Fill in the new Bot name, browse for the zip file, set the COPPA yes/no, set the IAM permissions, and then scroll down and click Import. You'll see a blue banner that the bot is being imported followed by a successfully imported banner.

7. Find the imported bot in the bots list and open it by clicking on its name. The details for the merged bot is shown. Notice the Intents section in the left pane has converted the NeuralSeek questions and and answers to intents.

8. Click the build button. You can now test the new imported intentions.

---

### Backup and Restore

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/backup_and_restore/index>

##### Backup / Restore Settings

1. Open NeuralSeek's Configure tab, and select "Show advanced options" (if not already shown):

![show_advanced_settings](https://draft-wiki.neuralseek.com/assets/guides/integration/show_advanced_settings.png)

2. From here, you are now offered the option to download/backup and upload/restore your instance settings.

![show_download_settings](https://draft-wiki.neuralseek.com/assets/guides/integration/show_download_settings.png)

##### Curated Data (Backup)

1. Open NeuralSeek's Curate tab

![show_curate_tab](https://draft-wiki.neuralseek.com/assets/guides/integration/show_curate_tab_1.png)

2. Select some, or all, curated intents to backup

![show_download_csv](https://draft-wiki.neuralseek.com/assets/guides/integration/show_download_csv.png)

3. As seen above, upon selecting curated intents, you are offered a "Download to CSV" button. This is useful not only for backing up your curated data, but also for allowing subject matter experts to edit curated Q&A content without direct access to the UI. After editing, you're able to re-upload the curated content in the next set of steps (Restore).

##### Curated Data (Restore)

1. When no intents are selected, you are offered a "Load Q&A" button near the top-right:

![show_curate_tab](https://draft-wiki.neuralseek.com/assets/guides/integration/show_curate_tab_1.png)

2. This takes us to the Q&A Upload page:

![show_upload_qa](https://draft-wiki.neuralseek.com/assets/guides/integration/show_upload_qa.png)

3. From here, we are able to upload a Curated Q&A CSV file (downloaded from previous steps). For Restoring purposes, you will not want to use "Improve my answers".

##### Data Policy

All user data and generated answers are owned by and for the sole use of the customer.

It is your responsibility to regularly backup curated content. There is no option to configure product availablilty at this time.

---

### ElasticSearch Vector Model

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/elasticsearch_vector_model/index>

##### Overview

This guide provides step-by-step instructions on configuring Vector search with ElasticSearch. It includes logging into the environments, creating keys for API access, setting up a machine learning instance, downloading necessary models, creating source and destination indices, and ingesting data to generate text embeddings. The guide also covers manual data loading steps and utilizing client helper functions for data ingestion. It concludes with verifying the data and content embeddings in the destination index.

##### Log into Environments

Begin by logging in to your IBM Cloud account

- **To provision in IBM Cloud**:,
  * Navigate to **Databases for ElasticSearch**.
  * Select the **Platinum Database Edition**.
- Otherwise, provision within Elastic Cloud as normal.

There are two environments to work from.

- **ElasticSearch Cloud** console. Notice the icons in the top right corner.
- **Kibana** console
  * Users may be taken directly to the Kibana console after creating a deployment. If not, navigate there by selecting Open on the deployment page from the ElasticSearch Cloud console.

![es_deploy_click_to_kibana](https://draft-wiki.neuralseek.com/assets/guides/integration/es_deploy_click_to_kibana.png)
![es_kibana_console](https://draft-wiki.neuralseek.com/assets/guides/integration/es_kibana_console.png)

##### Creating Keys

- Select the circle icon in the top right of the Kibana screen.
- Select `Connection Details`
- Here, you will see the **ElasticSearch endpoint** and the **Cloud ID**.
- Select **Create and Manage API Keys**.
- To create a new API key, click **Create API Key**.
  * Add a unique name.
  * Select the type as **User API Key**.
  * Click **Create API Key** button at the bottom of the dialog.

![es_connection_details](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_connection_details.png)
![es_manage_keys](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_manage_api_keys.png)
![es_create_api_key](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_create_api_key.png)
> **Tip**
> Save these values in a safe place for later use.

##### Create a Machine Learning Instance

Elastic requires a machine learning instance to run the NLP models required for vectorizing the data for indexing.

- Navigate to the Home screen of your ElasticSearch instance.
- Navigate to the newly created deployment and select **Manage**.
- On the side menu, select **Edit**.
- Scroll down to the **Machine Learning Instances** section.
- Select **Add Capacity**.
- Select 4 GB RAM.
- Click **Save** at the bottom of the page.

![ES_edit_deploy](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_edit_deploy.png)
![ES_add_ML_RAM](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_add_ML_RAM.png)
![ES_save_ML_add](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_save_ML_add.png)

##### Download Models
> **Abstract: Download ELSER model**
>
> - In Kibana, click the menu icon in the top left and navigate to **Analytics > Machine Learning > Trained Models**.
> - Click the **Download** button under the Actions column
> * Choose the recommended `".elser_model_2_linux-x86_64"` model
> * It may take some time for the download to finish.
> - Click the **Deploy** link that shows up when the mouse is hovered over the downloaded model.
> - Leave the default settings on the Dialog column and select **Start**.
> - The State column will show **Deployed** when successfully done.
> ![ES_download_trained_model](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_kibana_trained_model.png)
>
> **Abstract: Download A Text Embedding Model**
> It is recommended to use **Eland** to upload and download the desired model to ElasticSearch.
>
> - Run this command to install the Eland Python client with PyTorch: `python -m pip install 'eland[pytorch]'`
> - Run this script to download the model from Hugging Face, convert it to TorchScript format, and upload to the Elasticsearch cluster:
>
> eland_import_hub_model
> --cloud-id <cloud-id> \
> -u <username> -p <password> \
> --hub-model-id elastic
> distilbert-base-cased-finetuned-conll03-english \
> --task-type ner
>
> - Specify the **Elastic Cloud identifier** using the TLS setting with a downloaded cert from **IBM Cloud -> Database for Elasticsearch -> Overview tab**.
> - Provide authentication details to access your cluster.
> - Specify the **identifier** for the model in the Hugging Face model hub.
> - Specify the **NLP task type** as `"text_embedding"`.
> **Tip**
> It is recommended to use the `intflost/multilingual-e5-base` Hugging Face model to start.
>
> It may take time for the model to auto-start, up to a few hours.

##### Create Source Index and Upload Data

Indices can be created by either manually loading data using the _bulk API, or by using a client helper function which will create the index and load the data.

![kibana_dev_console](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_kibana_dev_console.png)
> **Abstract: Manual Data Load Steps**
>
> - Navigate to Kibana console.
> - From the side menu, select **Management > Dev Tools** to launch the dev console.
> - Delete any code that appears.
> - To create the source index, enter the following code:
>
> PUT /search-gs-docs-src
> {
> "mappings": {
> "properties": {
> "title": {
> "type": "text"
> },
> "content": {
> "type": "text"
> },
> "source": {
> "type": "text"
> },
> "url": {
> "type": "text"
> },
> "public_record": {
> "type": "boolean"
> }
> }
> }
> }
>
>
> - Hit the **run** icon.
> - Prepare the data for bulk ingestion by manually converting the data and using the dev console to load it by entering the following code:
>
> POST _bulk
> { "index" : { "_index" : "search-gs-docs-src", "_id" : "1" } }
> { "title" : "Top 3 Best Practices to Secure Your Gainsight PX Subscription",
> "content" : "We should all protect what has been entrusted…”,
> "url" : "https://support.gainsight.com/...",
> "source" : "docs”,
> “public_record”:true,
> “objectID”: “https://support.gainsight.com/...”
> }
> { "index" : { "_index" : "search-gs-docs-src", "_id" : "2" } }
> { "title" : "Using PX with Content Security Policy",
> "content" : "This article describes the steps to allow a Content Security Policy…”,
> "url" : "https://support.gainsight.com/...",
> "source" : "docs”,
> “public_record”:true,
> “objectID”: “https://support.gainsight.com/...”
> }
> …
>
> **Abstract: Utilizing Client Helper Function Steps**
>
> - Enter the following code to utilize the client helper function to create the index and load the data:
>
> 'use strict'
>
> require('array.prototype.flatmap').shim()
> const { Client } = require('@elastic/elasticsearch')
> const client = new Client({
> cloud: { id: '<cloud_id>'},
> auth: { apiKey: '<api_key>' }
> })
> const dataset = require('./gainsight_documentation_data/gainsight-en-federated.json')
>
> // Create and load the source index
> async function run () {
> await client.indices.create({
> index: 'search-gs-docs-src',
> operations: {
> mappings: {
> properties: {
> title: { type: 'text' },
> content: { type: 'text' },
> url: { type: 'text' },
> source: { type: 'text' },
> public_record: { type: 'boolean' },
> objectID: { type: 'text' }
> }
> }
> }
> }, { ignore: [400] })
>
> const operations = dataset.flatMap(doc => [{ index: { _index: 'search-gs-docs-src' } }, doc])
>
> const bulkResponse = await client.bulk({ refresh: true, operations })
>
> if (bulkResponse.errors) {
> const erroredDocuments = []
> // The items array has the same order of the dataset we just indexed.
> // The presence of the `error` key indicates that the operation
> // that we did for the document has failed.
> bulkResponse.items.forEach((action, i) => {
> const operation = Object.keys(action)[0]
> if (action[operation].error) {
> erroredDocuments.push({
> // If the status is 429 it means that you can retry the document,
> // otherwise it's very likely a mapping error, and you should
> // fix the document before to try it again.
> status: action[operation].status,
> error: action[operation].error,
> operation: operations[i * 2],
> document: operations[i * 2 + 1]
> })
> }
> })
> console.log(erroredDocuments)
> }
>
> const count = await client.count({ index: 'search-gs-docs-src' })
> console.log(count)
> }
>
> run().catch(console.log)
>
> - Use the **Cloud ID** and **API Key**.
> - Enter the following commands to run this script:
> * `npm i @elastic/elasticsearch`
> * `npm i array.prototype.flatmap`
> * `node data_load.js`

Once the data is loaded, either manually or programmatically, verify that it appears properly in the index.

- Navigate to the Kibana console.
- Navigate to **Search > Content > Indices**.
- Open the `search-gs-docs-src` index.
- Open the **Documents** tab to see the data for verification.

##### Create destination Index

Create a destination index using the same schema as the source index. Add a field to store the content embeddings.

- Enter the following code, then hit the **run** icon.

    PUT /search-gs-docs-dest
    {
    "mappings": {
        "properties": {
        "content_embedding": {
            "type": "sparse_vector"
        },
        "title": {
            "type": "text"
        },
        "content": {
            "type": "text"
        },
        "source": {
            "type": "text"
        },
        "url": {
            "type": "text"
        },
        "public_record": {
            "type": "boolean"
        }
        }
    }
    }

##### Ingest the Data to Generate Text Embeddings

- Create an ingest pipeline with an inference processor. Enter the following code:

    PUT _ingest/pipeline/my-content-embedding-pipeline
    {
    "processors": [
        {
        "inference": {
            "model_id": ".elser_model_2_linux-x86_64",
            "input_output": [
            {
                "input_field": "content",
                "output_field": "content_embedding"
            }
            ]
        }
        }
    ]
    }

- Click the **run** icon.

- Ingest the data through the inference index pipeline to create the text embeddings. Enter the following code into the dev console:

    POST _reindex?wait_for_completion=false
    {
    "source": {
        "index": "search-gs-docs-src",
        "size": 50
    },
    "dest": {
        "index": "search-gs-docs-dest",
        "pipeline": "my-content-embedding-pipeline"
    }
    }

- To get the name of the pipeline with the model loaded, navigate to **Kibana > Machine Learning > Trained Models**.
- Expand the Deployed model.
- Navigate to the **Pipelines** tab to view the `my-content-embesddings-pipeline` created in the above step.

> **Tip**
> To confirm the task was run successfully, run the following command using the **task ID** produced in the response from the previous command:
> `GET _tasks/<task_id>`.

- Verify the content embeddings are in the new destination index.
  * Navigate to Kibana.
  * Navigate to **Search > Content > Indices**.
  * Open the `search-gs-docs-dest` index.
  * Open the **Documents** tab to see the data.

##### Map a Field

Models compatible with ElasticSearch NLP generate dense vectors as output, so the `dense_vector` field type for the index is suitable for storing. This field type must be configured with the same number of dimensions using the `dims` option.

- Enter the following code into the dev console to create an index mapping that defines field containing the model output.

    PUT my-index
    {
    "mappings": {
        "properties": {
        "my_embeddings.predicted_value": {
            "type": "dense_vector",
            "dims": 384
        },
        "my_text_field": {
            "type": "text"
        }
        }
    }
    }

- `my_embeddings.predicted_value` is equal to the name of the field containing the embeddings generated by the model.
- The `"type"` field must be `"dense_vector"`.
- The `"dims"` field contains the number of dimensions of the embeddings produced by the model. Be sure that this number is configured in the `dense_vector` field.
- The `"my_text_field"` field is equal to the name of the field from which to create the dense vector representation.
- The `"type"` field is `text`.

##### Test the Semantic Search
> **Abstract: ELSER Model**
> Test the semantic search using the `text_expansion` query by providing the query text and the ELSER Model ID.
>
> - Enter the following code into the dev console:
>
> GET search-gs-docs-dest/_search
> {
> "query":{
> "text_expansion":{
> "content_embedding":{
> "model_id":".elser_model_2_linux-x86_64",
> "model_text":"Put sample query here"
> }
> }
> }
> }
>
> - The `content_embedding` field contains the generated ELSER output.
> **Abstract: Dense Vector Model**
> The dense vector models allow users to query rank features with a kNN search. In the `knn` clause, users will provide the name of the dense vector field. In the `query_vector_builder` clause, add the model ID and the query text.
>
> - Enter the following code into the dev console:
>
> GET my-index/_search
> {
> "knn": {
> "field": "my_embeddings.predicted_value",
> "k": 10,
> "num_candidates": 100,
> "query_vector_builder": {
> "text_embedding": {
> "model_id": "sentence-transformers__msmarco-minilm-l-12-v3",
> "model_text": "the query string"
> }
> }
> }
> }

##### Connect NeuralSeek to Elasticsearch

- Navigate to your IBM Cloud account.
- Open the NeuralSeek service instance.
- Navigate to the **Configure** screen.
- Save your current setting by clicking the **Download Settings** button at the bottom of the screen.
- Open the **KnowledgeBase Connection** accordion and update the following fields.
  * Set KnowledgeBase Type to `ElasticSeach`
  * Set the **ElasticSearch Endpoint**.
  * Set the **ElasticSearch Private API Key**.
  * Set the **ElasticSearch Index Name** to the destination index. In this case, `search-gs-docs-dest`.
  * Set the **Curation Data Field** to `content`.
  * Set the **Documentation Name Field** to `title`.
  * Set the **Link Field** to `url`.
- Click the **Save** button at the bottom of the page.

![ES_download_NS_settings](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_download_NS_settings.png)
![ES_NS_settings](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_NS_settings.png)

##### Enable Vector Search in NeuralSeek

In the NeuralSeek Configure screen, open the **Hybrid and Vector Search Settings** accordion to update the following fields.

- Set Elastic Query Type to `Hybrid`.
  * This will allow for both **Lucene** (exact match) and **Vector** (semantic) searching to achieve a more robust response.
- Set the **Model ID** to `".elser_model_2_linux-x86_64"`
- Set the **Embedding Field** to `content_embedding`
- Set the **Use the Elastic ELSER Model** field to `True` for ELSER Model Use, or set to `False` to allow NeuralSeek to expect JSON format for a kNN search query.
- Click **Save** at the bottom of the screen.

![ES_hybrid_NS_settings](https://draft-wiki.neuralseek.com/assets/guides/integration/ES_hybrid_NS_settings.png)
> **Warning: If using 'IBM Databases for ElasticSearch'**
> With Hybrid search, the KnnScoreDocQuery was created by a different reader. To fix this, enter the following code into the Kibana dev console:
>
> PUT /<INDEX_NAME>/_settings
> {
> "index" : {
> "highlight.weight_matches_mode.enabled" : "false"
> }
> }

---

### Pinecone Configuration

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/pinecone_configuration/index>

This guide provides step-by-step instructions for configuring Pinecone as the knowledge base and using it along with the embedding model. Additionally, a technical explanation of how this configuration works is provided. An example Node.js script for uploading documents to the Pinecone index is also included.

While this guide focuses on Pinecone, it is worth noting that you can also use Milvus as an alternative vector database.

##### Prerequisites

- Ensure you have Node.js installed.

##### Steps

###### 1. Create a Pinecone Account

- Go to [Pinecone](https://www.pinecone.io/) and create a new account.

###### 2. Create a New Index in Pinecone

- Navigate to the dashboard and create a new index.
  * Depending on the embedding model you plan to use, choose the appropriate vector size:

    + `text-embedding-ada-002`: Vector size 1536
    + `text-embedding-3-small`: Vector size 1536
    + `text-embedding-3-large`: Vector size 3072
    + `infloat-e5-small-v2`: Vector size 384

        ![Add Index](https://draft-wiki.neuralseek.com/assets/guides/integration/index.png)

###### 3. Configure NeuralSeek

###### 3.1. Configure the Knowledge Base Connection

- Access the **NeuralSeek** platform.

- Go to the **Configure** tab and set up the knowledge base connection:

  * Knowledge Base Type: `Pinecone`
  * Knowledge Base Language: `English`
  * Pinecone Index Name: `docs`
  * Pinecone Index Namespace: `ns1`
  * Pinecone API Key: `your-pinecone-api-key`
  * Curation Data Field: `text`
  * Document Name Field: `title`
  * Filter Field: `title`
  * Link Field: `link`
  * Attribute Resources: `enabled`

    ![Configure Knowledge Base Connection](https://draft-wiki.neuralseek.com/assets/guides/integration/kb-pine.png)

###### 3.2. Add an Embedding Model

- Go to the **Embedding Models** section and add a new embedding:

  * Choose the platform (either `Azure`, `NeuralSeek`, or `OpenAI`).
  * Select the appropriate embedding model:
    + For `OpenAI` and `Azure`:
      - `text-embedding-ada-002`: Vector size 1536
      - `text-embedding-3-small`: Vector size 1536
      - `text-embedding-3-large`: Vector size 3072
    + For `NeuralSeek`:
      - `infloat-e5-small-v2`

![Add Embedding Model 1](https://draft-wiki.neuralseek.com/assets/guides/integration/embedding.png)

![Add Embedding Model 2](https://draft-wiki.neuralseek.com/assets/guides/integration/embedding2.png)

###### 4. Add Documents to Pinecone Index via Node.js Script

###### 4.1. Install Required Packages

    npm install axios fs path @pinecone-database/pinecone @langchain/openai

    import axios from "axios";
    import fs from "fs";
    import path from "path";
    import { Pinecone } from "@pinecone-database/pinecone";
    import { OpenAIEmbeddings } from "@langchain/openai";

    const folder = "./docs";

    const pc = new Pinecone({
      apiKey: "your-pinecone-api-key", // Replace with your Pinecone API key
    });

    var kb = {};
    var ids = [];

    const openaiAPIKey = "your-openai-api-key"; // Replace with your OpenAI API key

    kb.importFiles = async (model, pineconeIndex, pineconeNamespace) => {
      var pineconeData = [];

      let fileList = fs.readdirSync(folder);
      var vectors = null;
      for (const file of fileList) {
        const data = JSON.parse(fs.readFileSync(path.join(folder, file)));

        if (model == "infloat-e5-small-v2") {
          const embeddings = await axios.post("http://url.com", {
            text: data.text,
          });
          vectors = embeddings.data;
        } else if (
          model == "text-embedding-ada-002" ||
          model == "text-embedding-3-small" ||
          model == "text-embedding-3-large"
        ) {
          var embedV2 = new OpenAIEmbeddings({
            openAIApiKey: openaiAPIKey,
            modelName: model,
          });

          vectors = await embedV2.embedQuery(data.text);
        } else {
          throw new Error(`Unsupported model "${model}"`);
        }

        const id = data.title;
        const metadata = {
          text: data.text,
          title: data.title,
          link: data.source_link,
        };
        const values = vectors;
        var record = { id, values, metadata };
        pineconeData.push(record);
        ids.push(id);
      }
      const index = pc.index(pineconeIndex);

      await index.namespace(pineconeNamespace).upsert(pineconeData);
    };

    kb.fetchRecords = async (recordIds) => {
      const index = pc.index("docs");
      const result = await index.namespace("ns1").fetch(ids);
    };

    kb.emptyQuery = async (dimensions, ns, indexName) => {
      const index = pc.index(indexName);

      const queryResponse = await index.namespace(ns).query({
        vector: new Array(dimensions).fill(0),
        topK: 1,
        includeMetadata: true,
      });

      console.log(queryResponse);
    };

    kb.describeIndex = async (indexName) => {
      var index = await pc.describeIndex(indexName);
      var dimension = index.dimension;
      console.log(`Dimensions: ${dimension}`);
    };

    kb.query = async (ns, indexName, text) => {
      const index = pc.index(indexName);

      const embeddings = await axios.post("http://url.com", {
        text: text,
      });
      const id = "Test";
      const metadata = { text: text };
      const values = embeddings.data;
      var record = { id, values, metadata };

      const queryResponse = await index.namespace(ns).query({
        vector: record.values,
        topK: 10,
        includeMetadata: true,
      });

      console.log(queryResponse);
    };

    kb.filterQuery = async (ns, indexName, text, filter) => {
      const index = pc.index(indexName);

      const embeddings = await axios.post("http://url.com", {
        text: text,
      });
      const id = "Test";
      const metadata = { text: text };
      const values = embeddings.data;
      var record = { id, values, metadata };

      const queryResponse = await index.namespace(ns).query({
        vector: record.values,
        filter: {
          contents: { $eq: filter },
        },
        topK: 11,
        includeMetadata: true,
      });

      console.log(queryResponse);
    };

    kb.getEmbedding = async (embedModel, query) => {
      var res = await embedModel.embedQuery(query);
      console.log(res);
    };

    var embedV2 = new OpenAIEmbeddings({
      openAIApiKey: "your-openai-api-key",
      modelName: "text-embedding-3-small",
    });

    await kb.importFiles("text-embedding-3-small", "docs", "ns1");

###### 4.2. Create and Run the Script

Create a file named upload-documents.js and add the following script:

    node upload-documents.js

###### 5. Save Configuration

Save all the configurations made in NeuralSeek.

###### 6. Test the Integration

Go to the Seek tab in NeuralSeek and perform a search to verify if the integration works.

Additionally, you can test the setup using Maistro.

#### Technical Explanation: How Pinecone and NeuralSeek Work Together

##### Pinecone

Pinecone is a vector database that provides efficient similarity search and retrieval capabilities. In the context of NeuralSeek, Pinecone serves as the knowledge base where all documents and their vector embeddings are stored. Key functionalities include:

###### Indexing

- Pinecone indexes vector embeddings of documents, making them easily searchable.

###### Querying

- It processes search queries by comparing query vectors with stored document vectors to find the most similar matches.

###### Scalability

- Pinecone can handle large volumes of data and provides quick search responses, making it suitable for extensive knowledge bases.

##### NeuralSeek Embedding Model

NeuralSeek uses sophisticated embedding models to generate vector representations of text data. The `infloat-e5-small-v2` model, in particular, transforms text into a 384-dimensional vector, capturing the semantic meaning of the text. Key functionalities include:

###### Text Embeddings

- Converts text data into dense vector representations that capture semantic information.

###### Similarity Matching

- Compares query vectors with document vectors to find the most relevant answers.

###### Contextual Understanding

- Leverages multiple layers to understand and generate contextually accurate responses.

##### Integration Workflow

1. **Data Ingestion**: Documents are ingested and processed to generate vector embeddings using NeuralSeek's embedding model.
2. **Indexing**: The generated vector embeddings are stored in Pinecone, where they are indexed for efficient search and retrieval.
3. **Query Processing**: When a query is entered, NeuralSeek converts the query text into a vector using the embedding model.
4. **Search and Retrieval**: The query vector is compared with document vectors in Pinecone to find the most relevant matches.
5. **Response Generation**: The most relevant documents are retrieved from Pinecone, and NeuralSeek formulates a response based on the retrieved data.

##### Benefits of This Configuration

###### Efficiency

- Combining Pinecone's efficient vector search capabilities with NeuralSeek's powerful embeddings ensures quick and accurate responses.

###### Scalability

- Pinecone can scale to handle large data volumes, while NeuralSeek's embeddings maintain high performance.

###### Accuracy

- NeuralSeek's contextual embeddings improve the accuracy of responses, providing relevant and precise information.

###### Troubleshooting
> **Warning: Issue: Model Not Providing Accurate Responses**
> **Success: Solution**
> Verify the model parameters and ensure that the content in the knowledge base is up-to-date.
>
> **Warning: Issue: Upload Errors**
> !!! success "Solution"
> Ensure that file formats are correct and data integrity is maintained.
>
> **Warning: Issue: Integration Issues**
> !!! success "Solution" Recheck the linkage between the model and the knowledge base, and verify that synchronization is correctly configured.

---

### Providing Context

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/providing_context/index>

##### Overview

**What is it?**

- Context refers to additional information passed through the API or session history that helps seek better understand the user's needs and provide more relevant answers. It can include previous questions, user preferences, or relevant data from earlier in the conversation.

**Why is it important?**

- Providing context improves the accuracy and relevance of the responses generated by Watsonx Assistant or NeuralSeek, as it allows the system to retain information from prior interactions and provide more personalized or situation-specific answers.

**How does it work?**

- After a user's input is processed, the context can be carried over through the `lastTurn` parameter or `Session History` in the API request, enabling the system to maintain a coherent conversation by referring to previously shared details or refining queries based on earlier interactions.

##### Passing Conversational Context with watsonx Assistant

In watsonx Assistant, we can use the `Session History` variable to pass it to the `options.lastTurn` of NeuralSeek.

1. Make sure a NeuralSeek Extension is already set up for watsonx Assistant to use it.
2. Select the created NeuralSeek Extension, choose the 'Seek an answer from NeuralSeek' operation, and set the `question` parameter with the `query_text` session variable.

![extension_config](https://draft-wiki.neuralseek.com/assets/guides/integration/extension_config.png)

3. Display the 'Optional parameters' list.

![optional_params](https://draft-wiki.neuralseek.com/assets/guides/integration/optional_params.png)

4. Look for the `options.lastTurn` parameter and set it to `Session History` in the 'Assistant Variables' dropdown.

![session_history](https://draft-wiki.neuralseek.com/assets/guides/integration/session_history.png)

5. Finally, hit 'Apply' and the configured extension will look like this. Remember to save the action.

![configured_extension](https://draft-wiki.neuralseek.com/assets/guides/integration/configured_extension.png)

6. You can attempt a first question, such as "How can NeuralSeek help businesses in different industries with Gen AI?" in the chatbot preview.

![first_attempt](https://draft-wiki.neuralseek.com/assets/guides/integration/first_attempt.png)

7. For a second attempt, try asking a follow-up question related to the first one. NeuralSeek will use the `lastTurn` parameter to infer the context of your intent.

![context_attempt](https://draft-wiki.neuralseek.com/assets/guides/integration/context_attempt.png)

##### Passing Conversational Context via API

The `lastTurn` parameter allows NeuralSeek API to incorporate the context of a previous conversation when generating responses. This is especially useful when a sequence of related questions or follow-ups is asked, as it helps NeuralSeek understand the progression of the conversation.

1. Navigating to the 'Integrate' tab within NeuralSeek's interface. There we will be using the 'API' menu item.
2. Send a request to the `/seek` endpoint. The `lastTurn` field should be an empty structure, since there is no prior context to reference. For example:

    {
      "question": "How NeuralSeek can help businesses in different industries with Gen AI?",
      "options": {
        "lastTurn": [
          {
            "input": "",
            "response": ""
          }
        ]
      }
    }

The answer will look like the one below. We should keep this `answer` value and the current user question for our next request.

    {
      "answer": "NeuralSeek can help your business harness the power of generative AI. Our no-code platform connects to large language models and your company's data, making it much easier to deploy AI-powered solutions like virtual agents, content gen eration, and more. With NeuralSeek, you can create an AI agent, connect it to your knowledge base, and quickly generate intents and responses to automate customer support and share information with employees. This can enhance customer experiences and boost internal productivity across various functions. NeuralSeek is especially valuable for Fortune 500 companies looking to streamline their operations with AI. We've already partnered with multiple Fortune 500 businesses to help them rapidly implement AI without the typical complexity. I'd encourage you to explore some of these resources to learn more about how NeuralSeek can drive results in your industry: - Understanding NeuralSeek and Its Business Applications: https://ceoweekly.com/neuralseek-wh y-businesses-need-more-than-gen-ai-chatbots/ - NeuralSeek: The Future of AI Integration for Fortune 500 Companies: https://11mr eporter.com/posts/neuralseek-the-future-of-ai-integration-for-fortune-500-companies/"
    }

3. Send a second request. The `lastTurn` field should contain now the input (the previous question) and the corresponding response from NeuralSeek. This enables the API to consider the prior exchange and provide a more context-aware answer.

Example of a follow-up request with context:

    {
      "question": "What about a pharmaceutical business?",
      "options": {
        "lastTurn": [
          {
            "input": "How NeuralSeek can help businesses in different industries with Gen AI?",
            "response": "NeuralSeek can help your business harness the power of generative AI. Our no-code platform connects to large language models and your company's data, making it much easier to deploy AI-powered solutions like virtual agents, content gen eration, and more. With NeuralSeek, you can create an AI agent, connect it to your knowledge base, and quickly generate intents and responses to automate customer support and share information with employees. This can enhance customer experiences and boost internal productivity across various functions. NeuralSeek is especially valuable for Fortune 500 companies looking to streamline their operations with AI. We've already partnered with multiple Fortune 500 businesses to help them rapidly implement AI without the typical complexity. I'd encourage you to explore some of these resources to learn more about how NeuralSeek can drive results in your industry: - Understanding NeuralSeek and Its Business Applications: https://ceoweekly.com/neuralseek-wh y-businesses-need-more-than-gen-ai-chatbots/ - NeuralSeek: The Future of AI Integration for Fortune 500 Companies: https://11mr eporter.com/posts/neuralseek-the-future-of-ai-integration-for-fortune-500-companies/"
          }
        ]
      }
    }

In this follow-up request, the `lastTurn` provides context by including the previous question about generative AI and its response. This helps NeuralSeek better understand and address the new question about the pharmaceutical business in light of the prior exchange.

    {
      "answer": "The pharmaceutical industry is a complex and highly regulated sector that discovers, develops, produces, and markets drugs for use as medications to be administered to patie nts. It's one of the fastest-growing economic sectors worldwide with sales exceeding $1 trillion, as a pharmaceutical business, you likely face challenges around drug development, clinical trials, regulatory compliance, patents, and commercialization. Utilizing AI and analytics at scale could help accelerate innovation and time-to-market for new therapies. NeuralSeek's no-code AI platform could enable your pharmaceutical company to:  - Automate customer support and medical information sharing - Generate content like scientific publications and regulatory documents - Streamline drug discovery and clinical trial processes - Personalize HCP and patient engagement  - Optimize supply chain and manufacturing operations. By connecting NeuralSeek to your company's proprietary data and systems, you can rapidly deploy AI solutions tailored to your specific needs and workflows as a pharma business. This can drive efficiencies, reduce costs, and ultimately help bring life-saving treatments to patients faster. I'd suggest checking out these resources to dive deeper into AI use cases fo r_pharma:  - The future of the pharmaceutical industry: https://www2.deloitte.com/us/en/insights/industry/health-care/future-of-pharmaceutical-industry.html - Pharma trends 2824: Sha ping the future landscape: https://www.zs.com/insights/trends-shaping-pharmaceutical-landscape-2824-and-beyond Let me know if you have any other questions!",
    }

---

### Watsonx Streaming Context Guide

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/wa_context_guide/index>

##### Overview

**What is it?**

- It's an endpoint called **`/maistro_stream`** that you'll find in our **Integrate** tab.

> **Note**
> This endpoint is designed to support streaming responses from both the LLM and the mAIstro Agent.

**Why is it important?**

- Streaming responses create the impression of a faster, more interactive experience by displaying the reply as it's being formed. This immediate feedback enhances the overall user experience.

> **Tip**
> Enabling streaming can make your chatbot feel more responsive, which is especially useful when handling longer responses or complex queries.

**How does it work?**

- To enable a more dynamic and responsive user experience, first enable streaming in mAIstro and on your LLM nodes. Then, set up your Watsonx Assistant Chatbot following the IBM Focus lab instructions, modify the extension configuration by setting the correct operation and parameters, and enable streaming in Watsonx Assistant. Finally, verify the streaming behavior with the provided demo.

###### Enable Streaming in mAIstro

- **Toggle the streaming feature:**
Locate the streaming option at the bottom right of mAIstro and enable it.

- **LLM Node Configuration:**
In every LLM node that should support streaming (ideally the final LLM call), set the option `enable_streaming`.

![enablestreaming](https://draft-wiki.neuralseek.com/assets/guides/integration/enablestreaming.png)

---

###### Configure Watsonx Assistant Chatbot

Follow steps **1.2** and **1.3** in our [Learning Lab IBM Focus](https://labs.neuralseek.com/module1/module1_ibm/ibm_module1-2/ibm_module1-2/) to set up your Watsonx Assistant Chatbot.

---

###### Modify the Extension Configuration

1. **Navigate to the Actions Tab:**

  - Select the extension you created.
  - Click on the step where you want to use the extension.
  - Click **Edit Extension**.

2. **Configure the Extension:**

  - **Extension Selection:** Choose the extension you previously created.
  - **Operation:** Set it to **`Stream mAIstro NTL or an agent`**.

3. **Set Your Parameters:**

  - **Agent Name:** Set `agent` to the name of the mAIstro agent you want to call.
  - **Optional Parameter:** Due to a known Watsonx Assistant bug, set an optional parameter, for example `timeout` to an appropriate value. This ensures streaming behaves correctly.
  - **Parameters Example:** Define your parameters (either as variables or expressions) that your agent expects. For example:

    [
      {
        "name": "question",
        "value": "userQuery" // 'userQuery' is a session variable provided by the user
      }
    ]

4. **Stream Response Option:**

  - Scroll to the bottom and set the **Stream response** option to `chunk`.

5. **Save Your Changes:**

  - Click **Apply**.
  - Remember to hit the **Save** button in the top left corner of your window.

![streamendpoint](https://draft-wiki.neuralseek.com/assets/guides/integration/streamendpoint.png)

---

###### Enable Streaming in Watsonx Assistant

1. **Go to the Preview Tab:**

  - Navigate to the Preview Tab in your IBM Watsonx Assistant menu.

2. **Toggle Streaming On:**

  - Turn the streaming toggle on to enable the feature.

![streamingfwatson](https://draft-wiki.neuralseek.com/assets/guides/integration/streamingfwatson.png)

---

###### Final Behavior

After configuring all settings, your system should behave as demonstrated below:

![final](https://draft-wiki.neuralseek.com/assets/guides/integration/finalresult.png)

---

### Implementing Feedback

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/implementing_feedback/index>

##### Overview

**What is it?**

- The Thumbs Up/Thumbs Down icons are available after each response given in the Seek tab of NeuralSeek's UI. These responses indicate a score of 5 for Thumbs Up and 0 for Thumbs Down. These icons are available to be shown and utilized in-line with the conversation.

**Why is it important?**

- The Thumbs Up/Thumbs Down icons within NeuralSeek are useful for clients to be able to provide feedback to answers generated by NeuralSeek based on queries relevant to their connect corporate content. Being able to implement these icons into a virtual agent is important for clients who want to provide their users with a way to provide relevant, trackable feedback that does not affect answer generation directly.

**How does it work?**

- After a query is submitted in NeuralSeek's Seek tab, users can simply click either the 'Thumbs Up' icon or the 'Thumbs Down' icon based on their impression of the generated response. The response is then tracked and recorded within the relevant intent on NeuralSeek's 'Curate' tab. Users are able to implement the icons into a virtual agent by using the uniquely generated SVG URL provided after each response. See below for information on using 'iframe' response type to integrate these feedback icons within the IBM virtual agent watsonx Assistant.

##### Integrating Thumbs with watsonx Assistant

Users are able to easily integrate the **Thumbs Up/Thumbs Down** feedback icons as an **iframe** response type within watsonx Assistant. The content, embeddable as an HTML iframe element, allows users to interact with NeuralSeek's rating endpoint seamlessly without leaving the chat by displaying the thumbs icons directly in the conversation.

To include the **Thumbs Up/Thumbs Down** icons within watsonx:

1. Navigate to the watsonx Assistant instance, and open an **Action**.
2. In the **Assistant says** field within the relevant conversation step, click the **iframe** icon.
3. Set the **Source URL** to the NeuralSeek step response **body.thumbs**
  - Optionally, users can include a query parameter for background-color to the thumbs url given: `?style=background-color%3A%23f4f4f4`
4. Optionally, add a descriptive title in the **Title** field.
5. Toggle the **Display iframe inline** button to **On** to display the thumbs icons inline with the conversation.
6. Set the **iframe height** to 45 for proper viewing.
7. Click **Apply** to save response type.

![iframe_response_type_1](https://draft-wiki.neuralseek.com/assets/guides/integration/iframe_response_type_1.png)
![iframe_response_type_2](https://draft-wiki.neuralseek.com/assets/guides/integration/iframe_response_type_2.png)

##### Viewing Ratings in NeuralSeek

Feedback from utilizing the Thumbs Up/Thumbs Down icons in NeuralSeek's Seek tab can be viewed from the Curate tab.

1. Navigate to the **Curate** tab within NeuralSeek's interface.
2. Expand desired intents by clicking the down-caret.

![curate stars](https://draft-wiki.neuralseek.com/assets/guides/integration/curate_star_rating.png)

3. Optionally, Select desired intents by checking the box.
4. Click the blue **Download to CSV** button.
5. A CSV file will be downloaded to the user's local machine. There, they can view the rating given from the Thumbs Up/Thumbs Down icons in the **Response** column.

> **Note**
> A score of 5 is given for a 'Thumbs Up'. A score of 0 is given for a 'Thumbs Down'. The score shown is an average of all ratings.

![download_csv](https://draft-wiki.neuralseek.com/assets/guides/integration/download_csv_new.png)
![csv_rating](https://draft-wiki.neuralseek.com/assets/guides/integration/csv_rating.png)

##### Integrating Custom Ratings via API

Users are able to further customize ratings within NeuralSeek using the `/rate` API.

POSTs to the `/seek` endpoint return a parameter `answerID`. You may pass this answer ID to the `/rate` endpoint with a number `0-5` to manually 'rate' a given answer.

To try it out:

1. Navigate to the **Integrate** tab within NeuralSeek's interface.
2. Select **API** from the side menu.
3. Click the **Authorize** button, and enter the given API key on the screen.
4. Select the **Seek** drop down option and post a query to `/seek`.
5. Pull the `answerID` return parameter from this `seek` query. E.g. `76574849`
6. Select the **Rate** drop down option to see options of the `/rate` endpoint. For example POST data:

    {
        "answerID: "76574849"
        "score": "5"
    }

---

### NICE CXone Integration

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/integration/nice_cxone_integration/index>

##### Architecture Overview

The following diagram illustrates the end-to-end flow from the Chat Point of Contact within NICE CXone to your NeuralSeek mAIstro Agent via the Custom Exchange Endpoint.

![Architecture Overview](https://draft-wiki.neuralseek.com/assets/guides/integration/nice_cxone_integration.png)
> **Abstract: Chat Point of Contact**
> The entry point where the customer initiates a conversation, typically via webchat, mobile app, or messaging platforms, connecting directly to NICE CXone.
>
> **Abstract: Studio Script**
> NICE CXone Studio Script controls the flow of interactions, integrating the Custom Exchange Endpoint to send and receive user messages dynamically.
>
> **Abstract: Custom Exchange Endpoint**
> Acts as the HTTP interface between CXone and external services, forwarding user requests to your Proxy Tunnel and handling responses from the Virtual Agent.
>
> **Abstract: Proxy Tunnel**
> A secure communication channel used to connect NICE CXone’s environment to your backend services and Virtual Agent without exposing public endpoints.
>
> **Abstract: Virtual Agent**
> Your AI-based chatbot or Virtual Assistant that processes user inputs and returns context-aware responses, integrated with NICE CXone through the Proxy Tunnel.

##### CXone Configuration

This section outlines the required CXone configuration settings for the Point of Contact integration.

##### NICE CXone Studio script

For the NeuralSeek integration test, you will use the standard `VAHSampleChatScript` provided by NICE CXone. This script handles the communication between CXone Studio and your Virtual Agent via the Virtual Agent Hub (VAH) Custom Exchange Endpoint.

You can download the Studio Script from the official NICE CXone resources here:

[Download sample chat script](https://draft-wiki.neuralseek.com/documentation/guides/integration/nice_cxone_integration/scripts/TDD_TEXT_VAHSampleChatScript.json)

![NICE CXone sample script for Chat](https://draft-wiki.neuralseek.com/assets/guides/integration/virtual_agent_hub_sample_chat_script.png)
![Virtual Agent Hub Text Bot Welcome intent flow](https://draft-wiki.neuralseek.com/assets/guides/integration/text_bot_welcome_message_flow.png)
![Virtual Agent Hub Text Bot conversational flow](https://draft-wiki.neuralseek.com/assets/guides/integration/text_bot_conversational_flow.png)

The script manages:

- Handling inbound chat requests via ACD Chat channel.
- Exchanging messages with your NeuralSeek Virtual Agent through the VAH endpoint.
- Managing session flow and error handling within the CXone Studio environment.

The first part of the flow handles the welcome message intent, and the latter handles the following conversational flow between the user and the NeuralSeek mAIstro agent.
> **Note: Studio script for production**
> No custom modifications to the script are required for basic integration testing with NeuralSeek. For production environments, you can extend or modify the script based on your specific business logic.

###### ACD Chat Configuration

![ACD configuration Sidebar](https://draft-wiki.neuralseek.com/assets/guides/integration/nice_cxone_sample_configuration.png)
> **Example: Sample Configuration**
>
> Campaign:
> - Campaign Name: Hospital Patient Digital Engagement
> Skill:
> - Media Type: Chat
> - Skill Name: Chat - Appointment Scheduling
> - Campaign: Hospital Patient Digital Engagement
> Chat Profile:
> - Profile Name: Chat Widget V2
> - Interface: V2 (HTML5)
> Point of Contact:
> - Media Type: Chat
> - Name: Chat - Home Page
> - Point of Contact:
> - Skill: Chat - Appointment Scheduling
> - Script: VAHSampleChatScript
> - Chat Profile: Chat Widget V2

##### Service Endpoint Authorization

The authorization mechanism for accessing the NeuralSeek Virtual Agent service endpoint is based on an API key passed through a custom request header.

![NeuralSeek mAIstro endpoint](https://draft-wiki.neuralseek.com/assets/guides/integration/maistro_endpoint.png)

###### Authorization Method

**Header-based API Key authentication** is used. This ensures secure and straightforward access control.

###### Required Header

- `apiKey`: `<your-neuralseek-api-key>`

The API key value will vary depending on the client and environment (staging or production).

No additional authentication mechanisms (such as OAuth) are required. This simplifies integration while maintaining secure access through per-client API key management.

##### Virtual Agent Hub Configuration

This section defines the necessary configuration for the Virtual Agent Hub (VAH) to connect with your NeuralSeek mAIstro Agent.

![Virtual Agent Hub Configuration for NeuralSeek mAIstro Agent](https://draft-wiki.neuralseek.com/assets/guides/integration/virtual_agent_hub_configuration.png)

###### Webhook URL

    https://api.neuralseek.com/v1/<your-neuralseek-instance>/maistro

###### Endpoint Parameters

- None required.

###### Custom Headers (Required for NeuralSeek)

- `apiKey`: `<your-neuralseek-api-key>`
- `overrideschema`: `"true"` – Accepts the request schema coming from Virtual Agent Hub.
- `overrideagent`: `proxy_tunnel_v3_agent` – The mAistro agent.
- `debug`: `"true"` – Recommended during setup to include debug details; disable for production.

###### Timeout

- No change needed.

###### Integration Version

- Version **3.0.0** is recommended for this integration.

###### Authorization and OAuth

- No authorization header or OAuth configuration required.

> **Note**
> Make sure that each TextBot Exchange action in your NICE CXone script is linked to the Neuralkseek virtual agent. You'll know it's selected when you see the green check mark next to its name in the Virtual Agent Hub.

##### Proxy Tunnel

The NeuralSeek integration uses a pre-configured proxy tunnel agent called `proxy_tunnel_v3_agent`.
This agent is designed to be compatible with CXone Textbot Exchange version 3.0, and also supports versions 1.0 and 2.0.
Version 3.0 is recommended for optimal flexibility and feature support.

![Proxy tunnel mAIstro Agent](https://draft-wiki.neuralseek.com/assets/guides/integration/proxy_tunnel_maistro_agent.png)

###### Hosting

The proxy tunnel is hosted directly within NeuralSeek as a **no-code Maistro agent**, requiring no additional infrastructure from the client side.
This setup reduces maintenance overhead and allows for rapid customization.

###### Customization and Expansion

The `proxy_tunnel_v3_agent` can be customized and extended within NeuralSeek to accommodate specific client use cases and workflows.

###### Failover Strategy

As the proxy tunnel is managed within NeuralSeek's cloud infrastructure, standard cloud resilience applies.
Clients do not need to set up a separate failover mechanism.

###### NeuralSeek Template Language (NTL)

**NTL (NeuralSeek Template Language)** is a simple, declarative language used to define NeuralSeek agents.
It allows you to easily share, customize, and extend agent behavior without writing complex code.

Below is the NTL configuration for the `proxy_tunnel_v3_agent` used in this integration:

###### NTL Code Example

Below is an example of NeuralSeek Template Language (NTL) code.
You can copy it easily using the button provided.
> **Example: Proxy tunnel mAIstro agent NTL (NeuralSeek Template Language)**
>
> << name: botSessionState, prompt: false >>=>{{ jsonToVars  }}
> {{ condition  | value: "'<< name: userInputType >>' == '5'" }}=>{{ variable  | name: "nextPromptSequence" | value: "{\"prompts\":[{\"transcript\":\"Welcome to CareHaven Health, What can I do for you?\"}]}" }}=>{{ variable  | name: "intentInfo" | value: "{\"Slots\": {},\"intent\":\"Welcome\",\"intentConfidence\":\"100\"}" }}
> {{ condition  | value: "'<< name: userInputType >>' == '1'" }}=>{{ seek  | query: "<< name: followUpCategory, prompt: false >>
> << name: followUpQuery, prompt: false >><< name: userInput, prompt: false >>
> << name: followUpContext, prompt: false >><< name: dataPoints, prompt: false >>" }}=>{{ variable  | name: "seekResult" }}
> << name: seekResult, prompt: false >>=>{{ jsonToVars  }}
> {{ condition  | value: "'<< name: intentInfo.Slots, prompt: false >>' == '[object Object]'" }}=>{{ variable  | name: "Slots" | value: "{}" }}
> {{ condition  | value: "'<< name: botSessionState.dataPoints, prompt: false >>' == '[object Object]'" }}=>{{ variable  | name: "dataPoints" | value: "''" }}
> {{ condition  | value: "'<< name: botSessionState.isCompleted, prompt: false >>' = ''" }}=>{{ variable  | name: "isCompleted" | value: "false" }}
> {{ varsToJSON  | path: "botSessionState.dataPoints" | variable: "botSessionStateDataPoints" | includePath: "false" | output: "" }}
> {{ varsToJSON  | path: "botSessionState.isCompleted" | variable: "botSessionStateIsCompleted" | includePath: "false" | output: "" }}
> {{ condition  | value: "'<< name: seek.categoryName >>' == 'FAQ'" }}=>{{ variable  | name: "nextPromptSequence" | value: "{\"prompts\":[{\"transcript\":\"<< name: seekResult>>\",\"textToSpeech\":\"<< name: seekResult >>\"}]}" }}=>{{ variable  | name: "intentInfo" | value: "{\"Slots\": {},\"intent\":\"NLU_NEEDED\",\"intentConfidence\":\"100\"}" }}
> {{ condition  | value: "<< name: seek.category >> == 706287" }}=>{{ variable  | name: "nextPromptSequence" | mode: "" | value: "{\"prompts\":[{\"transcript\":\"<< name: nextPromptSequence.prompts[0].transcript, prompt: false >>\",\"textToSpeech\":\"<< name: nextPromptSequence.prompts[0].textToSpeech, prompt: false >>\"}]}" }}=>{{ variable  | name: "intentInfo" | value: "{\"Slots\": {},\"intent\":\"NLU_NEEDED\",\"intentConfidence\":\"100\"}" }}=>{{ variable  | name: "botSessionState" | value: "{\"lastIntent\":\"<< name: seek.intent, prompt: false >>\",\"followUpQuery\":\"<< name: botSessionState.followUpQuery, prompt: false >>\",\"followUpCategory\":\"<< name: botSessionState.followUpCategory, prompt: false >>\",\"followUpTurn\":\"<< name: botSessionState.followUpTurn, prompt: false >>\",\"dataPoints\":\"<< name: botSessionStateDataPoints, prompt: false >>\",\"isCompleted\":\"<< name: botSessionState.isCompleted, prompt: false >>\"}" | mode: "overwrite" }}
> {{ condition  | value: "'<< name: userInputType >>' == '2'" }}=>{{ condition  | value: "AND('<< name: base64WavFile >>' == '')" }}=>
> TREATMENT: base64 audio=>{{ variable  | name: "nextPromptSequence" | value: "{\"prompts\":[{\"transcript\":\"No audio found\"}]}" }}
> {{ condition  | value: "'<< name: userInputType >>' == '0'" }}=>{{ condition  | value: "AND('<< name: mediaType >>' == 'voip')" }}=>
> TREATMENT: no input=>{{ variable  | name: "nextPromptSequence" | value: "{\"prompts\":[{\"base64EncodedG711ulawWithWavHeader\":\"<< name: base64WavFile >>\"}]}" }}
> {{ condition  | value: "'<< name: userInputType >>' == '0'" }}=>{{ condition  | value: "AND('<< name: mediaType >>' != 'voip')" }}=>
> TREATMENT: no input=>{{ variable  | name: "intentInfo" | value: "{\"Slots\": {},\"intent\":\"NLU_NEEDED\",\"intentConfidence\":\"100\"}" }}
> {{ condition  | value: "'<< name: botSessionState, prompt: false >>' == ''" }}=>{{ variable  | name: "botSessionState" | value: "{}" }}
> {{ variable  | name: "errorDetails" | value: "{\"errorBehaviour\":0,\"errorPromptSequence\":{\"prompts\":[{}]}}" }}=>{{ variable  | name: "nextPromptBehaviours" | value: "null" }}=>{{ variable  | name: "customPayload" | value: "{}" }}
> {{ variable  | name: "branchName" | value: "PromptAndCollectNextResponse" }}
> {"branchName":"<< name: branchName, prompt: false >>",
> "nextPromptSequence":<< name: nextPromptSequence, prompt: false >>,
> "intentInfo":<< name: intentInfo, prompt: false >>,
> "nextPromptBehaviours":<< name: nextPromptBehaviours, prompt: false >>,
> "errorDetails":<< name: errorDetails, prompt: false >>,
> "customPayload":<< name: customPayload, prompt: false >>,
> "botSessionState":<< name: botSessionState, prompt: false >>}

##### NeuralSeek mAIstro Agent use case

The NeuralSeek mAIstro Agent demonstrates how CXone can orchestrate multi‑turn conversations using NeuralSeek's agentic AI framework. In this use case, the agent is configured to handle appointment scheduling by collecting all required user inputs, maintaining session state, and generating structured JSON outputs compatible with Virtual Agent Hub. The workflow leverages NeuralSeek Template Language (NTL) to define conversation logic, enforce required fields, and determine when the session is complete, ensuring the Virtual Agent can pass validated data back to downstream CXone systems.

![NeuralSeek Appointment Scheduling Use Case](https://draft-wiki.neuralseek.com/assets/guides/integration/sample_appointment_scheduling_agent.png)
![NeuralSeek mAIstro Agent Use Case](https://draft-wiki.neuralseek.com/assets/guides/integration/nice_cxone_neuralseek_use_case.png)

The diagram and accompanying NTL example illustrate how the mAIstro Agent manages the full appointment scheduling workflow. Incoming user input is evaluated, missing fields are requested in a single prompt to minimize conversation turns, and session state is continuously updated in botSessionState. When all required fields are collected, the agent generates a final JSON response that includes a structured summary for CXone, while clearing the session state to prepare for the next interaction.
> **Example: Appointment scheduling Agent NTL (NeuralSeek Template Language)**
>
> {{ seekIn  }}=>{{ variable  | name: "seekInput" | value: "<< name: seekIn.originalQuery, prompt: false >>" | mode: "overwrite" }}
> {{ LLM  | prompt: "You are CareHaven Health's virtual scheduling assistant. Your job is to collect all required patient details to book healthcare appointments.
>
> **Required Fields**: Email, DoctorSpecialty, PreferredDate, PreferredTime
> **Response**: Return valid JSON (no markdown).
>
> **Schema**:
> {
> \"nextPromptSequence\":{\"prompts\":[{\"transcript\":\"\",\"textToSpeech\":\"\"}]},
> \"intentInfo\":{\"Slots\":{},\"intent\":\"\"},
> \"botSessionState\":{\"lastIntent\":\"<< name: seek.intent, prompt: false >>\",\"followUpQuery\":\"User input: \",\"followUpCategory\":\"Category: Appointments\",\"followUpTurn\":\"Last collected data: \",\"dataPoints\":{},\"isCompleted\":false}
> }
>
> **Instructions**:
> - Always return valid JSON matching the type.
> - Use dataPoints to pre-fill Slots.
> - Do not modify the values of followUpQuery, followUpCategory, or followUpTurn.
> - **CRITICAL**: If ANY fields are missing, ask for ALL missing fields in a SINGLE message in the transcript. Do not ask for fields one by one - gather all missing information at once to minimize conversation turns.
> - Only set isCompleted: true when ALL required fields (Email, DoctorSpecialty, PreferredDate, PreferredTime) are provided.
> - If all fields are filled, isCompleted: true and transcript confirms booking.
>
> **Input**:
> << name: seekInput, prompt: false >>
>
> **Important**
> - Always return a complete JSON with all closed braces.
> - Ask for multiple missing fields together, not individually." | cache: "true" | stream: "disable_streaming" | modelCard: "ns-claude3.5-haiku" }}=>{{ variable  | name: "llmResponse" }}
> << name: llmResponse, prompt: false >>=>{{ jsonToVars  }}
> {{ condition  | value: "'<< name: botSessionState.isCompleted, prompt: false >>' == 'true'" }}=>{{ LLM  | prompt: "Create a clean summary with the appointment details provided below. Return the summary in the required JSON format.
>
> **Response**: Return valid JSON (no markdown).
>
> **Schema**:
> {
> \"nextPromptSequence\":{\"prompts\":[{\"transcript\":\"\",\"textToSpeech\":\"\"}]},
> \"intentInfo\":{\"Slots\":{},\"intent\":\"\"},
> \"botSessionState\":{}
> }
>
> **Instructions**:
> - Always return valid JSON matching the exact schema above.
> - Put the appointment summary in the transcript field
> - Format the summary with each detail on a separate line: Email, Doctor Specialty, Preferred Date, Preferred Time
> - Use the format: \"Email: [value]\" for each line
> - Leave botSessionState as an empty object {}
> - Leave intentInfo.Slots and intentInfo.intent as empty
>
> << name: botSessionState.dataPoints.Email, prompt: false >>
> << name: botSessionState.dataPoints.PreferredDate, prompt: false >>
> << name: botSessionState.dataPoints.PreferredTime, prompt: false >>
> << name: botSessionState.dataPoints.DoctorSpecialty, prompt: false >>
>
> **Important**
> - Always return a complete JSON with all closed braces.
> - The summary goes in the transcript field, not as separate text.
> - botSessionState must be empty: {}" | cache: "true" | stream: "disable_streaming" | modelCard: "ns-claude3.5-haiku" }}=>{{ variable  | name: "llmResponse" }}
> << name: llmResponse, prompt: false >>

###### Governance and guardrails

The NeuralSeek mAIstro Agent demonstrates a reference implementation of an agent-driven workflow using NeuralSeek's NTL (NeuralSeek Template Language). This use case focuses on an appointment scheduling scenario, where the agent manages multi-turn conversations, captures required data fields, and maintains session state across interactions. The mAIstro Agent executes LLM-driven responses under strict governance controls, including PII redaction, prompt injection detection, semantic scoring, and length constraints. All collected data is structured in JSON for compatibility with CXone's Virtual Agent Hub, enabling downstream automation such as scheduling, logging, or analytics.

![mAIstro seek node settings](https://draft-wiki.neuralseek.com/assets/guides/integration/maistro_no_code_seek_node_settings.png)
![multi agent seek flows](https://draft-wiki.neuralseek.com/assets/guides/integration/multi_agent_seek_flows.png)

In this Agentic AI architecture, Governance configurations and guardrail settings can be modified for each agent flow. The NICE CXone hits the proxy tunnel mAIstro agent using the mAIstro API, and this agent calls Seek with the required context, where it can be properly routed to the appropriate agent, such as Appointments, FAQ, etc.

![NeuralSeek agent custom configurations](https://draft-wiki.neuralseek.com/assets/guides/integration/agent_governance_configuration.png)
![NeuralSeek agent custom guardrails](https://draft-wiki.neuralseek.com/assets/guides/integration/agent_guardrails_settings.png)

---

## Guides — Models

### Model Guides Overview

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/models/index>

##### Models

- [Multimodal LLM Configuration](https://draft-wiki.neuralseek.com/documentation/guides/models/multimodal/index)
- [Semantic Model Tuning](https://draft-wiki.neuralseek.com/documentation/guides/models/semantic_model/index)

---

### Multimodal LLM Configuration

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/models/multimodal/index>

##### Steps to Configure the LLM

To begin, navigate to the Configure tab and locate the LLM Details section.

![LLM details](https://draft-wiki.neuralseek.com/assets/guides/models/llmdetails3.png)

Click on "Add an LLM" and choose a model that can process images, such as OpenAI GPT-4o.

![Select LLM](https://draft-wiki.neuralseek.com/assets/guides/models/selectllm.png)

Once selected, add the model and enter the necessary connection details, which, for GPT-4o, would be the API Key.

Test the connection by clicking the Test button and ensure the button turns green, indicating a successful connection.

![Successful LLM](https://draft-wiki.neuralseek.com/assets/guides/models/successtestllm.png)

Save the configuration and provide a meaningful name for the version.

##### Steps to Process an Image

Next, switch to the Maistro tab to upload an image. Use the left side pane to search for "Upload data" and then select "Upload a File" under that section.

After selecting the local file, a local document node will be created. You can use the "Local Document" button to access a dropdown menu that shows all your locally uploaded files, and select the image you uploaded as your choice.

    << name: img, prompt: true, desc: Enter image file name >>

![Local document node](https://draft-wiki.neuralseek.com/assets/guides/models/localdocument.png)

If you plan to use this image for different purposes, it's best to set it as a variable. Add a set variable node to the right of the local document node and give the variable a descriptive name.

![Local document node](https://draft-wiki.neuralseek.com/assets/guides/models/setvariablenode.png)

Below these nodes, add a send to LLM node. For the prompt, you can use:

    What is this a picture of?

For the image, reference the variable you defined earlier:

    << name: img, prompt:false >>

And the node should be end up like this:

![Complete template](https://draft-wiki.neuralseek.com/assets/guides/models/sendtollmnode.png)

Select an LLM that supports reading images, such as GPT-4o.

Press the Evaluate button. You will be prompted to enter the name of the image file you want to process, including its file extension. Once entered, the setup will allow Maistro to describe the image.

![Complete template](https://draft-wiki.neuralseek.com/assets/guides/models/maistroworkflow.png)
> **Note**
> This is a basic example, but you can expand on this logic to achieve more complex procedures.

---

### Semantic Model Tuning

**Source:** <https://draft-wiki.neuralseek.com/documentation/guides/models/semantic_model/index>

##### Overview

This guide provides information on how to use Semantic Model Tuning to improve your search results. It includes detailed explanations of how each setting works, and what effects they have on the model depending on their tuning scores.

##### What is Semantic Model Tuning?

![semanticdetail](https://draft-wiki.neuralseek.com/assets/guides/models/semantic-score-details.png)

Whenever a question is asked in NeuralSeek's `Seek` feature, users are able to see the answer's semantic score, which is a measure of how confident NeuralSeek is in its answer, as well as its semantic analysis, which thoroughly details the information used to get the answer as well as any complications that made NeuralSeek less confident in its response. If you are consistently getting low semantic scores in your responses despite the answers being correct, you may find use in configuring the semantic model tuning results so that the semantic score does not get as penalized for various external factors.

##### Locating Semantic Scoring

To begin, navigate to the `Configure` tab on the Home page, and open the "Governance and Guardrails" dropdown. There, you will see a tab for Semantic Scoring.

![location](https://draft-wiki.neuralseek.com/assets/guides/models/governance-page.png)

You will notice a black button at the bottom of the Semantic Scoring settings labeled "Semantic Model Tuning". By clicking on it, you will be brought to a settings page where you can customize settings for Semantic Model answers.

![tuning](https://draft-wiki.neuralseek.com/assets/guides/models/semantic-model-tuning.png)

##### Tuning Your Search Results

The following is an in-depth analysis on how each setting in Semantic Model Tuning can affect your search results in NeuralSeek:

###### Missing key search term Penalty

This penalty is applied for answers that lack KnowledgeBase attribution of *proper* nouns included in the search. This setting is at 0.6 by default.

###### Missing search term Penalty

This penalty is applied for answers that are missing KnowledgeBase attribution of *other* nouns that were included in the search. This setting is at 0.25 by default.

###### Source Jump Penalty

When answers join across many source documents it can be an indication of lost meaning or intent, depending on your source documentation. This setting is at 3 by default. It is recommended to turn this setting low if you have many source documentations and generally need help "stitching" answers together from many documents. Likewise, increase this penalty to encourage citations from few or single documents.

###### LLM Decline Penalty

When LLM answers seem to indicate the question is unrelated to the documentation, or refuses to answer, NeuralSeek will apply an additional penalty to the semantic score. This setting is at a 1 by default.

###### Total Coverage Weight

Looking at the answer, how much weight should be given to the total coverage alone, regardless of other penalties. This setting is at a 0.25 by default. Increasing this helps prevent abnormally low scores from long, highly stitched answers. Decreasing will better catch hallucinations in short answers.

###### Re-Rank Min Coverage %

What is the minimum coverage of the total answer that the top used source document needs to be re-ranked over the top KB-sourced document. This setting is at a 0.25 by default.

###### Allowed Terms

We provide a text box at the bottom of the page where you can input words and phrases that should not be penalized, regardless of whether they are present in the sourced document passages.

##### How to make use of Semantic Model Tuning

###### Example 1

Suppose a user asks NeuralSeek a simple question that can easily be answered by our documentation, for example, "How do I connect to an LLM". Although NeuralSeek gives a correct response, you may notice that its Semantic Match score is unusually low.

![llm1](https://draft-wiki.neuralseek.com/assets/guides/models/llm-question-1.png)

By clicking on the Statistical Details button in Semantic Analysis, you will be brought to a page that thoroughly details the penalties that resulted in a low Semantic Match. In this case, we can see that the two biggest factors were a large amount of source jumps, and a lower-than-average Top Source Coverage score.

![llm2](https://draft-wiki.neuralseek.com/assets/guides/models/llm-question-2.png)

Since these two settings are the ones most responsible for our low Semantic Match score, the settings for those two should be appropriately adjusted so that they do not influence the results as much. By heading back into our Configuration tab and heading over to the Semantic Model Tuning settings, you can decrease their initial values so that NeuralSeek knows to factor those penalties in less severely.

![llm3](https://draft-wiki.neuralseek.com/assets/guides/models/llm-question-3.png)

After saving your settings, you can head back to the Seek tab and ask the same question, and notice that your Semantic Match score has increased greatly thanks to the adjusted settings.

![llm4](https://draft-wiki.neuralseek.com/assets/guides/models/llm-question-4.png)

###### Example 2

Suppose a question you ask NeuralSeek contains a term that is not contained in your source documentation and thus cannot be properly defined. For example, let's ask how NeuralSeek differs from other competitors on the market, like ChatGPT. Since ChatGPT is not a term defined in our documentation, NeuralSeek will penalize the response since it contains a "hallucinated term", which are terms generated by the model that are not present in our source material.

![gpt1](https://draft-wiki.neuralseek.com/assets/guides/models/chatgpt-1.png)

If you don't want to penalize responses containing ChatGPT in them, head over to the Semantic Model Tuning settings, and in the text box, type in ChatGPT. This will remove ChatGPT from the hallucinated terms list, and will no longer have a negative impact on future Seeks including the term.

![gpt2](https://draft-wiki.neuralseek.com/assets/guides/models/chatgpt-2.png)

By heading back to the Seek tab and asking the same question, we can see that the Semantic Analysis no longer penalizes the user for the use of the now allowed-term word ChatGPT.

![gpt3](https://draft-wiki.neuralseek.com/assets/guides/models/chatgpt-3.png)

##### Conclusions

Generally speaking, semantic model tuning should be a fine tuning exercise after data prep and kb tuning - not a first resort. Typically this activity is last after all other methods of data prep, kb tuning, etc have been tried and tested. These settings have a very broad effect on your answers, so change them sparingly and re-test broadly after changes are made.

---

## Features

### Answer Curation

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/answer_curation/index>

**What is it?**

- NeuralSeek is directly trained off of the documentation loaded into the KnowledgeBase. If there are undesired answers from NeuralSeek, the first step is to review the documentation within the KnowledgeBase, and effectively curate the answer which can then be used by NeuralSeek to train itself better the next time it answers.

**Why is it important?**

- One of the key factors in reducing costs is the utilization of curated answers sourced from a pool of responses, which proves to be more economical. Also, when the collection of answers becomes stagnant, potentially leading to outdated information, this feature will be able to detect it and refresh those with less manual process.

**How does it work?**

- To tackle this challenge, NeuralSeek provides a solution by automatically monitoring the sources of information. It continuously tracks and compares the generated responses with the source documents to determine if any changes have occurred. By doing so, NeuralSeek ensures that the answers remain up-to-date and relevant. This eliminates the need for manual intervention and the potential for outdated information, allowing users to trust the accuracy and currency of the answers provided.

###### Curating Intents and Answers

![curate](https://draft-wiki.neuralseek.com/assets/features/answer_curation/currate-page.png)

Let's first visit the UI page for curating intents and answers. Click the `Curate` tab on the top menu.

The UI is composed of the following columns:

**Intent**:

- Intents are a collection of questions that may be related to the similar `intent` of the question. It is prefixed by certain types of intents, such as `FAQ`, followed by the question's subject areas. By default, all the intents do fall under a category `Others`, but you can also define your own category in NeuralSeek's configuration.
- Intents also have a number of indicators that help users to understand the status of the intent. For example, it can show whether the intent has any new answers, whether the intent contains any PII (personally identifiable information), or whether the intent's underlying data has been outdated, etc.

**Q&A**:

- Shows the number of questions (white dialog icon) and answers (blue dialog icon) that this particular intent contains.

**Coverage %**:

- Indicates how much the KnowledgeBase has contributed to the answer's coverage. If NeuralSeek was able to find all the necessary information from the KnowledgeBase, this percentage is going to be very high.

**Confidence %**:

- Indicates how much NeuralSeek's answer is most likely to satisfy the user. If this score is high, it means the answer has a high score of being legitimate and true to the facts.

###### Reading the trend

![graph and color](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-002.png)

The data is presented through two distinct graphs: Coverage and Confidence.

1. **Coverage Graph**: This graph illustrates the total number of citations or reference materials utilized to address a specific question. A coverage value of zero indicates the absence of relevant documentation, while a value of 100% signifies comprehensive documentation available on the topic.

2. **Confidence Graph**: This graph assesses NeuralSeek’s confidence in the automated response provided. High confidence suggests that the answer is likely cited by the documentation well, whereas low confidence infers that the resource material might have conflicting documentation or ambiguity.

Both graphs are integral to data governance, directly reflecting the quality and reliability of the data used in generating answers. It is possible to have an accurate answer with low coverage but high confidence. It is also possible to have an inaccurate answer with high coverage and low confidence because the multiple resources have conflicting information.

**Color Coding**:

- **Coverage**: Represented in shades of blue, with intensity varying based on coverage levels. The darker the shade, the more comprehensive documentation is referenced.
- **Confidence**: Indicated by green for high confidence and red for low confidence.

**Slope**: The slope's height indicates the number of hits. A higher slope will show the majority of where the answers were bucketed - for example, if all the answers but one were scored at 99%, but there is one at 20%, the slope will be far larger at 99% and very small at 20%. By hovering over the graph, you can observe the trend of slope changes over time.

![changes](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-003.png)

In this case, there were instances of when the confidence had dropped from 83% to 22%, over the period between 14:07:31 to 14:12:15 on July 20th.

###### Displaying Intents and Answers

If you click the `⌄` Arrow next to the intent name, you will see the list of example questions and its generated answers:

![Alt text](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-004.png)

The example questions have either black color or gray color, depending on how they were created. The black colored examples are the ones that were actually submitted by the user's question. NeuralSeek automatically generates similar meaning questions per each question that it receives.

As necessary, you can also enter your own Example question in addition to the ones that NeuralSeek generates.

![Alt text](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-005.png)
> **Tip**
> It is also possible to add Notes that may save additional information regarding this particular intent.

###### Searching the intent

The size of intent can vary but could grow over multiple pages, so you may want to search for a particular intent from time to time. You could do that by using the search form at the top of the page. Enter the keyword and it will narrow down your search.

![search](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-010.png)

###### Filtering the intent

There is a more fine-grained way of filtering intents based on criteria such as whether they were edited, or a new answer was added, flagged, or out-of-date data was found. Click the filter button, set the criterias that you want, and the page will only show the ones that meet the filtering condition.

![filter](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-011.png)

###### Editing the Answer

On all the answers generated, a Subject Matter Expert can edit answers for both style and content. Edited answers automatically become training for the underlying LLM and will train the model on the style and content of the desired answer for that intent. Edited answers are also eligible for independant caching and can be directly served to the end user without going back to language genration.

Editing can be done by clicking the answer, modifying its content, and saving it.

![editing](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-006.png)

After saving, you will see that the answer that you edited will be marked as `Edited`.

![Alt text](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-007.png)
> **Note: Formating edited answers**
> Edited answers can be styled using [Markdown syntax](https://www.markdownguide.org/cheat-sheet/), depending on the formatting capabilities of the assistant/agent ([Supported Virtual Agents](https://documentation.neuralseek.com/ui/integrate/integrations/supported_virtual_agents/supported_virtual_agents/)) or the delivery channel (e.g., Slack, Facebook, WhatsApp).
>
> Supported elements may include: **bold**, *italic*, `inline code`, [hyperlinks](https://example.com), etc.
> **Note: Example of Mardown formating**
>
> This is a **bold** word, this is an *italic* word, and here is a [link to a website](https://example.com).
>
> Will render as:
>
> This is a **bold** word, this is an *italic* word, and here is a [link to a website](https://example.com).

###### Deleting Questions and Answers

If you wish to delete either the question or answer under the intent, you can do so by clicking the `circle with i` icon and selecting `Remove`.

![remove](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-008.png)
> **Warning**
> Once they are removed, there is no way to roll back the removal, so be careful.

###### Deleting all data

You can delete all data by selecting the gear icon at the top and selecting:

![deletion](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-009.png)

- Delete all data
- Delete all analytics
- Delete all unEdited Answers

These are a useful feature if you wish to simply reset all of these data and start from the scratch.

###### Intent operations

When you select an intent, a popup will be displayed which shows you the operations that you can do with the selected intent.

![operations](https://draft-wiki.neuralseek.com/assets/features/answer_curation/image-012.png)

- Edit category - will let you edit the current category
- Download to CSV - will export this into a CSV file. It will have the following format: `ID,question,score,kbCoverage,answer,category,intent,pii`
- Generate Conversation - This will convert the intent into conversation, instead of a simple question and answer. This will give a better context for the NeuralSeek to generate answers from.
- Flag - Will flag the intent so that you can quickly find it later.
- Rename - Will let you rename its name
- Delete - Deletes the selected intent(s).
- Backup - Backs up the intent for later recovery. Note that the backed up file is not a text file, but in binary format.
- Merge - appears only when two or more intents are selected. It merges all of their questions and answers into a single intent.

---

### Auto Data Cleanse

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/auto_data_cleanse/index>

**What is it?**

- When using webpages as documentation for the KnowledgeBase, nuisance information such as banners and cookies will deteriorate information relevant to the users organization. The Automatic Data Cleansing feature of NeuralSeek will automatically cleanse the web pages that were scraped, exposing information pertinent to the organization, at the users own pace.

**Why is it important?**

- Condensing and focusing the information, while removing useless wording returned by the KnowledgeBase is critical to high quality answer generation. Most web content is not great at directly answering questions because of the amount of nuisance webpage language that gets extracted with the core content.

**How does it work?**

- NeuralSeek will identify documents in the KnowledgeBase that come from webscrapes. NeuralSeek will then run its own algorithm against the full webpage HTML to extract just the core content and remove as much of the extraneous information as possible.

---

### Caching

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/caching/index>

**What is it?**

- NeuralSeek uses [caching](https://en.wikipedia.org/wiki/Cache_(computing)) strategy in two areas (Corporate KnowledgeBase and Answer) to enhance performance and reduce computational cost during its operation.

**Why is it important?**

- Caching frequently returned answers saves both time and computation cost to run virtual agents, as it reduces NeuralSeek having to generate responses repeatedly, especially on the more frequently asked questions or seldom updated answers.

**How does it work?**

- The first part is when NeuralSeek searches through the corporate knowledge base to obtain the original information. You can set the cache duration of such responses to be cached, so that the original information’s retrieval time can be reduced.
- NeuralSeek then utilizes two types of caches for both your edited answers and generated answers that can serve cached answers to user questions in order to speed up response times and produce more consistent results.

###### Corporate KnowledgeBase Cache

When NeuralSeek accesses the Corporate KnowledgeBase, it processes the original data from it, cleanses its contents (e.g. removing unnecessary contents, filtering, deduplicating, etc.), compresses it, and prioritize the returned contents which is then processed with LLM (Large Language Model) to form the completed response, usually at the range of 8,000 ~ 9,000 characters. It then derives a hash value of that response window which acts as a check to later see if the original data is updated. This response is what actually gets cached within NeuralSeek, so that all the search, processing, and LLM-generated time is effectively saved when the same answer needs to be derived.

Under the `Configure > Corporate KnowledgeBase Details` section, user can set the duration of the cache measured in minutes to control how long these responses need to be cached.

![kb cache setting](https://draft-wiki.neuralseek.com/assets/features/caching/image_001.png)

###### Answer Cache

When the user asks a question to NeuralSeek, it tries to use the question to find the matching ‘intent’ of the question. And when the matching intent is discovered (usually via fuzzy matching), the provided answer, either normal or user edited, can then be cached.

![answers](https://draft-wiki.neuralseek.com/assets/features/caching/image_002.png)

Under the `Configure > Intent Matching & Cache Configuration` section, you can enable or disable the edited answer cache or normal answer cache, and set the following parameters to control how it works:

![answer cache settings](https://draft-wiki.neuralseek.com/assets/features/caching/image_003.png)

Each cache type (edited answer, normal) would have the answer threshold bar and edited answer match tolerance. You can adjust the threshold to control when the caching will start caching for the answer, depending on how many answers exist for a given user question. For example, if you set the threshold to 5, the caching will not start until there exist 5 or more different answers to the given question. Setting the threshold to 1 would let NeuralSeek start caching as soon as it sees at least a single answer exists. Setting the value to 0 will disable caching completely.

The matching method (Exact Match, Fuzzy Match, etc.) is the method you can specify to tell NeuralSeek on how to perform the intent matching on the question.

There is also a more advanced matching method of ‘Exact Match, exact conversational context’ on the normal answers that would try to find the match if the consecutive conversation (e.g. one and the one after) both have the matching result, so that the match could be more correct in terms of how the conversation flow is occurring.

In terms of the edited answers, this ‘conversational context’ matching is not provided given that the edited answers should be more concise and based on a more substantial ground and thus should not rely on the conversational context.

###### Detecting changes in the original source

In order to make sure the cached answers retain the authenticity, every cached answers are fed into a hashing algorithm to generate a unique hash key, which is then compared with the original source to detect whether the original source has been altered or not.

If the hash keys do not match, NeuralSeek will notify users that the answers are not up-to-date with what’s found in the KnowledgeBase. This would happen when a particular answer is being used during the Seek time, so that the answer would be kept in check with the original.

![out of date data in kb](https://draft-wiki.neuralseek.com/assets/features/caching/image_004.png)

Users can then take a look at the outdated answer, and can either delete and reload it, or edit it and then mark it as current, so that NeuralSeek will be able to check it off from its outdated list.

![acknowledge of currency](https://draft-wiki.neuralseek.com/assets/features/caching/image_005.png)
> **Note**
> One other way the answer would be checked is when NeuralSeek is handling round trip logging. During that time, NeuralSeek would check which answers are getting frequently returned and also perform asynchronous checks with the KnowledgeBase to make sure they are up-to-date.

###### How do we know the answers are coming from cache?

You can check whether your query matched and returned the cached answer in the `Seek` tab. For example, this is an example of the answer returned from the cache.

![answer from cache](https://draft-wiki.neuralseek.com/assets/features/caching/image_006.png)

Next to the `Total Response Time`, you will see a label `Cached` which indicates that the answer came straight from the cache.

---

### Content Analytics

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/content_analytics/index>

**What is it?**

- NeuralSeek incorporates content analytics as a built-in feature, eliminating the need for additional code. With Content Analytics in NeuralSeek, users can effortlessly gather information about what users are searching for, assess the extent of documentation available on those topics, and evaluate documentation efficiency in addressing user queries.

**Why is it important?**

- Content Analytics are a powerful feature that enable insight on the performance of your corporate documentation. You can gain insights on where content is excellent, underperforming, nonexistent or seldom used - and inform the groups responsible for creating or updating that information on how better to allocate their time.

**How does it work?**

Two main scores are returned when a user asks a question to NeuralSeek:

- **Coverage Score:** This score represents the number of documents or sections of documents that discuss the subject area(s) of a question from NeuralSeek.
- **Confidence Score:** The confidence score represents the likelihood that the information found in the KnowledgeBase of NeuralSeek and presented as a response is correct. This probability is given as a percentage. Low scoring questions with low coverage scores tend to mean there is little or no documentation on the subject. Low scoring questions with high coverage tends to mean there are conflicting source documents.

---

### Conversational Context

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/convo_context/index>

**What is it?**

- NeuralSeek maintains context during each user interaction (conversation). When initiating a conversation, a session token is generated. Using this token and several Natural Language Processing (NLP) models, NeuralSeek tracks the topic of conversation to keep interactions focused and structured, allowing it to follow-up on questions that do not directly refer to the topic. In addition, these NLP models enable NeuralSeek to filter corporate knowledge topically by date to ensure that the information being returned is focused on the time period of the question.

**Why is it important?**

- Conversational Context allows for NeuralSeek to answer questions without users being specific about their language for every turn of the conversation. This enables higher containment rates in customer-facing conversations.

**How does it work?**

- NeuralSeek employs several NLP models to identify and extract meaning, intent, and main subject from user questions and generated responses. These then inform later turns of the conversation so that the proper context can be brought forward from the KnowledgeBase and used for answer formation. It also weighs heavily on caching and how the data can be cached. For example - The answer to a user question like "how does it work" depends heavily on the previous statements from a user. NeuralSeek requires that you pass an ID that can uniquely identify a user's session to enable this conversational context. The can be either or both the user_id and the session_id properties on the seek request. You do not need to maintain consistent id's over time for a specific actual person - the id must just be constant for the session that you wish to maintain context for.

---

### Dynamic Personalization

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/dynamic_pers/index>

**What is it?**

- One way NeuralSeek quickly ties into the users business is by automatically personalizing results based on information from their Customer Relationship Management (CRM) system. By analyzing user data such as past interactions, preferences, purchase history, and demographic information, NeuralSeek can dynamically adjust its outputs to match the specific needs and preferences of each individual user.

**Why is it important?**

- Personalized answers tend to engage users more, and can result in higher satisfaction and containment.

**How does it work?**

- This can be previewed in the Seek tab of the NeuralSeek UI, and in production environments users will pass the personalization details via our API as the REST call to when /seek is made.

---

### Entity Extraction

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/entity_extraction/index>

**What is it?**

- NeuralSeek has a feature called Extract which is a service to let users extract entities within a given user text. Users can also define their custom entities and provide descriptions for NeuralSeek to detect and extract entities that are defined by users. The service is provided with a REST endpoint which can be used by external applications such as virtual agents or chat bots to invoke it within their conversational flow to enhance their capabilities to detect entities within it.

**Why is it important?**

- Virtual Agents can define various entities, which may have values that need to be categorized into concepts or types that can play various roles during their request handling. For example, when a user types a question like:

> “I would like to buy a movie ticket.”

The term “movie ticket” could be categorized as “product” that the virtual agent might need to understand so that the agent could start a dialog that would continue like:
> “Sure, what kind of movie ticket do you want to purchase?”

Knowing that the user is interested in buying (intent) a movie ticket (product), the agent should perform an action of providing a list of the movies, as well as letting the user choose the date and time, and ultimately proceeding with billing and payment.

The inherent challenge in configuring virtual agents is to make sure these entities are accurately identified by providing various patterns, values, or an entity type, so that when those words appear in the conversation, such entities can be identified.

An example of that is how IBM Watson Assistant in dialog mode can define entity and its related values as such:

![wa entities](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_001.png)

In the above example, the entity ‘product’ would be identified in the dialog if the user mentioned these words such as ‘movie reservation,’ ‘movie ticket,’ or simply ‘ticket.’ Watson Assistant also provides fuzzy matching to match any incorrect spellings or slight deviation from these words to help it better cope with the request.

However, there are obviously clear limitations and caveats in doing this approach.

- You have to provide every possible value necessary for the bot to understand it as a certain type of entity. Anything out of the given value might not be categorized at all, or even categorized incorrectly.
- Maintaining a large set of entities and its subsequent values can be costly and time consuming.
- If you have to support multiple languages, you may need to provide all the possible values as legal vocabularies which can then be a pretty challenging feat.

**How does it work?**

- NeuralSeek’s Entity Extraction uses natural language processing to extract key entities that your virtual agent needs to understand, without requiring you to specify possible values or patterns and having the burden of constantly maintaining it.

###### Entity Extraction From Conversation

Let’s take a look at the above example of defining a movie ticket as a product. In the tab Extract, enter the same text of ‘I would like to buy a movie ticket’ and click the ‘Extract’ button.

![buying a movie ticket](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_002.png)

You will see NeuralSeek, without specifying anything, was able to identify the `movie ticket` as an entity of `product` and properly extracted it from the given string.

Moreover, you can ask the phrase in different languages, and NeuralSeek’s entity extraction will still work, without you doing anything!

![buying a movie ticket in Korean](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_003.png)

###### Custom Entities

In case there is a specific way that you need to categorize an entity, NeuralSeek provides a simpler and better way to define what your entity is, by using Custom Entity definition.

![custom entities](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_004.png)

Using this, Neural Seek can perform entity extraction in much more robust way:

![custom entities result](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_005.png)
![custom entities result](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_006.png)
![custom entities result](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_007.png)

And obviously, this single customer entity definition would work in other languages too!

![custom entities result](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_008.png)

###### Entity Extraction REST API

NeuralSeek’s entity extraction supports integration via REST API, so it makes calling the service easy with any external applications such as virtual agents or chatbots. It is easy to test its functionality by using API documentation located under the `Integrate` tab.

![entity extraction in REST API](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_009.png)

This will return the following JSON type response:

![entity extraction in REST API](https://draft-wiki.neuralseek.com/assets/features/entity_extraction/ee_image_010.png)

---

### Intent Categorization

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/intent_cat/index>

**What is it?**

- NeuralSeek can automatically categorize user input and questions into categories. These categories can be anything - products, organizations, departments, etc. Users can set up categories on the Configure Tab, by entering category names and descriptions. These will then be used to match user input into categories. User inputs that do not match any category, or that too closely match multiple categories will be placed in a default category called "Other". This default category cannot be modified.

**Why is it important?**

- Categorization is very useful at scaling NeuralSeek within an organization. By grouping intents into categories it can make things much easier for subject matter experts to quickly take action on their specific area of content. Categorization can be useful even outside the context of answering user questions - for example, in routing customer questions to the correct department or live agent. Categorization can be called directly via the API.

**How does it work?**

- User input is scored and bucketed based on the category title and description, and based on intents that have been manually moved into categories (self-learning). Once categorization is enabled, the Curate and Analytics screens will change to show groupings around categories. Categorization is not retroactive - meaning if you define a new category, we will not automatically re-run all old user input against the new categories. Users may move intents into categories manually through the Curate tab or the CSV download/edit features. The edits made will be used to train the system for future categorization events.

---

### Language Support

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/language/index>

**What is it?**

- NeuralSeek provides language translation that will let users call it to translate languages into different languages.

**Why is it important?**

- Any application that would need to translate a given text to another language can now use NeuralSeek to do it, rather than relying on other external translation services.

**How does it work?**

- Translation is provided as REST API, and can be tested on [NeuralSeek API documentation](https://api.neuralseek.com/).
- Message payload is in JSON format, and contains an array of `text` in certain language(s). Another attribute is `target` which specifies the target language the translation needs to be performed in. An example message would look something like this:

    {
        "text": [
        "NeuralSeek introduced several new features in July 2023, including streaming responses for web use cases, enhanced cross-lingual support, curate to CSV/upload curated QA from CSV, improved semantic match analysis, updated IBM WatsonX model compatibility, and AWS Lex round-trip monitoring."
        ],
        "target": "ko"
    },
> **Note**
> For more details on what language codes are supported, please refer to the **Multi Language Support** section below.

NeuralSeek would then translate the given text into the target language `ko` which is Korean:

    {
        "word_count": 39,
        "character_count": 289,
        "translations": [
            "NeuralSeek은 2023년 7월에 웹 사용 사례를 위한 스트리밍 응답, 향상된 교차 언어 지원, CSV에 대한 선별/선별 QA 업로드, 개선된 의미 일치 분석, 업데이트된 IBM WatsonX 모델 호환성 및 AWS Lex 왕복 모니터링과 같은 여러 가지 새로운 기능을 도입했습니다."
        ],
        "detected_language": "en",
        "detected_language_confidence": 0.9999967787054185
    }

You can also provide texts in different languages that can all be translated into the target language:

    {
        "text": [
        "soy un chico.",
        "나는 소년입니다.",
        "私は男の子です."
        ],
        "target": "en"
    }

Which will be translated into `en` which is English:

    {
    "word_count": 6,
    "character_count": 30,
    "translations": [
    "I am a boy.",
    "I am a boy.",
    "I am a boy."
    ],
    "detected_language": "es",
    "detected_language_confidence": 0.95
    }

##### Multi Language Support

**What is it?**

- NeuralSeek has several different language options available for understanding questions and delivering answers. These include English, Spanish, Portuguese, French, German, Italian, Arabic, Korean, Chinese, Czech, Dutch, Indonesian, Japanese, and more. These can be adjusted on the “Configure” section of the NeuralSeek console, or on the “Seek” endpoint. Please see the below table for the full list of supported languages.

**Why is it important?**

- Instead of having to train your virtual agents to understand various different languages, your question can be automatically converted into the response in the language of your choice.

**How does it work?**

- NeuralSeek will try to determine if the user is asking a question in a certain language (e.g. Spanish), and will try to convert the responses into the language that the user asked without any additional set ups.

###### Supported Languages
> **Languages and Language Codes**
>
> | Language | Code | Language | Code | Language | Code | Language | Code |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | English | en | Match Input | xx | Arabic | ar | Basque | eu |
> | Bengali | bn | Bosnian | bs | Bulgarian | bg | Catalan | ca |
> | Chinese (Simplified) | zh-cn | Chinese (Traditional) | zh-tw | Croatian | hr | Czech | cs |
> | Danish | da | Dutch | nl | Estonian | et | Finnish | fi |
> | French | fr | German | de | Greek | el | Gujarati | gu |
> | Hebrew | he | Hindi | hi | Hungarian | hu | Irish | ga |
> | Indonesian | id | Italian | it | Japanese | ja | Kannada | kn |
> | Korean | ko | Latvian | lv | Lithuanian | lt | Malay | ms |
> | Malayalam | ml | Maltese | mt | Marathi | mr | Montenegrin | cnr |
> | Nepali | ne | Norwegian Bokmål | nb | Polish | pl | Portuguese | pt-br |
> | Punjabi | pa | Romanian | ro | Russian | ru | Serbian | sr |
> | Sinhala | si | Slovak | sk | Slovenian | sl | Spanish | es |
> | Swedish | sv | Tamil | ta | Telugu | te | Thai | th |
> | Turkish | tr | Ukrainian | uk | Urdu | ur | Vietnamese | vi |
> | Welsh | cy |  |  |  |  |  |  |

Match Input Feature: NeuralSeek can understand and support conversations that are initiated in languages other than the ones listed through the Match Input Feature. On the “Seek” endpoint, click the dropdown for language navigation and click "Match Input".

---

### Language Identification

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/language_identification/index>

**What is it?**

- NeuralSeek provides a service that would analyze and identify the language of a given text.

**Why is it important?**

- Any application that would need to understand which language a given text is can now use NeuralSeek to do it, rather than relying on other external services.

**How does it work?**

- Language identification is provided as REST API, and can be tested on [NeuralSeek API documentation](https://api.neuralseek.com/). Message payload is in `text/plain` format, and contains `text` in certain languages. An example message would look something like this:

    이 언어는 어떤 언어입니까?

- NeuralSeek would then identify what language this is in, and returns the language code and the confidence score:

    [
        {
            "language": "ko",
            "confidence": 0.95
        }
    ]

###### Specifying a Language

If you would like to specify a certain target language that you want NeuralSeek to generate answers into, you can do so by specifying a language code (e.g. es) in the request when you are invoking `Seek`.

![lang selection](https://draft-wiki.neuralseek.com/assets/features/language_indentification/image-001.png)

The same can be achieved when you are invoking `Seek` using REST API. You can specify the language under the `options > language`.

###### Cross-language support for KBs

NeuralSeek offers robust multi-language support, allowing users to interact with a knowledge base (KB) in a different language than the one the KB is written in. This is particularly useful in scenarios where the knowledge base is in one language (e.g., English), but users need to query it in another language (e.g., Spanish).

**How It Works**

When a user queries the knowledge base in a different language, NeuralSeek handles the translation process seamlessly:

![query example](https://draft-wiki.neuralseek.com/assets/features/language_indentification/spanish-test.png)

1. **User Query in Native Language**: The user asks a question in their native language (e.g., Spanish).
2. **Translation to KB Language**: NeuralSeek translates the user's question into the language of the knowledge base (e.g., English).
3. **Querying the KB**: The translated question is used to search the knowledge base.
4. **Retrieving the Answer**: NeuralSeek retrieves the answer from the LLM in their native language.
5. **Delivering the Response**: The user receives the response in their native language.

> **Note: Example Scenario**
> Question in Spanish, KB in English
>
> 1. **User Query**: "¿Cuál es la capital de Francia?"
> 2. **Translate to English**: "What is the capital of France?"
> 3. **Query the English KB**: The system searches for "What is the capital of France?" in the English knowledge base.
> 4. **Retrieve Answer from the LLM in Spanish**: "La capital de Francia es París."
> 5. **Deliver Response**: "La capital de Francia es París."
> To configure NeuralSeek for multi-language support, follow these steps:
>
> **Step 1**: Configure the Knowledge Base Language
>
> ![kb](https://draft-wiki.neuralseek.com/assets/features/language_indentification/kb-language.png)
>
> - **Navigate to the Configure Tab**: Access the configuration settings of NeuralSeek.
> - **Select the Language of Your Knowledge Base**: Choose the language your knowledge base is written in (English, in this case).
> - **Save the Configuration**: Ensure that your settings are saved properly to apply the changes.
> **Step 2**: Testing Multi-Language Queries
>
> ![seek](https://draft-wiki.neuralseek.com/assets/features/language_indentification/french-example.png)
>
> - **Go to the Seek Tab**: Access the query interface of NeuralSeek.
> - **Enter a Question in Spanish**: Test the configuration by entering a question in Spanish, such as "¿Cuál es la capital de Francia?"
> - **Observe the Response**: NeuralSeek should translate the question, query the English knowledge base, and return the response in the desired language: "La capital de Francia es París."

---

### Multi-LLM Orchestration

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/multi_llm/index>

**What is it?**

Multimodal capabilities in large language models (LLMs) refer to their ability to process and generate content across multiple modalities, such as text, images, and even audio. This allows LLMs to understand and interact with the world in a more holistic and natural way, going beyond the traditional text-based interactions.

**Why is it important?**

Multimodal capabilities are crucial for a wide range of applications, particularly in areas like visual question answering, image captioning, and image-to-text generation. These capabilities enable LLMs to understand and reason about the world in a more comprehensive manner, allowing for more intuitive and user-friendly interactions.

**How does it work?**

Multimodal LLMs typically leverage techniques like transfer learning, where the model is first trained on a large corpus of text data, and then fine-tuned on datasets that combine text and images. This allows the model to learn the relationships between visual and textual information, enabling it to generate relevant and coherent responses to queries that involve both modalities.

---

### PII Detection

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/pii_detect/index>

**What is it?**

- NeuralSeek features an advanced Personal Identifiable Information (PII) detection routine that automatically identifies any PII within user inputs. It allows users to flag, mask, hide, or delete the detected PII.

**Why is it important?**

- Users can maintain a secure environment while providing accurate responses to user queries, ensuring compliance with data privacy regulations and protecting sensitive information.

**How does it work?**

- Common and well known PII detection is enabled by default in NeuralSeek. When you enter a PII information, for example, when you enter a credit card number in Seek:

![entering PII](https://draft-wiki.neuralseek.com/assets/features/pii_detect/credit-card.png)

In NeuralSeek, the question above will be logged and flagged as containing PII information and warns user about a potential risk.

![detecting PII](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_002.png)

The credit card number is also masked and removed, so that the data is protected from being viewed. The answers to these questions also indicate that they were generated from a question with PII in it, so that you can easily identify them.

![masking PII](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_003.png)

###### Defining a specific PII

However, this is what NeuralSeek does against common PII patterns, and there may be a specific PII that you would like to hide for your specific business needs. If you want to help NeuralSeek better detect and process PII for that, you can configure it under `Configure > Personal Identifiable Information (PII)` Handling in the top menu:

![defining pii](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_004.png)

How it works is based on an example sentence, and does not have to be an exact pattern or rules. For example, setting the example sentence as:

    My name is Howard Yoo and my blood type is O, and I live in Chicago.

For each PII element in that sentence, you can define the PII elements in that sentence delimited by comma as such:

    Howard Yoo, 0

So, next time, when somebody enters a PII matching the example as such:

    This is my blood type: A

NeuralSeek now detects that and masks the blood type that the user provided from being exposed:

![masking PII result](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_005.png)

###### Ignoring certain PII

You can also make NeuralSeek ignore certain PII by entering “No PII” to the element. For example, by setting the element as “No PII” with a given example sentence, NeuralSeek will not filter out the question even though it would contain an PII element:

![ignoring pii](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_006.png)

Therefore, when asked about a similar question, notice how dog’s name is now visible as not a PII information:

![ignoring pii result](https://draft-wiki.neuralseek.com/assets/features/pii_detect/pii_image_007.png)

The base reason to use this is that sometimes, NeuralSeek would mistake certain questions to be containing PII, even though the sentence may clearly not contain any such data. In that case, setting what not to consider as PII would be very helpful.

---

### Replay Feature

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/replay_feature/index>

**What is it?**

- The Replay feature in NeuralSeek enables users to revisit previously logged questions and their corresponding answers, semantic analysis, and the KnowledgeBase documentation used to generate the response at that point in time.

**Why is it important?**

- As documentation in our KnowledgeBase gets updated, questions on the Seek tab get updated to account for that new information. As a result, a user could ask a question identical to one asked previously and receive a completely different answer if the documentation has been significantly changed. If one wants to go back to a previous response and notice the changes that occurred in the documentation to see how the answers evolve, the Replay feature is very useful to get some insight.

**How does it work?**

- First, check to make sure that you have Corporate Logging enabled with an instance of Elasticsearch. You can find the settings for Corporate Logging underneatch the `Configure` tab.

![corporate-logging](https://draft-wiki.neuralseek.com/assets/features/replay_feature/corporate-logging.png)

- Navigate to the `Logs` tab on Neuralseek. There, you will find a log of all previously asked questions and answers from the `Seek` tab. Notice the small icon underneath the answer that resembles a clock turning backward. By clicking on it, you will be taken to the page as it appeared at that specific point in time.

![location](https://draft-wiki.neuralseek.com/assets/features/replay_feature/location.png)

![previous-answer](https://draft-wiki.neuralseek.com/assets/features/replay_feature/previous-answer.png)
![previous-context](https://draft-wiki.neuralseek.com/assets/features/replay_feature/previous-context.png)

- If the documentation used to answer the question has been updated, you can compare and contrast the results by asking the same question in the `Seek` tab.

![current-answer](https://draft-wiki.neuralseek.com/assets/features/replay_feature/current-answer.png)
![current-context](https://draft-wiki.neuralseek.com/assets/features/replay_feature/current-context.png)

---

### Real-time Logging

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/rt_logging/index>

**What is it?**

- Round-trip logging is a process that involves recording and storing all interactions between a user and a Virtual Agent. NeuralSeek supports receiving logs from Virtual Agents in order to monitor curated responses. This includes the user’s question, the Virtual Agent’s response, and any follow-up questions or clarifications.

**Why is it important?**

- The purpose of round-trip logging is to improve the Virtual Agent’s performance by alerting to content in the Virtual Agent that is likely out of date, because the source documentation has changed.

**How does it work?**

- The Source Virtual Agent is connected to NeuralSeek via the specific instructions per platform on the Integrate tab. Once connected, NeuralSeek will monitor for intents that are being used live in the Virtual Agent. Once per day NeuralSeek will search the connected KnowledgeBase and recompute the hash for the returned data. That hash will be compared to the hash of the answers stored, and if no match is found, an alert will be generated notifying that the source documentation has changed compared to the last Answer generation completed by the seek endpoint.

---

### Semantic Analytics

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/semantic_analytics/index>

**What is it?**

- NeuralSeek generates responses by directly utilizing content from corporate sources. In order to ensure transparency between the sources and answers, NeuralSeek reveals the specific origin of the words and phrases that are generated. Clarity is further achieved by employing semantic match scores. These scores compare the generated response with the ground truth documentation, providing a clear understanding of the alignment between the response and the meaning conveyed in source documents. This ensures accuracy and instills confidence in the reliability of the responses generated by NeuralSeek.

![what is semantic analytics](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/supported-integrations.png)

**Why is it important?**

- By being able to analyze how the answer generated would be originated from the actual facts given by the KnowledgeBase, users can analyze from which sources the responses actually originated from, and how much of the responses are directly coming from the knowledge versus how much of them are from LLM’s generated answer. This ensures accuracy and instills confidence in the reliability of the responses generated by NeuralSeek.

For example, NeuralSeek’s Seek will provide rich semantic analytics in terms of how well the response cover for the facts found in the KnowledgeBase (or cached generated answers) by color-coding the area of it in the response, visually linking it to the sources, and providing semantic analysis result to explain the key reasons behind the semantic match score given.

![why is it important](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_002.png)

**How does it work?**

- When NeuralSeek receives a question, it will first try to match for existing intents and answers, it will also try to search the underlying corporate KnowledgeBase and return any relevant passages from a number of sources. NeuralSeek will then either use these answers as-is directly, or use parts of the information to form a response using LLM’s generative AI capability.

###### Configuring Semantic Analytics

Configuration option for Semantic analysis is found under `Configure > Confidence & Warning` Thresholds . The semantic score model is enabled by default, but you can also disable it. You can also enable whether the semantic analysis should be used for confidence, and for reranking the search results from the knowledge base according to how much they semantically match. There are also sections for controlling how the analysis can apply penalties for missing key terms, search terms, or how frequent the sources are jumped (fragmented in the generated answer).

![configuring semantic analytics](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_003.png)
> **Question: How re-ranking the search result using semantic analysis can be helpful?**
> Having an option to re-rank the resulting KnowledgeBase search results can ensure the list of search results to appear in the order that corresponds better to the answer provided. That is because sometimes the search results returned from the KnowledgeBase do not align perfectly with the answer, and thus the provided URL of the resulting document can be misleading.

###### Using Semantic Analysis

In the ‘Seek’ tab of NeuralSeek, you can provide a question, and be given an answer from NeuralSeek. When enabling the ‘Provenance’, this will give you the color-coded portion of the response that were directly originated from those results.

![turning on provenance](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/answer_provenance_updated2.png)

Below the answer, you will see some of the key insights related to the answer, such as `Semantic Match score (in %)`, `Semantic Analysis`, as well as results coming from KnowledgeBase in terms of `KB Confidence`, `KB Coverage`, `KB Response Time`, and `KB Results`.

![scores](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_005.png)

Semantic Match % is the overall match ‘score’ that indicates how much NeuralSeek believes that the responses are well aligned with the underlying ground truth (from KnowledgeBase). The higher the % is, the more accurate and relevant the answer is based on the truth.

Semantic Analysis explains why NeuralSeek calculated the matching score given in a way that is easy for users to understand. By reading this summary, users are given a good understanding why the answer was given either a high or low score.

Knowledge confidence, coverage, response time, and results are all coming from the KnowledgeBase itself. These percentages indicate the level of confidence and coverage, signifying the extent to which the KnowledgeBase believes the retrieved sources are relevant to the provided question.

![kb results](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_006.png)

KnowledgeBase contexts are the ‘snippets’ of sources from the KnowledgeBase, based on the relevance of what it found within its data. Clicking one of them would reveal the found passage, and the color code matching that of the generated answer would be used to highlight the parts that were used.

![contexts](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_007.png)

Lastly, the `stump speech` that is defined in NeuralSeek’s configuration is shown and color-coded based on how much of it was used in the answer.

![stump speech](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_008.png)

If you are wondering where the Stump Speech is stored, you can find it in `Configure > Company / Organization Preferences` section:

![org preference](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/organization-prefs.png)

###### Setting the Date Penalty or Score Range

The resulting KnowledgeBase result does get affected by the configuration that you set for the corporate KnowledgeBase you are using with NeuralSeek. You can find these settings in `Configure > Corporate KnowledgeBase Details` section:

![org preference](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_010.png)

- Document score range dictates the range of possible ‘relevance scores’ that it will return as the result. For example, if the score range is 80%, the results will be of relevance score higher than 20% and equal or lower than 100%. If the score range is 20%, the relevancy score range would then be anything between 80% ~ 100%, respectively.
- Document Date Penalty, if specified higher than 0%, will start to impose penalty scores to reduce the relevancy based on how old the information is coming from. KnowledgeBase will try to find any time related information in the document and would reduce the score based on how old the time is, relative to current time.

![kb score and date penalty settings](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/image_011.png)

When the results say, '4 filtered by date penalty or score range', it means these settings came into play when retrieving relevant information from the KnowledgeBase.

###### Examples of Semantic Analysis

**High score example**

![example high score](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/high-example.png)

**Medium score example**

![example med score](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/medium-example.png)

**Low score example**

![example low score](https://draft-wiki.neuralseek.com/assets/features/semantic_analytics/low-example.png)

---

### Sentiment Analysis

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/sentiment/index>

---

title: Sentiment Analysis
tags:

- Feature
description: Discover NeuralSeek's Sentiment Analysis: Uncover emotional tones in text using advanced NLP. Enhance customer interactions by tailoring responses based on sentiment scores.

---

**What is it?**

- NeuralSeek's sentiment analysis is a feature that allows users to analyze the sentiment or emotional tone of a piece of text. It can determine whether the sentiment expressed in the text is positive, negative, or neutral. NeuralSeek's sentiment analysis is based on advanced natural language processing techniques and can provide valuable insights for businesses and organizations.

**Why is it important?**

- By being able to detect whether a user is negative or positive about certain questions, you can let the virtual agent use this information to provide more tailored services. For example, for a user who expresses negative sentiment, virtual agents might forward the session to human agents or assign higher priority so that more attention could be provided.

**How does it work?**

- NeuralSeek will run sentiment analysis on the user’s input text. Sentiment is returned as an integer between zero (0) and nine (9), with zero (0) being the most negative, nine (9) being the most positive, and five (5) being neutral.

> **Example of Sentiment Detection**
>
> When using REST API, for example, providing negative comments could trigger a low sentiment analysis score.
>
> {
> "question": "I don't like NeuralSeek",
> "context": {},
> "user_session": {
> "metadata": {
> "user_id": "string"
> },
> "system": {
> "session_id": "string"
> }
> }
> }
>
> Would yield a response with low sentiment score:
>
> {
> "answer": "String i'm sorry to hear that you don't like NeuralSeek. If you have any specific concerns or feedback, please let me know and I'll do my best to assist you.",
> "cachedResult": false,
> "langCode": "string",
> "sentiment": 3,
> "totalCount": 9,
> "KBscore": 3,
> "score": 3,
> "url": "https://neuralseek.com/faq",
> "document": "FAQ - NeuralSeek",
> "kbTime": 454,
> "kbCoverage": 24,
> "time": 2688
> }
>
> Notice the sentiment score of 3, which is in the low range of 0 - 10.
> On the other hand, if you express a positive sentiment as such:
>
> {
> "question": "I really love NeuralSeek. It's the best software in the world.",
> "context": {},
> "user_session": {
> "metadata": {
> "user_id": "string"
> },
> "system": {
> "session_id": "string"
> }
> }
> }
>
> The response will have a higher sentiment score:
>
> {
> "answer": "Thank you for sharing your positive feedback about NeuralSeek.  I cannot have personal opinions, but I'm glad to hear that you find NeuralSeek to be the best software in the world.",
> "cachedResult": false,
> "langCode": "string",
> "sentiment": 9,
> "totalCount": 9,
> "KBscore": 15,
> "score": 15,
> "url": "https://neuralseek.com/faq",
> "document": "FAQ - NeuralSeek",
> "kbTime": 5385,
> "kbCoverage": 8,
> "time": 7094
> }

---

### Table Understanding

**Source:** <https://draft-wiki.neuralseek.com/documentation/features/table_understanding/index>

**What is it?**

- Table Extraction, also known as `Table understanding`, pre-processes your documents to extract and parse table data into a format suitable for conversational queries. Since this preparation process is both **costly** and **time-consuming**, this feature is opt-in and will consume 1 seek query for every table preprocessed. Also, it should be noted that Web Crawl Collections are not eligible for table understanding, as the recrawl interval will cause excessive computing usage. Table preparation time takes several minutes per page.

**Why is it important?**

- Being able to understand data in tabular structure in documents and generating answers is an important capability for NeuralSeek in order to better find the relevant data for answering.

**How does it work?**

- To find table extraction, open up your instance of NeuralSeek and head over to the `Configure`.
- Select Table understanding

> **Warning: Note for users of lite/trial plans**
> To be able to access and use this feature you will have to contact [[email protected]](https://draft-wiki.neuralseek.com/cdn-cgi/l/email-protection#bbd8d7d4cedffbd8dec9ded9c9dad7d9d7cede95d8d4d6) with details of your opportunity and use case to be eligible.

---

## Reference — Integrate / Interface

### Integrate Tab Overview

**Source:** <https://draft-wiki.neuralseek.com/documentation/interface/integrate/index>

![integrate](https://draft-wiki.neuralseek.com/assets/ui/integrate/integrate.png)

**What is it?**

- The Integrate tab provides users with detailed instruction on integration of NeuralSeek with selected Virtual Agents, WebHook, API, or self-hosted LLM.

##### Integrations

- [KnowledgeBases](https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_knowledgebases)
- [Supported LLMs](https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_llms)
- [Supported Virtual Agents](https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_virtual_agents)

**Why is it important?**

- NeuralSeek provides comprehensive guidance on selected integrations which allows for a more user-friendly experience.

**How does it work?**

- The Integrate tab on NeuralSeek's user interface provides step-by-step instructions on how to connect to various virtual agent frameworks. Once connected, users are able to call on NeuralSeek through the chosen framework as either a "fallback intent" or other action.

  * **Custom Extension:** This contains the information to build a custom NeuralSeek extension within Watson Assistant.
  * **LexV2 Lambda:** Use AWS Lambda to send user input that routes the Lex FallbackIntent to NeuralSeek. Used in conjunction with AWS LexV2.
  * **LexV2 Logs:** How to enable Round-Trip Logging using LexV2 Logs, to monitor the usage of curated intents. The purpose of round-trip logging is to improve the virtual agent's performance by analyzing the data and identifying areas for improvement.
  * **Watson Logs**: How to enable Round-Trip Logging using Watson Logs, to monitor the usage of curated intents. The purpose of round-trip logging is to improve the virtual agent's performance by analyzing the data and identifying areas for improvement.
  * **WebHook**: This is the backbone of NeuralSeek, how users connect and communicate with the solution. One can make a call to this WebHook from any application (e.g. slack, servicenow, etc.) that can forward its question to it and receive answers from.
  * **API (REST)**: Where to find necessary information regarding how to invoke NeuralSeek's REST API, and navigate and test it right on its openAPI generated page. You can get examples of JSON message requests and responses, as well as JSON schema of the message payloads.
  * **KoreAI**: Activate Round-Trip monitoring for deployed NeuralSeek Intents. This feature enables NeuralSeek to continuously monitor the usage of its curated intents through KoreAI event Tasks. It will promptly alert you if any curated intents require updates due to changes in the associated KnowledgeBase documents.
  * **Console API**: This integration allows users to access debugging and monitoring features conveniently from within the NeuralSeek application, simplifying tasks such as error identification, performance analysis, and data insights without the need to switch between different tools or interfaces. It enhances the user experience by providing seamless access to the Console API's functionality within NeuralSeek's interface, streamlining development and monitoring tasks

##### API Keys

The API Keys page allows you to easily create API Keys for NeuralSeek that can be integrated with various other services.

To add an API Key, click on the Create ApiKey button and input the name you want to use for the Key in the pop-up prompt.

![addkey](https://draft-wiki.neuralseek.com/assets/ui/integrate/addkey.png)

After the key has been created, you will be able to see both the name of the key as well as the API code that you are able to copy immediately after creation.

![keycode](https://draft-wiki.neuralseek.com/assets/ui/integrate/keycode.png)

**If you don't copy the API key immediately after creating it, you won't be able to copy it again.** However, the key will continue to function normally for any services where it has already been defined.

If you want to delete an API Key and terminate its services, simply check off the checkbox next to a key's name and click on the Delete ApiKey button. This will remove the key from your instance.

![deletekey](https://draft-wiki.neuralseek.com/assets/ui/integrate/keydelete.png)

##### REST API

Virtual Agents, chatbots, and applications can send user questions and receive answers via NeuralSeek's REST API. In the `Integrate > API`, you can access its openAPI documentation that covers its service endpoints, and also can test its executions, as well as access the message schema. For more information, please refer to <https://api.neuralseek.com/>.

###### Example of curl command to invoke REST API

    curl -X 'POST' \
      'https://api.neuralseek.com/v1/test/seek' \
      -H 'accept: application/json' \
      -H 'apikey: xxxxxx07-xxxxxxbc-xxxxxxae-xxxxxxef' \
      -H 'Content-Type: application/json' \
      -d '{ "question": "I want to know more about NeuralSeek" }'

###### Example of JSON Response

    {
      "answer": "NeuralSeek is an AI-powered Answers-as-a-Service platform designed to enhance information sharing and customer support within virtual agents. It leverages a sophisticated Large Language Model (LLM) and a corporate KnowledgeBase to provide contextually relevant responses to user queries. NeuralSeek offers features such as fact-checking, data analytics, and step-by-step instructions to improve AI-generated responses. It can be integrated with virtual agents like IBM Watson Assistant or AWS Lex and used as an internal organization tool. NeuralSeek also provides training resources, demos, and support for users.",
      "ufa": "NeuralSeek is an AI-powered Answers-as-a-Service platform designed to enhance information sharing and customer support within virtual agents. It leverages a sophisticated Large Language Model (LLM) and a corporate KnowledgeBase to provide contextually relevant responses to user queries. NeuralSeek offers features such as fact-checking, data analytics, and step-by-step instructions to improve AI-generated responses. It can be integrated with virtual agents like IBM Watson Assistant or AWS Lex and used as an internal organization tool. NeuralSeek also provides training resources, demos, and support for users.",
      "intent": "FAQ-neuralseek",
      "category": 0,
      "categoryName": "Other",
      "answerId": 1706800601368,
      "warningMessages": [],
      "cachedResult": false,
      "langCode": "en",
      "sentiment": 5,
      "totalCount": 14,
      "KBscore": 53,
      "score": 26,
      "url": "http://documentation.neuralseek.com/overview/",
      "document": "NeuralSeek Overview",
      "kbTime": 7472,
      "kbCoverage": 56,
      "semanticScore": 26,
      "semanticAnalysis": "The answer has many jumps between source articles, which lowered the overall score.  Source jumping may indicate the meaning & intent of the source articles are not carrying thru to the answer.  The high standard deviation of the contributing sources increased the overall score.  The primary source does not match the full answer well, which decreased the total score.  The answer had the terms \"Service platform\" and \"leverages\" and \"checking\" that were not backed by a reference to source documentation, which decreased the final score significantly.",
      "semanticDetails": {
        "sourceJumps": 17,
        "stdDeviation": 78.71767414134023,
        "topSourceCoverage": 0.4640198511166253,
        "totalCoverage": 1.0397022332506203,
        "answerLength": 403,
        "longestPhrase": 41,
        "unattributedKeyTerms": [],
        "unattributedTerms": [
          "Service platform",
          "leverages",
          "checking"
        ],
        "unattributedNumbers": [],
        "missingKeyTerms": [],
        "missingTerms": []
      },
      "time": 13181,
      "thumbs": "https://api.neuralseek.com/v1/test/thumbs/1706800601368/1393218967/rate.svg"
    }

##### Supported Integrations

##### Guides

Here is a list of guides relevant to the Integrate tab.

---

### Supported KnowledgeBases

**Source:** <https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_knowledgebases>

##### Common Features

###### Relevance Tuning

This feature allows users to increase the response of a result when a query contains terms that match the attribute.

- We recommend connecting to **Watson Discovery**, **watsonx Discovery**, or **Elastic AppSearch** to utilize this feature.

###### Dynamic Filter Query

This feature allows for users to apply filters to their queries based on specific criteria in order to refine their search results.

- We recommend connecting to **Watson Discovery** or **watsonx Discovery** to utilize this feature.

###### Vector Search

This feature utilizes numerical representations of data, known as vectors, to conduct searches and identify relevance. In traditional leucine searches, documents are indexed based on keywords and queries are matched to documents containing those exact keywords. Vector searching utilizes semantic relationships to find related objects in the documentation that share similarity. This approach is ideal for broad or fuzzy queries, and improves the depth and breadth of searching and querying different types of data.

- We recommend connecting to **ElasticSearch** for document-oriented vector search.
- We recommend connecting to **Milvus** or **Pinecone** for flexible, and scalable data handling with high-performance vector search.
- Additonally, we recommend **Amazon Kendra** or **Amazon Bedrock** for managed vector search to aid in data chunking, embeddings, and indexing algorithm choices.

###### External Embedding Model Support

This feature utilizes an external embedding model to create vector embedding for indexing content. Upon query, the embedding model creates embeddings for that query, and uses them to query the database for similar vector embeddings for answer generation.

- We recommend connecting to **Pinecone** or **Milvus** to utilize this feature.

##### KnowledgeBase Capabilities
> **Abstract: Features Chart**
>
> | KnowledgeBase | Supported Search Types | Query Filters | Document Prioritization (Re-Sort) | Relevance Tuning | Dynamic Filter Querying | Full Document Retrieval | External Embedding Model Support |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | [Watson Discovery](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-about) | Lucene | checkmark | checkmark | checkmark | checkmark | checkmark | x |
> | [watsonx Discovery](https://cloud.ibm.com/docs/discovery-data?topic=discovery-data-about) | Lucene, Vector, Hybrid | checkmark | checkmark | checkmark | checkmark | checkmark | x |
> | [Elastic AppSearch](https://www.elastic.co/guide/en/app-search/current/index.html) | Lucene | checkmark | checkmark | checkmark | x | checkmark | x |
> | [ElasticSearch](https://www.elastic.co/elasticsearch) | Lucene, Vector, Hybrid | checkmark | checkmark | x | checkmark | checkmark | x |
> | [Amazon Kendra](https://aws.amazon.com/kendra/) | Vector (Managed) | checkmark | checkmark | x | *checkmark | x | x |
> | [Amazon Bedrock](https://aws.amazon.com/bedrock/) | Vector (Managed) | checkmark | checkmark | x | x | checkmark | x |
> | [OpenSearch](https://opensearch.org/) | Lucene | checkmark | checkmark | x | x | x | x |
> | [Pinecone](https://www.pinecone.io/product/) | Vector | checkmark | checkmark | x | x | checkmark | checkmark |
> | [Milvus](https://milvus.io/docs/overview.md) | Vector | checkmark | checkmark | x | x | checkmark | checkmark |
> *Kendra offers selective filtering support. Refer to the [Dynamic Filters Operator Reference](https://draft-wiki.neuralseek.com/guides/data/dynamic_filters/#operator_reference) for information on Amazon Kendra supported filters.

---

### Supported LLMs

**Source:** <https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_llms>

##### Overview

NeuralSeek supports LLMs from many providers, including:

- Amazon Bedrock
- Azure Cognitive Services
- Cloudflare
- Google Vertex AI
- HuggingFace
- OpenAI
- [together.ai](http://together.ai)
- [watsonx.ai](http://watsonx.ai)

In addition to any generic OpenAI-compatible endpoints.

**Supported LLM details by provider:**

(See full per-provider model tables on the source page. Providers covered: Amazon Bedrock, Azure Cognitive Services, Cloudflare, Google Vertex AI, HuggingFace, NeuralSeek, OpenAI, together.ai, watsonx.ai.)

> **Info**
> **LLM choice is available with NeuralSeek's BYOLLM (bring your own Large Language Model) plan.**
>
> LLMs can vary in their capabilities and performances. Some LLM can take up to 30 seconds and longer to generate a full response. Use caution when using in conjunction with a virtual agent platform that imposes a strict timeout.

##### Configuring an LLM
> **Warning**
> In order to configure an LLM, make sure that you have subscribed to the Bring Your Own LLM (BYOLLM) plan. All other plans will default to NeuralSeek's curated LLM, and this option will not be available.

1. In NeuralSeek UI, navigate to `Configure > LLM Details` page, using the top menu.
2. Click `Add an LLM` button.
3. Select the Platform and LLM Selection. (e.g. Platform: Self-Hosted, LLM: Flan-u2)
4. Click `Add`.
5. Enter the `LLM API key` in the LLM API Key input field.
6. Review the Enabled Languages (presented as multi-select)
7. Review the LLM functions available (presented as checkbox)
8. Click `Test` button to test whether the API key works.

> **Info**
> You must add at least one LLM. If you add multiple, NeuralSeek will load-balance across them for the selected functions that have multiple LLM's. Features that an LLM are not capable of will be unselectable. If you do not provide an LLM for a function, there is no fallback and that function of NeuralSeek will be disabled.

(Refer to source URL for the complete list of supported LLM model variants by provider.)

---

### Supported Virtual Agents

**Source:** <https://draft-wiki.neuralseek.com/documentation/interface/integrate/integrations/supported_virtual_agents>

| Virtual Agent Platform | Answer Curation | Round-Trip Monitoring | Fallback Search Template/Extension |
| --- | --- | --- | --- |
| [watsonx Assistant](https://www.ibm.com/products/watsonx-assistant) | checkmark | checkmark | checkmark |
| [AWS Lex](https://aws.amazon.com/lex/) | checkmark | checkmark | checkmark |
| [kore.ai](https://kore.ai/) | checkmark | checkmark | x |
| [Cognigy](https://www.cognigy.com/) | checkmark | x | x |
| [Azure AI Bot](https://azure.microsoft.com/en-us/products/ai-services/ai-bot-service) | checkmark | x | x |

- **What is Fallback Search?**

  * Fallback search is sometimes also known as "RAG". This allows you to helpfully answer customer/user questions where there is no intent/dialog mapping in your chatbot solution, providing an enhanced user experience.
  * We offer templates for some chatbot platforms to quick-start, eg watsonx Assistant and AWS Lex.
  * With the REST API, any platform that is able to utilize REST APIs are able to integrate with NeuralSeek.

- **What is Answer Curation?**

  * NeuralSeek offers an option to export questions and answers previously generated in a format compatible with some existing chatbot solutions, allowing users to "Curate" or import these generated answers directly into their chatbot service.

    +             Pros of this can be: Faster answers, reduced cost of language generation.

    +             Cons of this can be: Stagnant pools of answers that manually need updating. However, we do offer Round-trip monitoring to help with this task.

- **What is Round-Trip Monitoring?**

  * NeuralSeek will monitor the usage of NeuralSeek-curated intents that have been imported into your chatbot solution, and will inform you of any curated intents that may need to be updated, based on changes to relevant documents in the connected KnowledgeBase.

---

## Changelog

### Changelog

**Source:** <https://draft-wiki.neuralseek.com/documentation/changelog>

##### February - 2026

**New features**

- MultiMedia toolkit!! Generate and extend videos, merge or split multimedia, overlay audio on video
- mAIstro file browser for easy managment of documents.
- Microsoft Teams connector
- Improved handling and processing speed of huge files
- Updated LLM's.
- Email nodes to parse, modify, and create email with attachments

##### January - 2026

**New features**

- mAIstro run highlighting.
- Updated LLM's.
- Auto / title / auto description when saving a mAIstro agent.
- Support Subscriptions become available

##### December - 2025

**New features**

- Google custom search mAIstro node
- Delay mAIstro node
- S3 connector improvements
- Custom governance dashboards - add any dashboard to the Governance tab, powered by mAIstro agents

##### November - 2025

**New features**

- Hallucination removal improvements
- Custom Governance Guardrails - add pre and post LLM govenance agents to a Seek flow as guardrails to modify or alter anything in the Seek process
- Dynamic Personalization Agents - use mAIstro agents to do context personalization in Seek
- Chat SDK improvements

##### October - 2025

**New features**

- Recent / frequently used nodes menu bar for mAIstro
- Users dashboard
- Optimized max tonex calculation / context truncation
- OCR improvments for thruput / speed
- Charting nodes for mAIstro

##### September - 2025

**New Page!**

- The "Run" page released - Utilize Agents to build dynamic dashboards or small apps

**New features**

- Custom Governance - Build additional dashboards, backed by Agents you build in mAIstro. Show insights, charts, or something more unique....
- mAIstro debug timeline - A visual representation of where time is being spent on each action within an Agent.
- Webpage hosting - You can now use mAIstro to serve HTML files, making it trivial to build small apps.
- New LLM - Grok, and new connections to common LLMs in new providers.

##### August - 2025

**New features**

- New LLM's. GPT-5, and OpenAI open source models across several providers.
- New endpoint for logging external Agent runs into NeuralSeek Goverance.

##### July - 2025

**New features**

- New LLM's. Claude 4 and several OpenAI "o" series thinking models
- Increased runtime speed across mAIstro flows, improved performance of metaphone search, lots of bugfixes

##### June - 2025

**New features**

- MCP Server. Now you can consume any mAIstro agent via Model Context Protocol (MCP) <https://modelcontextprotocol.io/>
- Improve Prompt. Now in mAIstro, all LLM nodes have the ability to improve the prompt you have entered. Just click the magic wand...

##### May - 2025

**New features**

- mAIstro Speech Generation. Now you can generate audio/speech as part of an agent. See the new example templates
- Many New LLM's
- Numerous new mAIstro nodes
- Chat SDK enhancements

##### April - 2025

**New features**

- mAIstro Image Generation. Now you can generate images as part of an agent. See the new example templates
- NeuralSeek Curated LLM's - on byo-llm plans you can now select from leading commercial LLM's (including image generation) for a small increase in seek cost.
- New LLM's - llama 4
- Embed unique links - now when using the embed links feature, you can specify to embed only unique links
- Additional font support for document generation.
- Numerous improvements to existing mAIstro functionality.

##### March - 2025

**New features**

- mAIstro Agent Scheduler. Now you can schedule agents to run on a recurring basis, up to a year into the future.
- Instance Backup & Restore. Now you can fully back up and resore or migrate your instance. Move between plan types and clour providers or on-prem with click-button simplicity.
- new mAIstro connectors: SFTP, Box
- mAIstro Document conversion - convert any text-based document format to HTML
- mAIstro - HTML (document) translation. Now you can translate an HTML doc while retaining all the styles/markup. Couple that with document conversion for a powerful document translator. See the example agent.
- HAP allow-list and word additions - take greater control of the HAP filter.

##### February - 2025

**New features**

- mAIstro Logs & mAIstro replay. Now the governance tab will show all of the mAIstro runs, and if you have corporate logging enabled and configured - you can replay a mAIstro run, including all inputs, outputs, and step debugging. Effortlessly investigate your production agents after-the-fact!
- New LLM's: DeepSeek, AWS Nova
- mAIstro Updates:
  * LLM image preview. Now when sending an image to an LLM a thumbnail will be displayed in the debugger.
  * "Make NTL" node. Auto-generate NTL code as part of an agent (and auto-execute it if desired)
  * Powerpoint - We now support powerpoint ingest and automatic powerpoint generation

##### January - 2025

**New features**

- Agent Registry! Now Agents in mAistro can be cataloged into multiple registries, to allow for permissioned control and automatic selection of agents - either as single-shot or part of an automatically generated Agent Supervisor execution plan.
- mAIstro Updates:
  * Sandboxes! Now you can run arbitrary Javascript and Python code in our sandboxes in mAIstro. Generate code live from an LLM and then run it automatically in the sandbox.
  * Local Cache - load, search, access a local memory cache
  * Phonetic (metaphone) search for Loacal Cache

##### November - 2024

**New features**

- API Keys - now multiple api keys can be created and can be expired at any time. Individual key permissioning is coming soon
- Context keeping enhancements. We now natively support Hebrew, and added the ability to use an LLM for context keeping, opening the possibility to easily support any language. See platform Prefs / Context Detection
- Added support for Elastic's new "semantic" search type - in addition to lucene, hybrid, and vector
- mAIstro Updates:
  * Video! mAIstro now supports ingesting video via a new "Video Loop" node. You can easily pipeline a video to a multimodal LLM. See our example template "Video Loop"
  * PDF Loop - loop thru a pdf by page and automatically extract the text and take a snapshot image of the page for use in a multimodal LLM. Works great to get complicated information out of a business pdf. See the PDF Loop example template
  * OCR is now a callable node so you can use it as part of a backend process

##### October - 2024

**New features**

- mAIstro updates:
  * NTL now has code highlighting and rollup and a new editor
  * Code toolbox: a set of easy, single-node functions to:
  * extract generated code / sql / html from most LLMs,
  * protect, validate, and re-write SQL
  * Clean HTML and extract text
- HTML Cleanser updates. NeuralSeek automatically cleans scraped HTML docs in KB's that you connect. Now you can specify CSS selectors to remove on top of our normal cleansing, as well as disable the cleaner.
- Governance - Cost insights. Both sides of governance get a new tab that compares cost of your selected models across all other models we have capability and cost data for.
- DQL for elastic / watsonx discovery. We've brought our DQL interpreter over to elastic so you can pass DQL filters and easily do complicated filtering and lower migration risks when coming from discovery.

##### September - 2024

**New features**

- Multi-agent visual builder. Turn on multi-agent on the config tab and easily build category-driven multi-agent flows. No coding required! Every node of the multi-agent tree can have its own configuration (kb, llm's, everything) and guardrails. We've also unified the Seek and mAIstro sides of the house so you can call both from either api.
  * Each node can be of a traditional "seek" type, or a new mAIstro-lead node. mAIstro nodes send intents that hit them to a default action instead of creating a new intent. This lets you do disambiguation or focus the user onto capabilities you have enabled - like opening trouble tickets or other mAIstro-lead actions
  * Any intent can directly run a mAIstro flow. So for a question like "what's the weather like today" you could call out to a mAIstro flow instead of sending that to the traditional seek path/kb.
  * You can now directly add a new intent via the config and curate tabs.
  * Guardrails can run mAIstro flows. Min confidence, Min words and max words all can run custom mAIstro flows to give contextually & language -specific responses when those guardrails are hit.
- Chat! We've introduced a ChatGPT-like interface, as well as an SDK and embed code. You can quickly add a virtual agent to your website just by dropping in the embed code. The Chat SDK allows for drag & drop image and file operations - so you could easily build a bot that allows users to ask questions by providing images, such as "I want a refrigerator like this one"
- OCR! We soft-launched our OCR capabilities a few weeks back but never announced it. We now have OCR embedded into the system. When you use or document loader or upload a file into mAIstro - we'll automatically OCR any pdf's we find that are image-based and not text. You can also OCR image files. In addition we released a "dual ocr" template - basically showing you how to leverage and parralelize our OCR in addition to visual capabilities of a multi-modal model to do some amazing things for OCR'ing complex documents while keeping source formatting. This capability just blows away legacy OCR tools, with almost no tuning.
- Document Generation - we have built a new document generation behind the scenes, enabling greater capability in generating well-formatted PDF and Word files at scale.
- LLM's! LLama3.2 on both bedrock and [watsonx.ai](http://watsonx.ai). This is the first multi-modal model available on watsonx.
- new curated model! For PPA plans curated model 1.1 is available in all regions
- Logging updates. Seek Logs have moved into the Governance tab, and include even more details. Enable corporate logging for transactional replay - which has quickly become a must-have for business SME's
- new mAIstro nodes! We released an XML toolkit, as well as about a dozen other new nodes & connectors
- translation enhancements! Via the api you can override the max Chunk size we use - which can dramatically speed up translations for mid-length translations when using slow LLM's / inference platforms.

##### August - 2024

**New features**

- mAIstro Min Confidence - In a seek, when hitting your min confidence threshold, run a custom mAIstro flow. You can use this to simply create a contextually aware "I don't know note" - but can also use this to kick off a notification, or escalation or externals service call or ticket... Anything really.
- Semantic Insights - now on the "hallucinated terms" chart you can click on a term to directly allow-list items...
- Data Loader - Drag & drop files to our new loader, which leverages mAIstro to chunk/load docs. You can use any mAIstro function or integration, make rest calls, generate embeddings, automatically loop and chunk documents... We give an example loader for elastic/watsonx discovery.
- Governace for mAIstro!
  * Automatically track and provide insights for all mAIstro templates, filterable by template.
  * Flow insights helps track time spent across our parallel engine, helping you optimize flows and understand where they are spending the most of their time.
  * Token insights mirrors the Seek token insights tab, helping show token consumption, cost, and model comparison options for the LLM's used to power your mAIstro flows
- Seek Governance updates
  * Filter by filter... When using filters in seek, now you can automatically track governance by the applied filter.

##### July - 2024

**New features**

- New LLM's
  * Mistral-large on [watsonx.ai](http://watsonx.ai)
  * GPT-4o-mini on OpenAI.
- Streaming api endpoints for seek and mAIstro for watsonx assistant. These have the required content type in the openAPI spec. Note- at the moment streaming seek is not recommended as you can't use confidence scoring, nor get any payload fields like url. We'll be working on this with the Watson team.
New embedding models, and the ability to use a custom embedding model with NS intent detection and mAIstro
- Translation Improvements! NS translation is now up to 80% faster for large translations.
- NeuralSeek Hosted LLM's. When using a BYO-LLM plan we now provide a globally-hosted base LLM (mistral-7b) and purpose-built translation LLM for use with that plan for no additional charges, just the normal seek charge applies. THis should make it much easier to get started with NS.

##### June - 2024

**New features**

- New platforms supported:
  * vLLM / "generic" openAI-style inference engines. This allows you to plug-and play with many more on-prem and SaaS inference engines
  * Google Vertex is now supported, and we have added Gemini 1.5 pro and Flash. These models are quite good - Pro is on the same tier as GPT-4o, Claude3 Sonnet, and Mistral-Large
- mAIstro updates!
  * Built-in charting. With a compatible LLM you can ask for a chart to be generated as part of the output.
  * Formatted output - generate and display HTML and javascript
  * New "Raw" view - see the code behind charting and generated HTML
  * PDF output
  * Hover Menus! When on the visual builder, all of the nodes now will let you see and insert any secrets, user & system defined variables or generate a new variable. Makes building so much easier!
- Native integration to watsonx.governance. In mAistro, see our example template for how to configure this - it's really easy, just 3 steps. For watsonx.governance you just need an IAM API key, and from your "Production" deployment space in [x.gov](http://x.gov), under actions/model information we need your Evaluation datamart ID and Subscription ID. We'll send all of the NeuralSeek measures over to watsonx.governance so you can collect and govern them cross-instance and show a larger governance story. We also provide an open-ended integration in case you want to do something more custom.
- New mAIstro Integrations: (there are so many native functions and connectors in mAistro now we had to add a search feature!)
  * Jira
  * Trello
  * Github
  * Slack
  * AWS S3
  * Google/Bing/Yahoo/DuckDuckGo web searches.
- JSON Tools: We added JSON array filter and JSON Escape to make working with complicated payloads much easier inside mAIstro.
- Auto-Escaping. Now when using the mAIstro visual editor we will auto-escape any quotes. This should make building in mAIstro much easier for business users. We've found these updates plus the mAIstro auto-builder we released last month bring many usecases down to working "out of the box" with no additional modifications required to the autogenerated flows.
- Governance updates: We've enhanced the Token Insights tab, and added a new chart "Question Resolution" to the Overview tab to help track how many questions are hitting your minimum confidence threshold.
- The Logs tab now flags responses that had PII, HAP activation, and Prompt injection actions.

##### May - 2024

**New features**

- Virtual KB's! You can now use mAIstro to define a flow and use it as a virtual knowledgebase. Want to query multiple discovery instances at once? Easy. Elastic and DB2 and merge the results? Easy. Scrape a few webpages live and use those? Easy. See the new template in mAIstro for an example of how to configure this.
- Semantic Allow-list (Config / Semantic Model Tuning). Specify words or phrases to exclude from semantic penalties.
- Curate updates. Now answers generated by use of a filter will display the filter used during generation
- Custom Translations. Upload a training file via the API.

**mAIstro Features**

- Image processing / multimodal support in mAIstro. You can now grab images from the web, local file, or Google Docs and flow them thru LLM's that support image processing (Claude3, GPT-4, GPT-4o). See the new example template. And yes, you can power Seek based on images if you use this with the virtual KB!
- Auto-builder for mAIstro (SaaS - only). Have you been overwhelmed or afraid to try mAIstro? Not clear on how to build something? Now the welcome modal (and Load modal) will ask you to just describe your usecase, and then we'll auto-generate you a custom template.
- Snowflake connector! Now available in mAIstro

**Governance Features**

- Token Insights! A new module comes to NeuralSeek Governance (BYO-LLM plans only). Get cost insights on your LLM usage, metrics on generation speed, Cost comparisons to LLM's of similar capability. It's very compelling.
- Governance updates - now you can track cache and edited answer hit percentage from the Semantic Insights tab.

**New Models**

- Lots of new ones. GPT-4o, Mixtral8x-22, and more.

##### April - 2024

###### The launch of NeuralSeek Governance.

**New features**

- Remove Hallucinations - turn this on via the Configure tab under Semantic Scoring. As part of a Seek response, remove any sentence containing a key word (proper noun, entity) that is not contained in your source documentation.
- Proposals. Our take on versioning / configuration changes. You can now define a configuration as a "Proposal" and then call that proposal dynamically from the api or the Seek tab or Home tabs. This helps separate admin configuration from SME's testing proposed changes. It also lets you run multiple configs at once without passing a full override every time. Update a config, and click "Propose Changes" In addition, a new feature "Log Alternate Configs" - lets you block the curation of answers coming from these propsals, so you can test in isolation in a single instance.
Configuration Title and Description - as part of our Governance module and the launch of proposals we'll now as you for a configuration title and description on saving. These flow into the governance side of the house for explainability.
- Pinecone support - our initial release. more embedding model options are coming shortly.
- Milvus KB conector. So you can now do vector search into watsonx.data
- Return full Docs - we are rolling out the ability for you to return a full document instead of a passage. Currently release for Discovery and AppSearch. This way if you have carefully created or pre-snipped your documentation you can ensure the full document comes back.
- Performance improvements - some big updates on areas such as dynamic webscraping, context window splitting, and more.

**mAIstro Features**

- Secrets! - define variables on the Configure tab to hide them from normal mAIstro users. On prem users can also define variables at the OS level. Very useful for passing / hiding DB connection info.
- Context Loop - split a large block of text by tokens and loop over it. Ver useful for translating large documents, or sending big things thru a small LLM. See the Document Translation example in mAIstro
- Google Drive connector - pull from and write to a google drive
- Variable Loop - loop over an array of data

**Governance Features**

- Governance module. Our initial focus with this first release is a holistic view of RAG governance with time-based and Intent/Category filtering. We'll be rolling out many more additional capability in the weeks to come here. At launch we have:
  * Executive overview charts
  * Intent Analytics - what intents are trending, and how are they performing - model / document regression
  * System Performance - monitor your instance and compare to the NS universe
  * Semantic insights - What is the quality of the answers being generated
  * Documentation Insights - What documentation is most used, and how is it performing
  * Configuration Insights - monitor configuration changes and track churn over time

**New Models**

- LLama 3 - a big step up from llama 2 in terms of its ability to follow directions. In watsonx the context window is small, however so mixtral is still overall better.
- jais-13b-chat - in watsonx frankfurt, for Arabic usecases
- granite-7b-lab - This one seems better than the other granite models. Under the covers it's based on llama-2...
- Mistral-Large - similar and iteratively better than mixtral. not yet available on watsonx.

##### March - 2024

###### Explore is now renamed mAIstro and has gained a variety of new features.

**New features**

- Fully-custom RAG now available in NeuralSeek, offering simplicity via Seek and complexity via mAIstro, all out of the box and no-code required.

**mAIstro Features**

- Curate: Send your own Q&A into the curate, analytics, and log tabs.
- Categorize: Hook into the NS categorizer to get category and intent.
- Query Cache: Check for and return curated and edited answers.
- Semantic Score: Access the semantic scoring model from within a Maistro flow.
- Extract Grammar: Extract entities, nouns, dates, and more from text.
- Add Context: Recall the last turn of the conversation and inject the previous subject into text (for a KB or LLM call).
- Stop: Stop execution (useful for conditionals).
- Truncate by Tokens: Trim text by a set number of LLM tokens (use this to chop your KB documentation down to fit the LLM context window).

**New Models**

- Two new models added to watsonx in NeuralSeek: Granite 7B Japanese and Elyza Japanese Llama.

**Other Updates**

- New intro walk-me added to help new users get started on mAIstro.

##### February - 2024

**New features**

- Pre-LLM PII filtering/masking: Remove or mask personally identifiable information (PII) before sending queries to a Knowledge Base (KB) or LLM. Use pre-built elements or add your own using regular expressions.
- Prompt Injection detection: User input is scored against an internal model to identify potential prompt injection attempts. Problematic words are filtered out, and the entire input can be blocked based on the probability of prompt injection.
- Cross-language KB translation: When specifying a desired output language different from the KB language, user input can now be automatically translated into the KB language for better answers.
- Arbitrary Schemas for Explore: NeuralSeek Explore now supports arbitrary schemas, allowing users to hook it up to anything that sends a POST request, process it, and return it in the correct format. This feature enables dynamic rewording of messages based on saved context, chat history, or other criteria, providing a more personalized experience for users.
- Updates to Prompt Injection Mitigation: The try-it-out feature now displays scores of different phrases eligible to be removed from user input, enhancing the prompt injection detection capabilities.

**New Models**

- [watsonx.ai](http://watsonx.ai) introduces Granite-20b-5lang-instruct-rc model in tech preview, and several new models are added to Bedrock.

**Explore Enhancements**

- Guardrails such as Profanity Filter and Prompt Injection are now available in Explore.
- Several new example templates have been added to demonstrate these new features.
- Users can now modify the "WA Personalization" template provided in the examples on the Explore tab to dynamically reword messages flowing through Explore from Watson Assistant, offering a more personalized chatbot experience.
- The header parameters overrideschema and templatename in the explore API allow for easy configuration and customization of schemas in Explore, enabling seamless integration with various systems and applications.

##### January - 2024

**New features**

- Parallel "threaded" execution jobs introduced in Explore allow for faster execution of complicated templates, often outperforming custom-coding in Python.
- Enhancements to multi-turn seek: Users can now control the number of previous turns sent to the LLM for a more ChatGPT-style experience.
- Extract Enhancements:
  * Support for defining regex and keyword entity types, reducing workload on smaller/less capable LLMs and improving extraction speed.

**Explore Enhancements**

- Direct connectors to various databases including Postgres, Oracle, MySQL, MariaDB, MS SQL, and Redshift.
- System variables for injecting date, time, UUIDs, random numbers, etc.
- 'Extract' functionality added to Explore.
- Improved Explore OpenAPI template generator for easier integration with Watsonx Assistant.
- New templates available, including Custom RAG, Insurance Cause of Loss, and Conditional Logic.
- Option to specify the LLM to use in Explore LLM steps to avoid hitting rate limits and distribute the load effectively.

**Updates**

- Finer-grain user permissions: Users can now grant tab access while restricting write ability from specific tabs.
- All languages are now unlocked, allowing users to utilize NeuralSeek with any language supported by their chosen LLM.
- Stop/Cancel functionality for Seek and Explore during streaming responses.

##### December - 2023

**New features**

- Multilingual chain-of-thought prompting to enhance smaller LLMs like Llama and Granite for non-English languages.
- ElasticSearch / Watsonx Discovery Vector Search setup for hybrid or full vector search capabilities.
- KB ReRanker for custom result prioritization by field/tag and value lists.
- Profanity Filter implemented for multi-language profanity and hate speech filtering across all LLMs.
- Role-based access control for managing user permissions within the NeuralSeek UI.
- Explore enhancements:
  * OpenAPI spec generator for easy integration with Watson Assistant.
  * Inspector tool for debugging the Explore flow and variable states.
  * REST connector for making various HTTP requests and auto-parsing JSON into variables.
  * JSON to Variables stage for automatic variable creation from JSON input.
  * Output Variables formatting to match input parameters for seamless chaining in Explore.
  * Import/Export functionality for sharing templates across instances.
  * New functionality:
    + DB2 database connector
    + Table Prep (convert tables into natural language statements)
    + KB search filters
    + Stump for Seek (to sideload trusted data)
    + Regex
    + Several new example templates

**New integrations**

- Added Llama-2-chat Portuguese 13B to Watsonx Tech Preview.
- Release of Granite V2 in the model cards, offering improved performance over V1.

**Updates**

- [Watsonx.ai](http://Watsonx.ai) models transitioned to streaming for improved timeout handling.
- Enhanced error reporting in the UI for Knowledge Bases (KBs) to show more detailed configuration feedback.
- Semantic Scoring model improvements with lemmatization consideration for partial match scoring.
- Watsonx Discovery automatic API key generation for simplified access.

##### November - 2023

**New features**

- Explore:
  * Expanded NTL-based explore functionality with drag-and-drop simplicity for building Explore routines.
  * Added the ability to create and save templates within the UI.
  * Introduced variables for easy API calling by passing template name and variable values.
  * Dynamic Variable Setting - Introduce the ability to dynamically set variables within a chain or flow, capture outputs into variables for endless reuse, and return all variables via the API (multi-output capability).
  * Recursion / Chained Explore - Enabled the creation of small, repeatable task templates that can be called from other explore templates, with shared variable memory space across templates, facilitating the creation of complex flows with ease.
  * New functionality:
    + Math Equations - Implemented full graphing-calculator level equations, overcoming the LLM's limitations with math by allowing users to set variables with LLMs, perform calculations in the math node, and then provide correct answers back into the LLM.
    + Force Numeric - Added a feature to extract numbers from text, ensuring that when a number is requested from the LLM, a numeric response is provided.
    + Split - Automated the removal of document headers and footers, enabling users to extract the content they need with ease.
    + POST - Provided the ability to call any REST service to submit data or initiate a downstream process.
    + Email - Introduced the functionality to send the output of a flow or variable content directly via email.

**Updates**

- Semantic Details on Seek - Unveiled the math behind the semantic score through a new modal on the seek tab, previously exclusive to API/developer use.
- Enhanced context keeping and semantic score for improved abilities in Spanish.
- Rolled out a new Spanish micro-model to assist with Spanish NLP.
- Updated base weights and prompting to counter GPT's recent drifting.
- Semantic Scoring now has the ability to consider document title and URL, capturing unique words that may be missing in the document itself.
- Added the ability to pass a filter column for regression testing.

##### October - 2023

**New features**

- "Generate Data" options in Explore tab – Send to LLM, Table Understanding
- "Logs" tab - See history of questions/answers given
- Hyper-personalization (Corporate document filtering)
- Corporate Logging - Connect NeuralSeek to an ElasticSearch instance to log everything around Seek, updates, edits, changes
- Configuration Logs - History of changed settings
- Enhancements to Explore:
  * "Seek" data
  * PII removal
  * Table Understanding

**New integrations**

- Elastic Search integration
- Multi-Turn Conversation Generation for Cognigy
- Mistral 7B Model support

**Updates**

- Released On-Prem "Flex" plan
- Added version numbering to "Integrate" tab sidebar
- Seek tab - "Show generated" option when the minimum confidence is not met

##### September - 2023

**New features**

- Explore: An Open-Ended Retrieval Augmented Generation Playground
- Vector Similarity for Intent Matching

**New integrations**

- [Kore.ai](http://Kore.ai) Round Trip Monitoring
- IBM watsonx Granite Models Supported
- AWS Bedrock Integration / Models Supported
- Llama 2 Chat Model Support
- OpenSearch Integration
- HuggingFace Integration for Supported Models

**Updates**

- Refinements to Vector Similarity Matching

##### August - 2023

**New features**

- BYO-LLM plans – IBM watsonx language translation
- Option for summarization of document passage results from KB
- Option for Link Summarization of NeuralSeek Results, 1-5 Result Links
- 'Bring Your Own' Large Language Model (BYO-LLM) cards – ability to use multiple LLMs for a specific task

**New integrations**

- IBM Watson Assistant Dialog Multi-Turn Conversation Templates
- AWS Kendra Integration
- AWS Lex Multi-Turn Conversation Generation Templates

**Updates**

- New 'Seek' Parameter Call to Indicate LLM Preference
- Ability to set specific language on each LLM – e.g., "use THIS model for Spanish Seek / Translation"

##### July - 2023

**New features**

- Slot Filler - Ability to auto-fill slots when gathering information
- Offline spreadsheet editing with upload to Curate tab
- ConsoleAPI under Integrate tab
- Answer Streaming – users can now enable streaming responses from NeuralSeek with supported LLMs
- Translate Endpoint
- Curate to CSV / Upload Curated QA from CSV
- On-Prem deployment support
- New 'Identify Language' Endpoint
- Entity Extraction feature - Custom Entity Creation

**New integrations**

- IBM watsonx Model Compatibility
- AWS Lex Round-Trip Monitoring

**Updates**

- KnowledgeBase translation updated – questions now get translated to KnowledgeBase source language for summarization
- Cross-lingual support when using language code "xx" (Match Input) enhanced
- Semantic Match Analysis to describe the logic for the Semantic Score enhanced

##### June - 2023

**New integrations**

- IBM watsonx (LLM) connector

**Updates**

- AWS Partnership Announcement
- Improvements to Caching
- Confidence and Coverage Score Graphs added to Curate tab

##### May - 2023

**New features**

- Analytics API endpoint
- Table Extraction model to enable answers from tabular data

**Updates**

- Data Cleanser for non-HTML enabled

##### April - 2023

**New features**

- New plan - 'Bring Your Own' Large Language Model (BYO-LLM)
- Semantic Score Model, Improved Provenance and Semantic Source Re-Rank

**New integrations**

- Curate answers to [Kore.ai](http://Kore.ai), Cognigy, AWS Lex

**Updates**

- IBM Frankfurt (FRA) data center availability
- IBM Sydney (SYD) data center availability

##### March - 2023

**New features**

- Personal Identifiable Information (PII) Detection
- Sentiment Analysis
- Source Document Monitoring and Answer Regeneration

**New integrations**

- Watson Assistant Round-Trip Logging

**Updates**

- User-specified input length enabled

##### February - 2023

**New features**

- Personalization of generated answers

**New integrations**

- Auto-Build Watson Assistant Multi-Step Action

**Updates**

- Additional languages enabled (Chinese, Czech, Dutch, Indonesian, Japanese)
- Enhanced API to allow run-time modification of all parameters
- KB tuning parameters enabled
- Large Language Model (LLM) tuning

---
