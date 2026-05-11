from typing import NamedTuple, Any

from libqtile.lazy import lazy, LazyCall
from lwm.model.definitions import Definitions

PART_SEP = ":"
COMMAND_SEP = "."
ARG_SEP = ","


class CommandParts(NamedTuple):
    mode: str
    command: str
    args: str


def modifier_group(
    defs: Definitions, group_name: str, extra: list[str] | None = None
) -> list[str]:
    extra_modifiers = extra or []
    return [
        getattr(defs.key.modifier, name, name)
        for name in (defs.key.modifier_group[group_name] + extra_modifiers)
    ]


def _split_args(args: str) -> list[str]:
    if args != "":
        return args.split(ARG_SEP)
    else:
        return []


def _try_int(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


def _try_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None


def qtile_args(arg_string: str) -> list[Any]:
    def convert(arg: str) -> Any:
        return _try_int(arg) or _try_float(arg) or arg

    args = arg_string.split(ARG_SEP)
    return [convert(arg) for arg in args]


def qtilecmd(defs: Definitions, command: str) -> list[LazyCall]:
    """Returns a qtile lazy command from a string description"""

    elems = command.split(PART_SEP, maxsplit=3)
    if len(elems) == 2:
        elems.append("")
    parts = CommandParts(*elems)

    if parts.mode == "qtile":
        cmd_parts = parts.command.split(COMMAND_SEP)
        args_parts = _split_args(parts.args)

        cmd = lazy
        for elem in cmd_parts:
            cmd = getattr(cmd, elem)

        if args_parts:
            args = qtile_args(parts.args)
            return [cmd(*args)]
        else:
            return [cmd()]

    elif parts.mode == "lwm":
        args_parts = _split_args(parts.args)
        if len(args_parts) == 0:
            raise ValueError(
                f"qtilecmd: no arguments specified for lwm function definition '{command}'"
            )

        def_part = args_parts[0]
        args_parts = args_parts[1:]

        cmd = defs  # type: ignore
        for elem in def_part.split(COMMAND_SEP):
            cmd = getattr(cmd, elem)

        new_cmd = f"qtile:{parts.command}:{cmd}"
        if args_parts:
            new_cmd = new_cmd + (",".join(args_parts))
        return qtilecmd(defs, new_cmd)

    return []
