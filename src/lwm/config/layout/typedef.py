from typing import TypedDict, NotRequired

LayoutDefinition = str | int | float | dict[str, "LayoutDefinition"]
LayoutDefinitions = dict[str, LayoutDefinition]


class LayoutDefs(TypedDict):
    common: LayoutDefinitions
    Bsp: NotRequired[LayoutDefinitions]
    Columns: NotRequired[LayoutDefinitions]
    Floating: NotRequired[LayoutDefinitions]
    Matrix: NotRequired[LayoutDefinitions]
    Max: NotRequired[LayoutDefinitions]
    Plasma: NotRequired[LayoutDefinitions]
    RatioTile: NotRequired[LayoutDefinitions]
    ScrteenSplit: NotRequired[LayoutDefinitions]
    Slice: NotRequired[LayoutDefinitions]
    Spiral: NotRequired[LayoutDefinitions]
    Stack: NotRequired[LayoutDefinitions]
    Tile: NotRequired[LayoutDefinitions]
    TreeTab: NotRequired[LayoutDefinitions]
    VerticalTile: NotRequired[LayoutDefinitions]
    MonadTall: NotRequired[LayoutDefinitions]
    MonadThreeCol: NotRequired[LayoutDefinitions]
    MonadWide: NotRequired[LayoutDefinitions]
    Zoomy: NotRequired[LayoutDefinitions]
