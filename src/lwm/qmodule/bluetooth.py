from libqtile.widget import base
from qtile_extras.widget import Bluetooth as QEBluetooth
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon


class Bluetooth(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        bluetooth_props = {
            "name": "bluetooth",
            "padding": 8,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "menu_font": self.ctx.text_font_family,
            "menu_fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
        }

        bluetooth_icon_props = {
            "name": "bluetooth",
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
            bluetooth_props["background"] = TRANSPARENT
            bluetooth_icon_props["background"] = TRANSPARENT

        props = merge_props(
            bluetooth_props,
            self.ctx.props.pop("menu", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        bluetooth_widget = QEBluetooth(**props)

        props = merge_props(
            bluetooth_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        bluetooth_icon = MDIcon(**props)

        widgets: list[base._Widget] = [
            bluetooth_icon,
            bluetooth_widget,
        ]
        return widgets
