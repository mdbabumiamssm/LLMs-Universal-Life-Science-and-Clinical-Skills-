"""Tests for the bulkrna-deconvolution skill."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

SKILL_SCRIPT = Path(__file__).resolve().parent.parent / "bulkrna_deconvolution.py"


@pytest.fixture
def tmp_output(tmp_path):
    return tmp_path / "deconv_out"


def test_demo_mode(tmp_output):
    """bulkrna-deconvolution --demo should run without error."""
    result = subprocess.run(
        [sys.executable, str(SKILL_SCRIPT), "--demo", "--output", str(tmp_output)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(SKILL_SCRIPT.parent),
    )
    assert result.returncode == 0, f"stderr: {result.stderr}"
    assert (tmp_output / "report.md").exists()
    assert (tmp_output / "result.json").exists()
    assert (tmp_output / "figures").exists()
    assert (tmp_output / "tables" / "proportions.csv").exists()


def test_demo_report_content(tmp_output):
    """Report should contain expected sections."""
    subprocess.run(
        [sys.executable, str(SKILL_SCRIPT), "--demo", "--output", str(tmp_output)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(SKILL_SCRIPT.parent),
    )
    report = (tmp_output / "report.md").read_text()
    assert "Deconvolution" in report
    assert "Disclaimer" in report


def test_demo_result_json(tmp_output):
    """result.json should contain expected keys."""
    subprocess.run(
        [sys.executable, str(SKILL_SCRIPT), "--demo", "--output", str(tmp_output)],
        capture_output=True,
        text=True,
        timeout=120,
        cwd=str(SKILL_SCRIPT.parent),
    )
    data = json.loads((tmp_output / "result.json").read_text())
    assert data["skill"] == "bulkrna-deconvolution"
    assert "summary" in data
    assert data["summary"]["n_cell_types"] > 0
