from libqtile.backend.wayland.inputs import InputConfig

from lwm.model.definitions import Definitions


def build_input_rules(defs: Definitions) -> dict:
    kbd_input_rules = {}
    ptr_input_rules = {}

    for name, kbd_input_def in defs.input.keyboard.items():
        kbd_input_rules[name] = InputConfig(**kbd_input_def.model_dump())

    for name, ptr_input_def in defs.input.pointer.items():
        ptr_input_rules[name] = InputConfig(**ptr_input_def.model_dump())

    return kbd_input_rules | ptr_input_rules
