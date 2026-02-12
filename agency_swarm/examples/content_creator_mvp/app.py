"""QA scoring endpoint and campaign studio wireframe."""

from __future__ import annotations

import re
from dataclasses import dataclass

from .schemas import ComplianceRubric


@dataclass
class CampaignSubmission:
    """Payload scored by compliance rubric."""

    title: str
    body: str


def score_campaign_submission(submission: CampaignSubmission, rubric: ComplianceRubric | None = None) -> dict:
    """Return QA rubric score and violation details."""
    rubric = rubric or ComplianceRubric()
    body_lower = submission.body.lower()
    violations: list[str] = []

    for claim in rubric.banned_claims:
        if claim.lower() in body_lower:
            violations.append(f"banned_claim:{claim}")

    for term in rubric.mandatory_terms:
        if term.lower() not in body_lower:
            violations.append(f"missing_term:{term}")

    cta_hits = len(re.findall(r"\b(buy now|sign up|learn more|shop now)\b", body_lower))
    if cta_hits > rubric.max_cta_count:
        violations.append(f"cta_count:{cta_hits}")

    readability = max(0, 100 - len(submission.body) // 8)
    if readability < rubric.readability_floor:
        violations.append(f"readability:{readability}")

    score = max(0, 100 - 20 * len(violations))
    return {
        "score": score,
        "status": "pass" if score >= 80 else "fail",
        "violations": violations,
        "rubric": rubric.model_dump(),
    }


def build_campaign_studio_wireframe() -> str:
    """Simple HTML wireframe with approval states."""
    return """<!doctype html>
<html>
  <head>
    <meta charset=\"utf-8\" />
    <title>Campaign Studio Wireframe</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 24px; }
      .board { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
      .column { border: 1px solid #ddd; border-radius: 8px; padding: 12px; background: #fafafa; }
      .card { border: 1px solid #ccc; border-radius: 6px; padding: 8px; margin: 10px 0; background: #fff; }
      .pill { display: inline-block; font-size: 12px; padding: 2px 8px; border-radius: 999px; background: #eef; }
    </style>
  </head>
  <body>
    <h1>Campaign Studio</h1>
    <p>MVP Channels: Instagram, LinkedIn, Meta Ads | Segment: SMB ecommerce</p>
    <div class=\"board\">
      <section class=\"column\"><h2>Draft</h2><div class=\"card\">Spring Launch A</div></section>
      <section class=\"column\">
        <h2>In Review</h2>
        <div class=\"card\">Spring Launch B <span class=\"pill\">Legal</span></div>
      </section>
      <section class=\"column\"><h2>Approved</h2><div class=\"card\">Spring Launch C</div></section>
      <section class=\"column\"><h2>Scheduled</h2><div class=\"card\">Spring Launch D</div></section>
    </div>
  </body>
</html>
"""


def create_campaign_mvp_app():
    """Create FastAPI app lazily so package can be imported without FastAPI extras."""
    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    from pydantic import BaseModel

    app = FastAPI(title="Content Creator MVP")

    class SubmissionPayload(BaseModel):
        title: str
        body: str

    @app.post("/qa/score")
    def qa_score(payload: SubmissionPayload):
        return score_campaign_submission(CampaignSubmission(**payload.model_dump()))

    @app.get("/campaign-studio", response_class=HTMLResponse)
    def campaign_studio():
        return build_campaign_studio_wireframe()

    return app
