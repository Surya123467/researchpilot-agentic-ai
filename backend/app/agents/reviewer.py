from ..models import Claim, ResearchReport

def review(report: ResearchReport, claims: list[Claim]) -> dict:
    cited = sum(bool(c.source_ids) for c in claims)
    coverage = round((cited / len(claims)) * 100) if claims else 0
    issues = []
    if coverage < 80:
        issues.append("Some claims lack source provenance.")
    if not report.limitations:
        issues.append("Limitations section is missing.")
    return {"approved": not issues, "citation_coverage": coverage, "confidence": round(sum(c.confidence for c in claims) / len(claims)) if claims else 0, "issues": issues}
