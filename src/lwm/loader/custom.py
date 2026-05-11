from inspect import getmembers, isfunction
from pathlib import Path
import importlib.util
import importlib.machinery
import types

from lwm.model.custom import CustomFuncs


def import_custom(
    file_path: Path,
    module_name: str,
) -> types.ModuleType | None:
    full_path = str(file_path / f"{module_name}.py")
    loader = importlib.machinery.SourceFileLoader("custom", full_path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    if spec is not None:
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
        return module
    return None


def funcs_from_module(module_path: Path, name: str = "custom") -> CustomFuncs:
    funcs = {}
    m = import_custom(module_path, name)

    for name, func in getmembers(m, isfunction):
        if name[0] != "_":
            funcs[name] = func

    return funcs
