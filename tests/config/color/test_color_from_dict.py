from pathlib import Path

from lwm.config.color.loader import colordefs_from_config


def test_color_from_dict(test_data: Path):
    config = {
        "color": {
            "base16": {
                "scheme_dir": test_data / "config" / "color",
                "scheme_name": "gruvbox-material-dark-soft.yaml",
                "colors": {
                    "base07": "#282828",
                },
            },
            "named": {
                "panel_fg": "base07",
            },
        }
    }

    color = colordefs_from_config(config)
    assert color["base16"]["base00"] == "#32302f"
    assert color["named"]["panel_fg"] == "#282828"
