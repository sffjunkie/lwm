from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class VerticalTileLayout(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 2
    margin: int | Margin = 4
    single_border_width: int | None = None
    single_margin: int | None = None
