"""Central logging helpers for UniverseBox."""

from __future__ import annotations

import logging
from typing import Optional


def get_logger(name: str = "universebox", level: int = logging.INFO) -> logging.Logger:
    """Return a configured logger instance.

    The logger is configured only once to avoid duplicate handlers.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger


def set_log_level(level: int, name: Optional[str] = None) -> None:
    """Set log level for a named logger or root UniverseBox logger."""
    get_logger(name or "universebox").setLevel(level)
