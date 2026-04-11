from typing import Literal

from qtile_extras.widget.decorations import PowerLineDecoration  # type: ignore

from lwm.config.typedef import Config
from lwm.helper.color import opacity_to_str
from lwm.config.bar.default import DEFAULT_BAR_HEIGHT, DEFAULT_BAR_MARGIN


BarPosition = Literal["top", "bottom", "left", "right"]


class BarContext:
    height: int
    margin: tuple[int, int, int, int]
    powerline_start: list[PowerLineDecoration]
    powerline_end: list[PowerLineDecoration]

    text_font_family: str
    text_font_size: int
    icon_font_family: str
    icon_font_size: int
    logo_font_family: str
    logo_font_size: int

    background_rgb: str
    opacity: float

    def __init__(
        self,
        position: BarPosition,
        config: Config,
        props: dict = {},
    ):
        self.position = position
        self.config = config
        self.props = props

        self.height = props.get("height", DEFAULT_BAR_HEIGHT)
        self.margin = props.get("margin", DEFAULT_BAR_MARGIN)

        self.text_font_family = props.get(
            "text_font_family", config["font"]["text"]["family"]
        )
        self.text_font_size = props.get(
            "text_font_size", config["font"]["text"]["size"]
        )
        self.icon_font_family = props.get(
            "icon_font_family", config["font"]["icon"]["family"]
        )
        self.icon_font_size = props.get(
            "icon_font_size", config["font"]["icon"]["size"]
        )
        self.logo_font_family = props.get(
            "logo_font_family", config["font"]["logo"]["family"]
        )
        self.logo_font_size = props.get(
            "logo_font_size", config["font"]["logo"]["size"]
        )

        background = props.get("background", None)
        if background is None:
            bar_theme = config["bar"].get(self.position, None)

            if bar_theme is not None:
                background = config["color"]["named"].get("panel_bg", "000000")
            else:
                background = "000000"
        self.background_rgb = background

        self.opacity = props.get("opacity", 1.0)
        self.opacity_str = opacity_to_str(self.opacity)
        self.background_rgba = f"{self.background_rgb}{self.opacity_str}"

        if (powerline := props.get("powerline", None)) is not None:
            start = powerline.get("start", None)
            if start is not None:
                self.powerline_start = [PowerLineDecoration(path=start)]
                self.powerline_start = []

            if (end := powerline.get("end", None)) is not None:
                self.powerline_end = [PowerLineDecoration(path=end)]
            else:
                self.powerline_end = []

        else:
            self.powerline_start = []
            self.powerline_end = []
