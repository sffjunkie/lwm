from pathlib import Path
from dataclasses import dataclass

from lwm.loader.bar.model import BarDefinitions
from lwm.loader.branding.model import Branding
from lwm.loader.color.model import Colors
from lwm.loader.extension.model import Extension
from lwm.loader.font.model import FontDefinitions
from lwm.loader.floating.model import Floating
from lwm.loader.group.model import GroupDefs
from lwm.loader.apps.model import Apps
from lwm.loader.menu.model import Menus
from lwm.loader.device.model import Devices
from lwm.loader.controller.model import Controllers
from lwm.loader.key.model import Keys
from lwm.loader.wallpaper.model import WallpaperDefinitions
from lwm.loader.layout.model import LayoutDefs
from lwm.loader.widget.model import Widget

PropertyDefinition = str | int | float | dict[str, "PropertyDefinition"]
PropertyDefinitions = dict[str, PropertyDefinition]


@dataclass
class Config:
    app: Apps
    bar: BarDefinitions
    branding: Branding
    color: Colors
    controller: Controllers
    device: Devices
    extension: Extension
    floating: Floating
    font: FontDefinitions
    from_path: Path | None
    group: GroupDefs
    key: Keys
    layout: LayoutDefs
    menu: Menus
    widget: Widget
    wallpaper: WallpaperDefinitions
