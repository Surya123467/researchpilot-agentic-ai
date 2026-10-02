from typing import Literal
from pydantic import BaseModel, Field

class ResearchRequest(BaseModel):
    question: str = Field(min_length=8, max_length=1000)
    depth: Literal["quick", "standard", "deep"] = "standard"

class Source(BaseModel):
    id: str
    title: str
    publisher: str
    url: str
    type: str
    credibility: int = Field(ge=0, le=100)
    snippet: str

class Claim(BaseModel):
    id: str
    text: str
    source_ids: list[str]
    confidence: int = Field(ge=0, le=100)
    stance: Literal["supporting", "mixed", "open"] = "supporting"

class ResearchTask(BaseModel):
    id: str
    title: str
    objective: str
    status: Literal["planned", "completed"]

class ResearchMemory(BaseModel):
    id: str
    topic: str
    insight: str
    confidence: int

class ResearchReport(BaseModel):
    title: str
    executive_summary: str
    key_findings: list[str]
    claims: list[Claim]
    limitations: list[str]
    next_questions: list[str]

class ResearchRun(BaseModel):
    run_id: str
    question: str
    depth: str
    status: Literal["completed", "review_required"]
    plan: list[ResearchTask]
    sources: list[Source]
    claims: list[Claim]
    memories_used: list[ResearchMemory]
    report: ResearchReport
    review: dict
    trace: list[str]
