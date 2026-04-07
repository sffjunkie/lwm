from libqtile import layout
from libqtile.config import Match, _Match

from lwm.config.layout.default import DEFAULT_LAYOUT_COMMON
from lwm.config.typedef import Config

wmclass_float = [
    "com.github.wwmm.easyeffects",
    "org.pulseaudio.pavucontrol",
    "org.gnome.Calculator",
    "org.gnome.Characters",
    "Pinentry",
    "ssh-askpass",
    "waypaper",
    "yubico.org.",
]


def float_rules() -> list[_Match]:
    return [
        Match(wm_class=float_match) for float_match in wmclass_float
    ] + layout.Floating.default_float_rules


def build_floating(config: Config) -> layout.Floating:
    color_scheme = config["color"]["named"]
    return layout.Floating(
        float_rules=float_rules(),
        border_width=DEFAULT_LAYOUT_COMMON["border_width"],
        border_normal=color_scheme["window_border_focus"],
        border_focus=color_scheme["window_border_normal"],
    )
