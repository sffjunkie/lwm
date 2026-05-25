from pydantic import BaseModel


class MatrixLayout(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 1
    columns: int = 2
    margin: int | list[int] = 4
