from libqtile.widget import base  # type: ignore
from qtile_extras.widget import ThermalSensor  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon


class CPUTempStatus(WidgetModule):
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

        temp_props = {
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
            temp_props,
            self.ctx.props.pop("temperature", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        cpu_temp = ThermalSensor(**props)

        temp_icon_props = {
            "name": "cpu_temp",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
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
