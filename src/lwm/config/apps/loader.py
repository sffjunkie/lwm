from lwm.config.apps.typedef import Apps
from lwm.config.apps.default import DEFAULT_APPS


def appdefs_from_config(data: dict) -> Apps:
    apps: Apps
    app_data = data.get("app", None)
    if app_data is None:
        apps = DEFAULT_APPS
    else:
        if (brain := app_data.get("brain", None)) is None:
            brain = DEFAULT_APPS["brain"]
        if (browser := app_data.get("browser", None)) is None:
            browser = DEFAULT_APPS["browser"]
        if (code_editor := app_data.get("code_editor", None)) is None:
            code_editor = DEFAULT_APPS["code_editor"]
        if (editor := app_data.get("editor", None)) is None:
            editor = DEFAULT_APPS["editor"]
        if (file_manager := app_data.get("file_manager", None)) is None:
            file_manager = DEFAULT_APPS["file_manager"]
        if (launcher := app_data.get("launcher", None)) is None:
            launcher = DEFAULT_APPS["launcher"]
        if (music_player := app_data.get("music_player", None)) is None:
            music_player = DEFAULT_APPS["music_player"]
        if (pager := app_data.get("pager", None)) is None:
            pager = DEFAULT_APPS["pager"]
        if (terminal := app_data.get("terminal", None)) is None:
            terminal = DEFAULT_APPS["terminal"]
        apps = {
            "brain": brain,
            "browser": browser,
            "code_editor": code_editor,
            "editor": editor,
            "file_manager": file_manager,
            "launcher": launcher,
            "music_player": music_player,
            "pager": pager,
            "terminal": terminal,
        }

    return apps
