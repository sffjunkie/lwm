from lwm.config.bar.typedef import BarDefinitions
from lwm.config.bar.default import DEFAULT_BARS


def bardefs_from_config(config: dict) -> BarDefinitions:
    bars = DEFAULT_BARS.copy()
    if "bar" in config:
        bars.update(config["bar"])
    return bars
