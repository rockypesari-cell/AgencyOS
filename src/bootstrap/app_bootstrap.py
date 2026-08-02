"""
AppBootstrap - Wires up the entire AgencyOS system.

Creates and connects:
    - AgentRegistry (all agents)
    - WorkflowRegistry (all workflows)
    - ServiceContainer (all services)

Usage:
    from bootstrap.app_bootstrap import bootstrap
    app = bootstrap()

    app["agents"].get("lead_intake")
    app["workflows"].get("lead_workflow")
    app["services"].get("llm_service")
"""

from core.agent_registry import AgentRegistry
from core.workflow_registry import WorkflowRegistry
from core.service_container import ServiceContainer
from bootstrap.agent_loader import load_agents


def bootstrap() -> dict:
    """
    Initialize the entire AgencyOS system.

    Returns:
        Dictionary with keys: agents, workflows, services
    """
    # 1. Load all agents
    agent_registry = load_agents()

    # 2. Create workflow registry (empty for now, filled later)
    workflow_registry = WorkflowRegistry()

    # 3. Create service container (empty for now, filled later)
    service_container = ServiceContainer()

    return {
        "agents": agent_registry,
        "workflows": workflow_registry,
        "services": service_container,
    }