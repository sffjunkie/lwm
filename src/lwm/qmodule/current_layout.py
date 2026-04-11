from libqtile.widget import base  # type: ignore
from qtile_extras.widget import CurrentLayout as QCurrentLayout  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class CurrentLayout(WidgetModule):
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
        # if group_id != -1:
        decorations = [
            RectDecoration(
                colour=f"{background_color}{self.ctx.bar_ctx.opacity_str}",
                radius=5,
                filled=True,
                group=True,
                group_id=10,
            )
        ]

        current_layout_props = {
            "padding": 12,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": self.ctx.config["color"]["named"]["panel_fg"],
            "foreground": foreground_color,
            "background": f"{background_color}00",
        }

        props = self.ctx.merge_parameters(
            current_layout_props,
            self.ctx.props.pop("layout", {}),
        )

        current_layout = QCurrentLayout(
            **props,
            decorations=decorations,
        )

        widgets = [current_layout]
        return widgets
