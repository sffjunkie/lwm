from lwm.config.controller.model import Controllers


def controllerdefs_from_config(data: dict):
    controller_data = data.get("controller", None)
    if controller_data is None:
        controllers = Controllers()
    else:
        controllers = Controllers(**controller_data)
    return controllers
