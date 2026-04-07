from libqtile.log_utils import logger
from libqtile.config import Screen

from lwm.config.typedef import Config
from lwm.builder.bar import build_bars


def build_screens(config: Config) -> list[Screen]:
    # logger.warning(config["color"])
    bar_defs = build_bars(config)

    screen = Screen(
        top=bar_defs.get("top", None),
        bottom=bar_defs.get("bottom", None),
        left=bar_defs.get("left", None),
        right=bar_defs.get("right", None),
    )

    if (wpdef := config["wallpaper"].get("*", None)) is not None:
        screen.wallpaper = str(wpdef.path)
        screen.wallpaper_mode = wpdef.monitor

    return [screen]
