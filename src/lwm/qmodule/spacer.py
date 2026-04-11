from libqtile.widget import base
from qtile_extras.widget import Spacer as QSpacer

from lwm.context.module import ModuleContext
from lwm.qmodule.base import WidgetModule


class Spacer(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get(
            "background", self.ctx.config["color"]["named"]["widget_bg"]
        )
        background = f"{background_color}{self.ctx.bar_ctx.opacity_str}"
        foreground_color = self.ctx.props.get(
            "foreground", self.ctx.config["color"]["named"]["widget_fg_dark"]
        )

        spacer_props = {
            "background": background,
        }

        props = self.ctx.merge_parameters(
            spacer_props,
            self.ctx.props.pop("layout", {}),
        )

        spacer = QSpacer(**props)

        widgets = [spacer]
        return widgets
