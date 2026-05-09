from lwm.model.device import DeviceDefs


def devicedefs_from_data(data: dict):
    device_data = data.get("device", None)
    if device_data is None:
        devices = DeviceDefs()
    else:
        devices = DeviceDefs(**device_data)

    return devices
