from qtile_extras import widget


class LineSeparator(widget.TextBox):
    def __init__(self, **config):
        super().__init__(
            text="|",
            **config,
        )
