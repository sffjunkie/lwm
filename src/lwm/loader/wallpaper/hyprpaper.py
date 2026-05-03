from pathlib import Path
from typing import cast, get_args

from lwm.helper.fs import user_config_dir, read_ini
from lwm.loader.wallpaper.model import (
    WallpaperDefs,
    WallpaperDefinition,
    WallpaperMode,
)


def wallpapersdefs_hyprpaper(filepath: Path | None = None) -> WallpaperDefs:
    if filepath is not None and filepath.is_absolute():
        config_path = filepath
    else:
        if filepath is None:
            filepath = Path("config.ini")

        config_path = user_config_dir(Path("hypr.conf")) / filepath

    if config_path is None or not config_path.exists():
        return {}

    try:
        data = read_ini(config_path, has_sections=False)
        wallpaper_defs = data["wallpaper"]
        if not isinstance(wallpaper_defs, list):
            wallpaper_defs = [wallpaper_defs]

        wallpapers = {}
        for wdef in wallpaper_defs:
            monitor, image = wdef.split(",", maxsplit=1)
            monitor = monitor.strip()
            image = image.strip()

            if monitor == "":
                monitor = "*"

            if ":" in image:
                mode, image = image.split(":", maxsplit=1)
                if mode not in get_args(WallpaperMode):
                    mode = "fill"
            else:
                mode = "fill"

            wp = WallpaperDefinition(
                path=Path(image.strip()),
                mode=cast(WallpaperMode, mode),
                monitor=monitor,
            )
            wallpapers[monitor] = wp

        return wallpapers
    except KeyError:
        return {}
