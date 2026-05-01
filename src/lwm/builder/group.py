import re

from libqtile.config import Match
from libqtile.lazy import lazy
from libqtile.config import Key, Group

# from lwm.builder.match_registry import MATCH_REGISTRY
from lwm.loader.model import Config
from lwm.loader.group.model import GroupDef

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


def build_groups(config: Config) -> list[Group]:
    groupdefs = config.group
    groups = groupdefs.groups
    decoration_style = getattr(groupdefs, "decoration", DECORATION)

    groups = []
    for idx, grp in enumerate(groupdefs.groups, start=1):
        kwargs = {}

        matches = build_match(grp)
        if matches:
            kwargs["matches"] = matches

        group = Group(
            name=str(idx),
            label=grp.name + decoration(idx, decoration_style),
            **kwargs,
        )
        groups.append(group)
    return groups


def build_group_keys(config: Config) -> list[Key]:
    groupdefs = config.group

    cmd = config.key.mapping.cmd
    shift = config.key.mapping.shift
    keys = []
    for idx, _ in enumerate(groupdefs.groups, start=1):
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


def build_match(group: GroupDef) -> list[Match]:
    matches = []
    matchdef = getattr(group, "matches", None)
    if matchdef is not None:
        wmclass_regexes = matchdef.get("app_id", [])
        if wmclass_regexes:
            for regex in wmclass_regexes:
                match = Match(wm_class=re.compile(regex))
                matches.append(match)
    return matches
