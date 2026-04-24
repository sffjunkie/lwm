from lwm.qwidget.icon import MDIcon


def test_mdi_icon():
    i = MDIcon("account-cancel")
    assert i.text == "󱋟"

    i = MDIcon("z-wave")
    assert i.text == "󰫪"
