from lwm.loader.bar.model import BarDefinitions


def bardefs_from_config(config: dict) -> BarDefinitions:
    return BarDefinitions(**config["bar"])
