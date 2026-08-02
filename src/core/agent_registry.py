"""
AgentRegistry - Central management for all AgencyOS agents.

Responsibilities:
    - Register agents
    - Retrieve agents by name
    - List all agents
    - Remove agents
    - Check existence
    - Prevent duplicate registration

Does NOT:
    - Execute agents
    - Contain business logic
    - Communicate with LLM
    - Manage workflows
"""

from typing import Dict, List, Optional
from .base_agent import BaseAgent


class AgentRegistry:
    """Central registry for managing all agents in AgencyOS."""

    def __init__(self):
        self._agents: Dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        """
        Register an agent in the registry.

        Args:
            agent: An instance of BaseAgent.

        Raises:
            TypeError: If agent is not a BaseAgent instance.
            ValueError: If an agent with the same name already exists.
        """
        if not isinstance(agent, BaseAgent):
            raise TypeError(
                f"Expected BaseAgent instance, got {type(agent).__name__}."
            )

        if agent.name in self._agents:
            raise ValueError(
                f"Agent '{agent.name}' is already registered."
            )

        self._agents[agent.name] = agent

    def get(self, name: str) -> BaseAgent:
        """
        Retrieve an agent by name.

        Args:
            name: The agent's unique name.

        Returns:
            The registered BaseAgent instance.

        Raises:
            KeyError: If no agent with that name exists.
        """
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' not found in registry.")
        return self._agents[name]

    def exists(self, name: str) -> bool:
        """Check if an agent with the given name exists."""
        return name in self._agents

    def remove(self, name: str) -> None:
        """
        Remove an agent from the registry.

        Args:
            name: The agent's unique name.

        Raises:
            KeyError: If no agent with that name exists.
        """
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' not found in registry.")
        del self._agents[name]

    def list_agents(self) -> List[str]:
        """Return a sorted list of all registered agent names."""
        return sorted(self._agents.keys())

    def list_enabled(self) -> List[str]:
        """Return names of all enabled agents."""
        return sorted(
            name for name, agent in self._agents.items() if agent.enabled
        )

    def list_disabled(self) -> List[str]:
        """Return names of all disabled agents."""
        return sorted(
            name for name, agent in self._agents.items() if not agent.enabled
        )

    def count(self) -> int:
        """Return the total number of registered agents."""
        return len(self._agents)

    def clear(self) -> None:
        """Remove all agents from the registry. Useful for testing."""
        self._agents.clear()

    def info(self) -> Dict[str, dict]:
        """Return metadata for all registered agents."""
        return {name: agent.info() for name, agent in self._agents.items()}

    def __contains__(self, name: str) -> bool:
        return name in self._agents

    def __len__(self) -> int:
        return len(self._agents)

    def __repr__(self) -> str:
        return f"<AgentRegistry: {len(self._agents)} agents>"