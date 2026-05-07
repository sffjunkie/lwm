from libqtile.backend.wayland.inputs import InputConfig

from lwm.loader.model import Definitions


def build_input_rules(defs: Definitions) -> dict:
    input_rules = {}

    for name, input_def in defs.input.keyboard.items():
        input_rules[name] = InputConfig(**input_def.model_dump())

    for name, input_def in defs.input.pointer.items():
        input_rules[name] = InputConfig(**input_def.model_dump())

    return input_rules
