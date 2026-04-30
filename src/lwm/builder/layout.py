from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.base import _SimpleLayoutBase
from qtile_extras.layout.decorations.borders import RoundedCorners
from lwm.loader.typedef import Config


def _layout_type_args(config: Config, layout: str) -> dict:
    return getattr(config.layout, layout, None) or {}


def build_layouts(config: Config) -> list[_SimpleLayoutBase]:
    if config.layout.common.rounded:
        borders = {
            "border_focus": RoundedCorners(
                colour=config.color.named.tiled_border_focus
            ),
            "border_normal": RoundedCorners(
                colour=config.color.named.tiled_border_normal
            ),
        }
    else:
        borders = {}

    layout_args = dict(config.layout.common) | borders

    return [
        MonadTall(**(layout_args | _layout_type_args(config, "MonadTall"))),
        Max(**(layout_args | _layout_type_args(config, "Max"))),
    ]
