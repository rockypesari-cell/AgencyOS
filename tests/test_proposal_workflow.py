"""Tests for ProposalWorkflow."""

import pytest
from agents.proposal_agent import ProposalAgent
from workflows.proposal_workflow import ProposalWorkflow


@pytest.fixture
def workflow():
    agent = ProposalAgent()
    return ProposalWorkflow(proposal_agent=agent)


def test_workflow_creation(workflow):
    assert workflow.name == "proposal_workflow"


def test_workflow_success(workflow):
    result = workflow.run({
        "lead_data": {
            "service": "logo_design",
            "summary": "Need a logo",
            "client_name": "Test Client",
        }
    })
    assert result["success"] is True
    assert result["ready_to_send"] is True
    assert result["proposal"]["suggested_price"] == 150


def test_workflow_no_lead_data(workflow):
    result = workflow.run({})
    assert result["success"] is False


def test_workflow_no_agent():
    wf = ProposalWorkflow(proposal_agent=None)
    result = wf.run({"lead_data": {"service": "logo_design"}})
    assert result["success"] is False


def test_workflow_disabled(workflow):
    workflow.enabled = False
    result = workflow.run({"lead_data": {"service": "logo_design"}})
    assert result["success"] is False
    assert "disabled" in result["error"]