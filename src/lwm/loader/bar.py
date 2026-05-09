from lwm.model.bar import BarDefs


def bardefs_from_data(data: dict) -> BarDefs:
    return BarDefs(**data["bar"])
