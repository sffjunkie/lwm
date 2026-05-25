from pydantic import BaseModel


class MaxLayout(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 1
    margin: int | list[int] = 4
    only_focused: bool = True
