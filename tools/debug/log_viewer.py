"""CLI helper for tailing the project log file."""

from pathlib import Path


LOG_PATH = Path("logs/universebox.log")


def main(lines: int = 20) -> int:
    if not LOG_PATH.exists():
        print("No log file found yet.")
        return 1
    content = LOG_PATH.read_text(encoding="utf-8").splitlines()
    for line in content[-lines:]:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
