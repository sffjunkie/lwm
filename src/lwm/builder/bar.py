"""Bars for Qtile"""

import os
from itertools import cycle
from typing import Iterator

from libqtile.log_utils import logger
from libqtile.bar import Bar as QBar  # type: ignore
from qtile_extras.widget import Spacer as QSpacer  # type: ignore

from lwm.helper.color import contrast_color, TRANSPARENT
from lwm.config.bar.typedef import BarLocation
from lwm.config.typedef import Config
from lwm.context.bar import BarContext
from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.qmodule.bluetooth import Bluetooth
from lwm.qmodule.cpu_temp_status import CPUTempStatus
from lwm.qmodule.cpu_usage_status import CPUUsageStatus
from lwm.qmodule.current_layout import CurrentLayout
from lwm.qmodule.date_time import DateTime
from lwm.qmodule.group_box import GroupBox
from lwm.qmodule.memory_status import MemoryStatus
from lwm.qmodule.music_status import MusicStatus
from lwm.qmodule.network_status import NetworkStatus
from lwm.qmodule.separator import Separator
from lwm.qmodule.system_menu import SystemMenu
from lwm.qmodule.user_menu import UserMenu
from lwm.qmodule.volume_status import VolumeStatus
from lwm.qmodule.weather import Weather
from lwm.qmodule.window_name import WindowName

Bars = dict[BarLocation, QBar | None]


def fg_color(config: Config):
    def func(bg_color: str) -> str:
        return contrast_color(
            bg_color,
            config["color"]["named"]["widget_fg_light"],
            config["color"]["named"]["widget_fg_dark"],
        )

    return func


def widget_bg_iter(config: Config) -> Iterator:
    return cycle(config["color"]["named"].get("widget_bg", "000000"))


def build_top_bar(config: Config) -> QBar | None:
    idx = 0
    named_colors = config["color"]["named"]
    logger.warning(named_colors)

    bg_iter = widget_bg_iter(config)
    fg_func = fg_color(config)

    bar_context = BarContext(
        position="top",
        config=config,
        props={
            "height": config["bar"]["top"]["height"],
            "margin": config["bar"]["top"]["margin"],
            "opacity": config["bar"]["top"]["opacity"],
        },
    )

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            config=config,
        )
    )

    # region start
    bg = next(bg_iter)
    fg = fg_func(bg)
    start: list[WidgetModule] = [
        UserMenu(
            ModuleContext(
                bar_context,
                config=config,
                props={
                    "foreground": fg,
                    "background": bg,
                },
            )
        ),
        GroupBox(
            ModuleContext(
                bar_context,
                config=config,
                props={
                    "background": named_colors["panel_bg"],
                },
            )
        ),
        CurrentLayout(
            ModuleContext(
                bar_context,
                config=config,
                props={
                    "background": named_colors["panel_bg"],
                },
            )
        ),
    ]

    for idx, group in enumerate(start):
        if idx != 0:
            widgets.extend(separator.widgets())

        widgets.extend(group.widgets(group_id=idx))
    # endregion

    # region middle
    middle: list[WidgetModule] = [
        WindowName(
            ModuleContext(
                bar_context,
                config=config,
                props={
                    # "background": next(bg_iter),
                    "group": 4,
                    "background": named_colors["panel_bg"],
                },
            )
        ),
    ]

    if middle == []:
        widgets.append(QSpacer(background=TRANSPARENT))
    else:
        widgets.extend(separator.widgets())
        for idx, group in enumerate(middle, start=idx + 1):
            widgets.extend(group.widgets(group_id=idx))
        widgets.extend(separator.widgets())
    # endregion

    # region end
    bg = next(bg_iter)
    fg = fg_func(bg)
    weather_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
            "weather": {
                "app_key": os.environ.get("OWM_API_KEY", ""),
                "coordinates": {
                    "latitude": os.environ.get("USER_LOCATION_LATITUDE", "51.5"),
                    "longitude": os.environ.get("USER_LOCATION_LONGITUDE", "-0.15"),
                },
                "format": "{main_temp:.1f}/{main_feels_like:.1f}°{units_temperature} {icon}",
            },
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    date_time_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    system_menu_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
        },
    )

    end: list[WidgetModule] = [
        Weather(weather_context),
        DateTime(date_time_context),
        SystemMenu(system_menu_context),
    ]

    group_id = idx + 1
    for idx, group in enumerate(end):
        widgets.extend(group.widgets(group_id=group_id + idx))
        if idx != len(end) - 1:
            widgets.extend(separator.widgets())

    # endregion

    return QBar(
        widgets=widgets,
        size=bar_context.height,
        margin=bar_context.margin,
    )


