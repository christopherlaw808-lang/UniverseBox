"""Starter helper for export preset checks."""

from pathlib import Path


def main() -> int:
    export_file = Path("godot/export_presets.cfg")
    if export_file.exists():
        print("Export presets found.")
        return 0
    print("No export presets configured yet (optional for prototype).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
