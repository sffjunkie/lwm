from lwm.config.color.default import DEFAULT_NAMED_COLORS
from lwm.config.color.deref import deref_colors
from lwm.config.color.typedef import Base16Colors, NamedColors


def named_colors_deref(colors: dict, base16: Base16Colors) -> NamedColors:
    new_colors = deref_colors(colors, base16, DEFAULT_NAMED_COLORS)

    named = DEFAULT_NAMED_COLORS.copy()
    for k, v in new_colors.items():
        named[k.lower()] = v

    return named


def named_colors_from_config(config: dict, base16: Base16Colors) -> NamedColors:
    new = DEFAULT_NAMED_COLORS.copy()
    for k, v in config.items():
        new[k.lower()] = v

    return named_colors_deref(dict(new), base16)
