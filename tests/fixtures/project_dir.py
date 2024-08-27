import json
import subprocess
from pathlib import Path
from typing import Dict
from copy import deepcopy
import pytest
import shutil

from tests.utils.project import generate_project


@pytest.fixture(scope="session")
def project_dir() -> Path:
    template_values = {
        "repo_name": "test-repo",
    }
    generated_repo_dir: Path = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(path=generated_repo_dir)
