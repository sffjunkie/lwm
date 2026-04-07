from socket import gethostname

from libqtile.lazy import lazy  # type: ignore
from libqtile.widget import base  # type: ignore
from qtile_extras.widget import TextBox  # type: ignore
from qtile_extras.widget.decorations import RectDecoration  # type: ignore

from lwm.qmodule.base import WidgetModule
from lwm.context.module import ModuleContext


class SystemMenu(WidgetModule):
    def __init__(
        self,
        context: ModuleContext,
    ):
        self.context = context

    def widgets(self, group_id: int = -1) -> list[base._Widget]:
        background_color = self.context.props.get(
            "background", self.context.bar.background
        )

        decorations = None
        if group_id != -1:
            decorations = [
                RectDecoration(
                    colour=f"{background_color}{self.context.bar.opacity_str}",
                    radius=5,
                    filled=True,
                    group=True,
                    group_id=group_id,
                )
            ]

        system_menu = self.context.config["menu"].get("system", None)
        hostname_props = {
            "text": gethostname(),
            # "fmt": "<b>{}</b>",
            "font": self.context.text_font_family,
            "fontsize": self.context.text_font_size,
            "padding": 8,
            "background": f"{background_color}00",
        }

        if system_menu is not None:
            hostname_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

        props = self.context.merge_parameters(
            hostname_props,
            self.context.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        hostname = TextBox(**props)

        icon_props = {
            "text": self.context.config["branding"]["icon"],
            "font": self.context.icon_font_family,
            "fontsize": self.context.icon_font_size,
            "width": self.context.bar.height,
            "padding": 8,
            "background": f"{background_color}00",
        }

        if system_menu is not None:
            icon_props["mouse_callbacks"] = {"Button1": lazy.spawn(system_menu)}

        props = self.context.merge_parameters(
            icon_props,
            self.context.props.pop("layout", {}),
        )

        if decorations is not None:
            props["decorations"] = decorations

        icon = TextBox(**props)

        widgets = [hostname, icon]
        return widgets
