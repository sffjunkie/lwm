from lwm.loader.bar.model import BarDefs


def bardefs_from_data(data: dict) -> BarDefs:
    return BarDefs(**data["bar"])
