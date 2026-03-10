from python.core.config_loader import ConfigLoader


def test_config_loader_fallback_for_missing_file(tmp_path):
    loader = ConfigLoader(config_dir=str(tmp_path))
    fallback = {"default_seed": 7}
    data = loader.load("missing", fallback=fallback)
    assert data["default_seed"] == 7
