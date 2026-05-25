from pathlib import Path
from lwm.load import load_defs


def test_loader_layout(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    assert defs.layout.layouts.monadtall is not None
    assert defs.layout.layouts.monadtall.border_width == 6

    assert defs.layout.base.border_rounded
