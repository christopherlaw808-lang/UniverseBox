"""Shared logging utilities for UniverseBox tooling."""

from __future__ import annotations

import logging
import sys
from typing import Optional

_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"


def configure_logging(level: str = "INFO") -> None:
    """Configure global logging once.

    Args:
        level: Desired logging level string (e.g. INFO, DEBUG).
    """
    root = logging.getLogger()
    if root.handlers:
        root.setLevel(level.upper())
        return

    logging.basicConfig(
        level=level.upper(),
        format=_LOG_FORMAT,
        stream=sys.stdout,
    )


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a logger with shared formatting configured."""
    configure_logging()
    return logging.getLogger(name or "universebox")


def fail_with_actionable_error(logger: logging.Logger, message: str, action: str, code: int = 1) -> int:
    """Log a clear error + action and return an error code for CLI exit."""
    logger.error("%s", message)
    logger.error("Action: %s", action)
    return code
