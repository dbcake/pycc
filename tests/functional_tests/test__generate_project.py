# import json
# import subprocess
from pathlib import Path
from typing import Dict
from copy import deepcopy

# import pytest
# import shutil

from tests.utils.project import generate_project


def test__can_generate_project(project_dir: Path):
    """ """

    assert project_dir.exists()
    # generated_project_dir = PROJECT_DIR / "sample" / cookicutter_config["default_context"]["repo_name"]
