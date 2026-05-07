from pydantic import BaseModel


class MenuDefs(BaseModel):
    system: str = "rofi-system-menu"
    user: str = ""
    de: str = ""
