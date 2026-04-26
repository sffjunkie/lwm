import configparser
import os
import random
import string
import tomllib
from itertools import chain
from pathlib import Path
from typing import Any, Iterable
from io import TextIOWrapper
import yaml


def user_config_dir(config_dir: Path) -> Path:
    xdg_config = Path(
        os.environ.get(
            "XDG_CONFIG_HOME",
            os.path.expanduser("~/.config"),
        )
    )
    return xdg_config / config_dir


def read_yaml(filepath: Path) -> dict[str, Any]:
    data: dict[str, Any] = {}
    if filepath.exists():
        try:
            with filepath.open("r") as fp:
                return read_yaml_stream(fp)
        except (IOError, yaml.YAMLError):
            pass

    return data


def read_yaml_stream(fp: TextIOWrapper) -> dict[str, Any]:
    data = yaml.load(fp, Loader=yaml.SafeLoader)
    return data


def read_toml(filepath: Path | None = None) -> dict[str, Any]:
    data: dict[str, Any] = {}
    if filepath is not None and filepath.exists():
        try:
            with open(filepath, "rb") as fp:
                return tomllib.load(fp)
        except (IOError, tomllib.TOMLDecodeError):
            pass

    return data


class _MultiDict(dict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super().__setitem__(key, value)


def read_ini(filepath: Path, has_sections: bool = True) -> dict[str, list[str]]:
    data = {}
    parser = configparser.ConfigParser(
        strict=False,
        empty_lines_in_values=False,
        dict_type=_MultiDict,
        interpolation=None,
    )
    dummy = "".join(random.choices(string.ascii_uppercase + string.digits, k=16))
    try:
        with open(filepath, "r") as fp:
            lines = fp.readlines()

            contents: Iterable[str]
            if not has_sections:
                contents = chain((f"[{dummy}]\n",), lines)
            else:
                contents = lines

            parser.read_file(contents)

            items = parser.items(dummy)
            for name, value in items:
                if "\n" in value:
                    data[name] = value.split("\n")
                else:
                    data[name] = [value]
    except IOError:
        pass

    return data
