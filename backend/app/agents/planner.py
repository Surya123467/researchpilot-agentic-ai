from ..models import ResearchTask

def plan(question: str, depth: str) -> list[ResearchTask]:
    tasks = [
        ResearchTask(id="task-1", title="Landscape", objective=f"Map the main concepts and current landscape around: {question}", status="planned"),
        ResearchTask(id="task-2", title="Evidence", objective="Identify evidence, measurable observations, and source provenance.", status="planned"),
        ResearchTask(id="task-3", title="Trade-offs", objective="Compare benefits, limitations, risks, and implementation considerations.", status="planned"),
    ]
    if depth == "deep":
        tasks.append(ResearchTask(id="task-4", title="Open questions", objective="Identify unresolved questions and areas requiring further primary-source research.", status="planned"))
    return tasks
