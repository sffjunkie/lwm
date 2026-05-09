from pathlib import Path
from lwm.load import load_defs
from lwm.builder.floating import build_floating


def test_build_floating(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_defs(data_path.absolute())

    assert config is not None
    floating = build_floating(config)

    assert floating.border_focus is not None
    assert floating.border_focus.colour == "#f4dbd6"
