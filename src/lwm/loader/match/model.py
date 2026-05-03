from typing import Literal
from pydantic import BaseModel

DefType = Literal["appid", "title"]

AppName = str
AppMatch = str


class AppDef(BaseModel):
    appid: list[AppMatch] = []
    title: list[AppMatch] = []


class MatchDefs(BaseModel):
    defs: dict[AppName, AppDef] = {}
