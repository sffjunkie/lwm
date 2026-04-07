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

    background: str
    opacity: float

    def __init__(
        self,
        bar: BarContext,
        config: Config,
        props: dict = {},
    ):
        self.bar = bar
        self.config = config
        self.props = props

        self.text_font_family = props.get("text_font_family", bar.text_font_family)
        self.text_font_size = props.get("text_font_size", bar.text_font_size)
        self.icon_font_family = props.get("icon_font_family", bar.icon_font_family)
        self.icon_font_size = props.get("icon_font_size", bar.icon_font_size)
        self.logo_font_family = props.get("logo_font_family", bar.logo_font_family)
        self.logo_font_size = props.get("logo_font_size", bar.logo_font_size)

        self.opacity = props.get("opacity", bar.opacity)
        self.background_color = props.get("background", bar.background_color)

        self.opacity_str = opacity_to_str(self.opacity)
        self.background = f"{self.background_color}{self.opacity_str}"

    def merge_parameters(self, base: dict, *overrides: dict):
        cfg = base.copy()
        for override in overrides:
            cfg.update(override)
        return cfg
