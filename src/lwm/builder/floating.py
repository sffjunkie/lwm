from libqtile import layout
from libqtile.config import _Match
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.helper.match import build_matches
from lwm.loader.model import Definitions


def build_float_rules(defs: Definitions) -> list[_Match]:
    matches = []
    for match_name in defs.floating.matches:
        matches.extend(build_matches(defs, match_name))

    return layout.Floating.default_float_rules + matches


def build_floating(defs: Definitions) -> layout.Floating:
    return layout.Floating(
        float_rules=build_float_rules(defs),
        border_width=defs.layout.base.border_width,
        border_normal=RoundedCorners(
            colour=defs.color.named.floating_border_normal,
        ),
        border_focus=RoundedCorners(
            colour=defs.color.named.floating_border_focus,
        ),
    )
