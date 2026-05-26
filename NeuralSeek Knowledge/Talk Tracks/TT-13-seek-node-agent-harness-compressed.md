# TT-13. "The seek node = the agent harness, compressed"

## Category
Explaining how NeuralSeek works to non-technical people

## Punchline
The agent harness is defined as "the wiring that connects the models to the tools and manages the loop... it pulls the model into messaging platforms, manages execution, packages workflows as repeatable skills."

## NeuralSeek tie-in
The seek node IS the agent harness — except one line of NTL equals ~6,000 lines of TypeScript that Anthropic and OpenAI hand-build. From 07-product-talking-points.md: "When you drag and drop one seek node, you're dragging and dropping a governed, guardrailed RAG pipeline end-to-end — PII removal, query check, cache check, profanity filter, prompt injection protection, context addition, RAG, LLM call, semantic scoring, logging, curation."

## Use
Technical buyer demo, especially when they've seen Claude Code or Cursor. "They built an agent harness for coding. We built one for regulated enterprise — and ours is a drag-and-drop, not 6,000 lines of code."
