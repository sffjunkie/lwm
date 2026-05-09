from lwm.model.font import FontDefs


def fontdefs_from_data(data: dict) -> FontDefs:
    if (font_data := data.get("font", None)) is None:
        fonts = FontDefs()
    else:
        fonts = FontDefs(**font_data)

    return fonts
