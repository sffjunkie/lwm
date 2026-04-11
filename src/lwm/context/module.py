from typing import Literal

from lwm.helper.color import opacity_to_str
from lwm.config.typedef import Config
from lwm.context.bar import BarContext

GroupPosition = Literal["start", "middle", "end"]


class ModuleContext:
    text_font_family: str
    text_font_size: int
    icon_font_family: str
    icon_font_size: int
    logo_font_family: str
    logo_font_size: int

    background_rgba: str
    opacity: float

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
        self.background_rgb = props.get("background", bar_ctx.background_rgba)

        self.opacity_str = opacity_to_str(self.opacity)
        self.background_rgba = f"{self.background_rgb}{self.opacity_str}"

    def merge_parameters(self, base: dict, *overrides: dict):
        cfg = base.copy()
        for override in overrides:
            cfg.update(override)
        return cfg
