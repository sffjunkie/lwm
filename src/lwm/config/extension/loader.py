from lwm.config.color.deref import deref_colors
from lwm.config.color.typedef import Base16Colors, NamedColors
from lwm.config.extension.default import DEFAULT_EXTENSION


def extensiondefs_from_config(
    config: dict, base16: Base16Colors, named: NamedColors
) -> dict:
    extension = DEFAULT_EXTENSION.copy()
    if "extension" in config:
        extension.update(config["extension"])
    else:
        extension.update(config)

    tc = deref_colors(extension, base16, named)
    extension.update(tc)
    return extension
