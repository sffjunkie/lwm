from lwm.loader.key.model import KeyDefs, KeyMapping


def keydefs_from_data(data: dict) -> KeyDefs:
    key_data = data.get("key", None)
    if key_data is None:
        mapping = KeyMapping()
        keys = KeyDefs(mapping=mapping, defs=[])
    else:
        keys = KeyDefs(**key_data)

    return keys
