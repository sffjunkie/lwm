import os
from pathlib import Path

import yaml

from lwm.loader.color.model import Base16Colors
from lwm.helper.color import is_base16, is_color


def load_base16_color_scheme(
    scheme_name: Path, scheme_dir: Path | None = None
) -> Base16Colors | None:
    if scheme_dir is None:
        xdg_data_home = os.environ.get("XDG_DATA_HOME", None)
        if xdg_data_home is not None:
            search_folder = Path(xdg_data_home) / "base16" / "schemes"
        else:
            search_folder = Path(__file__).parent / "schemes"
    else:
        search_folder = Path(scheme_dir)

    scheme_path = Path(scheme_name)
    if scheme_path.suffix != ".yaml":
        scheme_path = scheme_path.with_suffix(".yaml")

    for file_path in search_folder.rglob(os.path.join("**", "*.yaml")):
        if file_path.name.endswith(scheme_path.name):
            with file_path.open("r") as fp:
                color_yaml = yaml.load(fp, Loader=yaml.SafeLoader)
                base16_colors = Base16Colors()
                for name, value in color_yaml["palette"].items():
                    if is_base16(name) and is_color(value):
                        base16_colors.__setattr__(name.lower(), value.lower())
                return base16_colors

    return None


def base16_colors_from_data(data: dict) -> Base16Colors:
    scheme_dir = data.get("scheme_dir", None)
    scheme_name = data.get("scheme_name", None)
    if scheme_dir is not None and scheme_name is not None:
        base16_colors = load_base16_color_scheme(
            scheme_name=scheme_name,
            scheme_dir=scheme_dir,
        )
        if base16_colors is None:
            base16_colors = Base16Colors()
    else:
        base16_colors = Base16Colors()

    override_colors = data.get("colors", {})
    for k, v in override_colors.items():
        if is_base16(k) and is_color(v):
            base16_colors.__setattr__(k, v)

    return base16_colors
