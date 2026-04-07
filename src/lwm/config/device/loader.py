from lwm.config.device.default import DEFAULT_DEVICES
from lwm.config.device.typedef import Devices


def devicedefs_from_config(data: dict):
    device_data = data.get("device", None)
    if device_data is None:
        devices = DEFAULT_DEVICES
    else:
        if (wifi := device_data.get("wifi", None)) is None:
            wifi = DEFAULT_DEVICES["wifi"]
        if (eth := device_data.get("eth", None)) is None:
            eth = DEFAULT_DEVICES["eth"]
        devices: Devices = {
            "eth": eth,
            "wifi": wifi,
        }

    return devices
