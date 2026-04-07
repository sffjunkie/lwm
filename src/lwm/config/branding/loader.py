from lwm.config.branding.default import DEFAULT_BRANDING
from lwm.config.branding.typedef import Branding


def branding_from_config(data: dict):
    branding_data = data.get("branding", None)
    if branding_data is None:
        branding = DEFAULT_BRANDING
    else:
        if (description := branding_data.get("description", None)) is None:
            description = DEFAULT_BRANDING["description"]
        if (homepage := branding_data.get("homepage", None)) is None:
            homepage = DEFAULT_BRANDING["homepage"]
        if (icon := branding_data.get("icon", None)) is None:
            icon = DEFAULT_BRANDING["icon"]

        branding: Branding = {
            "description": description,
            "homepage": homepage,
            "icon": icon,
        }

    return branding
