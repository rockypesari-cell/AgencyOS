"""
AgentLoader - Wires up all agents and returns a ready-to-use registry.

Usage:
    from bootstrap.agent_loader import load_agents
    registry = load_agents()
    agent = registry.get("lead_intake")

Architecture Rule:
    No part of the codebase should instantiate agents directly.
    All agent creation goes through this loader.
"""

from typing import List, Optional

from core.agent_registry import AgentRegistry
from core.base_agent import BaseAgent


# ─── Placeholder Agents for MVP ───────────────────────────────

class LeadIntakeAgent(BaseAgent):
    """Placeholder: Converts raw requests into structured leads."""

    def __init__(self):
        super().__init__(
            name="lead_intake",
            description="Converts raw customer requests into structured lead data.",
            version="0.1.0",
            skills=["text_analysis", "lead_qualification"],
            tools=["llm_service"],
        )

    def execute(self, input_data):
        raw = input_data.get("request", "")

        return {
            "service": "unknown",
            "summary": raw[:100] if raw else "",
            "priority": "normal",
            "status": "new",
        }


class ProposalAgent(BaseAgent):
    """Placeholder: Generates project proposals."""

    def __init__(self):
        super().__init__(
            name="proposal_generator",
            description="Generates professional proposals from lead data.",
            version="0.1.0",
            skills=["proposal_writing", "pricing"],
            tools=["llm_service"],
        )

    def execute(self, input_data):
        return {
            "proposal": "Draft proposal",
            "status": "draft",
        }


# ─── Agent Loader ─────────────────────────────────────────────

AGENT_CLASSES = [
    LeadIntakeAgent,
    ProposalAgent,
]


def load_agents(
    agent_classes: Optional[List[type]] = None,
) -> AgentRegistry:
    """
    Create and register all agents.

    Args:
        agent_classes:
            Optional list of agent classes to load.
            Defaults to AGENT_CLASSES.

    Returns:
        Fully populated AgentRegistry.
    """

    registry = AgentRegistry()

    classes = (
        agent_classes
        if agent_classes is not None
        else AGENT_CLASSES
    )

    for agent_class in classes:
        try:
            agent = agent_class()

        except TypeError:
            agent = agent_class(
                name=agent_class.__name__
            )

        registry.register(agent)

    return registry