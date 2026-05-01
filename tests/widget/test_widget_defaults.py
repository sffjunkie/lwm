from lwm.loader.model import Config


def test_widget_defaults(config: Config):
    wd = config.widget
    assert wd is not None
    assert wd.fontsize == 800
    assert wd.foreground == "non existent"
    assert wd.background == "#f0c6c6"
