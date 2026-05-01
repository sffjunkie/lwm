from pathlib import Path
from lwm.loader import load_config


def test_floating_loader(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_config(data_path.absolute())

    assert config is not None
    assert len(config.floating.match["wm_appid"]) == 8
