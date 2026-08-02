"""
AgencyOS - Agent Registry

Central registry for managing all AI agents.

Responsibilities:
- Register agents
- Retrieve agents
- Remove agents
- List registered agents
- Check agent existence

Business logic MUST NOT live here.
"""

from typing import Any


class AgentRegistry:
    """
    Central registry for AgencyOS agents.

    This class stores agent instances and provides a simple API
    for registering, retrieving, listing, and removing them.
    """

    def __init__(self) -> None:
        self._agents: dict[str, Any] = {}

    def register(self, name: str, agent: Any) -> None:
        """
        Register a new agent.

        Raises:
            ValueError: if the agent name already exists.
        """
        if not name:
            raise ValueError("Agent name cannot be empty.")

        if name in self._agents:
            raise ValueError(f"Agent '{name}' is already registered.")

        self._agents[name] = agent

    def get(self, name: str) -> Any:
        """
        Retrieve an agent by name.

        Raises:
            KeyError: if the agent does not exist.
        """
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' is not registered.")

        return self._agents[name]

    def exists(self, name: str) -> bool:
        """
        Check whether an agent exists.
        """
        return name in self._agents

    def remove(self, name: str) -> None:
        """
        Remove an agent.

        Raises:
            KeyError: if the agent does not exist.
        """
        if name not in self._agents:
            raise KeyError(f"Agent '{name}' is not registered.")

        del self._agents[name]

    def list_agents(self) -> list[str]:
        """
        Return all registered agent names.
        """
        return sorted(self._agents.keys())

    def count(self) -> int:
        """
        Return total registered agents.
        """
        return len(self._agents)

    def clear(self) -> None:
        """
        Remove all registered agents.

        Mainly used for testing.
        """
        self._agents.clear()

    def __contains__(self, name: str) -> bool:
        """
        Support:

            if "LeadAgent" in registry:
                ...
        """
        return name in self._agents

    def __len__(self) -> int:
        """
        Support:

            len(registry)
        """
        return len(self._agents)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(agents={self.list_agents()})"
        )