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
    base: BaseLayoutDefs = BaseLayoutDefs()
