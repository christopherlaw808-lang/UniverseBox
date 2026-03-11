#!/usr/bin/env python3
"""Check build readiness and prepare packaging artifacts."""

from __future__ import annotations

import argparse

from pathlib import Path

from tools.build.package_project import check_build_readiness, format_build_issues, prepare_packaging
from tools.common.logging_utils import configure_logging, fail_with_actionable_error, get_logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-level", default="INFO", help="Logging level")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure_logging(args.log_level)
    logger = get_logger("package_build")
    root = Path(__file__).resolve().parent

    ok, issues = check_build_readiness(root)
    if not ok:
        return fail_with_actionable_error(
            logger,
            format_build_issues(issues),
            "Resolve readiness issues and rerun `python3 package_build.py`.",
        )

    out_dir = prepare_packaging(root)
    logger.info("Packaging prep complete. Output directory: %s", out_dir)
    logger.info("You can now run Godot export commands to create distributable builds.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
