from lwm.loader.key.model import KeyDefs


def keydefs_from_data(data: dict) -> KeyDefs:
    key_data = data.get("key", {})
    keys = KeyDefs(**key_data)

    return keys
