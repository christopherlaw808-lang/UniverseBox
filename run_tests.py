"""Test runner wrapper with readable output."""

from __future__ import annotations

import subprocess
import sys


def main() -> int:
    result = subprocess.run([sys.executable, "-m", "pytest", "python/tests", "-q"], check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
