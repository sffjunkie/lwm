from lwm.config.group.model import GroupDefs


def groupdefs_from_config(data: dict) -> GroupDefs:
    group_data = data.get("group", None)
    if group_data is None:
        group = GroupDefs()
    else:
        group = GroupDefs(**group_data)

    return group
