from lwm.model.color import Base16Colors, NamedColors
from lwm.model.layout.defs import LayoutDefs
from lwm.context.validation import ValidationContext


def layoutdef_from_data(
    data: dict, base16: Base16Colors, named: NamedColors
) -> LayoutDefs:
    layout: LayoutDefs
    layout_data = data.get("layout", None)
    if layout_data is None:
        layout = LayoutDefs()
    else:
        context = ValidationContext(base16=base16, named=named)
        layout = LayoutDefs.model_validate(layout_data, context=context)

    return layout
