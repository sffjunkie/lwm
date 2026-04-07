from libqtile.log_utils import logger

from lwm.config.menu.default import DEFAULT_MENU
from lwm.config.menu.typedef import Menus


def menudefs_from_config(data: dict) -> Menus:
    menu_data = data.get("menu", None)
    if menu_data is None:
        menu = DEFAULT_MENU
    else:
        if (system := menu_data.get("system", None)) is None:
            system = DEFAULT_MENU["system"]
        if (user := menu_data.get("user", None)) is None:
            user = DEFAULT_MENU["user"]
        menu: Menus = {
            "system": system,
            "user": user,
        }

    return menu