def build_bottom_bar(config: Config) -> QBar | None:
    idx = 0
    bg_iter = widget_bg_iter(config)
    fg_func = fg_color(config)

    bar_context = BarContext(
        position="bottom",
        config=config,
        props={
            "height": config["bar"]["bottom"]["height"],
            "margin": config["bar"]["bottom"]["margin"],
            "opacity": config["bar"]["bottom"]["opacity"],
        },
    )

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            config=config,
        )
    )

    # region start
    bg = next(bg_iter)
    fg = fg_func(bg)
    network_status_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "network": {
                "interface": config["device"].get("net", "eth0"),
            },
            "foreground": fg,
            "background": bg,
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    memory_status_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "memory": {
                "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            },
            "foreground": fg,
            "background": bg,
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    cpu_usage_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    cpu_temp_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
        },
    )

    bg = next(bg_iter)
    fg = fg_func(bg)
    bluetooth_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "foreground": fg,
            "background": bg,
            "menu": {
                "menu_font": "JetBrainsMono Nerd Font",
                "menu_fontsize": 16,
                "menu_width": 400,
            },
        },
    )

    start: list[WidgetModule] = [
        NetworkStatus(network_status_context),
        MemoryStatus(memory_status_context),
        CPUUsageStatus(cpu_usage_context),
        CPUTempStatus(cpu_temp_context),
        Bluetooth(bluetooth_context),
    ]

    for idx, group in enumerate(start):
        if idx != 0:
            widgets.extend(separator.widgets())

        widgets.extend(group.widgets(group_id=idx))
    # endregion

    # region middle
    middle: list[WidgetModule] = []

    if middle == []:
        widgets.append(QSpacer(background=TRANSPARENT))
    else:
        widgets.extend(separator.widgets())
        for idx, group in enumerate(middle, start=idx + 1):
            widgets.extend(group.widgets(group_id=idx))
        widgets.extend(separator.widgets())
    # endregion

    # region end
    end: list[WidgetModule] = []
    bg = next(bg_iter)
    fg = fg_func(bg)
    music_status_context = ModuleContext(
        bar_context,
        config=config,
        props={
            "music": {
                "status_format": "󰝚 {title} | 󰠃 {artist} | 󰀥 {album} {play_status}",
                "idle_format": "Play queue empty",
            },
            "foreground": fg,
            "background": next(bg_iter),
        },
    )
    end.append(MusicStatus(music_status_context))

    volume_control = config["controller"]["volume"]
    bg = next(bg_iter)
    fg = fg_func(bg)
    if volume_control is not None:
        volume_context = ModuleContext(
            bar_context,
            config=config,
            props={
                "foreground": fg,
                "background": next(bg_iter),
                "volume": {
                    "volume_up_command": f"{volume_control} up",
                    "volume_down_command": f"{volume_control} down",
                    "mute_command": f"{volume_control} toggle",
                    "volume_app": config["controller"]["audio"],
                },
            },
        )
        end.append(VolumeStatus(volume_context))

    group_id = idx + 1
    for idx, group in enumerate(end):
        widgets.extend(group.widgets(group_id=group_id + idx))
        if idx != len(end) - 1:
            widgets.extend(separator.widgets())
    # endregion

    return QBar(
        widgets=widgets,
        size=bar_context.height,
        margin=bar_context.margin,
    )


def build_bars(config: Config) -> Bars:
    bars: Bars = {
        "left": None,
        "right": None,
    }

    if "top" in config["bar"]:
        bars["top"] = build_top_bar(config=config)

    if "bottom" in config["bar"]:
        bars["bottom"] = build_bottom_bar(config=config)

    return bars
