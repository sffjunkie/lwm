from enum import StrEnum
from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin, ClientPosition


class MainPanePosition(StrEnum):
    top = "top"
    bottom = "bottom"
    left = "left"
    right = "right"


class SpiralLayout(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_on_single: bool = True
    border_width: int = 2
    clockwise: bool = True
    main_pane: MainPanePosition = MainPanePosition.left
    margin: int | Margin = 4
    new_client_position: ClientPosition = ClientPosition.top
    ratio: float = 0.6180469715698392
    ratio_increment: float = 0.1
