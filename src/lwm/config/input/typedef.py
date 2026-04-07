from enum import StrEnum, auto
from typing import TypedDict


class Keyboard(TypedDict):
    kb_layout: str
    kb_options: str
    kb_variant: str
    kb_repeat_rate: int
    kb_repeat_delay: int


class AccelerationProfile(StrEnum):
    adaptive = auto()
    flat = auto()


class ClickMethod(StrEnum):
    none = auto()
    button_areas = auto()
    clickfinger = auto()


class ScrollMethod(StrEnum):
    none = auto()
    two_finger = auto()
    edge = auto()
    on_button_down = auto()


class TapButtonMap(StrEnum):
    lrm = auto()
    lmr = auto()


class Pointer(TypedDict):
    accel_profile: AccelerationProfile | None
    click_method: ClickMethod | None
    drag: bool | None
    drag_lock: bool | None
    left_handed: bool | None
    middle_emulation: bool | None
    natural_scroll: bool | None
    pointer_accel: float | None
    scroll_button: str | None
    scroll_method: ScrollMethod | None
    tap: bool | None
    tap_button_map: TapButtonMap | None


class InputDefs(TypedDict):
    keyboard: dict[str, Keyboard] | None
    pointer: dict[str, Pointer] | None
