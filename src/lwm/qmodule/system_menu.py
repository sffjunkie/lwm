from socket import gethostname

from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import TextBox  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class SystemMenu(WidgetModule):
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

        system_menu = self.ctx.config["menu"].get("system", None)
        hostname_props = {
            "text": gethostname(),
            # "fmt": "<b>{}</b>",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        if system_menu is not None:
            hostname_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

        props = self.ctx.merge_parameters(
            hostname_props,
            self.ctx.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        hostname = TextBox(**props)

        icon_props = {
            "text": self.ctx.config["branding"]["icon"],
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "width": self.ctx.bar_ctx.height,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        if system_menu is not None:
            icon_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

        props = self.ctx.merge_parameters(
            icon_props,
            self.ctx.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        icon = TextBox(**props)

        widgets = [hostname, icon]
        return widgets
