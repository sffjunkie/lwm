from lwm.loader.input.model import InputDefs


def inputdef_from_data(data: dict) -> InputDefs:
    input_data = data.get("input", {})
    inputs = InputDefs(**input_data)
    return inputs
