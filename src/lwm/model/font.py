from pydantic import BaseModel

FontType = str


class FontDefinition(BaseModel):
    family: str
    size: int


DEFAULT_FONT_SIZE = 12
DEFAULT_FONTDEF = FontDefinition(
    family="Hack Nerd Font Mono",
    size=DEFAULT_FONT_SIZE,
)


class FontDefs(BaseModel):
    content: FontDefinition = DEFAULT_FONTDEF
    icon: FontDefinition = DEFAULT_FONTDEF
    ui: FontDefinition = DEFAULT_FONTDEF
