from libqtile.layout.base import _SimpleLayoutBase
from libqtile import layout
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.model.definitions import Definitions

_layouts = {
    "bsp": layout.Bsp,
    "columns": layout.Columns,
    "floating": layout.Floating,
    "matrix": layout.Matrix,
    "max": layout.Max,
    "plasma": layout.Plasma,
    "ratiotile": layout.RatioTile,
    "screensplit": layout.ScreenSplit,
    "slice": layout.Slice,
    "spiral": layout.Spiral,
    "stack": layout.Stack,
    "tile": layout.Tile,
    "treetab": layout.TreeTab,
    "verticaltile": layout.VerticalTile,
    "monadtall": layout.MonadTall,
    "monadthreecol": layout.MonadThreeCol,
    "monadwide": layout.MonadWide,
    "zoomy": layout.Zoomy,
}


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
        layouts.append(_layouts[layout_name](**d))

    return layouts
