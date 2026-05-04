from dataclasses import dataclass
from pathlib import Path

from lwm.loader.apps.model import AppDefs
from lwm.loader.bar.model import BarDefs
from lwm.loader.branding.model import Branding
from lwm.loader.color.model import ColorDefs
from lwm.loader.controller.model import ControllerDefs
from lwm.loader.device.model import DeviceDefs
from lwm.loader.extension.model import ExtensionDefs
from lwm.loader.floating.model import FloatingDefs
from lwm.loader.font.model import FontDefs
from lwm.loader.group.model import GroupDefs
from lwm.loader.key.model import KeyDefs
from lwm.loader.layout.model import LayoutDefs
from lwm.loader.match.model import MatchDefs
from lwm.loader.menu.model import MenuDefs
from lwm.loader.wallpaper.model import WallpaperDefs
from lwm.loader.widget.model import WidgetDefs


@dataclass
class Definitions:
    app: AppDefs
    bar: BarDefs
    branding: Branding
    color: ColorDefs
    controller: ControllerDefs
    device: DeviceDefs
    extension: ExtensionDefs
    floating: FloatingDefs
    font: FontDefs
    from_path: Path | None
    group: GroupDefs
    key: KeyDefs
    layout: LayoutDefs
    match: MatchDefs
    menu: MenuDefs
    widget: WidgetDefs
    wallpaper: WallpaperDefs
