"""Tests for WorkflowRegistry."""

import pytest
from core.base_workflow import BaseWorkflow
from core.workflow_registry import WorkflowRegistry


class MockWorkflow(BaseWorkflow):
    def execute(self, context):
        return {"ok": True}


@pytest.fixture
def registry():
    return WorkflowRegistry()


@pytest.fixture
def sample_wf():
    return MockWorkflow(name="mock_wf", description="Mock")


def test_register_and_get(registry, sample_wf):
    registry.register(sample_wf)
    assert registry.get("mock_wf") is sample_wf


def test_register_duplicate_raises(registry, sample_wf):
    registry.register(sample_wf)
    with pytest.raises(ValueError):
        registry.register(MockWorkflow(name="mock_wf"))


def test_register_non_workflow_raises(registry):
    with pytest.raises(TypeError):
        registry.register("not a workflow")


def test_get_missing_raises(registry):
    with pytest.raises(KeyError):
        registry.get("ghost")


def test_exists(registry, sample_wf):
    assert registry.exists("mock_wf") is False
    registry.register(sample_wf)
    assert registry.exists("mock_wf") is True


def test_remove(registry, sample_wf):
    registry.register(sample_wf)
    registry.remove("mock_wf")
    assert registry.exists("mock_wf") is False


def test_remove_missing_raises(registry):
    with pytest.raises(KeyError):
        registry.remove("ghost")


def test_list_workflows(registry):
    registry.register(MockWorkflow(name="beta"))
    registry.register(MockWorkflow(name="alpha"))
    assert registry.list_workflows() == ["alpha", "beta"]


def test_count(registry, sample_wf):
    assert registry.count() == 0
    registry.register(sample_wf)
    assert registry.count() == 1


def test_clear(registry, sample_wf):
    registry.register(sample_wf)
    registry.clear()
    assert registry.count() == 0


def test_contains(registry, sample_wf):
    registry.register(sample_wf)
    assert "mock_wf" in registry


def test_len(registry, sample_wf):
    registry.register(sample_wf)
    assert len(registry) == 1


def test_list_enabled_disabled(registry):
    w1 = MockWorkflow(name="active")
    w2 = MockWorkflow(name="inactive")
    w2.enabled = False
    registry.register(w1)
    registry.register(w2)
    assert registry.list_enabled() == ["active"]
    assert registry.list_disabled() == ["inactive"]


def test_info(registry, sample_wf):
    registry.register(sample_wf)
    info = registry.info()
    assert "mock_wf" in info


def test_repr(registry, sample_wf):
    registry.register(sample_wf)
    assert "1 workflows" in repr(registry)