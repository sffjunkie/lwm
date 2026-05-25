from qtile_extras import widget

from lwm.widget.mdi_codepoint import MDI_CODEPOINT


class MDIcon(widget.TextBox):
    """Material Design Icon"""

    MDI_CODEPOINTS: dict[str, str] = {}

    def __init__(self, name: str, **config):
        text = chr(int(MDI_CODEPOINT[name], 16))
        super().__init__(text=text, **config)
