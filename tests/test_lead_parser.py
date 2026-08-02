"""Tests for LeadParserSkill."""

import pytest
from skills.lead_parser import LeadParserSkill


@pytest.fixture
def parser():
    return LeadParserSkill()


def test_empty_input(parser):
    result = parser.parse("")
    assert result["service"] == "unknown"
    assert result["confidence"] == 0.0


def test_none_input(parser):
    result = parser.parse(None)
    assert result["service"] == "unknown"


def test_logo_detection(parser):
    result = parser.parse("I need a logo for my startup")
    assert result["service"] == "logo_design"
    assert result["confidence"] > 0


def test_brand_identity_detection(parser):
    result = parser.parse("Looking for complete branding and brand identity")
    assert result["service"] == "brand_identity"


def test_web_design_detection(parser):
    result = parser.parse("Need a website designed for our company")
    assert result["service"] == "web_design"


def test_presentation_detection(parser):
    result = parser.parse("Need a pitch deck presentation for investors")
    assert result["service"] == "presentation"


def test_video_detection(parser):
    result = parser.parse("Looking for someone to make a promo video")
    assert result["service"] == "video"


def test_social_media_detection(parser):
    result = parser.parse("Need instagram social media posts designed")
    assert result["service"] == "social_media"


def test_budget_extraction(parser):
    result = parser.parse("Need a logo. Budget is $500")
    assert result["budget"] == 500


def test_budget_extraction_comma(parser):
    result = parser.parse("Budget: $2,500 for the project")
    assert result["budget"] == 2500


def test_high_priority(parser):
    result = parser.parse("URGENT: Need a logo ASAP")
    assert result["priority"] == "high"


def test_low_priority(parser):
    result = parser.parse("Need a logo whenever you have time, no rush")
    assert result["priority"] == "low"


def test_normal_priority(parser):
    result = parser.parse("Need a logo for my company")
    assert result["priority"] == "normal"


def test_summary_truncation(parser):
    long_text = "x" * 300
    result = parser.parse(long_text)
    assert len(result["summary"]) <= 204  # 200 + "..."


def test_raw_text_preserved(parser):
    result = parser.parse("Need a logo")
    assert result["raw_text"] == "Need a logo"


def test_illustration_detection(parser):
    result = parser.parse("Looking for an illustrator for a children's book")
    assert result["service"] == "illustration"


def test_translation_detection(parser):
    result = parser.parse("Need translation of documents from English to Arabic")
    assert result["service"] == "translation"


def test_seo_detection(parser):
    result = parser.parse("Need SEO optimization for our website")
    assert result["service"] == "seo"


def test_unknown_service(parser):
    result = parser.parse("Looking for a quantum physicist")
    assert result["service"] == "unknown"