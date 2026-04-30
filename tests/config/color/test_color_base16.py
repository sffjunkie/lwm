from pathlib import Path
from lwm.loader.color.base16 import (
    load_base16_color_scheme,
    base16_colors_from_config,
)


def test_load_base16_color_scheme(test_data: Path):
    scheme = load_base16_color_scheme(
        Path("gruvbox-material-dark-soft.yaml"),
        test_data / "config" / "color_scheme",
    )

    assert scheme is not None
    assert scheme.base07 == "#fbf1c7"


def test_load_base16_colors_from_scheme(test_data: Path):
    config = {
        "scheme_dir": test_data / "config" / "color_scheme",
        "scheme_name": "gruvbox-material-dark-soft.yaml",
    }

    base16_colors = base16_colors_from_config(config)

    assert base16_colors is not None
    assert base16_colors.base07 == "#fbf1c7"


def test_load_base16_colors_from_colors(test_data: Path):
    config = {
        "scheme_dir": test_data / "config" / "color_scheme",
        "scheme_name": "gruvbox-material-dark-soft.yaml",
        "colors": {
            "base07": "#282828",
        },
    }

    base16_colors = base16_colors_from_config(config)

    assert base16_colors is not None
    assert base16_colors.base07 == "#282828"
