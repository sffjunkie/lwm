from typing import Any

from lwm.helper.color import is_base16, is_color
from lwm.loader.color.model import Base16Colors, NamedColors


def deref_done(data: dict, base16: Base16Colors, named: NamedColors) -> bool:
    for k, v in data.items():
        if isinstance(v, list):
            if not all([is_color(elem) for elem in v]):
                return False
        elif isinstance(v, dict):
            if not deref_done(v, base16, named):
                return False
        elif isinstance(v, str):
            if v in NamedColors.model_fields or is_base16(v):
                if k == v:
                    raise ValueError(
                        "Invalid base16 or named color data: key and value are the same"
                    )
                return False

    return True


def deref_value(value: Any, base16: Base16Colors, named: NamedColors) -> Any:
    if is_color(value):
        return value
    elif is_base16(value):
        return getattr(base16, value)
    elif value in NamedColors.model_fields:
        return getattr(named, value)
    else:
        return value


def deref_data(data: dict, base16: Base16Colors, named: NamedColors) -> dict:
    d = {}
    for name, value in data.items():
        if not isinstance(value, (int, float, bool)):
            if isinstance(value, dict):
                value = deref_data(value, base16, named)
            elif isinstance(value, list):
                value = [deref_value(item, base16, named) for item in value]
            else:
                value = deref_value(value, base16, named)

        d[name] = value
    return d


def deref_colors(
    data: dict, base16: Base16Colors, named: NamedColors, recursion: int = 0
) -> dict:
    while not deref_done(data, base16, named):
        if recursion == 2:
            raise ValueError("Coor deref recursion depth exceeded")
        data = deref_data(data, base16, named)
        recursion = recursion + 1
    return data
