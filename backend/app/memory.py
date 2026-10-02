from .models import ResearchMemory

_MEMORY = [
    ResearchMemory(id="mem-001", topic="AI agents", insight="Agentic systems decompose work into planning, tool use, state and review steps.", confidence=91),
    ResearchMemory(id="mem-002", topic="software engineering", insight="Reliable AI engineering benefits from deterministic tests, observability and human approval for consequential actions.", confidence=94),
    ResearchMemory(id="mem-003", topic="research", insight="Source provenance and claim-level citation coverage are important for trustworthy synthesis.", confidence=93),
]

def search_memory(question: str, limit: int = 3) -> list[ResearchMemory]:
    tokens = set(question.lower().split())
    scored = []
    for item in _MEMORY:
        score = len(tokens.intersection(set(item.topic.lower().split())))
        scored.append((score, item))
    return [item for _, item in sorted(scored, key=lambda x: x[0], reverse=True)[:limit]]

def add_memory(item: ResearchMemory) -> None:
    _MEMORY.append(item)

def all_memory() -> list[ResearchMemory]:
    return list(_MEMORY)
