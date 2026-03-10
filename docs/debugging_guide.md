# Debugging Guide

## Logs
- Main log file: `logs/universebox.log`.
- Tail logs: `python tools/debug/log_viewer.py`.

## Validation errors
- Run `python run_dev.py` for config/schema/build checks.
- Fix missing files and malformed JSON first.

## Seed system checks
- Run tests: `python run_tests.py`.
- Deterministic generation validated in `test_world_seed.py` and `test_planet_generator.py`.

## Startup diagnostics
1. Run `python setup_env.py`.
2. Run `python run_dev.py`.
3. Open `godot/project.godot` with Godot 4.x.
4. Verify main scene and debug overlay labels update during runtime.
