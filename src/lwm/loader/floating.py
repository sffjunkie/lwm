from lwm.model.floating import FloatingDefs


def floatingdefs_from_data(data: dict) -> FloatingDefs:
    floating_data = data.get("floating", None)
    if floating_data is None:
        floating = FloatingDefs()
    else:
        floating = FloatingDefs(**floating_data)

    return floating
