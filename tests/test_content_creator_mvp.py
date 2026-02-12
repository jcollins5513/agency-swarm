from datetime import datetime, timedelta, timezone

from agency_swarm.examples.content_creator_mvp.app import (
    CampaignSubmission,
    build_campaign_studio_wireframe,
    score_campaign_submission,
)
from agency_swarm.examples.content_creator_mvp.orchestration import MockToolOrchestrator
from agency_swarm.examples.content_creator_mvp.schemas import (
    BrandProfile,
    CampaignBrief,
    CampaignObjective,
    FunnelStage,
    Tone,
)


def _build_brand_profile() -> BrandProfile:
    return BrandProfile(
        brand_name="Acme Co",
        voice="Practical and energetic guidance for ecommerce founders.",
        tone=[Tone.confident, Tone.educational],
        messaging_pillars=["speed", "clarity"],
        forbidden_phrases=["guaranteed results"],
        visual_cues=["clean typography", "UGC-style video"],
    )


def _build_campaign_brief() -> CampaignBrief:
    now = datetime.now(timezone.utc)
    return CampaignBrief(
        campaign_name="Spring Growth Sprint",
        objective=CampaignObjective.conversions,
        funnel_stage=FunnelStage.conversion,
        offer="20% off starter bundle",
        audience_persona="Shopify apparel founder",
        key_message="Launch faster with campaign workflows built for lean teams.",
        channels=["Instagram", "LinkedIn"],
        start_at=now,
        end_at=now + timedelta(days=7),
        budget_usd=1500,
        primary_cta="Shop now",
        landing_page_url="https://example.com/spring",
    )


def test_orchestration_chain_executes_all_mock_tools():
    orchestrator = MockToolOrchestrator()
    results = orchestrator.run(_build_brand_profile(), _build_campaign_brief())

    assert [result.tool_name for result in results] == list(orchestrator.chain)
    assert results[-1].payload["budget_usd"] == 1500


def test_qa_scoring_flags_violations():
    result = score_campaign_submission(
        CampaignSubmission(
            title="Claim-heavy ad",
            body="Guaranteed results! Buy now buy now buy now with instant cure messaging.",
        )
    )

    assert result["status"] == "fail"
    assert any(item.startswith("banned_claim") for item in result["violations"])


def test_campaign_studio_wireframe_contains_approval_states():
    html = build_campaign_studio_wireframe()

    assert "Campaign Studio" in html
    assert "In Review" in html
    assert "Approved" in html
