from typing import Literal, TypedDict

# region bar
BarLocation = Literal["top", "bottom", "right", "left"]


class BarDefinition(TypedDict):
    height: int
    opacity: float
    margin: tuple[int, int, int, int]


BarDefinitions = dict[BarLocation, BarDefinition]
# endregion
