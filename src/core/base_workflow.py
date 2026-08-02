"""
BaseWorkflow - Abstract contract for all AgencyOS workflows.

A workflow orchestrates a business process by coordinating
agents, services, and tools in a defined sequence.

Architecture Decision:
    - Workflows EXECUTE. Agents DECIDE.
    - Workflows do NOT contain AI logic.
    - Each workflow has a unique name and version.
    - Workflows are stateless between runs.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone


class BaseWorkflow(ABC):
    """Abstract base class for all AgencyOS workflows."""

    def __init__(
        self,
        name: str,
        description: str = "",
        version: str = "1.0.0",
        steps: Optional[List[str]] = None,
        enabled: bool = True,
    ):
        if not name or not name.strip():
            raise ValueError("Workflow name cannot be empty.")

        self._name = name.strip()
        self._description = description.strip()
        self._version = version
        self._steps = steps or []
        self._enabled = enabled
        self._created_at = datetime.now(timezone.utc).isoformat()
        self._last_run_at: Optional[str] = None
        self._run_count: int = 0

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
    def steps(self) -> List[str]:
        return list(self._steps)

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
    def last_run_at(self) -> Optional[str]:
        return self._last_run_at

    @property
    def run_count(self) -> int:
        return self._run_count

    @abstractmethod
    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the workflow.

        Args:
            context: Input data and dependencies.

        Returns:
            Result dictionary with workflow output.
        """
        pass

    def validate_context(self, context: Dict[str, Any]) -> bool:
        """Validate input context. Override for custom validation."""
        return isinstance(context, dict)

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Safe execution wrapper.
        Validates, tracks usage, handles errors.
        """
        if not self._enabled:
            return {
                "success": False,
                "workflow": self._name,
                "error": f"Workflow '{self._name}' is disabled.",
            }

        if not self.validate_context(context):
            return {
                "success": False,
                "workflow": self._name,
                "error": "Invalid context.",
            }

        try:
            self._run_count += 1
            self._last_run_at = datetime.now(timezone.utc).isoformat()
            result = self.execute(context)
            result["workflow"] = self._name
            result["success"] = True
            return result
        except Exception as e:
            return {
                "success": False,
                "workflow": self._name,
                "error": str(e),
            }

    def info(self) -> Dict[str, Any]:
        """Return workflow metadata."""
        return {
            "name": self._name,
            "description": self._description,
            "version": self._version,
            "steps": self._steps,
            "enabled": self._enabled,
            "created_at": self._created_at,
            "last_run_at": self._last_run_at,
            "run_count": self._run_count,
        }

    def __repr__(self) -> str:
        status = "enabled" if self._enabled else "disabled"
        return f"<Workflow: {self._name} v{self._version} ({status})>"