from .model import FontDefinitions


def fontdefs_from_config(data: dict) -> FontDefinitions:
    if (font_data := data.get("font", None)) is None:
        fonts = FontDefinitions()
    else:
        fonts = FontDefinitions(**font_data)

    return fonts
