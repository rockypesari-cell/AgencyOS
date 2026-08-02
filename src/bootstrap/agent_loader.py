"""
AgentLoader - Wires up all agents and returns a ready-to-use registry.
"""

from core.agent_registry import AgentRegistry
from core.base_agent import BaseAgent
from typing import List, Optional

from agents.proposal_agent import ProposalAgent


# ─── Placeholder: LeadIntakeAgent ─────────────────────────────

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


# ─── Agent Loader ─────────────────────────────────────────────

AGENT_CLASSES = [
    LeadIntakeAgent,
    ProposalAgent,
]


def load_agents(
    agent_classes: Optional[List[type]] = None,
) -> AgentRegistry:
    registry = AgentRegistry()
    classes = agent_classes if agent_classes is not None else AGENT_CLASSES

    for agent_class in classes:
        agent = agent_class()
        registry.register(agent)

    return registry