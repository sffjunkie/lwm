from pathlib import Path

from lwm.load import load_defs


def test_loader_key(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path)
    assert defs is not None
    assert len(defs.key.defs) == 34

    assert defs.key.defs[2].key == "Return"
