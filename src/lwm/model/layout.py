from pydantic import BaseModel

type LayoutDefinition = dict[str, LayoutDefinition] | str | int | float
LayoutDefinitions = dict[str, LayoutDefinition]


class BaseLayoutDefs(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 4
    margin: int | list[int] = 4
    rounded: bool = False


class LayoutDefs(BaseModel):
    base: BaseLayoutDefs = BaseLayoutDefs()
    defs: dict[str, LayoutDefinitions] = {}
