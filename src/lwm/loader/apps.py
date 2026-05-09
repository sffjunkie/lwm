from lwm.model.apps import AppDefs


def appdefs_from_data(data: dict) -> AppDefs:
    apps: AppDefs
    app_data = data.get("app", None)
    if app_data is None:
        apps = AppDefs()
    else:
        apps = AppDefs(**app_data)

    return apps
