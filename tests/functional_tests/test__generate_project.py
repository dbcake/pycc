"""Test the generate_project function."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """docstring"""
    assert project_dir.exists()
