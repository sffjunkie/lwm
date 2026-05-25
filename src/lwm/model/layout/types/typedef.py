from enum import StrEnum
from typing import NamedTuple


class Margin(NamedTuple):
    N: int
    E: int
    S: int
    W: int


class ClientPosition(StrEnum):
    after_current = "after_current"
    before_current = "before_current"
    top = "top"
    bottom = "bottom"
