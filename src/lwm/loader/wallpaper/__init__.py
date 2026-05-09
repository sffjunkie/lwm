from lwm.model.wallpaper import WallpaperDefinition, WallpaperDefs
from lwm.loader.wallpaper.waypaper import wallpapersdefs_waypaper


def wallpaperdefs() -> WallpaperDefs:
    return wallpapersdefs_waypaper()


def wallpaper_for_screen(
    screen: str, definitions: WallpaperDefs
) -> WallpaperDefinition | None:
    if (definition := definitions.get(screen, None)) is not None:
        return definition

    if (definition := definitions.get("*", None)) is not None:
        return definition

    return None
