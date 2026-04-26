from typing import Self
from pydantic import BaseModel, model_validator

Color = str


class Base16Colors(BaseModel):
    base00: str = "#24273a"  # base
    base01: str = "#1e2030"  # mantle
    base02: str = "#363a4f"  # surface0
    base03: str = "#494d64"  # surface1
    base04: str = "#5b6078"  # surface2
    base05: str = "#cad3f5"  # text
    base06: str = "#f4dbd6"  # rosewater
    base07: str = "#b7bdf8"  # lavender
    base08: str = "#ed8796"  # red
    base09: str = "#f5a97f"  # peach
    base0a: str = "#eed49f"  # yellow
    base0b: str = "#a6da95"  # green
    base0c: str = "#8bd5ca"  # teal
    base0d: str = "#8aadf4"  # blue
    base0e: str = "#c6a0f6"  # mauve
    base0f: str = "#f0c6c6"  # flamingo


class Base16(BaseModel):
    colors: Base16Colors
    scheme_name: str | None = None
    scheme_dir: str | None = None


class NamedColors(BaseModel):
    group_current_fg: Color = "base05"
    group_current_bg: Color = "base0f"
    group_active_fg: Color = "base01"
    group_active_bg: Color = "base09"
    group_inactive_fg: Color = "base03"
    group_inactive_bg: Color = "base03"

    bar_fg: Color = "base01"
    bar_bg: Color = "base0f"

    widget_bg: list[str] = ["base06"]
    widget_fg_dark: Color = "base00"
    widget_fg_light: Color = "base01"

    tiled_border_focus: Color = "base06"
    tiled_border_normal: Color = "base01"

    floating_border_focus: Color | None = None
    floating_border_normal: Color | None = None

    @model_validator(mode="after")
    def border_colors(self) -> Self:
        self.floating_border_focus = (
            self.floating_border_focus or self.tiled_border_focus
        )
        self.floating_border_normal = (
            self.floating_border_normal or self.tiled_border_normal
        )
        return self


class Colors(BaseModel):
    base16: Base16Colors
    named: NamedColors
