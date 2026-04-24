# from lwm.config.color.default import DEFAULT_NAMED_COLORS
from lwm.config.color.deref import deref_colors
from lwm.config.color.model import Base16Colors, NamedColors


def named_colors_deref(colors: dict, base16: Base16Colors) -> NamedColors:
    new_colors = deref_colors(colors, base16, NamedColors())
    return NamedColors(**new_colors)


def named_colors_from_config(config: dict, base16: Base16Colors) -> NamedColors:
    new = NamedColors()
    for k, v in config.items():
        new.__setattr__(k.lower(), v)

    return named_colors_deref(dict(new), base16)
