from pydantic import BaseModel

from lwm.model.font import DEFAULT_FONTDEF


class ExtensionDefs(BaseModel):
    font: str = DEFAULT_FONTDEF.family
    fontsize: int = DEFAULT_FONTDEF.size
    foreground: str = "bar_fg"
    background: str = "bar_bg"
