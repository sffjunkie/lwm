from dataclasses import dataclass
from typing import Literal
from pydantic import BaseModel

CommandType = Literal["std", "var", "wm", "terminal"]


@dataclass
class Command:
    type: CommandType
    command: str


class KeyMapping(BaseModel):
    alt: str = "mod1"
    cmd: str = "mod4"
    ctrl: str = "control"
    hyper: str = "mod3"
    shift: str = "shift"


class KeyDefinition(BaseModel):
    key: str
    command: str
    modifiers: list[str] = []
    desc: str | None
    swallow: bool = False


class KeyDefs(BaseModel):
    mapping: KeyMapping = KeyMapping()
    defs: list[KeyDefinition] = []
