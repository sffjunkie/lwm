from pathlib import Path
from lwm.loader import load_config, get_config_path


def test_config_app(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_config(data_path)

    assert config is not None
    assert (
        config.app.terminal
        == "/nix/store/gzwsjzz2lgalvjs4dfikk9rwq0m0b27a-ghostty-1.3.1/bin/ghostty"
    )


def test_config_key(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_config(data_path)

    assert config is not None
    assert config.key.mapping.cmd == "mod4"


def test_config_loader(test_data: Path):
    data_path = test_data / "config" / "desktop"
    _config = load_config(data_path)


def test_config_real_path():
    data_path = get_config_path()
    expected_path = Path("~/.config").expanduser() / "lde"
    assert str(data_path) == str(expected_path)
