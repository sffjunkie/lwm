from typing import Literal

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

        self.text_font_family = props.get("text_font_family", bar_ctx.text_font_family)
        self.text_font_size = props.get("text_font_size", bar_ctx.text_font_size)
        self.icon_font_family = props.get("icon_font_family", bar_ctx.icon_font_family)
        self.icon_font_size = props.get("icon_font_size", bar_ctx.icon_font_size)
        self.logo_font_family = props.get("logo_font_family", bar_ctx.logo_font_family)
        self.logo_font_size = props.get("logo_font_size", bar_ctx.logo_font_size)

        self.opacity = props.get("opacity", bar_ctx.opacity)
        opacity_str = opacity_to_hex(self.opacity)

        self.background_rgb = props.get(
            "background", config["color"]["named"]["widget_bg"][0]
        )
        self.background_rgba = f"{self.background_rgb}{opacity_str}"

        fg_dark = config["color"]["named"]["widget_fg_dark"]
        fg_light = config["color"]["named"]["widget_fg_light"]
        self.foreground_rgb = props.get(
            "foreground",
            contrast_color(self.background_rgb, dark=fg_dark, light=fg_light),
        )
