from lwm.loader.group.model import GroupDefs


def groupdefs_from_data(data: dict) -> GroupDefs:
    group_data = data.get("group", None)
    if group_data is None:
        group_defs = GroupDefs()
    else:
        group_defs = GroupDefs(**group_data)

    return group_defs
