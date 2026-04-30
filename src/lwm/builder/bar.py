"""Bars for Qtile"""

import os
from itertools import cycle
from typing import Iterator

from libqtile.bar import Bar as QBar
from qtile_extras.widget import Spacer as QSpacer

from lwm.helper.color import contrast_color, TRANSPARENT
from lwm.loader.bar.model import BarLocation
from lwm.loader.typedef import Config
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
            config.color.named.widget_fg_light,
            config.color.named.widget_fg_dark,
        )

    return func


def widget_bg_iter(config: Config) -> Iterator:
    return cycle(getattr(config.color.named, "widget_bg", "000000"))


def build_top_bar(config: Config) -> QBar | None:
    if config.bar.top is None:
        return None

    idx = 0

    bar_context = BarContext(position="top", config=config)
    bar_context.props = {
        "height": config.bar.top.height,
        "margin": config.bar.top.margin,
        "opacity": config.bar.top.opacity,
    }

    widgets = []

    ctx = ModuleContext(
        bar_context,
        config,
        props={
            "background": TRANSPARENT,
            "foreground": TRANSPARENT,
        },
    )
    separator = Separator(ctx)

    user_menu_context = ModuleContext(
        bar_context,
        config,
        props={"background": "base0f"},
    )
    group_box_context = ModuleContext(bar_context, config)
    current_layout_context = ModuleContext(bar_context, config)

    # region start
    start: list[WidgetModule] = [
        UserMenu(user_menu_context),
        GroupBox(group_box_context),
        CurrentLayout(current_layout_context),
    ]

    for idx, group in enumerate(start):
        if idx != 0:
            widgets.extend(separator.widgets())

        widgets.extend(group.widgets(group_id=idx))
    # endregion

    window_name_context = ModuleContext(bar_context, config)

    # region middle
    middle: list[WidgetModule] = [
        WindowName(window_name_context),
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
    weather_context = ModuleContext(
        bar_context,
        config,
        props={
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

    date_time_context = ModuleContext(bar_context, config)
    system_menu_context = ModuleContext(
        bar_context,
        config,
        props={"background": "base0f"},
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
    if config.bar.bottom is None:
        return None

    idx = 0

    bar_context = BarContext(position="bottom", config=config)
    bar_context.props = {
        "height": config.bar.bottom.height,
        "margin": config.bar.bottom.margin,
        "opacity": config.bar.bottom.opacity,
    }

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            config=config,
        )
    )

    # region start
    network_status_context = ModuleContext(
        bar_context,
        config,
        props={
            "network": {
                "interface": getattr(config.device, "net", "eth0"),
            },
        },
    )

    memory_status_context = ModuleContext(
        bar_context,
        config,
        props={
            "memory": {
                "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            },
        },
    )

    cpu_usage_context = ModuleContext(bar_context, config)
    cpu_temp_context = ModuleContext(bar_context, config)

    bluetooth_context = ModuleContext(
        bar_context,
        config,
        props={
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
    music_status_context = ModuleContext(
        bar_context,
        config,
        props={
            "music": {
                "status_format": "󰝚 {title} | 󰠃 {artist} | 󰀥 {album} {play_status}",
                "idle_format": "Play queue empty",
            },
        },
    )
    end.append(MusicStatus(music_status_context))

    volume_control = config.controller.volume
    if volume_control is not None:
        volume_context = ModuleContext(
            bar_context,
            config,
            props={
                "volume": {
                    "volume_up_command": f"{volume_control} up",
                    "volume_down_command": f"{volume_control} down",
                    "mute_command": f"{volume_control} toggle",
                    "volume_app": config.controller.audio,
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


def build_left_bar(config: Config) -> QBar | None:
    return None


def build_right_bar(config: Config) -> QBar | None:
    return None


def build_bars(config: Config) -> Bars:
    bars: Bars = {}

    if config.bar.top is not None:
        bars["top"] = build_top_bar(config=config)

    if config.bar.bottom is not None:
        bars["bottom"] = build_bottom_bar(config=config)

    if config.bar.left is not None:
        bars["left"] = build_left_bar(config=config)

    if config.bar.right is not None:
        bars["right"] = build_right_bar(config=config)

    return bars
