"""Event system extension hook."""


def emit_event(event_name: str) -> str:
    """Return acknowledgement for future event dispatch implementation."""
    return f"event_stub:{event_name}"
