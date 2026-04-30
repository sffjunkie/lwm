from lwm.loader.color.deref import deref_colors
from lwm.loader.color.model import Base16Colors, NamedColors
from lwm.loader.widget.model import Widget


def widgetdef_from_config(
    config: dict, base16: Base16Colors, named: NamedColors
) -> Widget:
    widget_data = config.get("widget", None)
    if widget_data is None:
        widget = Widget()
    else:
        widget = Widget(**widget_data)

    tc = deref_colors(dict(widget), base16, named)
    return widget.model_copy(update=tc)
