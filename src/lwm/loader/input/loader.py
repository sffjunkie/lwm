from lwm.loader.input.model import InputDefs


def inputdef_from_config(config: dict) -> InputDefs:
    input_data = config.get("input", None)
    if input_data is None:
        inputs = InputDefs()
    else:
        inputs = InputDefs(**input_data)

    return inputs
