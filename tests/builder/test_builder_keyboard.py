from pathlib import Path
from lwm.load import load_defs
from lwm.builder.keyboard import build_keys


def test_build_keyboard(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    keys = build_keys(defs)

    assert keys is not None
