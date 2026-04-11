from libqtile.widget import base  # type: ignore
from qtile_extras.widget import GroupBox as QGroubBox  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class GroupBox(WidgetModule):
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

        group_box_props = {
            "margin_y": 3,
            "padding_y": 4,
            "margin_x": 6,
            "padding_x": 6,
            "borderwidth": 0,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": f"{background_color}00",
            "active": self.ctx.config["color"]["named"]["group_active_fg"],
            "inactive": self.ctx.config["color"]["named"]["group_inactive_fg"],
            "rounded": True,
            "highlight_method": "block",
            "this_current_screen_border": self.ctx.config["color"]["named"][
                "group_current_bg"
            ],
            "this_screen_border": self.ctx.config["color"]["named"]["group_current_bg"],
            "use_mouse_wheel": False,
            # other_current_screen_border=theme_colors["panel_bg"],
            # other_screen_border=theme_colors["panel_bg"],
        }

        props = self.ctx.merge_parameters(
            group_box_props,
            self.ctx.props.pop("group_box", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        group_box = QGroubBox(**props)

        widgets = [group_box]
        return widgets
