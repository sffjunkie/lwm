from lwm.loader.color.deref import deref_colors
from lwm.loader.color.model import Base16Colors, NamedColors
from lwm.loader.layout.model import LayoutDefs


def layoutdef_from_data(
    data: dict, base16: Base16Colors, named: NamedColors
) -> LayoutDefs:
    layout: LayoutDefs
    layout_data = data.get("layout", None)
    if layout_data is None:
        layout = LayoutDefs()
    else:
        layout = LayoutDefs(**layout_data)

    tc = deref_colors(dict(layout), base16, named)
    return layout.model_copy(update=tc)
