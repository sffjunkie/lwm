from pathlib import Path
from lwm.load import load_defs


def test_floating_loader(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path.absolute())

    assert defs is not None
    assert len(defs.floating.matches) == 5
