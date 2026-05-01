from pydantic import BaseModel


class Floating(BaseModel):
    match: dict[str, list[str]] = {}
