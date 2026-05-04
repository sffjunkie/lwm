from pydantic import BaseModel

MatchName = str


class FloatingDefs(BaseModel):
    matches: list[MatchName] = []
