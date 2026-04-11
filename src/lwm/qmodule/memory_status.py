from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Memory  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule
from lwm.qwidget.icon import MDIcon
from lwm.terminal import terminal_run_command


class MemoryStatus(WidgetModule):
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

        system_status = terminal_run_command(command=["htop"])

        memory_props = {
            "format": "{MemUsed:6.0f}M/{MemTotal:.0f}M",
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button1": lazy.spawn(system_status),
            },
        }

        props = self.ctx.merge_parameters(
            memory_props,
            self.ctx.props.pop("memory", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        memory = Memory(**props)

        icon_props = {
            "name": "memory",
            "font": self.ctx.icon_font_family,
            "fontsize": self.ctx.icon_font_size,
            "padding": 8,
            "foreground": foreground_color,
            "background": f"{background_color}00",
            "mouse_callbacks": {
                "Button1": lazy.spawn(system_status),
            },
        }

        props = self.ctx.merge_parameters(
            icon_props,
            self.ctx.props.pop("icon", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        memory_icon = MDIcon(**props)

        return [
            memory_icon,
            memory,
        ]
