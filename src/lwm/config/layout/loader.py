from lwm.config.color.deref import deref_colors
from lwm.config.color.typedef import Base16Colors, NamedColors
from lwm.config.layout.default import DEFAULT_LAYOUT
from lwm.config.layout.typedef import LayoutDefs


def layoutdef_from_config(
    config: dict, base16: Base16Colors, named: NamedColors
) -> LayoutDefs:
    layout: LayoutDefs
    layout_data = config.get("layout", None)
    if layout_data is None:
        layout = DEFAULT_LAYOUT.copy()
    else:
        layout = layout_data

    tc = deref_colors(dict(layout), base16, named)
    layout.update(tc)
    return layout
