"""Environment verification helpers for local development."""

from __future__ import annotations

import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from tools.common.logging_utils import get_logger

logger = get_logger(__name__)

MIN_PYTHON = (3, 10)


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    details: str
    action: str | None = None


def check_python_version(minimum: tuple[int, int] = MIN_PYTHON) -> CheckResult:
    current = sys.version_info[:2]
    ok = current >= minimum
    details = f"Python {current[0]}.{current[1]} detected (required >= {minimum[0]}.{minimum[1]})."
    action = None if ok else "Install or switch to a supported Python version before running scripts."
    return CheckResult(name="python_version", ok=ok, details=details, action=action)


def check_executable(name: str) -> CheckResult:
    found = shutil.which(name)
    ok = found is not None
    details = f"Executable '{name}' resolved to: {found or 'not found'}."
    action = None if ok else f"Install '{name}' and ensure it is available on your PATH."
    return CheckResult(name=f"exe:{name}", ok=ok, details=details, action=action)


def check_paths(project_root: Path, required_paths: Iterable[str]) -> list[CheckResult]:
    results: list[CheckResult] = []
    for rel_path in required_paths:
        target = project_root / rel_path
        ok = target.exists()
        action = None if ok else f"Create the missing path '{rel_path}' or run setup_env.py to scaffold it."
        results.append(
            CheckResult(
                name=f"path:{rel_path}",
                ok=ok,
                details=f"{target} {'exists' if ok else 'is missing'}.",
                action=action,
            )
        )
    return results


def summarize_results(results: Iterable[CheckResult]) -> bool:
    all_ok = True
    for result in results:
        if result.ok:
            logger.info("[OK] %s - %s", result.name, result.details)
        else:
            all_ok = False
            logger.error("[FAIL] %s - %s", result.name, result.details)
            if result.action:
                logger.error("Action: %s", result.action)
    return all_ok
