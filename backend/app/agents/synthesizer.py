from ..models import Claim, ResearchReport

def synthesize(question: str, claims: list[Claim]) -> ResearchReport:
    return ResearchReport(
        title=f"Research brief: {question}",
        executive_summary="The evidence suggests that effective AI research and intelligence systems benefit from explicit decomposition, retrieval, provenance, and review rather than relying on a single opaque generation step.",
        key_findings=[
            "Agent workflows become easier to reason about when planning, retrieval, synthesis and review have explicit responsibilities.",
            "RAG provides a mechanism for grounding generation in retrieved external context.",
            "Source provenance and claim-level confidence make a research report easier to audit.",
            "Evaluation and risk controls should be treated as part of system design, not as a final add-on.",
        ],
        claims=claims,
        limitations=[
            "This local demo uses a deterministic source set rather than live web search.",
            "The findings are a demonstration of the orchestration pipeline and should not be treated as a comprehensive current literature review.",
        ],
        next_questions=[
            "Which primary sources should be added for the target research domain?",
            "What evaluation dataset should be used to measure retrieval and synthesis quality?",
            "Which workflow steps require human approval in a production deployment?",
        ],
    )
