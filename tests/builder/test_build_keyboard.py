from pathlib import Path

from lwm.loader import load_config


def test_key_defs(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_config(data_path)
    assert config is not None
    assert len(config.key.definitions) == 3

    assert config.key.definitions[2].key == "Right"
