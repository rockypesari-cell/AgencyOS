"""Tests for AgentRegistry."""

import pytest
from core.base_agent import BaseAgent
from core.agent_registry import AgentRegistry


class MockAgent(BaseAgent):
    def execute(self, input_data):
        return {"ok": True}


@pytest.fixture
def registry():
    return AgentRegistry()


@pytest.fixture
def sample_agent():
    return MockAgent(name="mock", description="Mock agent")


# ─── Tests ────────────────────────────────────────────────────

def test_register_and_get(registry, sample_agent):
    registry.register(sample_agent)
    assert registry.get("mock") is sample_agent


def test_register_duplicate_raises(registry, sample_agent):
    registry.register(sample_agent)
    with pytest.raises(ValueError):
        registry.register(MockAgent(name="mock"))


def test_register_non_agent_raises(registry):
    with pytest.raises(TypeError):
        registry.register("not an agent")


def test_get_missing_raises(registry):
    with pytest.raises(KeyError):
        registry.get("ghost")


def test_exists(registry, sample_agent):
    assert registry.exists("mock") is False
    registry.register(sample_agent)
    assert registry.exists("mock") is True


def test_remove(registry, sample_agent):
    registry.register(sample_agent)
    registry.remove("mock")
    assert registry.exists("mock") is False


def test_remove_missing_raises(registry):
    with pytest.raises(KeyError):
        registry.remove("ghost")


def test_list_agents(registry):
    registry.register(MockAgent(name="beta"))
    registry.register(MockAgent(name="alpha"))
    assert registry.list_agents() == ["alpha", "beta"]


def test_count(registry, sample_agent):
    assert registry.count() == 0
    registry.register(sample_agent)
    assert registry.count() == 1


def test_clear(registry, sample_agent):
    registry.register(sample_agent)
    registry.clear()
    assert registry.count() == 0


def test_contains(registry, sample_agent):
    registry.register(sample_agent)
    assert "mock" in registry
    assert "ghost" not in registry


def test_len(registry, sample_agent):
    registry.register(sample_agent)
    assert len(registry) == 1


def test_list_enabled_disabled(registry):
    a1 = MockAgent(name="active")
    a2 = MockAgent(name="inactive")
    a2.enabled = False
    registry.register(a1)
    registry.register(a2)
    assert registry.list_enabled() == ["active"]
    assert registry.list_disabled() == ["inactive"]


def test_info(registry, sample_agent):
    registry.register(sample_agent)
    info = registry.info()
    assert "mock" in info
    assert info["mock"]["name"] == "mock"


def test_repr(registry, sample_agent):
    registry.register(sample_agent)
    assert "1 agents" in repr(registry)