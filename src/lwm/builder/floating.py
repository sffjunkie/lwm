from libqtile import layout
from libqtile.config import Match, _Match
from qtile_extras.layout.decorations.borders import RoundedCorners

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
    return layout.Floating(
        float_rules=float_rules(),
        border_width=config.layout.common.border_width,
        border_normal=RoundedCorners(
            color=config.color.named.window_border_focus,
        ),
        border_focus=RoundedCorners(
            color=config.color.named.window_border_normal,
        ),
    )
