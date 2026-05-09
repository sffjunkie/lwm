from libqtile.config import DropDown, Key, ScratchPad
from libqtile.lazy import lazy

from lwm.anchor import WindowLocation, anchor_window
from lwm.helper.key import modifier_group
from lwm.helper.terminal import terminal_run_command
from lwm.model.definitions import Definitions


def build_scratchpads(defs: Definitions) -> list[ScratchPad]:
    ncmpcpp_dimension = anchor_window(
        location=WindowLocation.BottomCenter,
        width=0.5,
        height=0.5,
    )
    home_automation_dimension = anchor_window(
        location=WindowLocation.BottomCenter,
        width=0.5,
        height=0.5,
    )

    return [
        ScratchPad(
            "0",
            dropdowns=[
                DropDown(
                    name="music-player",
                    cmd=terminal_run_command(
                        command=["ncmpcpp"],
                        terminal=defs.app.terminal,
                    ),
                    height=ncmpcpp_dimension.height,
                    width=ncmpcpp_dimension.width,
                    x=ncmpcpp_dimension.x,
                    y=ncmpcpp_dimension.y,
                    opacity=1.0,
                    warp_pointer=False,
                ),
            ],
            single=True,
        ),
        ScratchPad(
            "home-automation",
            dropdowns=[
                DropDown(
                    name="home-automation",
                    cmd=f"{defs.app.browser} https://hass.looniversity.net",
                    height=home_automation_dimension.height,
                    width=home_automation_dimension.width,
                    x=home_automation_dimension.x,
                    y=home_automation_dimension.y,
                    opacity=1.0,
                    warp_pointer=False,
                ),
            ],
            single=True,
        ),
    ]


def build_scratchpad_keys(defs: Definitions) -> list[Key]:
    app_launch = modifier_group(defs, "app_launch")
    return [
        Key(
            app_launch,
            "F8",
            lazy.group["0"].dropdown_toggle("music-player"),
        ),
        Key(
            app_launch,
            "Home",
            lazy.group["home-automation"].dropdown_toggle("home-automation"),
        ),
    ]
