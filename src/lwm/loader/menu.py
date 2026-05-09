from lwm.model.menu import MenuDefs


def menudefs_from_data(data: dict) -> MenuDefs:
    menu_data = data.get("menu", None)
    if menu_data is None:
        menu = MenuDefs()
    else:
        menu = MenuDefs(**menu_data)

    return menu
