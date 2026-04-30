from pydantic import BaseModel

AppName = str

MatchType = str
MatchDef = list[str]


class GroupDef(BaseModel):
    name: str
    layouts: list[str] = []
    matches: dict[MatchType, MatchDef] = {}


class GroupDefs(BaseModel):
    decoration: str = "superscript"
    groups: list[GroupDef] = [
        GroupDef(
            name="WWW",
            layouts=["max"],
            matches={
                "app_id": ["firefox"],
            },
        ),
        GroupDef(
            name="TERM",
            layouts=["max"],
            matches={
                "app_id": ["ghostty"],
            },
        ),
    ]
