from pathlib import Path
from lwm.load import load_defs
from lwm.builder.layout import build_layouts


def test_build_layout(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    layouts = build_layouts(defs)

    assert layouts is not None
