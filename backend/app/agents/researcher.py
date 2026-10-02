from ..models import Source

def research(question: str, depth: str) -> list[Source]:
    q = question.strip()
    return [
        Source(id="src-001", title="NIST AI Risk Management Framework", publisher="NIST", url="https://www.nist.gov/itl/ai-risk-management-framework", type="Framework", credibility=97, snippet="A framework for managing risks across the AI lifecycle, useful for evaluating trustworthy system design."),
        Source(id="src-002", title="ReAct: Synergizing Reasoning and Acting in Language Models", publisher="arXiv", url="https://arxiv.org/abs/2210.03629", type="Research paper", credibility=90, snippet="Research describing an approach that interleaves reasoning and actions for language-model agents."),
        Source(id="src-003", title="Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks", publisher="arXiv", url="https://arxiv.org/abs/2005.11401", type="Research paper", credibility=91, snippet="Foundational RAG work connecting generation with retrieved external knowledge."),
        Source(id="src-004", title="Attention Is All You Need", publisher="arXiv", url="https://arxiv.org/abs/1706.03762", type="Research paper", credibility=94, snippet="The Transformer architecture paper underpinning modern language-model systems."),
    ]
