from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .models import ResearchRequest
from .orchestrator import run_research
from .memory import all_memory

app = FastAPI(title="ResearchPilot AI", version="1.0.0", description="Multi-agent research and intelligence API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health():
    return {"status": "ok", "service": "researchpilot-api", "mode": "deterministic-demo"}

@app.post("/api/research/run")
def research_run(request: ResearchRequest):
    return run_research(request)

@app.get("/api/research/demo")
def demo():
    return run_research(ResearchRequest(question="How are AI agents changing software engineering?", depth="standard"))

@app.get("/api/memory")
def memory():
    return {"items": all_memory()}
