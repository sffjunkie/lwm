import os

from libqtile.lazy import lazy
from libqtile.widget import base
from qtile_extras.widget import TextBox
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon


class UserMenu(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        icon_props = {
            "name": "account",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            # "width": self.context.bar.height,
            "padding": 8,
            "mouse_callbacks": {"Button1": lazy.spawn(self.ctx.defs.menu.user)},
            "foreground": foreground_color,
            "background": background_color,
        }

        username_props = {
            "text": os.environ["USER"],
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "mouse_callbacks": {"Button1": lazy.spawn(self.ctx.defs.menu.user)},
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
                    # padding_x=8,
                )
            ]
            icon_props["background"] = TRANSPARENT
            username_props["background"] = TRANSPARENT

        props = merge_props(
            icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        icon = MDIcon(**props)

        props = merge_props(
            username_props,
            self.ctx.props.pop("username", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        username = TextBox(**props)

        widgets: list[base._Widget] = [
            icon,
            username,
        ]
        return widgets
