from pathlib import Path
from typing import Literal

from pydantic import BaseModel

ScreenName = str


WallpaperMode = Literal["fill", "stretch", "center"]

DEFAULT_MODE = "fill"


class WallpaperDefinition(BaseModel):
    path: Path
    mode: WallpaperMode
    monitor: str = "*"


WallpaperDefs = dict[ScreenName, WallpaperDefinition]


class ColorPalette(BaseModel):
    count: int
    colors: dict[str, str]
