from lwm.config.typedef import PropertyDefinitions
from typing import TypedDict, NotRequired


class LayoutDefs(TypedDict):
    common: PropertyDefinitions
    Bsp: NotRequired[PropertyDefinitions]
    Columns: NotRequired[PropertyDefinitions]
    Floating: NotRequired[PropertyDefinitions]
    Matrix: NotRequired[PropertyDefinitions]
    Max: NotRequired[PropertyDefinitions]
    Plasma: NotRequired[PropertyDefinitions]
    RatioTile: NotRequired[PropertyDefinitions]
    ScrteenSplit: NotRequired[PropertyDefinitions]
    Slice: NotRequired[PropertyDefinitions]
    Spiral: NotRequired[PropertyDefinitions]
    Stack: NotRequired[PropertyDefinitions]
    Tile: NotRequired[PropertyDefinitions]
    TreeTab: NotRequired[PropertyDefinitions]
    VerticalTile: NotRequired[PropertyDefinitions]
    MonadTall: NotRequired[PropertyDefinitions]
    MonadThreeCol: NotRequired[PropertyDefinitions]
    MonadWide: NotRequired[PropertyDefinitions]
    Zoomy: NotRequired[PropertyDefinitions]
