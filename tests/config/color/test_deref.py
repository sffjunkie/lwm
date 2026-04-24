from lwm.config.color.deref import deref_colors
from lwm.config.color.model import Base16Colors, NamedColors


def test_deref_colors_base16():
    colors = {
        "fg": "base01",
    }

    new_colors = deref_colors(colors, base16=Base16Colors(), named=NamedColors())

    assert new_colors["fg"] == "#1e2030"


def test_deref_colors_named():
    new_colors = deref_colors(
        dict(NamedColors()),
        base16=Base16Colors(),
        named=NamedColors(),
    )

    assert new_colors["bar_fg"] == "#1e2030"
    assert new_colors["bar_bg"] == "#f0c6c6"
    assert new_colors["widget_bg"] == ["#f4dbd6"]
