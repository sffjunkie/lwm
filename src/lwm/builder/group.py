from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from lwm.loader.group.model import GroupDef

from lwm.helper.match import build_matches
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
        layout = grp.layout or defs.group.common.layout

        matches = []
        for match_name in grp.matches:
            matches.extend(build_matches(defs, match_name))

        group = Group(
            name=str(idx),
            label=grp.name + decoration(idx, decoration_style),
            layout=layout,
            matches=matches or None,
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


def build_match(defs: Definitions, group: GroupDef) -> list[Match]:
    matches = []

    for match_name in group.matches:
        matches.extend(build_matches(defs, match_name))

    return matches
