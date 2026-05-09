from pydantic import BaseModel

AppName = str

MatchType = str
MatchDef = list[str]


class MatchTypes(BaseModel):
    appid: list[str] = []
    title: list[str] = []


class CommonGroupDefs(BaseModel):
    decoration: str = "superscript"
    layout: str | None = None
    layouts: list[str] = []


class GroupDef(BaseModel):
    name: str
    layout: str = ""
    layouts: list[str] = []
    matches: list[str] = []


class GroupDefs(BaseModel):
    common: CommonGroupDefs = CommonGroupDefs()
    defs: list[GroupDef] = [
        GroupDef(
            name="WWW",
            layout="max",
            matches=["firefox"],
        ),
        GroupDef(
            name="TERM",
            layout="max",
            matches=["ghostty"],
        ),
    ]
