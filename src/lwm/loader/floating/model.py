from pydantic import BaseModel


class MatchTypes(BaseModel):
    appid: list[str] = []
    title: list[str] = []


class Floating(BaseModel):
    matches: MatchTypes = MatchTypes()
