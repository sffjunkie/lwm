import re

from libqtile import layout
from libqtile.config import Match, _Match
from qtile_extras.layout.decorations.borders import RoundedCorners

from lwm.loader.model import Definitions


def float_rules(defs: Definitions) -> list[_Match]:
    matches = []
    for app in defs.floating.matches.appid:
        if app not in defs.match.defs:
            continue
        appid_matches = defs.match.defs[app].appid
        matches.extend([Match(wm_class=re.compile(appid)) for appid in appid_matches])

    for app in defs.floating.matches.title:
        if app not in defs.match.defs:
            continue
        title_matches = defs.match.defs[app].title
        matches.extend([Match(title=title) for title in title_matches])

    return matches + layout.Floating.default_float_rules


def build_floating(defs: Definitions) -> layout.Floating:
    return layout.Floating(
        float_rules=float_rules(defs),
        border_width=defs.layout.common.border_width,
        border_normal=RoundedCorners(
            colour=defs.color.named.floating_border_normal,
        ),
        border_focus=RoundedCorners(
            colour=defs.color.named.floating_border_focus,
        ),
    )
