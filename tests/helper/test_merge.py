from lwm.helper.merge import override_parameters


def test_override_parameters_additional_data():
    d1 = {
        "a": 1,
        "b": 2,
    }

    d2 = {
        "c": 3,
    }

    assert override_parameters(d1, d2) == {
        "a": 1,
        "b": 2,
        "c": 3,
    }


def test_override_parameters_update_data():
    d1 = {
        "a": 1,
        "b": 2,
    }

    d2 = {
        "b": 3,
    }

    assert override_parameters(d1, d2) == {
        "a": 1,
        "b": 3,
    }
