from libqtile.widget import base
from qtile_extras.widget import Sep

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.widget_group.base import WidgetGroup


class Separator(WidgetGroup):
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

        widgets: list[base._Widget] = [separator]
        return widgets
