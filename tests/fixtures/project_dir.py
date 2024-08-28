"""Pytest fixtures for test projects."""

import shutil
import subprocess
from pathlib import Path

import pytest

from tests.utils.project import (  # pylint: disable=no-name-in-module
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Path:  # type: ignore
    """Generate project and return the path."""
    template_values = {
        "repo_name": "test-repo",
        "package_import_name": "default-package-name",
    }
    generated_repo_dir: Path = generate_project(
        template_values=template_values
    )
    try:
        initialize_git_repo(repo_dir=generated_repo_dir)
        subprocess.run(
            ["make", "lint-ci"], cwd=generated_repo_dir, check=False
        )
        yield generated_repo_dir
    finally:
        shutil.rmtree(path=generated_repo_dir)
