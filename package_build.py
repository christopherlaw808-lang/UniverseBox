"""Prepare build/package readiness for UniverseBox."""

from __future__ import annotations

from pathlib import Path

from tools.build.package_project import verify_build_ready


def main() -> int:
    issues = verify_build_ready()
    if issues:
        print("Build is not ready:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    out_dir = Path("dist")
    out_dir.mkdir(exist_ok=True)
    manifest = out_dir / "build_manifest.txt"
    manifest.write_text("UniverseBox build-ready prototype\n", encoding="utf-8")
    print(f"Build preparation complete. Manifest written to {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
