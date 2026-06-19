from pydantic import BaseModel

MatchName = str


class FloatDef(BaseModel):
    match: str
    size: tuple[int, int] | None = None


class FloatingDefs(BaseModel):
    matches: list[FloatDef] = []

    def match(self, name: str) -> FloatDef | None:
        for item in self.matches:
            if item.match == name:
                return item
        return None
