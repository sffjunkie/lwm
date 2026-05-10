from libqtile.widget import base
from qtile_extras.widget import GroupBox as QGroubBox
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule


class GroupBox(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        group_box_props = {
            "margin_y": 3,
            "padding_y": 4,
            "margin_x": 6,
            "padding_x": 6,
            "borderwidth": 0,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
            "active": self.ctx.defs.color.named.group_active_fg,
            "inactive": self.ctx.defs.color.named.group_inactive_fg,
            "rounded": True,
            "highlight_method": "block",
            "this_current_screen_border": self.ctx.defs.color.named.group_current_bg,
            "this_screen_border": self.ctx.defs.color.named.group_current_bg,
            "use_mouse_wheel": False,
            # other_current_screen_border=theme_colors["bar_bg"],
            # other_screen_border=theme_colors["bar_bg"],
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
            group_box_props["background"] = TRANSPARENT

        props = merge_props(
            group_box_props,
            self.ctx.props.pop("group_box", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        group_box = QGroubBox(**props)

        widgets: list[base._Widget] = [group_box]
        return widgets
