"""Tests for AppBootstrap."""

from bootstrap.app_bootstrap import bootstrap
from core.agent_registry import AgentRegistry
from core.workflow_registry import WorkflowRegistry
from core.service_container import ServiceContainer


def test_bootstrap_returns_dict():
    app = bootstrap()
    assert isinstance(app, dict)


def test_bootstrap_has_agents():
    app = bootstrap()
    assert "agents" in app
    assert isinstance(app["agents"], AgentRegistry)


def test_bootstrap_has_workflows():
    app = bootstrap()
    assert "workflows" in app
    assert isinstance(app["workflows"], WorkflowRegistry)


def test_bootstrap_has_services():
    app = bootstrap()
    assert "services" in app
    assert isinstance(app["services"], ServiceContainer)


def test_bootstrap_agents_loaded():
    app = bootstrap()
    assert app["agents"].count() >= 2
    assert app["agents"].exists("lead_intake")