from socket import gethostname

from libqtile.lazy import lazy
from libqtile.widget import base
from qtile_extras.widget import TextBox
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule


class SystemMenu(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        system_menu = getattr(self.ctx.defs.menu, "system", None)
        hostname_props = {
            "text": gethostname(),
            # "fmt": "<b>{}</b>",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        if system_menu is not None:
            hostname_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

        icon_props = {
            "text": self.ctx.defs.branding.icon,
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "width": self.ctx.bar_ctx.height,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
        }

        if system_menu is not None:
            icon_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

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
            hostname_props["background"] = TRANSPARENT
            icon_props["background"] = TRANSPARENT

        props = merge_props(
            hostname_props,
            self.ctx.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        hostname = TextBox(**props)

        props = merge_props(
            icon_props,
            self.ctx.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        icon = TextBox(**props)

        widgets: list[base._Widget] = [
            hostname,
            icon,
        ]
        return widgets
