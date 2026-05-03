from pydantic import BaseModel
from typing import Literal

# region bar
BarLocation = Literal["top", "bottom", "right", "left"]


class BarDefinition(BaseModel):
    height: int
    opacity: float
    margin: tuple[int, int, int, int]


class BarDefs(BaseModel):
    top: BarDefinition | None = None
    bottom: BarDefinition | None = None
    left: BarDefinition | None = None
    right: BarDefinition | None = None


# endregion
