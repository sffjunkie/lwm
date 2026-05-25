from typing import Self

from pydantic import BaseModel, ValidationInfo, model_validator

from lwm.model.color import NamedColors, Base16Colors
from lwm.context.validation import validate_color, ValidationContext


class LayoutBase(BaseModel):
    border_focus: str = "base02"
    border_normal: str = "base07"
    border_width: int = 4
    border_rounded: bool = False
    margin: int | list[int] = 4

    @model_validator(mode="after")
    def colors(self, info: ValidationInfo) -> Self:
        if info.context is None:
            ctx = ValidationContext(base16=Base16Colors(), named=NamedColors())
        else:
            ctx = info.context

        self.border_focus = validate_color(ctx, self.border_focus)
        self.border_normal = validate_color(ctx, self.border_normal)

        return self
