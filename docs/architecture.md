# ResearchPilot Architecture Notes

The workflow is intentionally explicit. Each stage accepts structured input and emits structured output. This makes the system easier to test and explain than a single free-form agent.

## State

A run contains: question, depth, plan, sources, claims, memories, report, review and trace.

## Production evolution

1. Replace deterministic researcher with a search connector.
2. Add document ingestion and chunking.
3. Store embeddings in pgvector.
4. Add durable LangGraph state/checkpointing.
5. Add an LLM gateway with retries, model routing and cost tracking.
6. Add evaluation sets for retrieval precision, citation coverage and factuality.
7. Add authentication, rate limiting, audit logs and observability.
