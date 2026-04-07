from lwm.config.group.default import DEFAULT_GROUPS
from lwm.config.group.typedef import GroupDefs


def groupdefs_from_config(data: dict) -> GroupDefs:
    group_data = data.get("group", None)
    if group_data is None:
        group = DEFAULT_GROUPS
    else:
        group: GroupDefs = group_data

    return group
