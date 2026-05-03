from lwm.loader.color.base16 import base16_colors_from_data
from lwm.loader.color.named import named_colors_from_data, named_colors_deref
from lwm.loader.color.model import ColorDefs, Base16Colors, NamedColors


def colordefs_from_data(data: dict) -> ColorDefs:
    color_data = data.get("color", None)
    if color_data is None:
        named_colors = NamedColors()
        base16_colors = Base16Colors()
    else:
        if (base16 := color_data.get("base16", None)) is not None:
            base16_colors = base16_colors_from_data(base16)
        else:
            base16_colors = Base16Colors()

        if (named := color_data.get("named", None)) is not None:
            named_colors = named_colors_from_data(named, base16_colors)
        else:
            named_colors = named_colors_deref(dict(NamedColors()), base16_colors)

    return ColorDefs(base16=base16_colors, named=named_colors)
