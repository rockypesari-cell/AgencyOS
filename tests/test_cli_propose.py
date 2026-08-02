"""Tests for CLI propose pipeline."""

import os
import pytest
from cli.propose import run_pipeline


def test_pipeline_with_raw_text():
    filepath = run_pipeline(
        raw_text="Need a logo for my startup. Budget $300.",
        client_name="Test Client",
    )
    assert filepath is not None
    assert os.path.exists(filepath)
    assert filepath.endswith(".html")

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    assert "Test Client" in html
    assert "Logo Design" in html

    # Cleanup
    os.remove(filepath)


def test_pipeline_with_service():
    filepath = run_pipeline(
        service="web_design",
        summary="Company website",
        priority="high",
        client_name="Web Client",
    )
    assert filepath is not None
    assert os.path.exists(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    assert "Web Design" in html
    assert "$780" in html  # 600 * 1.3

    os.remove(filepath)


def test_pipeline_rush():
    filepath = run_pipeline(
        service="poster",
        summary="Event poster",
        rush=True,
    )
    assert filepath is not None

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    assert "$156" in html  # 120 * 1.3

    os.remove(filepath)


def test_pipeline_custom_agency():
    filepath = run_pipeline(
        service="logo_design",
        summary="Logo",
        agency_name="MyStudio",
        agency_email="info@mystudio.com",
    )
    assert filepath is not None

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    assert "MyStudio" in html
    assert "info@mystudio.com" in html

    os.remove(filepath)


def test_pipeline_creates_proposals_dir():
    filepath = run_pipeline(service="logo_design", summary="Test")
    assert "proposals" in filepath
    assert os.path.exists(filepath)
    os.remove(filepath)