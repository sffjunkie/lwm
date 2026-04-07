from lwm.config.color.deref import deref_colors
from lwm.config.color.typedef import Base16Colors, NamedColors
from lwm.config.widget.default import DEFAULT_WIDGET
from lwm.config.typedef import PropertyDefinitions


def widgetdef_from_config(
    config: dict, base16: Base16Colors, named: NamedColors
) -> PropertyDefinitions:
    widget_data = config.get("widget", None)
    if widget_data is None:
        widget = DEFAULT_WIDGET.copy()
    else:
        widget = widget_data

    tc = deref_colors(widget, base16, named)
    widget.update(tc)
    return widget
