from pathlib import Path
from typing import TypedDict


from lwm.config.bar.typedef import BarDefinitions
from lwm.config.branding.typedef import Branding
from lwm.config.color.typedef import Colors
from lwm.config.font.typedef import FontDefinitions
from lwm.config.group.typedef import GroupDefs
from lwm.config.apps.typedef import Apps
from lwm.config.menu.typedef import Menus
from lwm.config.device.typedef import Devices
from lwm.config.controller.typedef import Controllers
from lwm.config.key.typedef import Keys
from lwm.config.wallpaper.typedef import WallpaperDefinitions
from lwm.config.layout.typedef import LayoutDefs

PropertyDefinition = str | int | float | dict[str, "PropertyDefinition"]
PropertyDefinitions = dict[str, PropertyDefinition]


class Config(TypedDict):
    app: Apps
    bar: BarDefinitions
    branding: Branding
    color: Colors
    controller: Controllers
    device: Devices
    extension: PropertyDefinitions
    font: FontDefinitions
    from_path: Path | None
    group: GroupDefs
    key: Keys
    layout: LayoutDefs
    menu: Menus
    widget: PropertyDefinitions
    wallpaper: WallpaperDefinitions
