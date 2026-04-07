from dataclasses import dataclass
from pathlib import Path
from typing import Literal

ScreenName = str


WallpaperMode = Literal["fill", "stretch", "center"]

DEFAULT_MODE = "fill"


@dataclass
class WallpaperDefinition:
    path: Path
    mode: WallpaperMode
    monitor: str = "*"


WallpaperDefinitions = dict[ScreenName, WallpaperDefinition]


@dataclass
class ColorPalette:
    count: int
    colors: dict[str, str]
