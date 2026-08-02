"""Tests for ProposalAgent."""

import pytest
from agents.proposal_agent import ProposalAgent
from services.pricing_service import PricingService


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
    assert "John" in result["proposal_text"]
    assert result["status"] == "draft"


def test_high_priority_pricing(agent):
    result = agent.run({
        "service": "logo_design",
        "summary": "Urgent logo",
        "priority": "high",
    })
    assert result["suggested_price"] == 195


def test_complex_pricing(agent):
    result = agent.run({
        "service": "logo_design",
        "summary": "Complex logo",
        "complexity": "complex",
    })
    assert result["suggested_price"] == 225


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


def test_proposal_text_not_empty(agent):
    result = agent.run({"service": "web_design", "summary": "Build a site"})
    assert len(result["proposal_text"]) > 100


def test_pricing_breakdown_included(agent):
    result = agent.run({"service": "logo_design", "summary": "Logo"})
    assert "pricing" in result
    assert "breakdown" in result["pricing"]


def test_custom_pricing_service():
    custom = PricingService(currency="EUR")
    agent = ProposalAgent(pricing_service=custom)
    result = agent.run({"service": "logo_design", "summary": "Logo"})
    assert result["currency"] == "EUR"