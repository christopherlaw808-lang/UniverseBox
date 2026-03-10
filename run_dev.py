"""Run local validation checks and provide Godot launch guidance."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from python.core.logging_system import configure_logging
from tools.build.package_project import verify_build_ready
from tools.validation.config_validator import validate_config_files
from tools.validation.schema_validator import validate_project_settings


def main() -> int:
    configure_logging()
    issues = []
    issues.extend(validate_config_files())
    issues.extend(validate_project_settings())
    issues.extend(verify_build_ready())

    if issues:
        print("Validation issues found:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Validation passed.")
    print("Running Python smoke tests...")
    test_rc = subprocess.run([sys.executable, "run_tests.py"], check=False).returncode
    if test_rc != 0:
        return test_rc

    project_file = Path("godot/project.godot")
    if not project_file.exists():
        print("Godot project file missing.")
        return 1

    godot_bin = shutil.which("godot4") or shutil.which("godot")
    if godot_bin:
        print(f"Launching Godot via {godot_bin}...")
        return subprocess.run([godot_bin, "--path", "godot"], check=False).returncode

    print("Godot binary not found in PATH.")
    print("Open godot/project.godot manually in Godot 4.x.")
    print("Starter world config:")
    print(json.dumps(json.loads(Path("config/project_settings.json").read_text()), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
