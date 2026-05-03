from lwm.loader.color.deref import deref_colors
from lwm.loader.color.model import Base16Colors, NamedColors
from lwm.loader.extension.model import ExtensionDefs


def extensiondefs_from_data(
    data: dict, base16: Base16Colors, named: NamedColors
) -> ExtensionDefs:

    extension_data = data.get("widget", None)
    if extension_data is None:
        extension = ExtensionDefs()
    else:
        extension = ExtensionDefs(**extension_data)

    tc = deref_colors(dict(extension), base16, named)
    return extension.model_copy(update=tc)
