from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_research_run():
    r = client.post("/api/research/run", json={"question":"How do AI agents use tools?", "depth":"standard"})
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "completed"
    assert len(body["plan"]) >= 3
    assert len(body["claims"]) >= 3
    assert body["review"]["citation_coverage"] == 100
