from lwm.config.key.model import Keys


def keydefs_from_config(data: dict) -> Keys:
    key_data = data.get("key", None)
    if key_data is None:
        keys = Keys()
    else:
        keys = Keys(**key_data)

    return keys
