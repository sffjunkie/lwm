from libqtile import layout
from libqtile.config import Match, _Match
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.loader.model import Config


def float_rules(config: Config) -> list[_Match]:
    return [
        Match(wm_class=float_match) for float_match in config.floating.match["wm_appid"]
    ] + layout.Floating.default_float_rules


def build_floating(config: Config) -> layout.Floating:
    return layout.Floating(
        float_rules=float_rules(config),
        border_width=config.layout.common.border_width,
        border_normal=RoundedCorners(
            colour=config.color.named.floating_border_normal,
        ),
        border_focus=RoundedCorners(
            colour=config.color.named.floating_border_focus,
        ),
    )
