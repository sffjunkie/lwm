import pytest
from pathlib import Path


@pytest.fixture
def module_root():
    return Path(__file__).parent.parent


@pytest.fixture
def test_data() -> Path:
    return Path(__file__).parent / "data"
