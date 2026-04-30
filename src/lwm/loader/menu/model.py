from pydantic import BaseModel


class Menus(BaseModel):
    system: str = "rofi-system-menu"
    user: str = ""
