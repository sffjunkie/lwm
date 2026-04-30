from pydantic import BaseModel


class Controllers(BaseModel):
    audio: str = "pavucontrol"
    clipboard: str = "rofi-clip"
    music: str = "musicctl"
    volume: str = "volumectl"
