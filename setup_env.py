#!/usr/bin/env python3
"""Set up and validate local development environment for UniverseBox."""

from __future__ import annotations

import argparse
from pathlib import Path

from tools.bootstrap.project_initializer import ensure_required_paths, initialize_project_structure
from tools.bootstrap.verify_environment import (
    check_executable,
    check_paths,
    check_python_version,
    summarize_results,
)
from tools.common.logging_utils import configure_logging, fail_with_actionable_error, get_logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-level", default="INFO", help="Logging level (default: INFO)")
    parser.add_argument(
        "--required-path",
        action="append",
        default=["README.md", "tools"],
        help="Path that must exist relative to project root (can be repeated).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure_logging(args.log_level)
    logger = get_logger("setup_env")
    root = Path(__file__).resolve().parent

    logger.info("Initializing baseline project directories...")
    initialize_project_structure(root)

    checks = [check_python_version(), check_executable("python3")]
    checks.extend(check_paths(root, args.required_path))

    if not summarize_results(checks):
        return fail_with_actionable_error(
            logger,
            "Environment checks failed.",
            "Resolve the failing checks and re-run: python3 setup_env.py",
        )

    missing = ensure_required_paths(root, args.required_path)
    if missing:
        return fail_with_actionable_error(
            logger,
            "Required paths are still missing after initialization.",
            "Create the missing paths manually or adjust --required-path values.",
        )

    logger.info("Environment setup complete.")
    logger.info("Next steps: install dependencies (if any) and run `python3 run_dev.py`.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
