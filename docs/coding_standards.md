# Coding Standards

## General Principles

- Prefer clarity over cleverness.
- Keep modules small and purpose-focused.
- Use contract-first design at Python↔Godot boundaries.
- Avoid hidden side effects; make data flow explicit.

## Python Standards

- Follow PEP 8 style and type-hint public interfaces.
- Use `ruff` for linting and `black` for formatting.
- Keep deterministic behavior for simulation logic.
- Isolate randomness through seeded RNG abstractions.
- Write unit tests for pure logic and integration tests for boundaries.

## Godot Standards

- Use clear scene naming and folder organization by feature.
- Keep scripts focused on presentation/input concerns.
- Avoid embedding simulation logic in rendering scripts.
- Use signals/events for decoupled interaction where possible.

## Contract & Schema Standards

- Version external payload structures.
- Validate all incoming command/snapshot payloads.
- Fail fast on incompatible schema versions.
- Document every contract field and semantic meaning.

## Logging & Error Handling

- Emit structured logs with timestamp, subsystem, and context.
- Use explicit error codes for boundary failures.
- Include seed/tick identifiers in simulation errors.

## Documentation Standards

- Update docs with every architectural or contract change.
- Keep README command examples current.
- Add migration notes when changing snapshot/event schemas.
