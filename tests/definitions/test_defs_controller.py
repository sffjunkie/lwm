from lwm.loader.controller.model import ControllerDefs


def test_controller_defaults():
    defs = ControllerDefs()
    assert defs.audio.app == "pavucontrol"

    assert defs.music.app == "musicctl"
    assert defs.music.cmd_next == "musicctl next"

    assert defs.clipboard.cmd_copy == "rofi-clip copy"
