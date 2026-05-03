from libqtile.widget import base
from qtile_extras.widget import Spacer as QSpacer
from qtile_extras.widget import WindowName as QWindowName
from qtile_extras.widget.decorations import RectDecoration

from lwm.context.module import ModuleContext
from lwm.helper.color import TRANSPARENT
from lwm.helper.merge import merge_props
from lwm.qmodule.base import WidgetModule


class WindowName(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        window_name_props = {
            "padding": 12,
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "foreground": foreground_color,
            "background": background_color,
        }

        props = merge_props(
            window_name_props,
            self.ctx.props.pop("name", {}),
        )

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
            window_name_props["background"] = TRANSPARENT

        widgets = [
            QSpacer(
                background=TRANSPARENT,
                decorations=decorations,
            ),
            QWindowName(
                **props,
                decorations=decorations,
            ),
            QSpacer(
                background=TRANSPARENT,
                decorations=decorations,
            ),
        ]
        return widgets
