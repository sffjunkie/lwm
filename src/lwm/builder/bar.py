"""Bars for Qtile"""

import os
from itertools import cycle
from typing import Iterator

from libqtile.bar import Bar as QBar
from qtile_extras.widget import Spacer as QSpacer

from lwm.context.bar import BarContext
from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT, contrast_color
from lwm.model.bar import Bars
from lwm.model.definitions import Definitions
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
from lwm.qmodule.weather import Weather
from lwm.qmodule.window_name import WindowName


def fg_color(defs: Definitions):
    def func(bg_color: str) -> str:
        return contrast_color(
            bg_color,
            defs.color.named.widget_fg_light,
            defs.color.named.widget_fg_dark,
        )

    return func


def widget_bg_iter(defs: Definitions) -> Iterator:
    return cycle(getattr(defs.color.named, "widget_bg", "000000"))


def build_top_bar(defs: Definitions) -> QBar | None:
    if defs.bar.top is None:
        return None

    idx = 0

    bar_context = BarContext(position="top", defs=defs)
    bar_context.props = {
        "height": defs.bar.top.height,
        "margin": defs.bar.top.margin,
        "opacity": defs.bar.top.opacity,
    }

    widgets = []

    ctx = ModuleContext(
        bar_context,
        defs,
        props={
            "background": TRANSPARENT,
            "foreground": TRANSPARENT,
        },
    )
    separator = Separator(ctx)

    user_menu_context = ModuleContext(
        bar_context,
        defs,
        props={"background": "base0f"},
    )
    group_box_context = ModuleContext(bar_context, defs)
    current_layout_context = ModuleContext(bar_context, defs)

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

    window_name_context = ModuleContext(bar_context, defs)

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
        defs,
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

    date_time_context = ModuleContext(bar_context, defs)
    system_menu_context = ModuleContext(
        bar_context,
        defs,
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


def build_bottom_bar(defs: Definitions) -> QBar | None:
    if defs.bar.bottom is None:
        return None

    idx = 0

    bar_context = BarContext(position="bottom", defs=defs)
    bar_context.props = {
        "height": defs.bar.bottom.height,
        "margin": defs.bar.bottom.margin,
        "opacity": defs.bar.bottom.opacity,
    }

    widgets = []

    separator = Separator(
        ModuleContext(
            bar_context,
            defs=defs,
        )
    )

    # region start
    network_status_context = ModuleContext(
        bar_context,
        defs,
        props={
            "network": {
                "interface": "wlp3s0",
            },
        },
    )

    memory_status_context = ModuleContext(
        bar_context,
        defs,
        props={
            "memory": {
                "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            },
        },
    )

    cpu_usage_context = ModuleContext(bar_context, defs)
    cpu_temp_context = ModuleContext(bar_context, defs)

    bluetooth_context = ModuleContext(
        bar_context,
        defs,
        props={
            "menu": {
                "menu_font": defs.font.text.family,
                "menu_fontsize": defs.font.text.size,
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
        defs,
        props={
            "music": {
                "status_format": "󰝚 {title} | 󰠃 {artist} | 󰀥 {album} {play_status}",
                "idle_format": "Play queue empty",
            },
        },
    )
    end.append(MusicStatus(music_status_context))

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


def build_left_bar(defs: Definitions) -> QBar | None:
    return None


def build_right_bar(defs: Definitions) -> QBar | None:
    return None


def build_bars(defs: Definitions) -> Bars:
    bars: Bars = {}

    if defs.bar.top is not None:
        bars["top"] = build_top_bar(defs=defs)

    if defs.bar.bottom is not None:
        bars["bottom"] = build_bottom_bar(defs=defs)

    if defs.bar.left is not None:
        bars["left"] = build_left_bar(defs=defs)

    if defs.bar.right is not None:
        bars["right"] = build_right_bar(defs=defs)

    return bars
