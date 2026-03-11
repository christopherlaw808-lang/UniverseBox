import json

from universebox.core.config_loader import ConfigLoader, DEFAULT_CONFIG


def test_config_loader_returns_defaults_when_no_path() -> None:
    loader = ConfigLoader()
    config = loader.load()
    assert config == DEFAULT_CONFIG


def test_config_loader_fallback_for_missing_file(tmp_path) -> None:
    loader = ConfigLoader()
    config = loader.load(tmp_path / "missing.json")
    assert config == DEFAULT_CONFIG


def test_config_loader_merges_with_defaults(tmp_path) -> None:
    override = {"simulation": {"tick_duration": 0.25}, "world": {"planet_count": 3}}
    config_file = tmp_path / "config.json"
    config_file.write_text(json.dumps(override), encoding="utf-8")

    config = ConfigLoader().load(config_file)

    assert config["simulation"]["tick_duration"] == 0.25
    assert config["simulation"]["seed"] == DEFAULT_CONFIG["simulation"]["seed"]
    assert config["world"]["planet_count"] == 3
