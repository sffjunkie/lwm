from pathlib import Path

from lwm.helper.key import modifier_group, qtile_args, qtilecmd
from lwm.load import load_defs


def test_helper_key_modfifier_group(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    assert tuple(modifier_group(defs, "app_launch")) == ("mod4", "mod1")


def test_helper_key_qtilecmd(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None

    qtile_cmd = qtilecmd(defs, "qtile:group.next_window")
    assert qtile_cmd is not None
    assert qtile_cmd.name == "next_window"  # type: ignore

    lwm_cmd = qtilecmd(defs, "lwm:spawn:app.terminal")
    assert lwm_cmd is not None
    assert lwm_cmd.name == "spawn"  # type: ignore


def test_helper_keycmd_qtile_args():
    assert qtile_args("1") == [1]
    assert qtile_args("1,2") == [1, 2]
    assert qtile_args("1.23") == [1.23]
    assert qtile_args("1,1.23") == [1, 1.23]
    assert qtile_args("a") == ["a"]
    assert qtile_args("1,a") == [1, "a"]
