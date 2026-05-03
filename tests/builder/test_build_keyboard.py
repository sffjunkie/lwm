from pathlib import Path

from lwm.loader import load_defs


def test_key_defs(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_defs(data_path)
    assert config is not None
    assert len(config.key.defs) == 3

    assert config.key.defs[2].key == "Right"
