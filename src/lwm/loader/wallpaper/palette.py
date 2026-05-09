from pathlib import Path

from lwm.helper.shellcmd import shellcmd_exists, shellcmd_output
from lwm.model.wallpaper import ColorPalette


def wallpaper_palette_imagemagik(
    wallpaper: Path, count: int = 16
) -> ColorPalette | None:
    if not wallpaper.exists():
        return None

    if not shellcmd_exists("magick"):
        return None

    image_colors = shellcmd_output(
        [
            "magick",
            str(wallpaper),
            "-resize",
            "25%",
            "-colors",
            str(count),
            "-unique-colors",
            "txt:-",
        ]
    )

    colors = {}
    for idx, line in enumerate(image_colors.split("\n")):
        line = line.strip()
        if not line.startswith("#"):
            elems = line.split()
            colors[f"color{idx:02x}"] = elems[2]

    return ColorPalette(
        count=count,
        colors=colors,
    )
