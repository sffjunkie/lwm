from pydantic import BaseModel


class Keys(BaseModel):
    alt: str = "mod1"
    cmd: str = "mod4"
    ctrl: str = "control"
    hyper: str = "mod3"
    shift: str = "shift"
