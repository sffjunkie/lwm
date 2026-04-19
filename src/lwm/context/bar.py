from typing import Literal
from itertools import cycle
from typing import Any

from lwm.config.bar.default import DEFAULT_BAR_HEIGHT, DEFAULT_BAR_MARGIN
from lwm.config.font.default import DEFAULT_FONTS
from lwm.config.typedef import Config
from lwm.helper.color import opacity_to_hex, contrast_color
from lwm.context.module import ModuleContext
from lwm.helper.merge import override_parameters

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
        self.position = position
        self.config = config
        self.props = props
        self.height = props.get(
            "height",
            config["bar"][position].get(
                "height",
                DEFAULT_BAR_HEIGHT,
            ),
        )
        self.margin = props.get(
            "margin",
            config["bar"][position].get(
                "margin",
                DEFAULT_BAR_MARGIN,
            ),
        )
        self.text_font_family = props.get(
            "text_font_family",
            config["font"]["text"].get(
                "family",
                DEFAULT_FONTS["text"]["family"],
            ),
        )
        self.text_font_size = props.get(
            "text_font_size",
            config["font"]["text"].get(
                "size",
                DEFAULT_FONTS["text"]["size"],
            ),
        )
        self.icon_font_family = props.get(
            "icon_font_family",
            config["font"]["icon"].get(
                "family",
                DEFAULT_FONTS["icon"]["family"],
            ),
        )
        self.icon_font_size = props.get(
            "icon_font_size",
            config["font"]["icon"].get(
                "size",
                DEFAULT_FONTS["icon"]["size"],
            ),
        )
        self.logo_font_family = props.get(
            "logo_font_family",
            config["font"]["logo"].get(
                "family",
                DEFAULT_FONTS["logo"]["family"],
            ),
        )
        self.logo_font_size = props.get(
            "logo_font_size",
            config["font"]["logo"].get(
                "size",
                DEFAULT_FONTS["logo"]["size"],
            ),
        )

        self.background_rgb = props.get(
            "background", config["color"]["named"]["bar_bg"]
        )

        self.opacity = props.get("opacity", config["bar"][position]["opacity"])
        self.opacity_hex = opacity_to_hex(self.opacity)
        self.background_rgba = f"{self.background_rgb}{self.opacity_hex}"

        self.widget_bg_iter = cycle(self.config["color"]["named"]["widget_bg"])

    def widget_fg(self, bg_color: str):
        return contrast_color(
            bg_color,
            self.config["color"]["named"]["widget_fg_light"],
            self.config["color"]["named"]["widget_fg_dark"],
        )

    def module_ctx(self, props: dict[str, Any] | None = None) -> ModuleContext:
        props = props or {}

        bg = next(self.widget_bg_iter)
        fg = self.widget_fg(bg)

        return ModuleContext(
            self,
            config=self.config,
            props=override_parameters(
                {
                    "foreground": fg,
                    "background": bg,
                },
                props,
            ),
        )
