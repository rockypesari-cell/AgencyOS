"""Tests for ProposalAgent."""

import pytest
from agents.proposal_agent import ProposalAgent


@pytest.fixture
def agent():
    return ProposalAgent()


def test_agent_creation(agent):
    assert agent.name == "proposal_generator"
    assert agent.enabled is True


def test_basic_proposal(agent):
    result = agent.run({
        "service": "logo_design",
        "summary": "Need a modern logo for tech startup",
        "priority": "normal",
        "client_name": "John",
    })
    assert result["success"] is True
    assert result["suggested_price"] == 150
    assert result["currency"] == "USD"
    assert "3-5 days" in result["timeline"]
    assert "John" in result["proposal_text"]
    assert result["status"] == "draft"


def test_high_priority_pricing(agent):
    result = agent.run({
        "service": "logo_design",
        "summary": "Urgent logo",
        "priority": "high",
    })
    assert result["suggested_price"] == 195  # 150 * 1.3
    assert "rush" in result["timeline"]


def test_unknown_service(agent):
    result = agent.run({
        "service": "quantum_computing",
        "summary": "Need quantum stuff",
    })
    assert result["success"] is True
    assert result["suggested_price"] == 200


def test_empty_input(agent):
    result = agent.run({})
    assert result["success"] is True
    assert result["service"] == "unknown"


def test_proposal_text_not_empty(agent):
    result = agent.run({"service": "web_design", "summary": "Build a site"})
    assert len(result["proposal_text"]) > 100


def test_brand_identity_pricing(agent):
    result = agent.run({"service": "brand_identity", "summary": "Full brand"})
    assert result["suggested_price"] == 400


def test_web_design_pricing(agent):
    result = agent.run({"service": "web_design", "summary": "Website"})
    assert result["suggested_price"] == 600