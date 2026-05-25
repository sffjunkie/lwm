from pydantic import BaseModel

from lwm.model.layout.types.typedef import Margin


class RatioTileLayout(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 1
    fancy: bool = False
    margin: int | Margin = 0
    ratio: float = 1.618
    ratio_increment: float = 0.1
