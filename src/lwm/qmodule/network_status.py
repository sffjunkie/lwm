from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon
from lwm.qwidget.net_min import NetMin
from lwm.terminal import terminal_run_command
from lwm.helper.merge import merge_props
from lwm.helper.color import TRANSPARENT


class NetworkStatus(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx
        self.wifi = ctx.config.device.wifi
        self.eth = ctx.config.device.eth

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        network = self.ctx.props.pop("network", {})

        slurm = terminal_run_command(
            command=[
                "slurm",
                "-i",
                network.get("interface", self.wifi),
            ],
        )

        up_props = {
            "format": "{up:4.0f}{up_suffix:<2}",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(slurm),
            },
        }

        up_icon_props = {
            "name": "net_up",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(slurm),
            },
        }

        down_props = {
            "format": "{down:4.0f}{down_suffix:<2}",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(slurm),
            },
        }

        down_icon_props = {
            "name": "net_down",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(slurm),
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
            up_props["background"] = TRANSPARENT
            up_icon_props["background"] = TRANSPARENT
            down_props["background"] = TRANSPARENT
            down_icon_props["background"] = TRANSPARENT

        props = merge_props(
            up_props,
            self.ctx.props.pop("up", {}),
            self.ctx.props.pop("network", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        up = NetMin(**props)

        props = merge_props(
            up_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        up_icon = MDIcon(**props)

        props = merge_props(
            down_props,
            self.ctx.props.pop("down", {}),
            self.ctx.props.pop("network", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        down = NetMin(**props)

        props = merge_props(
            down_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        down_icon = MDIcon(**props)

        widgets = [
            up_icon,
            up,
            down_icon,
            down,
        ]
        return widgets
