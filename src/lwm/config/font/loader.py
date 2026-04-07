from .default import DEFAULT_FONTS
from .typedef import FontDefinitions


def fontdefs_from_config(data: dict) -> dict:
    if (font_data := data.get("font", None)) is None:
        fonts = DEFAULT_FONTS
    else:
        if (text := font_data.get("text", None)) is None:
            text = DEFAULT_FONTS["text"]
        if (icon := font_data.get("icon", None)) is None:
            icon = DEFAULT_FONTS["icon"]
        if (weather := font_data.get("weather", None)) is None:
            weather = DEFAULT_FONTS["weather"]
        if (logo := font_data.get("logo", None)) is None:
            logo = DEFAULT_FONTS["logo"]
        fonts: FontDefinitions = {
            "text": text,
            "icon": icon,
            "weather": weather,
            "logo": logo,
        }

    return fonts
