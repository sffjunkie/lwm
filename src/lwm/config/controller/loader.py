from lwm.config.controller.default import DEFAULT_CONTROLLERS
from lwm.config.controller.typedef import Controllers


def controllerdefs_from_config(data: dict):
    controller_data = data.get("controller", None)
    if controller_data is None:
        controllers = DEFAULT_CONTROLLERS
    else:
        if (audio := controller_data.get("audio", None)) is None:
            audio = DEFAULT_CONTROLLERS["audio"]
        if (clipboard := controller_data.get("clipboard", None)) is None:
            clipboard = DEFAULT_CONTROLLERS["clipboard"]
        if (music := controller_data.get("music", None)) is None:
            music = DEFAULT_CONTROLLERS["music"]
        if (volume := controller_data.get("volume", None)) is None:
            volume = DEFAULT_CONTROLLERS["volume"]
        controllers: Controllers = {
            "audio": audio,
            "clipboard": clipboard,
            "music": music,
            "volume": volume,
        }

    return controllers
