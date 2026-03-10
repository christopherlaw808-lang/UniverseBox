# Architecture

## Python ↔ Godot relationship

- Python hosts simulation/tooling logic, config handling, persistence, and validation.
- Godot hosts visualization, user controls, and debug overlay presentation.
- A bridge script (`simulation_bridge.gd`) mirrors deterministic generation concepts for in-engine startup.

## Module boundaries

- `python/core`: logging/config/events/services.
- `python/simulation`: deterministic world generation and time loop.
- `python/persistence`: JSON snapshot save/load.
- `python/gameplay`: extension stubs.
- `tools/`: automation, validation, debug CLI helpers.

## Data flow

1. Load settings from `config/`.
2. Initialize simulation controller with seed and map size.
3. Generate deterministic tile/resource state.
4. Update tick based on speed multiplier.
5. Save/load JSON snapshots from `saves/`.

## Simulation loop

`SimulationController.step()` increments tick according to `TimeSystem` state.

## Future expansion

Add ecosystem, civilization, and event modules that consume `WorldState` and publish events through `EventBus`.
