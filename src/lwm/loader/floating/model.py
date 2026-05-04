from pydantic import BaseModel

MatchName = str


class Floating(BaseModel):
    matches: list[MatchName] = []
