from pathlib import Path
from lwm.loader import load_config
from lwm.builder.bar import build_bars
from lwm.helper.color import is_color


def test_bars_not_base16(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_config(data_path.absolute())

    assert config is not None
    bars = build_bars(config)

    top = bars.get("top", None)
    assert top is not None
    assert len(top.widgets) > 1

    for widget in top.widgets:
        assert is_color(str(widget.background))
