"""First orchestration chain using mock tools."""

from __future__ import annotations

from dataclasses import dataclass

from .schemas import BrandProfile, CampaignBrief


@dataclass
class MockToolResult:
    """Container for mocked tool output."""

    tool_name: str
    payload: dict


class MockToolOrchestrator:
    """MVP chain: strategist -> planner -> brief -> copywriter -> QA -> ad ops."""

    chain = (
        "brand_strategist",
        "content_planner",
        "creative_brief",
        "copywriter",
        "qa",
        "ad_ops",
    )

    def run(self, brand_profile: BrandProfile, campaign_brief: CampaignBrief) -> list[MockToolResult]:
        outputs = [
            self._brand_strategist(brand_profile),
            self._content_planner(campaign_brief),
            self._creative_brief(brand_profile, campaign_brief),
            self._copywriter(campaign_brief),
            self._qa(campaign_brief),
            self._ad_ops(campaign_brief),
        ]
        return outputs

    def _brand_strategist(self, profile: BrandProfile) -> MockToolResult:
        return MockToolResult(
            tool_name="brand_strategist",
            payload={
                "voice": profile.voice,
                "tone": [tone.value for tone in profile.tone],
                "pillars": profile.messaging_pillars,
            },
        )

    def _content_planner(self, brief: CampaignBrief) -> MockToolResult:
        return MockToolResult(
            tool_name="content_planner",
            payload={
                "objective": brief.objective.value,
                "channels": brief.channels,
                "timeline": [brief.start_at.isoformat(), brief.end_at.isoformat()],
            },
        )

    def _creative_brief(self, profile: BrandProfile, brief: CampaignBrief) -> MockToolResult:
        return MockToolResult(
            tool_name="creative_brief",
            payload={
                "campaign_name": brief.campaign_name,
                "key_message": brief.key_message,
                "visual_cues": profile.visual_cues,
            },
        )

    def _copywriter(self, brief: CampaignBrief) -> MockToolResult:
        return MockToolResult(
            tool_name="copywriter",
            payload={
                "headline": f"{brief.offer} for {brief.audience_persona}",
                "cta": brief.primary_cta,
            },
        )

    def _qa(self, brief: CampaignBrief) -> MockToolResult:
        return MockToolResult(
            tool_name="qa",
            payload={
                "status": "pass",
                "checks": ["tone", "compliance", "platform-fit"],
                "campaign": brief.campaign_name,
            },
        )

    def _ad_ops(self, brief: CampaignBrief) -> MockToolResult:
        return MockToolResult(
            tool_name="ad_ops",
            payload={
                "budget_usd": brief.budget_usd,
                "structure": ["campaign", "ad_set", "ad"],
            },
        )
