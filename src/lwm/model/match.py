from pydantic import BaseModel

MatchName = str


class MatchDef(BaseModel):
    appid: str | None = None
    title: str | None = None


class MatchDefs(BaseModel):
    defs: dict[MatchName, list[MatchDef]] = {}
