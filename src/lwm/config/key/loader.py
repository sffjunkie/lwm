from lwm.config.key.default import DEFAULT_KEYS
from lwm.config.key.typedef import Keys


def keydefs_from_config(data: dict) -> Keys:
    key_data = data.get("key", None)
    if key_data is None:
        keys = DEFAULT_KEYS
    else:
        if (alt := key_data.get("alt", None)) is None:
            alt = DEFAULT_KEYS["alt"]
        if (cmd := key_data.get("cmd", None)) is None:
            cmd = DEFAULT_KEYS["cmd"]
        if (ctrl := key_data.get("ctrl", None)) is None:
            ctrl = DEFAULT_KEYS["ctrl"]
        if (hyper := key_data.get("hyper", None)) is None:
            hyper = DEFAULT_KEYS["hyper"]
        if (shift := key_data.get("shift", None)) is None:
            shift = DEFAULT_KEYS["shift"]
        keys: Keys = {
            "alt": alt,
            "cmd": cmd,
            "ctrl": ctrl,
            "hyper": hyper,
            "shift": shift,
        }

    return keys
