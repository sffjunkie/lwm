from lwm.helper.color import is_base16
from lwm.model.color import Base16Colors, NamedColors
from lwm.loader.color.deref import deref_value


class ValidationContext:
    def __init__(self, base16: Base16Colors, named: NamedColors):
        self.base16 = base16
        self.named = named


def validate_color(ctx: ValidationContext, color: str) -> str:
    base16 = ctx.base16 or Base16Colors()
    named = ctx.named or NamedColors()

    color = deref_value(color, base16, named)
    if is_base16(color):
        color = deref_value(color, base16, named)
    return color
