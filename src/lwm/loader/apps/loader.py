from lwm.loader.apps.model import Apps


def appdefs_from_config(data: dict) -> Apps:
    apps: Apps
    app_data = data.get("app", None)
    if app_data is None:
        apps = Apps()
    else:
        apps = Apps(**app_data)

    return apps
