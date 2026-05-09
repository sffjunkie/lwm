from dataclasses import dataclass
from pathlib import Path

from lwm.model.apps import AppDefs
from lwm.model.bar import BarDefs
from lwm.model.branding import Branding
from lwm.model.color import ColorDefs
from lwm.model.controller import ControllerDefs
from lwm.model.device import DeviceDefs
from lwm.model.extension import ExtensionDefs
from lwm.model.floating import FloatingDefs
from lwm.model.font import FontDefs
from lwm.model.group import GroupDefs
from lwm.model.input import InputDefs
from lwm.model.key import KeyDefs
from lwm.model.layout import LayoutDefs
from lwm.model.match import MatchDefs
from lwm.model.menu import MenuDefs
from lwm.model.notifier import NotifierDefs
from lwm.model.wallpaper import WallpaperDefs
from lwm.model.widget import WidgetDefs


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
    input: InputDefs
    key: KeyDefs
    layout: LayoutDefs
    match: MatchDefs
    menu: MenuDefs
    notifier: NotifierDefs
    widget: WidgetDefs
    wallpaper: WallpaperDefs
