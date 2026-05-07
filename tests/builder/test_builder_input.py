from pathlib import Path

from lwm.loader import load_defs
from lwm.builder.input import build_input_rules


def test_builder_input(test_data: Path):
    data_path = test_data / "config" / "desktop"
    defs = load_defs(data_path)
    assert defs is not None

    input_rules = build_input_rules(defs)
    assert "1452:591:Keychron Keychron K1" in input_rules
