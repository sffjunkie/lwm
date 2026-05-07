from libqtile.lazy import lazy
from libqtile.widget import base
from qtile_extras.widget import PulseVolume
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon


class VolumeStatus(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        volume_text_props = {
            "name": "bar_volume",
            "volume_app": "volumectl app",
            "mute_format": "   M",
            "unmute_format": "{volume:>3}%",
            "menu_font": self.ctx.text_font_family,
            "menu_fontsize": int(self.ctx.text_font_size * 0.8),
            "menu_width": 500,
            "menu_offset_x": -250,
            "padding": 8,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button4": lazy.widget["bar_volume"].decrease_vol(),
                "Button5": lazy.widget["bar_volume"].increase_vol(),
            },
        }

        volume_icon_props = {
            "name": "volume-high",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button4": lazy.widget["bar_volume"].decrease_vol(),
                "Button5": lazy.widget["bar_volume"].increase_vol(),
            },
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
            volume_text_props["background"] = TRANSPARENT
            volume_icon_props["background"] = TRANSPARENT

        props = merge_props(
            volume_text_props,
            self.ctx.props.pop("volume", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        volume_text = PulseVolume(**props)

        props = merge_props(
            volume_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        volume_icon = MDIcon(**props)

        widgets: list[base._Widget] = [
            volume_text,
            volume_icon,
        ]
        return widgets
