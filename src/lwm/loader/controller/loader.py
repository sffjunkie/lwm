from lwm.loader.controller.model import ControllerDefs


def controllerdefs_from_data(data: dict):
    controller_data = data.get("controller", {})
    controllers = ControllerDefs(**controller_data)
    return controllers
