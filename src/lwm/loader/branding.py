from lwm.model.branding import Branding


def branding_from_data(data: dict):
    branding_data = data.get("branding", None)
    if branding_data is None:
        branding = Branding()
    else:
        branding = Branding(**branding_data)

    return branding
