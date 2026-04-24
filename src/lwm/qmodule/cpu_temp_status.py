from libqtile.widget import base
from qtile_extras.widget import ThermalSensor
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon
from lwm.helper.merge import merge_props
from lwm.helper.color import TRANSPARENT


class CPUTempStatus(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        temp_props = {
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        temp_icon_props = {
            "name": "cpu_temp",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
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
            temp_props["background"] = TRANSPARENT
            temp_icon_props["background"] = TRANSPARENT

        props = merge_props(
            temp_props,
            self.ctx.props.pop("temperature", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        cpu_temp = ThermalSensor(**props)

        props = merge_props(
            temp_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        cpu_temp_icon = MDIcon(**props)

        widgets = [
            cpu_temp_icon,
            cpu_temp,
        ]
        return widgets
