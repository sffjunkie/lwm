from libqtile.widget import base  # type: ignore
from qtile_extras.widget import OpenWeather  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.helper.merge import override_parameters
from lwm.helper.color import TRANSPARENT


class Weather(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        weather_props = {
            "padding": 12,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
        }

        decorations = None
        if group_id != -1:
            decorations = [
                RectDecoration(
                    colour=background_color,
                    radius=5,
                    filled=True,
                    group=True,
                    group_id=group_id,
                )
            ]
            weather_props["background"] = TRANSPARENT

        props = override_parameters(
            weather_props,
            self.ctx.props.pop("weather", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        weather = OpenWeather(**props)

        widgets = [weather]
        return widgets
