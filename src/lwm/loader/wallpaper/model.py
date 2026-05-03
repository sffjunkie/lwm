from pydantic import BaseModel
from pathlib import Path
from typing import Literal

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
