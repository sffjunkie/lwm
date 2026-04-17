from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import CPU  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext
from lwm.qwidget.icon import MDIcon
from lwm.terminal import terminal_run_command
from lwm.helper.merge import override_parameters
from lwm.helper.color import TRANSPARENT


class CPUUsageStatus(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        htop = terminal_run_command(command=["htop"])

        usage_props = {
            "format": "{load_percent:4.1f}%",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(htop),
            },
        }

        usage_icon_props = {
            "name": "cpu_usage",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": background_color,
            "mouse_callbacks": {
                "Button1": lazy.spawn(htop),
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
            usage_props["background"] = TRANSPARENT
            usage_icon_props["background"] = TRANSPARENT

        props = override_parameters(
            usage_props,
            self.ctx.props.pop("usage", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        cpu_usage = CPU(**props)

        props = override_parameters(
            usage_icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        cpu_usage_icon = MDIcon(**props)

        widgets = [
            cpu_usage_icon,
            cpu_usage,
        ]
        return widgets
