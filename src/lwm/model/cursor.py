from pydantic import BaseModel


class CursorDefs(BaseModel):
    name: str | None = None
    size: int = 24
