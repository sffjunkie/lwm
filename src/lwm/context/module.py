from typing import Literal, Any

from lwm.context.bar import BarContext
from lwm.helper.color import contrast_color, opacity_to_hex
from lwm.helper.merge import merge_props
from lwm.loader.color.deref import deref_colors
from lwm.model.definitions import Definitions

GroupPosition = Literal["start", "middle", "end"]


class ModuleContext:
    _props: dict[str, Any]
    text_font_family: str
    text_font_size: int
    icon_font_family: str
    icon_font_size: int
    logo_font_family: str
    logo_font_size: int

    opacity: float
    background_rgb: str
    background_rgba: str
    foreground_rgb: str

    def __init__(
        self,
        bar_ctx: BarContext,
        defs: Definitions,
        props: dict = {},
    ):
        self.bar_ctx = bar_ctx
        self.defs = defs
        self._props = {}
        self.props = props

    @property
    def props(self) -> dict:
        return self._props or {}

    @props.setter
    def props(self, new_props: dict) -> None:
        new_props = (
            deref_colors(
                new_props,
                self.defs.color.base16,
                self.defs.color.named,
            )
            or {}
        )

        self.text_font_family = new_props.get(
            "text_font_family", self.bar_ctx.text_font_family
        )
        self.text_font_size = new_props.get(
            "text_font_size", self.bar_ctx.text_font_size
        )
        self.icon_font_family = new_props.get(
            "icon_font_family", self.bar_ctx.icon_font_family
        )
        self.icon_font_size = new_props.get(
            "icon_font_size", self.bar_ctx.icon_font_size
        )
        self.logo_font_family = new_props.get(
            "logo_font_family", self.bar_ctx.logo_font_family
        )
        self.logo_font_size = new_props.get(
            "logo_font_size", self.bar_ctx.logo_font_size
        )

        self.opacity = new_props.get("opacity", self.bar_ctx.opacity)
        opacity_str = opacity_to_hex(self.opacity)

        self.background_rgb = new_props.get(
            "background", self.defs.color.named.widget_bg[0]
        )
        self.background_rgba = f"{self.background_rgb}{opacity_str}"

        fg_dark = self.defs.color.named.widget_fg_dark
        fg_light = self.defs.color.named.widget_fg_light
        self.foreground_rgb = new_props.get(
            "foreground",
            contrast_color(self.background_rgb, dark=fg_dark, light=fg_light),
        )

        bg = next(self.bar_ctx.widget_bg_iter)
        fg = self.bar_ctx.widget_fg(bg)

        self._props = merge_props(
            self._props,
            {
                "foreground": fg,
                "background": bg,
            },
            new_props,
        )
