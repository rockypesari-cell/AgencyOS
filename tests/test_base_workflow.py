"""Tests for BaseWorkflow."""

import pytest
from core.base_workflow import BaseWorkflow


class DummyWorkflow(BaseWorkflow):
    def execute(self, context):
        return {"processed": context.get("input", "")}


class FailingWorkflow(BaseWorkflow):
    def execute(self, context):
        raise RuntimeError("Workflow broke.")


def test_workflow_creation():
    wf = DummyWorkflow(name="test_wf", description="Test")
    assert wf.name == "test_wf"
    assert wf.enabled is True


def test_workflow_empty_name_raises():
    with pytest.raises(ValueError):
        DummyWorkflow(name="")


def test_workflow_execute():
    wf = DummyWorkflow(name="test_wf")
    result = wf.run({"input": "hello"})
    assert result["success"] is True
    assert result["processed"] == "hello"
    assert result["workflow"] == "test_wf"


def test_workflow_disabled():
    wf = DummyWorkflow(name="test_wf")
    wf.enabled = False
    result = wf.run({"input": "x"})
    assert result["success"] is False
    assert "disabled" in result["error"]


def test_workflow_error_handling():
    wf = FailingWorkflow(name="fail_wf")
    result = wf.run({})
    assert result["success"] is False
    assert "Workflow broke" in result["error"]


def test_workflow_run_count():
    wf = DummyWorkflow(name="test_wf")
    wf.run({"input": "1"})
    wf.run({"input": "2"})
    assert wf.run_count == 2


def test_workflow_last_run_at():
    wf = DummyWorkflow(name="test_wf")
    assert wf.last_run_at is None
    wf.run({"input": "x"})
    assert wf.last_run_at is not None


def test_workflow_info():
    wf = DummyWorkflow(name="test_wf", steps=["a", "b"])
    info = wf.info()
    assert info["name"] == "test_wf"
    assert info["steps"] == ["a", "b"]


def test_workflow_repr():
    wf = DummyWorkflow(name="test_wf")
    assert "test_wf" in repr(wf)


def test_workflow_invalid_context():
    wf = DummyWorkflow(name="test_wf")
    result = wf.run("not a dict")
    assert result["success"] is False


def test_workflow_steps_immutable():
    wf = DummyWorkflow(name="test_wf", steps=["a"])
    steps = wf.steps
    steps.append("b")
    assert wf.steps == ["a"]