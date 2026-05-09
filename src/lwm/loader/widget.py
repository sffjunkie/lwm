from lwm.loader.color.deref import deref_colors
from lwm.model.color import Base16Colors, NamedColors
from lwm.model.widget import WidgetDefs


def widgetdef_from_data(
    data: dict, base16: Base16Colors, named: NamedColors
) -> WidgetDefs:
    widget_data = data.get("widget", None)
    if widget_data is None:
        widget = WidgetDefs()
    else:
        widget = WidgetDefs(**widget_data)

    tc = deref_colors(dict(widget), base16, named)
    return widget.model_copy(update=tc)
