# UniverseBox Master Project File

This document defines the starter repository layout for UniverseBox, a hybrid Python simulation + Godot game project.

## Repository Structure

```text
.
├── MASTER_PROJECT_FILE.md
├── LICENSE
├── .gitignore
├── .editorconfig
├── pyproject.toml
├── requirements.txt
├── setup_env.py
├── run_tests.py
├── run_dev.py
├── package_build.py
├── docs/
│   ├── README.md
│   ├── architecture.md
│   └── development.md
├── config/
│   ├── README.md
│   ├── settings.example.toml
│   └── logging.yaml
├── tools/
│   ├── bootstrap/
│   │   ├── README.md
│   │   └── init_env.py
│   ├── build/
│   │   ├── README.md
│   │   └── build_package.py
│   ├── debug/
│   │   ├── README.md
│   │   └── inspect_state.py
│   └── validation/
│       ├── README.md
│       └── validate_project.py
├── agents/
│   ├── README.md
│   └── prompts/
│       ├── system_prompt.md
│       └── gameplay_prompt.md
├── python/
│   ├── core/
│   │   ├── __init__.py
│   │   └── engine.py
│   ├── simulation/
│   │   ├── __init__.py
│   │   └── world.py
│   ├── gameplay/
│   │   ├── __init__.py
│   │   └── loop.py
│   ├── persistence/
│   │   ├── __init__.py
│   │   └── save_manager.py
│   └── tests/
│       ├── __init__.py
│       └── test_smoke.py
├── godot/
│   ├── scenes/
│   │   ├── main.tscn
│   │   └── ui/
│   │       └── hud.tscn
│   ├── scripts/
│   │   ├── game.gd
│   │   └── ui/
│   │       └── hud.gd
│   ├── assets/
│   │   └── placeholder/
│   │       ├── textures/
│   │       │   └── README.md
│   │       └── audio/
│   │           └── README.md
│   └── data/
│       └── starter_worlds/
│           └── default_world.json
├── saves/
│   └── .gitkeep
└── logs/
    └── .gitkeep
```

## Baseline Rules

1. Every directory includes at least one meaningful starter file.
2. Python modules should be importable with simple smoke tests.
3. Tooling scripts should be executable from repository root.
4. Godot folders include scene/script/data stubs for immediate iteration.
