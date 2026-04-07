from lwm.config.default import DEFAULT_MARGIN
from lwm.config.bar.typedef import BarDefinitions

DEFAULT_BAR_HEIGHT = 22
DEFAULT_BAR_MARGIN = DEFAULT_MARGIN

DEFAULT_BARS: BarDefinitions = {
    "top": {
        "height": DEFAULT_BAR_HEIGHT,
        "margin": (
            DEFAULT_BAR_MARGIN,
            DEFAULT_BAR_MARGIN,
            0,
            DEFAULT_BAR_MARGIN,
        ),
        "opacity": 1.0,
    }
}
