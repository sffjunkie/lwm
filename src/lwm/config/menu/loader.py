from lwm.config.menu.model import Menus


def menudefs_from_config(data: dict) -> Menus:
    menu_data = data.get("menu", None)
    if menu_data is None:
        menu = Menus()
    else:
        menu = Menus(**menu_data)

    return menu
