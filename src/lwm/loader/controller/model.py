from pydantic import BaseModel


class ControllerDefs(BaseModel):
    audio: str = "pavucontrol"
    clipboard: str = "rofi-clip"
    music: str = "musicctl"
    volume: str = "volumectl"
