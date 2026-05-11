from pathlib import Path
from lwm.load import load_defs
from lwm.builder.bar import build_bars
from lwm.helper.color import is_color


def test_bars_not_base16(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    bars = build_bars(defs)

    top = bars.get("top", None)
    assert top is not None
    assert len(top.widgets) > 1

    for widget in top.widgets:
        assert is_color(str(widget.background))
