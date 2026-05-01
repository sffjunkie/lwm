import pytest
from pathlib import Path
from lwm.loader.model import Config
from lwm.loader import load_config


@pytest.fixture
def module_root():
    return Path(__file__).parent.parent


@pytest.fixture
def test_data() -> Path:
    return Path(__file__).parent / "data"


def config(test_data: Path) -> Config | None:
    data_path = test_data / "config" / "desktop"
    return load_config(data_path.absolute())
