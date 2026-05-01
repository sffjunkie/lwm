from lwm.loader.floating.model import Floating


def floatingdefs_from_config(data: dict):
    floating_data = data.get("floating", None)
    if floating_data is None:
        floating = Floating()
    else:
        floating = Floating(**floating_data)

    return floating
