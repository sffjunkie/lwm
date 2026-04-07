from libqtile.layout.max import Max
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.base import _SimpleLayoutBase
from qtile_extras.layout.decorations.borders import RoundedCorners
from lwm.config.typedef import Config


def build_layouts(config: Config) -> list[_SimpleLayoutBase]:
    layout_args = config["layout"]["common"] | {
        "border_focus": RoundedCorners(
            colour=config["color"]["named"]["window_border_focus"]
        ),
        "border_normal": RoundedCorners(
            colour=config["color"]["named"]["window_border_normal"]
        ),
    }
    return [
        MonadTall(**(layout_args | config["layout"].get("MonadTall", {}))),
        Max(**(layout_args | config["layout"].get("Max", {}))),
    ]
