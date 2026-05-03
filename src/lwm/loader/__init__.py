from pathlib import Path
from typing import Any, Literal, get_args

from libqtile.log_utils import logger

from lwm.helper.fs import read_toml, user_config_dir
from lwm.loader.apps.loader import appdefs_from_data
from lwm.loader.bar.loader import bardefs_from_data
from lwm.loader.branding.loader import branding_from_data
from lwm.loader.color.loader import colordefs_from_data
from lwm.loader.controller.loader import controllerdefs_from_data
from lwm.loader.device.loader import devicedefs_from_data
from lwm.loader.extension.loader import extensiondefs_from_data
from lwm.loader.floating.loader import floatingdefs_from_data
from lwm.loader.font.loader import fontdefs_from_data
from lwm.loader.group.loader import groupdefs_from_data
from lwm.loader.key.loader import keydefs_from_data
from lwm.loader.layout.loader import layoutdef_from_data
from lwm.loader.match.loader import matchdefs_from_data
from lwm.loader.menu.loader import menudefs_from_data
from lwm.loader.model import Definitions
from lwm.loader.wallpaper.loader import wallpaperdefs
from lwm.loader.widget.loader import widgetdef_from_data

DEFS_DIR = "lde"
DEFS_FORMAT = "toml"

DefsKeys = Literal[
    "app",
    "bar",
    "branding",
    "color",
    "controller",
    "device",
    "extension",
    "floating",
    "font",
    "group",
    "input",
    "key",
    "layout",
    "match",
    "menu",
    "widget",
]
DefsValues = dict[str, Any]
DefsData = dict[DefsKeys, DefsValues]


def get_defs_path(filepath: Path | None = None) -> Path | None:
    if filepath is not None and filepath.is_absolute():
        config_path = filepath
    else:
        config_path = user_config_dir(Path(DEFS_DIR))

    if not config_path.exists():
        logger.warning(f"No config found at {config_path}")
        config_path = None

    return config_path


def get_defs_from_file(base_name: str, defspath: Path) -> DefsValues:
    config_filename = defspath / base_name
    config = read_toml(config_filename)
    return config


def load_def_files(defspath: Path) -> DefsData:
    configs = {}
    for name in get_args(DefsKeys):
        config = get_defs_from_file(f"{name}.{DEFS_FORMAT}", defspath)
        configs[name] = config.get(name, config)
    return configs


def load_defs(defspath: Path | None = None) -> Definitions | None:
    defs_path = get_defs_path(defspath)
    logger.warning(f"Loading definitions from path: {defs_path}")

    if defs_path is not None and defs_path.exists():
        configs = load_def_files(defs_path)
        logger.warning(f"Definitions loaded: {', '.join(configs.keys())}")

        colordefs = colordefs_from_data(configs)
        base16_defs = colordefs.base16
        named_defs = colordefs.named

        defs = Definitions(
            from_path=defs_path,
            app=appdefs_from_data(configs),
            bar=bardefs_from_data(configs),
            branding=branding_from_data(configs),
            color=colordefs,
            controller=controllerdefs_from_data(configs),
            device=devicedefs_from_data(configs),
            extension=extensiondefs_from_data(configs, base16_defs, named_defs),
            floating=floatingdefs_from_data(configs),
            font=fontdefs_from_data(configs),
            group=groupdefs_from_data(configs),
            key=keydefs_from_data(configs),
            layout=layoutdef_from_data(configs, base16_defs, named_defs),
            match=matchdefs_from_data(configs),
            menu=menudefs_from_data(configs),
            wallpaper=wallpaperdefs(),
            widget=widgetdef_from_data(configs, base16_defs, named_defs),
        )

        return defs
    # TODO: Default config
