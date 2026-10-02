# Interview talking points

## 30-second pitch
ResearchPilot is a multi-agent research and intelligence system. Instead of asking one model to do everything, I split the workflow into planning, research, memory retrieval, evidence normalization, synthesis and review. Each stage has a clear contract, and the final report exposes source provenance and confidence.

## Why this is agentic
The system has stateful task decomposition and sequential specialist stages. Agents contribute intermediate artifacts that influence downstream decisions rather than simply generating independent chat messages.

## Biggest production concern
Grounding. A polished answer is not enough; the system needs reliable retrieval, provenance, claim-level evaluation and human review for high-impact outputs.
