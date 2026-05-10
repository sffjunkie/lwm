from libqtile.widget import base
from qtile_extras.widget import WiFiIcon as QEWifi
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule


class Wifi(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        wifi_props = {
            "name": "wifi",
            "interface": self.ctx.defs.device.wifi,
            "padding": 8,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "menu_font": self.ctx.text_font_family,
            "menu_fontsize": self.ctx.text_font_size,
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
            wifi_props["background"] = TRANSPARENT

        props = merge_props(
            wifi_props,
            self.ctx.props.pop("menu", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        wifi_widget = QEWifi(**props)

        # wifi_icon_props = {
        #     "name": "wifi",
        #     "font": self.context.icon_font_family,
        #     "fontsize": self.context.icon_font_size,
        #     "padding": 8,
        #     "background": f"{background_color}00",
        # }

        # props = self.context.override_parameters(
        #     wifi_icon_props,
        #     self.context.props.pop("icon", {}),
        # )

        # if decorations is not None:
        #     props["decorations"] = decorations

        # wifi_icon = MDIcon(**props)

        widgets: list[base._Widget] = [
            wifi_widget,
            # wifi_icon,
        ]
        return widgets
