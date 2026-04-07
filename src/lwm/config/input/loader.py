from lwm.config.input.typedef import InputDefs


def inputdef_from_config(config: dict) -> InputDefs:
    input_data = config.get("input", None)
    if input_data is None:
        inputs: InputDefs = {
            "keyboard": None,
            "pointer": None,
        }
    else:
        inputs = input_data

    return inputs
