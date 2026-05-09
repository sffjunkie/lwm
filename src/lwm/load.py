from pathlib import Path
from typing import Any, Literal, get_args

from libqtile.log_utils import logger

from lwm.helper.fs import read_toml, user_config_dir
from lwm.loader.apps import appdefs_from_data
from lwm.loader.bar import bardefs_from_data
from lwm.loader.branding import branding_from_data
from lwm.loader.color.loader import colordefs_from_data
from lwm.loader.controller import controllerdefs_from_data
from lwm.loader.device import devicedefs_from_data
from lwm.loader.extension import extensiondefs_from_data
from lwm.loader.floating import floatingdefs_from_data
from lwm.loader.font import fontdefs_from_data
from lwm.loader.group import groupdefs_from_data
from lwm.loader.input import inputdef_from_data
from lwm.loader.key import keydefs_from_data
from lwm.loader.layout import layoutdef_from_data
from lwm.loader.match import matchdefs_from_data
from lwm.loader.menu import menudefs_from_data
from lwm.model.definitions import Definitions
from lwm.loader.notifier import notifierdefs_from_data
from lwm.loader.wallpaper import wallpaperdefs
from lwm.loader.widget import widgetdef_from_data

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
    "notifier",
    "widget",
]
DefsValues = dict[str, Any]
DefsData = dict[DefsKeys, DefsValues]


def get_defs_path(filepath: Path | None = None) -> Path | None:
    if filepath is not None and filepath.is_absolute():
        defs_path = filepath
    else:
        defs_path = user_config_dir(Path(DEFS_DIR))

    if not defs_path.exists():
        logger.warning(f"No config found at {defs_path}")
        return None

    return defs_path


def get_defs_from_file(base_name: str, defspath: Path) -> DefsValues:
    defs_filename = defspath / base_name
    defs = read_toml(defs_filename)
    return defs


def load_def_files(defspath: Path) -> DefsData:
    all_defs = {}
    for name in get_args(DefsKeys):
        defs = get_defs_from_file(f"{name}.{DEFS_FORMAT}", defspath)
        all_defs[name] = defs.get(name, defs)
    return all_defs


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
            input=inputdef_from_data(configs),
            key=keydefs_from_data(configs),
            layout=layoutdef_from_data(configs, base16_defs, named_defs),
            match=matchdefs_from_data(configs),
            menu=menudefs_from_data(configs),
            notifier=notifierdefs_from_data(configs),
            wallpaper=wallpaperdefs(),
            widget=widgetdef_from_data(configs, base16_defs, named_defs),
        )

        return defs
    return None
