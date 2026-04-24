from lwm.config.device.model import Devices


def devicedefs_from_config(data: dict):
    device_data = data.get("device", None)
    if device_data is None:
        devices = Devices()
    else:
        devices = Devices(**device_data)

    return devices
