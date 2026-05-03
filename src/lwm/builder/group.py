import re

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from lwm.loader.group.model import GroupDef
from lwm.loader.match.model import MatchDefs

# from lwm.builder.match_registry import MATCH_REGISTRY
from lwm.loader.model import Definitions

SUPERSCRIPT = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
SUBSCRIPT = ["₀", "₁", "₂", "₃", "₄", "₅", "₆", "₇", "₈", "₉"]

DECORATION = "superscript"


def decoration(group_idx: int, style: str) -> str:
    if style == "superscript":
        return SUPERSCRIPT[group_idx]
    elif style == "subscript":
        return SUBSCRIPT[group_idx]
    else:
        return ""


def build_groups(defs: Definitions) -> list[Group]:
    decoration_style = defs.group.common.decoration

    groups = []
    for idx, grp in enumerate(defs.group.defs, start=1):
        kwargs = {}

        layout = grp.layout or defs.group.common.layout

        matches = build_match(grp, defs.match)
        if matches:
            kwargs["matches"] = matches

        group = Group(
            name=str(idx),
            label=grp.name + decoration(idx, decoration_style),
            layout=layout,
            **kwargs,
        )
        groups.append(group)
    return groups


def build_group_keys(defs: Definitions) -> list[Key]:
    cmd = defs.key.mapping.cmd
    shift = defs.key.mapping.shift
    keys = []
    for idx, _ in enumerate(defs.group.defs, start=1):
        name = str(idx)
        keys.append(
            Key(
                [cmd],
                str(idx),
                lazy.group[name].toscreen(toggle=True),
                desc=f"Switch to group {name}",
            )
        )
        keys.append(
            Key(
                [cmd, shift],
                str(idx),
                lazy.window.togroup(name),
                desc=f"Send current window to group {name}",
            )
        )
    return keys


def build_match(group: GroupDef, match: MatchDefs) -> list[Match]:
    matches = []

    appid_matches = []
    for app_name in group.matches.appid:
        nm = match.defs[app_name].appid
        appid_matches.extend(nm)
    matches.extend([Match(wm_class=m) for m in appid_matches])

    title_matches = []
    for app_name in group.matches.title:
        nm = match.defs[app_name].title
        title_matches.extend(nm)
    matches.extend([Match(title=re.compile(m)) for m in title_matches])

    return matches
