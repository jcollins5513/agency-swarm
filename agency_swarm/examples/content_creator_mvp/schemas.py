"""Schemas for the content creator MVP."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl

APPROVED_TARGET_SEGMENT = "SMB ecommerce"
APPROVED_MVP_CHANNEL_SCOPE = ["Instagram", "LinkedIn", "Meta Ads"]


class Tone(str, Enum):
    """Brand tone options."""

    confident = "confident"
    playful = "playful"
    educational = "educational"
    premium = "premium"


class FunnelStage(str, Enum):
    """Marketing funnel stage."""

    awareness = "awareness"
    consideration = "consideration"
    conversion = "conversion"
    retention = "retention"


class CampaignObjective(str, Enum):
    """Campaign objective."""

    awareness = "awareness"
    traffic = "traffic"
    lead_generation = "lead_generation"
    conversions = "conversions"


class BrandProfile(BaseModel):
    """Brand setup contract consumed by strategist and copy agents."""

    brand_name: str = Field(min_length=2, description="Public-facing brand name")
    target_segment: str = Field(default=APPROVED_TARGET_SEGMENT)
    voice: str = Field(min_length=10, description="Primary brand voice narrative")
    tone: list[Tone] = Field(min_length=1, description="Allowed tone settings")
    messaging_pillars: list[str] = Field(min_length=1, description="Core messaging themes")
    forbidden_phrases: list[str] = Field(default_factory=list)
    required_disclaimers: list[str] = Field(default_factory=list)
    visual_cues: list[str] = Field(min_length=1, description="Visual styling and asset cues")
    primary_channels: list[str] = Field(default_factory=lambda: APPROVED_MVP_CHANNEL_SCOPE.copy())
    legal_review_required: bool = True


class CampaignBrief(BaseModel):
    """Cross-agent campaign request contract."""

    campaign_name: str = Field(min_length=3)
    objective: CampaignObjective
    funnel_stage: FunnelStage
    offer: str = Field(min_length=5)
    audience_persona: str = Field(min_length=5)
    key_message: str = Field(min_length=10)
    channels: list[str] = Field(min_length=1)
    start_at: datetime
    end_at: datetime
    budget_usd: float = Field(gt=0)
    primary_cta: str = Field(min_length=2)
    landing_page_url: HttpUrl


class ComplianceRubric(BaseModel):
    """Simple rubric for QA scoring."""

    banned_claims: list[str] = Field(default_factory=lambda: ["guaranteed results", "instant cure"])
    mandatory_terms: list[str] = Field(default_factory=lambda: ["terms apply"])
    max_cta_count: int = 2
    readability_floor: int = 65
