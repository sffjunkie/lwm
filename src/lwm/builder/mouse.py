# Keybindings for groups are defined in groups.py

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from lwm.loader.model import Definitions


def build_buttons(defs: Definitions):
    cmd = defs.key.modifier.cmd
    return [
        Drag(
            [cmd],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [cmd],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([cmd], "Button2", lazy.window.bring_to_front()),
    ]
