from lwm.config.group.typedef import GroupDefs

DEFAULT_GROUPS: GroupDefs = {
    "decoration": "superscript",
    "groups": [
        {
            "name": "WWW",
            "layouts": ["max"],
            "matches": {
                "app_id": ["firefox"],
            },
        },
        {
            "name": "TERM",
            "layouts": ["max"],
            "matches": {
                "app_id": ["ghostty"],
            },
        },
    ],
}
