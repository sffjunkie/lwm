# Keybindings for groups are defined in groups.py

from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from lwm.config.typedef import Config


def build_buttons(config: Config):
    cmd = config["key"].cmd
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
