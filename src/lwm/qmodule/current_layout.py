from libqtile.widget import base
from qtile_extras.widget import CurrentLayout as QCurrentLayout
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule


class CurrentLayout(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        current_layout_props = {
            "padding": 12,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
        }

        decorations = None
        if group_id != -1:
            decorations = [
                RectDecoration(
                    colour=background_color,
                    radius=5,
                    filled=True,
                    group=True,
                    group_id=10,
                )
            ]
            current_layout_props["background"] = TRANSPARENT

        props = merge_props(
            current_layout_props,
            self.ctx.props.pop("layout", {}),
        )

        current_layout = QCurrentLayout(
            **props,
            decorations=decorations,
        )

        widgets: list[base._Widget] = [current_layout]
        return widgets
