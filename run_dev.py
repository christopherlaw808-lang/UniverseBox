#!/usr/bin/env python3
"""Run development validation and optionally launch Godot."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from tools.bootstrap.verify_environment import check_executable, check_paths, summarize_results
from tools.common.logging_utils import configure_logging, fail_with_actionable_error, get_logger
from tools.validation.world_sanity_checks import check_world_directory


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-level", default="INFO", help="Logging level")
    parser.add_argument("--launch", action="store_true", help="Launch Godot after checks pass")
    return parser.parse_args()


def run_smoke_checks(root: Path) -> tuple[bool, list[str]]:
    issues: list[str] = []

    ok, message = check_world_directory(root / "worlds")
    if not ok:
        issues.append(message)

    if not (root / "project.godot").exists():
        issues.append("Missing project.godot. Ensure this repository is a Godot project.")

    return (len(issues) == 0, issues)


def launch_godot(root: Path, logger) -> int:
    godot_bin = "godot4"
    if check_executable(godot_bin).ok:
        logger.info("Launching Godot via '%s'...", godot_bin)
        return subprocess.call([godot_bin, "--path", str(root)])

    return fail_with_actionable_error(
        logger,
        "Could not launch Godot automatically because 'godot4' was not found.",
        "Install Godot 4 and re-run with --launch, or open the project manually.",
    )


def main() -> int:
    args = parse_args()
    configure_logging(args.log_level)
    logger = get_logger("run_dev")
    root = Path(__file__).resolve().parent

    checks = [check_executable("python3"), check_executable("pytest")]
    checks.extend(check_paths(root, ["README.md", "tools", "worlds"]))
    if not summarize_results(checks):
        return fail_with_actionable_error(
            logger,
            "Prerequisite checks failed.",
            "Run `python3 setup_env.py` and install missing tools before development run.",
        )

    ok, issues = run_smoke_checks(root)
    if not ok:
        return fail_with_actionable_error(
            logger,
            "Smoke checks failed:\n- " + "\n- ".join(issues),
            "Fix the listed issues, then rerun `python3 run_dev.py`.",
        )

    logger.info("Validation and smoke checks passed.")

    if args.launch:
        return launch_godot(root, logger)

    logger.info("Launch skipped. To launch automatically, run: python3 run_dev.py --launch")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
