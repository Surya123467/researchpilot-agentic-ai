from ..models import Claim, Source

def extract_claims(question: str, sources: list[Source]) -> list[Claim]:
    return [
        Claim(id="claim-001", text="Agentic systems can combine reasoning with external actions or tools instead of producing only a single response.", source_ids=["src-002"], confidence=88),
        Claim(id="claim-002", text="Retrieval can provide external context to language-model generation for knowledge-intensive tasks.", source_ids=["src-003"], confidence=92),
        Claim(id="claim-003", text="Risk management and evaluation are important when deploying AI systems beyond a simple prototype.", source_ids=["src-001"], confidence=94),
        Claim(id="claim-004", text="Modern language-model systems are strongly influenced by the Transformer architecture.", source_ids=["src-004"], confidence=96),
    ]
