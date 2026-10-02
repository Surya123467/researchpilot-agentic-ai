from uuid import uuid4
from .agents.planner import plan
from .agents.researcher import research
from .agents.evidence import extract_claims
from .agents.synthesizer import synthesize
from .agents.reviewer import review
from .memory import search_memory, add_memory
from .models import ResearchRequest, ResearchRun, ResearchMemory

def run_research(req: ResearchRequest) -> ResearchRun:
    trace = []
    tasks = plan(req.question, req.depth); trace.append("PlannerAgent: research plan created")
    sources = research(req.question, req.depth); trace.append(f"ResearcherAgent: {len(sources)} candidate sources collected")
    memories = search_memory(req.question); trace.append(f"MemoryAgent: {len(memories)} prior memories retrieved")
    claims = extract_claims(req.question, sources); trace.append(f"EvidenceAgent: {len(claims)} claims normalized with provenance")
    report = synthesize(req.question, claims); trace.append("SynthesizerAgent: structured report drafted")
    review_result = review(report, claims); trace.append(f"ReviewerAgent: citation coverage {review_result['citation_coverage']}%")
    for t in tasks: t.status = "completed"
    if review_result["approved"]:
        add_memory(ResearchMemory(id=f"mem-{uuid4().hex[:8]}", topic=req.question[:60], insight=report.key_findings[0], confidence=review_result["confidence"]))
        trace.append("MemoryAgent: key finding stored for future runs")
    return ResearchRun(run_id=uuid4().hex[:12], question=req.question, depth=req.depth, status="completed" if review_result["approved"] else "review_required", plan=tasks, sources=sources, claims=claims, memories_used=memories, report=report, review=review_result, trace=trace)
