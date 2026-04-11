from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Sep  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class Separator(WidgetModule):
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

        separator_props = {
            "padding": 12,
            "linewidth": 0,
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
            separator_props,
            self.ctx.props.pop("separator", {}),
        )

        separator = Sep(**props)

        widgets = [separator]
        return widgets
