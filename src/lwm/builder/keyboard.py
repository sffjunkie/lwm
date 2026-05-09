# Keybindings for groups are defined in group.py

from libqtile.config import Key

from lwm.model.definitions import Definitions
from lwm.helper.key import modifier_group, qtilecmd


def build_keys(defs: Definitions) -> list[Key]:
    keys = []
    for key_def in defs.key.defs:
        key = key_def.key
        if key_def.modifier_group is not None:
            modifiers = modifier_group(defs, key_def.modifier_group)
        else:
            modifiers = []

        funcs = qtilecmd(defs, key_def.command)

        kwargs = {}
        if key_def.desc:
            kwargs["desc"] = key_def.desc

        keys.append(
            Key(
                modifiers,
                key,
                *funcs,
                **kwargs,
                swallow=key_def.swallow,
            )
        )

    return keys
