"""
BaseAgent - Abstract contract for all AgencyOS agents.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone


class BaseAgent(ABC):
    """Abstract base class for all AgencyOS agents."""

    def __init__(
        self,
        name: str,
        description: str = "",
        version: str = "1.0.0",
        skills: Optional[List[str]] = None,
        tools: Optional[List[str]] = None,
        enabled: bool = True,
    ):
        if not name or not name.strip():
            raise ValueError("Agent name cannot be empty.")

        self._name = name.strip()
        self._description = description.strip()
        self._version = version
        self._skills = skills or []
        self._tools = tools or []
        self._enabled = enabled
        self._created_at = datetime.now(timezone.utc).isoformat()
        self._last_used_at: Optional[str] = None
        self._execution_count: int = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @property
    def version(self) -> str:
        return self._version

    @property
    def skills(self) -> List[str]:
        return list(self._skills)

    @property
    def tools(self) -> List[str]:
        return list(self._tools)

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def last_used_at(self) -> Optional[str]:
        return self._last_used_at

    @property
    def execution_count(self) -> int:
        return self._execution_count

    @abstractmethod
    def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def validate_input(self, input_data: Dict[str, Any]) -> bool:
        return isinstance(input_data, dict)

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if not self._enabled:
            return {
                "success": False,
                "agent": self._name,
                "error": f"Agent '{self._name}' is disabled.",
            }

        if not self.validate_input(input_data):
            return {
                "success": False,
                "agent": self._name,
                "error": "Invalid input data.",
            }

        try:
            self._execution_count += 1
            self._last_used_at = datetime.now(timezone.utc).isoformat()
            result = self.execute(input_data)
            result["agent"] = self._name
            result["success"] = True
            return result
        except Exception as e:
            return {
                "success": False,
                "agent": self._name,
                "error": str(e),
            }

    def info(self) -> Dict[str, Any]:
        return {
            "name": self._name,
            "description": self._description,
            "version": self._version,
            "skills": self._skills,
            "tools": self._tools,
            "enabled": self._enabled,
            "created_at": self._created_at,
            "last_used_at": self._last_used_at,
            "execution_count": self._execution_count,
        }

    def __repr__(self) -> str:
        status = "enabled" if self._enabled else "disabled"
        return f"<Agent: {self._name} v{self._version} ({status})>"