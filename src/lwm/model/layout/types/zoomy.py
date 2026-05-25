from pydantic import BaseModel


from lwm.model.layout.types.typedef import Margin


class ZoomyLayout(BaseModel):
    column_width: int = 150
    margin: int | Margin = 0
    property_big: str = "1.0"
    property_name: str = "ZOOM"
    property_small: str = "0.1"
