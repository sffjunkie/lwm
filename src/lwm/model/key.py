from pydantic import BaseModel

ModifierName = str
ModifierGroupName = str


class ModifierMapping(BaseModel):
    alt: ModifierName = "mod1"
    cmd: ModifierName = "mod4"
    ctrl: ModifierName = "control"
    hyper: ModifierName = "mod3"
    shift: ModifierName = "shift"


class KeyBind(BaseModel):
    key: str
    command: str
    modifier_group: ModifierGroupName | None = None
    desc: str | None
    swallow: bool = True


class KeyDefs(BaseModel):
    modifier: ModifierMapping = ModifierMapping()
    modifier_group: dict[ModifierGroupName, list[ModifierName]] = {}
    defs: list[KeyBind] = []
