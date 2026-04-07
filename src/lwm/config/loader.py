from pathlib import Path
from typing import Literal, get_args, Any

from libqtile.log_utils import logger

from lwm.config.apps.loader import appdefs_from_config
from lwm.config.bar.loader import bardefs_from_config
from lwm.config.branding.loader import branding_from_config
from lwm.config.color.loader import colordefs_from_config
from lwm.config.controller.loader import controllerdefs_from_config
from lwm.config.device.loader import devicedefs_from_config
from lwm.config.extension.loader import extensiondefs_from_config
from lwm.config.font.loader import fontdefs_from_config
from lwm.config.group.loader import groupdefs_from_config
from lwm.config.key.loader import keydefs_from_config
from lwm.config.layout.loader import layoutdef_from_config
from lwm.config.menu.loader import menudefs_from_config
from lwm.config.typedef import Config
from lwm.config.widget.loader import widgetdef_from_config
from lwm.config.wallpaper.loader import wallpaperdefs
from lwm.fs import read_yaml, user_config_dir


CONFIG_DIR = "lwm"
CONFIG_FORMAT = "yaml"
ConfigKeys = Literal[
    "app",
    "bar",
    "branding",
    "color",
    "controller",
    "device",
    "extension",
    "font",
    "group",
    "key",
    "layout",
    "menu",
    "widget",
]
ConfigDefs = dict[ConfigKeys, dict]


def get_config_path(filepath: Path | None = None) -> Path | None:
    if filepath is not None and filepath.is_absolute():
        config_path = filepath
    else:
        config_path = user_config_dir(f"desktop/{CONFIG_DIR}")

    if not config_path.exists():
        logger.warning(f"No config found at {config_path}")
        config_path = None

    return config_path


def get_config_from_file(base_name: str, configpath: Path) -> dict[str, Any]:
    config_filename = configpath / base_name
    config = read_yaml(config_filename)
    return config


def load_configs(configpath: Path) -> ConfigDefs:
    configs = {}
    for name in get_args(ConfigKeys):
        config = get_config_from_file(f"{name}.{CONFIG_FORMAT}", configpath)
        configs[name] = config.get(name, config)
    return configs


def load_config(configpath: Path | None = None) -> Config | None:
    config_path = get_config_path(configpath)
    logger.warning(f"Loading config from: {config_path}")

    if config_path is not None and config_path.exists():
        configs = load_configs(config_path)
        logger.warning(f"Configs loaded: {', '.join(configs.keys())}")

        colordefs = colordefs_from_config(configs)
        base16 = colordefs["base16"]
        named = colordefs["named"]

        config = Config(
            from_path=config_path,
            app=appdefs_from_config(configs),
            bar=bardefs_from_config(configs),
            branding=branding_from_config(configs),
            color=colordefs,
            controller=controllerdefs_from_config(configs),
            device=devicedefs_from_config(configs),
            extension=extensiondefs_from_config(configs, base16, named),
            font=fontdefs_from_config(configs),
            group=groupdefs_from_config(configs),
            key=keydefs_from_config(configs),
            layout=layoutdef_from_config(configs, base16, named),
            menu=menudefs_from_config(configs),
            wallpaper=wallpaperdefs(),
            widget=widgetdef_from_config(configs, base16, named),
        )

        return config
    # TODO: Default config
