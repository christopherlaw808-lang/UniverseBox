"""Setup helper for UniverseBox local environment readiness."""

from __future__ import annotations

import subprocess
import sys

from tools.bootstrap.verify_environment import verify


def main() -> int:
    if sys.version_info < (3, 12):
        print("ERROR: Python 3.12+ required.")
        return 1

    issues = verify()
    if issues:
        print("Environment issues:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("Environment checks passed.")
    print("Installing dependencies from requirements.txt ...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
