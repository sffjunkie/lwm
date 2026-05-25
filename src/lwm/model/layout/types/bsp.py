from pydantic import BaseModel

from lwm.model.layout.types.typedef import Margin


class BspLayout(BaseModel):
    border_on_single: bool = False
    fair: bool = True
    grow_amount: int = 10
    lower_right: bool = True
    margin_on_single: Margin | None = None
    ratio: float = 1.6
    wrap_clients: bool = False
