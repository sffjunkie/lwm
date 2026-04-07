from lwm.config.typedef import PropertyDefinitions
from lwm.config.layout.typedef import LayoutDefs
from lwm.config.default import DEFAULT_MARGIN

DEFAULT_LAYOUT_COMMON: PropertyDefinitions = {
    "margin": DEFAULT_MARGIN,
    "border_width": 4,
    "border_focus": "base02",
    "border_normal": "base07",
}


DEFAULT_LAYOUT: LayoutDefs = {
    "common": DEFAULT_LAYOUT_COMMON,
}
