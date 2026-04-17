from typing import TypedDict

Color = str


class Base16Colors(TypedDict):
    base00: str
    base01: str
    base02: str
    base03: str
    base04: str
    base05: str
    base06: str
    base07: str
    base08: str
    base09: str
    base0a: str
    base0b: str
    base0c: str
    base0d: str
    base0e: str
    base0f: str


class Base16(TypedDict):
    colors: Base16Colors
    scheme_name: str | None
    scheme_dir: str | None


class NamedColors(TypedDict):
    group_current_fg: Color
    group_current_bg: Color
    group_active_fg: Color
    group_active_bg: Color
    group_inactive_fg: Color
    group_inactive_bg: Color

    bar_fg: Color
    bar_bg: Color

    widget_bg: list[str]
    widget_fg_dark: Color
    widget_fg_light: Color

    window_border_focus: Color
    window_border_normal: Color


class Colors(TypedDict):
    base16: Base16Colors
    named: NamedColors
