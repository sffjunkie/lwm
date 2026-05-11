from lwm.loader.color.deref import deref_colors
from lwm.model.color import Base16Colors, NamedColors


def named_colors_deref(defs: dict, base16: Base16Colors) -> NamedColors:
    new_colors = deref_colors(defs, base16, NamedColors())
    return NamedColors(**new_colors)


def named_colors_from_data(defs: dict, base16: Base16Colors) -> NamedColors:
    new = NamedColors()
    for k, v in defs.items():
        new.__setattr__(k.lower(), v)

    return named_colors_deref(dict(new), base16)
