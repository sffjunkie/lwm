from pathlib import Path
from typing import TypedDict


from lwm.config.bar.model import BarDefinitions
from lwm.config.branding.model import Branding
from lwm.config.color.model import Colors
from lwm.config.extension.model import Extension
from lwm.config.font.model import FontDefinitions
from lwm.config.group.model import GroupDefs
from lwm.config.apps.model import Apps
from lwm.config.menu.model import Menus
from lwm.config.device.model import Devices
from lwm.config.controller.model import Controllers
from lwm.config.key.model import Keys
from lwm.config.wallpaper.model import WallpaperDefinitions
from lwm.config.layout.model import LayoutDefs
from lwm.config.widget.model import Widget

PropertyDefinition = str | int | float | dict[str, "PropertyDefinition"]
PropertyDefinitions = dict[str, PropertyDefinition]


class Config(TypedDict):
    app: Apps
    bar: BarDefinitions
    branding: Branding
    color: Colors
    controller: Controllers
    device: Devices
    extension: Extension
    font: FontDefinitions
    from_path: Path | None
    group: GroupDefs
    key: Keys
    layout: LayoutDefs
    menu: Menus
    widget: Widget
    wallpaper: WallpaperDefinitions
