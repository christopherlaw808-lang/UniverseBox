#!/usr/bin/env python3
"""Run pytest with a readable summary for UniverseBox."""

from __future__ import annotations

import argparse
import subprocess
import sys

from tools.common.logging_utils import configure_logging, fail_with_actionable_error, get_logger


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log-level", default="INFO", help="Logging level")
    parser.add_argument("pytest_args", nargs="*", help="Additional pytest arguments")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    configure_logging(args.log_level)
    logger = get_logger("run_tests")

    cmd = [sys.executable, "-m", "pytest", "-q", *args.pytest_args]
    logger.info("Running test command: %s", " ".join(cmd))

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.stdout:
        print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)

    if proc.returncode == 0:
        logger.info("Test run passed.")
        return 0

    return fail_with_actionable_error(
        logger,
        f"Pytest failed with exit code {proc.returncode}.",
        "Inspect output above, fix failing tests, and rerun `python3 run_tests.py`.",
        code=proc.returncode,
    )


if __name__ == "__main__":
    raise SystemExit(main())
