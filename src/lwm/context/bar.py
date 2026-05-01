from typing import Literal
from itertools import cycle
from typing import Any

from lwm.loader.model import Config
from lwm.helper.color import opacity_to_hex, contrast_color

BarPosition = Literal["top", "bottom", "left", "right"]

px = int


class BarContext:
    height: px
    margin: tuple[px, px, px, px]

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
        position: BarPosition,
        config: Config,
        props: dict = {},
    ):
        self._position = position
        self.config = config
        self.props = props

    @property
    def props(self):
        return self._props

    @props.setter
    def props(self, new_props: dict[str, Any]):
        self._props = new_props or {}
        bar_config = getattr(self.config.bar, self._position)
        self.height = new_props.get("height", bar_config.height)
        self.margin = new_props.get("margin", bar_config.margin)

        self.text_font_family = new_props.get(
            "text_font_family",
            self.config.font.text.family,
        )
        self.text_font_size = new_props.get(
            "text_font_size",
            self.config.font.text.size,
        )
        self.icon_font_family = new_props.get(
            "icon_font_family",
            self.config.font.icon.family,
        )
        self.icon_font_size = new_props.get(
            "icon_font_size",
            self.config.font.icon.size,
        )
        self.logo_font_family = new_props.get(
            "logo_font_family",
            self.config.font.logo.family,
        )
        self.logo_font_size = new_props.get(
            "logo_font_size",
            self.config.font.logo.size,
        )

        self.background_rgb = new_props.get(
            "background", self.config.color.named.bar_bg
        )

        self.opacity = new_props.get("opacity", bar_config.opacity)
        self.opacity_hex = opacity_to_hex(self.opacity)
        self.background_rgba = f"{self.background_rgb}{self.opacity_hex}"

        self.widget_bg_iter = cycle(self.config.color.named.widget_bg)

    def widget_fg(self, bg_color: str):
        return contrast_color(
            bg_color,
            self.config.color.named.widget_fg_light,
            self.config.color.named.widget_fg_dark,
        )
