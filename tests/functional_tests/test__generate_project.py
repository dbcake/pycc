"""Test the generate_project function."""

from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Ensure the directory can be generated."""
    assert project_dir.exists()
