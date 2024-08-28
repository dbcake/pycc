"""Test the makefile functions."""

import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """Run make lint-ci to ensure it passes."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """Run make test to ensure it passes."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
