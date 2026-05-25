from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class StackLayout(BaseModel):
    autosplit: bool = False
    border_focus: str = "base02"
    border_focus_stack: str | None = None
    border_normal: str = "base07"
    border_normal_stack: str | None = None
    border_width: int = 2
    fair: bool = False
    margin: int | Margin = 0
    num_stacks: int = 2
