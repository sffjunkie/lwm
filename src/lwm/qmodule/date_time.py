from libqtile.widget import base
from qtile_extras.widget import Clock
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon


class DateTime(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        date_text_props = {
            "format": "%a %Y-%m-%d",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        date_icon_props = {
            "name": "calendar",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        time_text_props = {
            "format": "%H:%M",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        time_icon_props = {
            "name": "clock-outline",
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
            date_text_props["background"] = TRANSPARENT
            date_icon_props["background"] = TRANSPARENT
            time_text_props["background"] = TRANSPARENT
            time_icon_props["background"] = TRANSPARENT

        props = merge_props(
            date_text_props,
            self.ctx.props.pop("date", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        date_text = Clock(**props)

        props = merge_props(
            date_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        date_icon = MDIcon(**props)

        props = merge_props(
            time_text_props,
            self.ctx.props.pop("time", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        time_text = Clock(**props)

        props = merge_props(
            time_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        time_icon = MDIcon(**props)

        widgets: list[base._Widget] = [
            date_text,
            date_icon,
            time_text,
            time_icon,
        ]
        return widgets
