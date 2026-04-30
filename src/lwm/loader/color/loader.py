from lwm.loader.color.base16 import base16_colors_from_config
from lwm.loader.color.named import named_colors_from_config, named_colors_deref
from lwm.loader.color.model import Colors, Base16Colors, NamedColors


def colordefs_from_config(config: dict) -> Colors:
    color_data = config.get("color", None)
    if color_data is None:
        named_colors = NamedColors()
        base16_colors = Base16Colors()
    else:
        if (base16 := color_data.get("base16", None)) is not None:
            base16_colors = base16_colors_from_config(base16)
        else:
            base16_colors = Base16Colors()

        if (named := color_data.get("named", None)) is not None:
            named_colors = named_colors_from_config(named, base16_colors)
        else:
            named_colors = named_colors_deref(dict(NamedColors()), base16_colors)

    return Colors(base16=base16_colors, named=named_colors)
