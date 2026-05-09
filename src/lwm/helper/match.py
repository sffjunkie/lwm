import re

from libqtile.config import Match

from lwm.model.definitions import Definitions


def build_matches(defs: Definitions, match_name: str) -> list[Match]:
    if match_name not in defs.match.defs:
        return []

    matches = []
    for md in defs.match.defs[match_name]:
        match_args = {}
        if md.appid is not None:
            match_args["wm_class"] = re.compile(md.appid)

        if md.title is not None:
            match_args["title"] = re.compile(md.title)

        matches.append(Match(**match_args))

    return matches
