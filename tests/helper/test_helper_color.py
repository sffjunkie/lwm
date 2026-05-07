from pytest import approx

from lwm.helper.color import (
    is_color,
    is_base16,
    contrast_color,
    opacity_to_hex,
    rgb_intensity,
    rgbhex_to_rgb,
    rgbcolor_to_rgb_hex,
)


def test_is_color():
    assert is_color("#abcdef")
    assert is_color("abcdef")
    assert is_color("#abcdef91")

    assert not is_color("gabcde")


def test_is_base16():
    assert is_base16("base00")
    assert not is_base16("base0G")


def test_opacity_to_string():
    assert opacity_to_hex(0.5) == "7f"


def test_rgb_intensiy():
    assert rgb_intensity((0.5, 0.5, 0.5)) == approx(0.5)


def test_rgbhex_to_rgb_with_hash():
    assert rgbhex_to_rgb("#404040") == approx((0.25, 0.25, 0.25), rel=0.1)


def test_rgbhex_to_rgb_without_hash():
    assert rgbhex_to_rgb("404040") == approx((0.25, 0.25, 0.25), rel=0.1)


def test_rgbcolor_to_rgb_hex():
    assert rgbcolor_to_rgb_hex((0.25, 0.25, 0.25)) == "3f3f3f"


def test_rgbcolor_to_rgb_hex_with_hash():
    assert rgbcolor_to_rgb_hex((0.5, 0.5, 0.5), with_hash=True) == "#7f7f7f"


def test_contrast_color():
    assert contrast_color("#888888") == "ffffff"
    assert contrast_color("888888") == "ffffff"

    assert contrast_color("aAbBcC") == "000000"
