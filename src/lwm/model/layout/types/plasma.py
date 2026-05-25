from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class PlasmaLayout(BaseModel):
    border_focus: str = "#00e891"
    border_focus_fixed: str = "#00e8dc"
    border_normal: str = "#333333"
    border_normal_fixed: str = "#333333"
    border_width: int = 1
    border_width_single: int = 0
    fair: bool = True
    margin: int | Margin = 0
    name: str = "Plasma"
