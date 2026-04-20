from lwm.helper.merge import merge_props


def test_override_parameters_additional_data():
    d1 = {
        "a": 1,
        "b": 2,
    }

    d2 = {
        "c": 3,
    }

    assert merge_props(d1, d2) == {
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

    assert merge_props(d1, d2) == {
        "a": 1,
        "b": 3,
    }
