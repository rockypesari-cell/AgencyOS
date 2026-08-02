"""Tests for AgentLoader."""

from core.base_agent import BaseAgent
from core.agent_registry import AgentRegistry
from bootstrap.agent_loader import load_agents, AGENT_CLASSES


def test_load_agents_returns_registry():
    registry = load_agents()
    assert isinstance(registry, AgentRegistry)


def test_load_agents_registers_all():
    registry = load_agents()
    assert registry.count() == len(AGENT_CLASSES)


def test_load_agents_has_lead_intake():
    registry = load_agents()
    assert registry.exists("lead_intake")
    agent = registry.get("lead_intake")
    assert isinstance(agent, BaseAgent)


def test_load_agents_has_proposal():
    registry = load_agents()
    assert registry.exists("proposal_generator")


def test_load_agents_custom_list():
    class CustomAgent(BaseAgent):
        def __init__(self):
            super().__init__(name="custom", description="Custom test agent")

        def execute(self, input_data):
            return {}

    registry = load_agents(agent_classes=[CustomAgent])
    assert registry.count() == 1
    assert registry.exists("custom")


def test_load_agents_empty_list():
    registry = load_agents(agent_classes=[])
    assert registry.count() == 0


def test_lead_intake_execute():
    registry = load_agents()
    agent = registry.get("lead_intake")
    result = agent.run({"request": "I need a logo"})
    assert result["success"] is True
    assert result["status"] == "new"


def test_proposal_agent_execute():
    registry = load_agents()
    agent = registry.get("proposal_generator")
    result = agent.run({
        "service": "logo_design",
        "summary": "Need a logo",
        "client_name": "Test",
    })
    assert result["success"] is True
    assert result["suggested_price"] == 150