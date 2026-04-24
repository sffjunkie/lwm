from lwm.config.bar.model import BarDefinitions


def bardefs_from_config(config: dict) -> BarDefinitions:
    return BarDefinitions(**config["bar"])
