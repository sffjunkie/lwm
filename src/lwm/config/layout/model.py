from pydantic import BaseModel

type LayoutDefinition = dict[str, LayoutDefinition] | str | int | float
LayoutDefinitions = dict[str, LayoutDefinition]


class CommonLayoutDefs(BaseModel):
    rounded: bool = False
    margin: int = 4
    border_width: int = 4
    border_focus: str = "base02"
    border_normal: str = "base07"


class LayoutDefs(BaseModel):
    common: CommonLayoutDefs = CommonLayoutDefs(
        rounded=False,
        margin=4,
        border_width=4,
        border_focus="base02",
        border_normal="base07",
    )
    Bsp: LayoutDefinitions | None = None
    Columns: LayoutDefinitions | None = None
    Floating: LayoutDefinitions | None = None
    Matrix: LayoutDefinitions | None = None
    Max: LayoutDefinitions | None = None
    Plasma: LayoutDefinitions | None = None
    RatioTile: LayoutDefinitions | None = None
    ScrteenSplit: LayoutDefinitions | None = None
    Slice: LayoutDefinitions | None = None
    Spiral: LayoutDefinitions | None = None
    Stack: LayoutDefinitions | None = None
    Tile: LayoutDefinitions | None = None
    TreeTab: LayoutDefinitions | None = None
    VerticalTile: LayoutDefinitions | None = None
    MonadTall: LayoutDefinitions | None = None
    MonadThreeCol: LayoutDefinitions | None = None
    MonadWide: LayoutDefinitions | None = None
    Zoomy: LayoutDefinitions | None = None
