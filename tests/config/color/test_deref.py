from lwm.config.color.deref import deref_colors
from lwm.config.color.default import DEFAULT_BASE16_COLORS, DEFAULT_NAMED_COLORS


def test_deref_colors_base16():
    colors = {
        "fg": "base01",
    }

    new_colors = deref_colors(
        colors, base16=DEFAULT_BASE16_COLORS, named=DEFAULT_NAMED_COLORS
    )

    assert new_colors["fg"] == "#1e2030"


def test_deref_colors_named():
    new_colors = deref_colors(
        dict(DEFAULT_NAMED_COLORS),
        base16=DEFAULT_BASE16_COLORS,
        named=DEFAULT_NAMED_COLORS,
    )

    assert new_colors["panel_fg"] == "#5b6078"
    assert new_colors["panel_bg"] == "#ed8796"
    assert new_colors["widget_bg"] == ["#f0c6c6"]
