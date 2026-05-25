from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class TileLayout(BaseModel):
    add_after_last: bool = False
    add_on_top: bool = True
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_on_single: bool = True
    border_width: int = 1
    expand: bool = True
    margin: int | Margin = 0
    margin_on_single: bool = True
    master_length: int = 1
    master_match: str | list[str] | None = None
    max_ratio: float = 0.85
    min_ratio: float = 0.15
    ratio: float = 0.618
    ratio_increment: float = 0.05
    shift_windows: bool = False
