import subprocess
import sys

from libqtile import hook
from libqtile.log_utils import logger

from lwm.builder.floating import build_floating
from lwm.builder.group import build_group_keys, build_groups
from lwm.builder.input import build_input_rules
from lwm.builder.keyboard import build_keys
from lwm.builder.layout import build_layouts
from lwm.builder.mouse import build_buttons
from lwm.builder.scratchpad import build_scratchpad_keys, build_scratchpads
from lwm.builder.screen import build_screens
from lwm.loader import load_defs
from lwm.runtime_info import log_runtime_info
from lwm.secret.loader import load_secrets

is_under_pytest = "pytest" in sys.modules

if not is_under_pytest:
    log_runtime_info()

    secrets = load_secrets()
    config = load_defs()

    if config is None:
        logger.error("lwm: Unable to load configuration")
    else:
        screens = build_screens(config)

        floating_layout = build_floating(config)
        groups = build_groups(config) + build_scratchpads(config)
        keys = (
            build_keys(config)
            + build_group_keys(config)
            + build_scratchpad_keys(config)
        )
        layouts = build_layouts(config)
        mouse = build_buttons(config)

        extension_defaults = config.extension.model_copy()
        widget_defaults = config.widget.model_copy()

        auto_fullscreen = True
        bring_front_click = "floating_only"
        cursor_warp = False
        focus_on_window_activation = "smart"
        follow_mouse_focus = False
        wmname = "lwm"

        wl_input_rules = build_input_rules(config)

        wl_xcursor_size = 32


@hook.subscribe.startup_once
def autostart() -> None:
    subprocess.run(
        [
            "dbus-update-activation-environment",
            "--all",
            "--systemd",
        ],
        check=False,
    )
    subprocess.run(
        [
            "systemctl",
            "--user",
            "start",
            "lde-session.target",
        ],
        check=False,
    )
