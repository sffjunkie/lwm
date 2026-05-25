from libqtile.layout.base import _SimpleLayoutBase
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.model.definitions import Definitions


def _layout_type_args(defs: Definitions, layout: str) -> dict:
    return getattr(defs.layout, layout, None) or {}


def build_layouts(defs: Definitions) -> list[_SimpleLayoutBase]:
    if defs.layout.base.border_rounded:
        borders = {
            "border_focus": RoundedCorners(colour=defs.color.named.tiled_border_focus),
            "border_normal": RoundedCorners(
                colour=defs.color.named.tiled_border_normal
            ),
        }
    else:
        borders = {}

    base_args = dict(defs.layout.base) | borders
    layouts = []
    for layout_name in defs.layout.default_layouts:
        d = dict(getattr(defs.layout.layouts, layout_name)) | base_args
        layouts.append(d)

    return layouts
