from pathlib import Path
from lwm.load import load_defs


def test_loader_custom(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    assert "float_to_front" in defs.custom
