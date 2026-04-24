from pydantic import BaseModel


class Branding(BaseModel):
    description: str = "Loonniversity Window Manager"
    homepage: str = "https://github.com/sffjunkie/lwm"
    icon: str = ""
