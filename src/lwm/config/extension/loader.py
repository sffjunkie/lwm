from lwm.config.color.deref import deref_colors
from lwm.config.color.model import Base16Colors, NamedColors
from lwm.config.extension.model import Extension


def extensiondefs_from_config(
    config: dict, base16: Base16Colors, named: NamedColors
) -> Extension:

    extension_data = config.get("widget", None)
    if extension_data is None:
        extension = Extension()
    else:
        extension = Extension(**extension_data)

    tc = deref_colors(dict(extension), base16, named)
    return extension.model_copy(update=tc)
