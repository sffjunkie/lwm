# from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import WiFiIcon as QEWifi  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class Wifi(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get(
            "background", self.ctx.config["color"]["named"]["widget_bg"]
        )
        foreground_color = self.ctx.props.get(
            "foreground", self.ctx.config["color"]["named"]["widget_fg_dark"]
        )

        decorations = None
        if group_id != -1:
            decorations = [
                RectDecoration(
                    colour=f"{background_color}{self.ctx.bar_ctx.opacity_str}",
                    radius=5,
                    filled=True,
                    group=True,
                    group_id=group_id,
                )
            ]

        wifi_props = {
            "name": "wifi",
            "interface": self.ctx.config["device"]["wifi"],
            "padding": 8,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "menu_font": self.ctx.text_font_family,
            "menu_fontsize": self.ctx.text_font_size,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
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

        # props = self.context.merge_parameters(
        #     wifi_icon_props,
        #     self.context.props.pop("icon", {}),
        # )

        # if decorations is not None:
        #     props["decorations"] = decorations

        # wifi_icon = MDIcon(**props)

        widgets = [
            wifi_widget,
            # wifi_icon,
        ]
        return widgets
