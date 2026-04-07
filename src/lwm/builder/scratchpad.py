from libqtile.config import DropDown, Key, ScratchPad  # type: ignore
from libqtile.lazy import lazy  # type: ignore

from lwm.anchor import WindowLocation, anchor_window
from lwm.config.typedef import Config
from lwm.terminal import terminal_run_command


def build_scratchpads(config: Config) -> list[ScratchPad]:
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
                        terminal=config["app"]["terminal"],
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
                    cmd=f"{config['app']['browser']} https://hass.looniversity.net",
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


def build_scratchpad_keys(config: Config) -> list[Key]:
    Super = config["key"]["cmd"]
    Alt = config["key"]["alt"]
    return [
        Key(
            [Super, Alt],
            "F8",
            lazy.group["0"].dropdown_toggle("music-player"),
        ),
        Key(
            [Super, Alt],
            "Home",
            lazy.group["home-automation"].dropdown_toggle("home-automation"),
        ),
    ]
