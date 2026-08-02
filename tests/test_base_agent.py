"""Tests for BaseAgent."""

import pytest
from core.base_agent import BaseAgent


# ─── Concrete test agent ──────────────────────────────────────

class DummyAgent(BaseAgent):
    def execute(self, input_data):
        return {"echo": input_data.get("message", "")}


class FailingAgent(BaseAgent):
    def execute(self, input_data):
        raise RuntimeError("Something broke.")


# ─── Tests ────────────────────────────────────────────────────

def test_agent_creation():
    agent = DummyAgent(name="test", description="A test agent")
    assert agent.name == "test"
    assert agent.description == "A test agent"
    assert agent.version == "1.0.0"
    assert agent.enabled is True


def test_agent_empty_name_raises():
    with pytest.raises(ValueError):
        DummyAgent(name="")


def test_agent_execute():
    agent = DummyAgent(name="test")
    result = agent.run({"message": "hello"})
    assert result["success"] is True
    assert result["echo"] == "hello"
    assert result["agent"] == "test"


def test_agent_disabled():
    agent = DummyAgent(name="test")
    agent.enabled = False
    result = agent.run({"message": "hello"})
    assert result["success"] is False
    assert "disabled" in result["error"]


def test_agent_error_handling():
    agent = FailingAgent(name="fail")
    result = agent.run({})
    assert result["success"] is False
    assert "Something broke" in result["error"]


def test_agent_execution_count():
    agent = DummyAgent(name="test")
    agent.run({"message": "1"})
    agent.run({"message": "2"})
    assert agent.execution_count == 2


def test_agent_info():
    agent = DummyAgent(name="test", skills=["a", "b"])
    info = agent.info()
    assert info["name"] == "test"
    assert info["skills"] == ["a", "b"]


def test_agent_repr():
    agent = DummyAgent(name="test")
    assert "test" in repr(agent)


def test_agent_invalid_input():
    agent = DummyAgent(name="test")
    result = agent.run("not a dict")
    assert result["success"] is False


def test_agent_last_used_at():
    agent = DummyAgent(name="test")
    assert agent.last_used_at is None
    agent.run({"message": "hi"})
    assert agent.last_used_at is not None


def test_agent_skills_immutable():
    agent = DummyAgent(name="test", skills=["a"])
    skills = agent.skills
    skills.append("b")
    assert agent.skills == ["a"]


def test_agent_created_at():
    agent = DummyAgent(name="test")
    assert agent.created_at is not None