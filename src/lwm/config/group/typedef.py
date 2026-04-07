from typing import TypedDict

AppName = str

MatchType = str
MatchDef = list[str]


class GroupDef(TypedDict):
    name: str
    layouts: list[str]
    matches: dict[MatchType, MatchDef]


class GroupDefs(TypedDict):
    decoration: str
    groups: list[GroupDef]
