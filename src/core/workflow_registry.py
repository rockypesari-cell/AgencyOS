"""
WorkflowRegistry - Central management for all AgencyOS workflows.

Mirrors AgentRegistry design for consistency.

Responsibilities:
    - Register workflows
    - Retrieve workflows by name
    - List all workflows
    - Remove workflows
    - Check existence
    - Prevent duplicate registration

Does NOT:
    - Execute workflows
    - Contain business logic
    - Communicate with LLM
"""

from typing import Dict, List
from .base_workflow import BaseWorkflow


class WorkflowRegistry:
    """Central registry for managing all workflows in AgencyOS."""

    def __init__(self):
        self._workflows: Dict[str, BaseWorkflow] = {}

    def register(self, workflow: BaseWorkflow) -> None:
        """
        Register a workflow.

        Raises:
            TypeError: If not a BaseWorkflow instance.
            ValueError: If name already exists.
        """
        if not isinstance(workflow, BaseWorkflow):
            raise TypeError(
                f"Expected BaseWorkflow instance, got {type(workflow).__name__}."
            )

        if workflow.name in self._workflows:
            raise ValueError(
                f"Workflow '{workflow.name}' is already registered."
            )

        self._workflows[workflow.name] = workflow

    def get(self, name: str) -> BaseWorkflow:
        """
        Retrieve a workflow by name.

        Raises:
            KeyError: If not found.
        """
        if name not in self._workflows:
            raise KeyError(f"Workflow '{name}' not found in registry.")
        return self._workflows[name]

    def exists(self, name: str) -> bool:
        return name in self._workflows

    def remove(self, name: str) -> None:
        if name not in self._workflows:
            raise KeyError(f"Workflow '{name}' not found in registry.")
        del self._workflows[name]

    def list_workflows(self) -> List[str]:
        return sorted(self._workflows.keys())

    def list_enabled(self) -> List[str]:
        return sorted(
            n for n, w in self._workflows.items() if w.enabled
        )

    def list_disabled(self) -> List[str]:
        return sorted(
            n for n, w in self._workflows.items() if not w.enabled
        )

    def count(self) -> int:
        return len(self._workflows)

    def clear(self) -> None:
        self._workflows.clear()

    def info(self) -> Dict[str, dict]:
        return {n: w.info() for n, w in self._workflows.items()}

    def __contains__(self, name: str) -> bool:
        return name in self._workflows

    def __len__(self) -> int:
        return len(self._workflows)

    def __repr__(self) -> str:
        return f"<WorkflowRegistry: {len(self._workflows)} workflows>"