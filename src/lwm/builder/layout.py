from libqtile.layout.base import _SimpleLayoutBase
from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.loader.model import Definitions


def _layout_type_args(defs: Definitions, layout: str) -> dict:
    return getattr(defs.layout, layout, None) or {}


def build_layouts(defs: Definitions) -> list[_SimpleLayoutBase]:
    if defs.layout.base.rounded:
        borders = {
            "border_focus": RoundedCorners(colour=defs.color.named.tiled_border_focus),
            "border_normal": RoundedCorners(
                colour=defs.color.named.tiled_border_normal
            ),
        }
    else:
        borders = {}

    layout_args = dict(defs.layout.base) | borders

    return [
        MonadTall(**(layout_args | _layout_type_args(defs, "MonadTall"))),
        Max(**(layout_args | _layout_type_args(defs, "Max"))),
    ]
