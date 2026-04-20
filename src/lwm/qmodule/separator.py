from libqtile.widget import base  # type: ignore
from qtile_extras.widget import Sep  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext
from lwm.helper.merge import merge_props
from lwm.helper.color import TRANSPARENT


class Separator(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        separator_props = {
            "padding": 12,
            "linewidth": 0,
            "foreground": TRANSPARENT,
            "background": TRANSPARENT,
        }

        props = merge_props(
            separator_props,
            self.ctx.props.pop("separator", {}),
        )

        separator = Sep(**props)

        widgets = [separator]
        return widgets
