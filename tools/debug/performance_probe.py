"""Lightweight timing probe helpers."""

from __future__ import annotations

import time
from collections.abc import Callable
from typing import TypeVar

T = TypeVar("T")


def measure(label: str, fn: Callable[[], T]) -> tuple[T, float, str]:
    start = time.perf_counter()
    result = fn()
    elapsed = time.perf_counter() - start
    return result, elapsed, f"{label} took {elapsed:.3f}s"
