# ResearchPilot AI

ResearchPilot AI is a portfolio-grade multi-agent research and intelligence platform designed to demonstrate **Agentic AI orchestration**, source retrieval, evidence synthesis, memory, structured reporting, and human review.

> **Important:** Mock mode is the default. The application runs locally without paid API keys. Optional LLM integration can be added through an OpenAI-compatible endpoint.

## What it demonstrates

- Multi-agent workflow orchestration
- Planner → Researcher → Evidence → Synthesizer → Reviewer → Report pipeline
- Source collection and evidence cards
- Source quality / confidence signals
- Research memory and reusable findings
- Structured research reports
- Human review before final publication
- FastAPI backend + React/TypeScript frontend
- Optional OpenAI-compatible LLM provider
- Docker Compose
- Tests and CI

## Architecture

```text
                    ┌──────────────────────┐
                    │   Research Question   │
                    └──────────┬───────────┘
                               │
                        ┌──────▼──────┐
                        │    Planner  │
                        └──────┬──────┘
                               │ research plan
             ┌─────────────────┼──────────────────┐
             │                 │                  │
       ┌─────▼─────┐     ┌─────▼──────┐    ┌─────▼──────┐
       │ Researcher│     │   Memory   │    │  Evidence  │
       │  Agents   │     │   Agent    │    │  Collector │
       └─────┬─────┘     └─────┬──────┘    └─────┬──────┘
             └─────────────────┼──────────────────┘
                               │ evidence
                        ┌──────▼──────┐
                        │ Synthesizer │
                        └──────┬──────┘
                               │ draft
                        ┌──────▼──────┐
                        │   Reviewer  │
                        └──────┬──────┘
                               │ approved report
                        ┌──────▼──────┐
                        │   Report    │
                        │  Generator  │
                        └─────────────┘
```

## Agents

### Planner Agent
Breaks a broad question into focused research tasks and identifies what evidence is needed.

### Researcher Agent
Runs source-search tasks. In mock mode it uses a deterministic local knowledge set; with an optional provider, this layer can be connected to a search/retrieval service.

### Evidence Agent
Normalizes findings, attaches provenance, extracts claims, and detects supporting/contradicting evidence.

### Memory Agent
Stores reusable research notes and retrieves relevant prior context for subsequent runs.

### Synthesizer Agent
Combines evidence into a structured answer while separating facts, analysis, and open questions.

### Reviewer Agent
Checks citation coverage, unsupported claims, confidence, and report completeness before publication.

## Tech stack

- Frontend: React, TypeScript, Vite, CSS
- Backend: Python, FastAPI, Pydantic
- Agent orchestration: explicit state graph inspired by LangGraph patterns
- Optional LLM: OpenAI-compatible API
- Storage: local JSON memory in demo mode
- Containers: Docker + Docker Compose
- Testing: pytest + frontend build

The implementation deliberately keeps the orchestration understandable rather than hiding the entire system behind a single agent call.

## Run locally

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

### Docker

```bash
docker compose up --build
```

Frontend: `http://localhost:5173`
Backend: `http://localhost:8000`
API docs: `http://localhost:8000/docs`

## Optional LLM

Copy the environment template:

```bash
cp backend/.env.example backend/.env
```

Set an OpenAI-compatible endpoint and key if desired. The UI continues to work in deterministic mock mode when no key is configured.

## API

- `GET /health` — health check
- `POST /api/research/run` — execute a research workflow
- `GET /api/research/demo` — return a demo research run
- `GET /api/memory` — inspect saved research memory

Example:

```bash
curl -X POST http://localhost:8000/api/research/run \
  -H 'Content-Type: application/json' \
  -d '{"question":"How are AI coding agents changing software engineering?","depth":"standard"}'
```

## Interview explanation

**Why multiple agents?** Different stages have different responsibilities: planning, retrieval, evidence handling, synthesis, and review. This makes the workflow observable and gives each stage a clear contract.

**Why human review?** Research systems can produce plausible but weakly supported statements. The reviewer stage creates a checkpoint for citation coverage and confidence before a report is considered final.

**How would you productionize it?** Replace local memory with PostgreSQL/pgvector, add a real web/search connector, add durable workflow state, authentication, rate limits, tracing, evaluation datasets, and a real LLM gateway. The agent contracts can remain largely unchanged.

## Project structure

```text
researchpilot-agentic-ai/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── orchestrator.py
│   │   ├── memory.py
│   │   └── main.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── data/
│   │   ├── lib/
│   │   └── types/
│   └── package.json
├── docs/
├── docker-compose.yml
└── README.md
```

## Status

Portfolio project / local demo. The default workflow is deterministic so it can be demonstrated without external API dependencies.
