from libqtile.widget import base
from qtile_extras.widget import Mpd2
from qtile_extras.widget.decorations import RectDecoration

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext
from lwm.helper.merge import merge_props
from lwm.helper.color import TRANSPARENT


class MusicStatus(WidgetModule):
    def __init__(
        self,
        ctx: ModuleContext,
    ):
        self.ctx = ctx

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.ctx.props.get("background", self.ctx.background_rgba)
        foreground_color = self.ctx.props.get("foreground", self.ctx.foreground_rgb)

        mpd2_props = {
            "font": self.ctx.text_font_family,
            "fontsize": self.ctx.text_font_size,
            "padding": 8,
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
                    group_id=group_id,
                )
            ]
            mpd2_props["background"] = TRANSPARENT

        props = merge_props(
            mpd2_props,
            self.ctx.props.pop("music", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        mpd2 = Mpd2(**props)

        widgets = [
            mpd2,
        ]
        return widgets
