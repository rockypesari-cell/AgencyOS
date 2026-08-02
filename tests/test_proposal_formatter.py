"""Tests for ProposalFormatterSkill."""

import pytest
from skills.proposal_formatter import ProposalFormatterSkill
from agents.proposal_agent import ProposalAgent


@pytest.fixture
def formatter():
    return ProposalFormatterSkill(agency_name="TestAgency", agency_email="test@agency.com")


@pytest.fixture
def sample_proposal():
    agent = ProposalAgent()
    return agent.run({
        "service": "logo_design",
        "summary": "Need a modern logo",
        "priority": "normal",
        "client_name": "John Doe",
    })


def test_html_output(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "<!DOCTYPE html>" in html
    assert "TestAgency" in html
    assert "$150" in html
    assert "USD" in html


def test_html_contains_service(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "Logo Design" in html


def test_html_contains_client(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "John Doe" in html


def test_html_contains_proposal_id(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "PROP-" in html


def test_html_contains_cta(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "Approve Proposal" in html
    assert "test@agency.com" in html


def test_html_contains_timeline(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert "3-5 days" in html


def test_html_validity(formatter, sample_proposal):
    html = formatter.format_html(sample_proposal)
    assert html.count("<html") == 1
    assert html.count("</html>") == 1
    assert html.count("<body") == 1
    assert html.count("</body>") == 1


def test_plain_text_output(formatter, sample_proposal):
    text = formatter.format_plain_text(sample_proposal)
    assert "TestAgency" in text
    assert "$150" in text
    assert "Logo Design" in text


def test_plain_text_contains_separator(formatter, sample_proposal):
    text = formatter.format_plain_text(sample_proposal)
    assert "=" * 50 in text


def test_custom_agency_name():
    formatter = ProposalFormatterSkill(agency_name="MyStudio")
    agent = ProposalAgent()
    proposal = agent.run({"service": "poster", "summary": "Event poster"})
    html = formatter.format_html(proposal)
    assert "MyStudio" in html


def test_high_priority_proposal(formatter):
    agent = ProposalAgent()
    proposal = agent.run({
        "service": "web_design",
        "summary": "Urgent website",
        "priority": "high",
    })
    html = formatter.format_html(proposal)
    assert "$780" in html  # 600 * 1.3