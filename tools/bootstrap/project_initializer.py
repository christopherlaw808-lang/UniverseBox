"""Project initializer entrypoint."""

from tools.bootstrap.verify_environment import verify


def main() -> int:
    issues = verify()
    if issues:
        print("Environment issues detected:")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("UniverseBox environment looks healthy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
