from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Bluetooth as QEBluetooth  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qwidget.icon import MDIcon
from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class Bluetooth(WidgetModule):
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

        bluetooth_props = {
            "name": "bluetooth",
            "padding": 8,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "menu_font": self.ctx.text_font_family,
            "menu_fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
            bluetooth_props,
            self.ctx.props.pop("menu", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        bluetooth_widget = QEBluetooth(**props)

        bluetooth_icon_props = {
            "name": "bluetooth",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button4": lazy.widget["bar_volume"].decrease_vol(),
                "Button5": lazy.widget["bar_volume"].increase_vol(),
            },
        }

        props = self.ctx.merge_parameters(
            bluetooth_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        bluetooth_icon = MDIcon(**props)

        widgets = [
            bluetooth_icon,
            bluetooth_widget,
        ]
        return widgets
