import re

from libqtile.config import Match

from lwm.model.definitions import Definitions


def build_matches(defs: Definitions, match: str) -> list[Match]:
    if match not in defs.match.defs:
        return []

    matches = []
    for md in defs.match.defs[match]:
        wm_class = None
        if md.appid is not None:
            wm_class = re.compile(md.appid)

        title = None
        if md.title is not None:
            title = re.compile(md.title)

        matches.append(Match(wm_class=wm_class, title=title))

    return matches
