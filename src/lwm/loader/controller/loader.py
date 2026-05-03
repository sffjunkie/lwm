from lwm.loader.controller.model import ControllerDefs


def controllerdefs_from_data(data: dict):
    controller_data = data.get("controller", None)
    if controller_data is None:
        controllers = ControllerDefs()
    else:
        controllers = ControllerDefs(**controller_data)
    return controllers
