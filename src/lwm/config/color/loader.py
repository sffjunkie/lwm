from libqtile.log_utils import logger

from lwm.config.color.base16 import base16_colors_from_config
from lwm.config.color.default import (
    DEFAULT_BASE16_COLORS,
    DEFAULT_COLORS,
    DEFAULT_NAMED_COLORS,
)
from lwm.config.color.named import named_colors_from_config, named_colors_deref
from lwm.config.color.typedef import Colors


def colordefs_default() -> Colors:
    new_colors = DEFAULT_COLORS.copy()
    new_colors["named"] = named_colors_deref(
        dict(DEFAULT_NAMED_COLORS),
        DEFAULT_BASE16_COLORS,
    )
    return new_colors


def colordefs_from_config(config: dict) -> Colors:
    color_data = config.get("color", None)
    if color_data is None:
        color = colordefs_default()
    else:
        if (base16 := color_data.get("base16", None)) is not None:
            base16_colors = base16_colors_from_config(base16)
        else:
            base16_colors = DEFAULT_BASE16_COLORS.copy()

        if (named := color_data.get("named", None)) is not None:
            named_colors = named_colors_from_config(named, base16_colors)
        else:
            named_colors = named_colors_deref(dict(DEFAULT_NAMED_COLORS), base16_colors)

        color: Colors = {
            "base16": base16_colors,
            "named": named_colors,
        }

    return color
