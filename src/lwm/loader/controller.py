from lwm.model.controller import ControllerDefs


def controllerdefs_from_data(data: dict):
    controller_data = data.get("controller", {})
    controllers = ControllerDefs(**controller_data)
    return controllers
