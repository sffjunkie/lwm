from typing import Literal

from lwm.helper.merge import override_parameters
from lwm.helper.color import opacity_to_hex
from lwm.config.typedef import Config
from lwm.context.bar import BarContext
from lwm.helper.color import contrast_color

GroupPosition = Literal["start", "middle", "end"]


class ModuleContext:
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
        config: Config,
        props: dict = {},
    ):
        self.bar_ctx = bar_ctx
        self.config = config
        self.props = props

    @property
    def props(self) -> dict:
        return self._props or {}

    @props.setter
    def props(self, new_props: dict) -> None:
        new_props = new_props or {}

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
            "background", self.config["color"]["named"]["widget_bg"][0]
        )
        self.background_rgba = f"{self.background_rgb}{opacity_str}"

        fg_dark = self.config["color"]["named"]["widget_fg_dark"]
        fg_light = self.config["color"]["named"]["widget_fg_light"]
        self.foreground_rgb = new_props.get(
            "foreground",
            contrast_color(self.background_rgb, dark=fg_dark, light=fg_light),
        )

        bg = next(self.bar_ctx.widget_bg_iter)
        fg = self.bar_ctx.widget_fg(bg)

        self._props = override_parameters(
            self._props,
            {
                "foreground": fg,
                "background": bg,
            },
            new_props,
        )
