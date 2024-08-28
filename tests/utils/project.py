import json
import subprocess
from pathlib import Path
from typing import Dict
from copy import deepcopy

# import pytest
# import shutil
from tests.consts import PROJECT_DIR


def initialize_git_repo(repo_dir: Path):
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)

    subprocess.run(["git", "branch", "-M", "main"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "'feat: initial commit by pytest'"], cwd=repo_dir, check=True)


def generate_project(template_values: Dict[str, str]):
    template_values_: Dict[str, str] = deepcopy(template_values)
    cookicutter_config = {"default_context": template_values_}
    cookicutter_config_fpath = PROJECT_DIR / "cookiecutter-test-config.json"
    cookicutter_config_fpath.write_text(json.dumps(cookicutter_config))

    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookicutter_config_fpath),
    ]

    print(" ".join(cmd))
    subprocess.run(cmd, check=True)
    generated_repo_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    return generated_repo_dir
