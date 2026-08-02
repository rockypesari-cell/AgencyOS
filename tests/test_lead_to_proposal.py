"""Integration test: Lead text -> Parsed -> Proposal."""

from skills.lead_parser import LeadParserSkill
from agents.proposal_agent import ProposalAgent
from services.pricing_service import PricingService


def test_full_pipeline():
    """Raw text -> LeadParser -> ProposalAgent -> Ready proposal."""

    parser = LeadParserSkill()
    lead = parser.parse(
        "Hi! I need a professional logo for my coffee shop. "
        "Budget around $300. Need it done quickly, it's urgent!"
    )

    assert lead["service"] == "logo_design"
    assert lead["priority"] == "high"
    assert lead["budget"] == 300

    pricing = PricingService()
    agent = ProposalAgent(pricing_service=pricing)
    result = agent.run({
        "service": lead["service"],
        "summary": lead["summary"],
        "priority": lead["priority"],
        "client_name": "Coffee Shop Owner",
    })

    assert result["success"] is True
    assert result["suggested_price"] == 195  # 150 * 1.3 rush
    assert "Coffee Shop Owner" in result["proposal_text"]
    assert result["status"] == "draft"
    assert len(result["proposal_text"]) > 100


def test_full_pipeline_web_design():
    parser = LeadParserSkill()
    lead = parser.parse(
        "Looking for a web designer to build a landing page. "
        "Budget $800. Flexible timeline."
    )

    assert lead["service"] in ["web_design", "landing_page"]
    assert lead["priority"] == "low"  # "flexible" = low priority

    agent = ProposalAgent()
    result = agent.run({
        "service": lead["service"],
        "summary": lead["summary"],
        "priority": lead["priority"],
    })

    assert result["success"] is True
    # landing_page base=350, low priority=0.9 -> 315
    assert result["suggested_price"] >= 300
    assert result["suggested_price"] <= 600