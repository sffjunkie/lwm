import pytest
from pathlib import Path
from lwm.loader.model import Definitions
from lwm.loader import load_defs


@pytest.fixture
def module_root():
    return Path(__file__).parent.parent


@pytest.fixture
def test_data() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def config(test_data: Path) -> Definitions | None:
    data_path = test_data / "config" / "desktop"
    return load_defs(data_path.absolute())
