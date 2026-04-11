from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Sep  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class LineSeparator(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get(
            "background", self.ctx.bar_ctx.background_rgb
        )
        foreground_color = self.ctx.props.get(
            "foreground", self.ctx.config["color"]["named"]["panel_fg"]
        )
        background = f"{background_color}00"

        separator_props = {
            "size_percent": 50,
            "linewidth": 1,
            "padding": 12,
            "foreground": self.ctx.config["color"]["named"]["panel_fg"],
            "foreground": foreground_color,
            "background": background,
        }

        props = self.ctx.merge_parameters(
            separator_props,
            self.ctx.props.pop("separator", {}),
        )

        separator = Sep(**props)

        widgets = [separator]
        return widgets
