# Module Guide

This guide defines expected responsibilities for major project modules.

## `python/sim/`

**Purpose:** Authoritative simulation core.

- `kernel/`: tick runner, scheduler, system registration.
- `state/`: world state models, persistence, migrations.
- `systems/`: terrain/ecology/population/etc. domain systems.
- `commands/`: command definitions, validation, application.
- `events/`: event emission and subscriptions.

## `python/bridge/`

**Purpose:** Communication adapters between Python and Godot.

- Transport adapters (socket/websocket/local IPC).
- Serialization/deserialization for shared schemas.
- Retry/timeout and boundary diagnostics.

## `shared/contracts/`

**Purpose:** Cross-runtime schema definitions.

- Snapshot/event/command structures.
- Version metadata and compatibility utilities.
- Fixtures for schema regression tests.

## `godot/client/`

**Purpose:** Rendering, input, and UI layer.

- Snapshot ingestion and scene update systems.
- UI panels (world inspector, logs, controls).
- Input mapping and command dispatch to Python.

## `tools/`

**Purpose:** Developer support tools.

- Replay tools and state inspectors.
- Profiling scripts and benchmark harnesses.
- Data generation utilities for testing scenarios.

## Ownership Rules

- Simulation logic must not live in Godot modules.
- Rendering/UI logic must not live in Python simulation modules.
- Shared contracts are the only approved boundary format.
