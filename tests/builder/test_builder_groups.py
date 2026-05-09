from pathlib import Path

from lwm.load import load_defs
from lwm.builder.group import build_groups, build_group_keys


def test_build_groups(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_defs(data_path)
    assert config is not None
    # TODO: actually test something
    _groups = build_groups(config)
    pass


def test_build_group_keys(test_data: Path):
    data_path = test_data / "config" / "desktop"
    config = load_defs(data_path)
    assert config is not None
    # TODO: actually test something
    _keys = build_group_keys(config)
    pass
