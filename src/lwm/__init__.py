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
from lwm.load import load_defs
from lwm.runtime_info import log_runtime_info
from lwm.secret.loader import load_secrets

is_under_pytest = "pytest" in sys.modules

if not is_under_pytest:
    log_runtime_info()

    secrets = load_secrets()
    defs = load_defs()

    if defs is None:
        logger.error("lwm: Unable to load configuration")
        raise ValueError("Loading definitions failed")
    else:
        screens = build_screens(defs)

        floating_layout = build_floating(defs)
        groups = build_groups(defs) + build_scratchpads(defs)
        keys = build_keys(defs) + build_group_keys(defs) + build_scratchpad_keys(defs)
        layouts = build_layouts(defs)
        mouse = build_buttons(defs)

        extension_defaults = defs.extension.model_copy()
        widget_defaults = defs.widget.model_copy()

        auto_fullscreen = True
        bring_front_click = "floating_only"
        cursor_warp = False
        floats_kept_above = True
        focus_on_window_activation = "smart"
        follow_mouse_focus = False
        wmname = "lwm"

        wl_input_rules = build_input_rules(defs)

        wl_xcursor_theme = defs.cursor.name
        wl_xcursor_size = defs.cursor.size


@hook.subscribe.startup_once
def autostart() -> None:
    subprocess.run(
        [
            "systemctl",
            "--user",
            "import-environment",
            "DISPLAY",
            "WAYLAND_DISPLAY",
            "XCURSOR_SIZE",
            "XCURSOR_THEME",
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
