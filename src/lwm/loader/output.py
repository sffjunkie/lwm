import json
from subprocess import Popen

from lwm.model.output import OutputDefs


def wlr_randr() -> OutputDefs | None:
    cp = Popen(  # type: ignore
        ["wlr-randr", "--json"],
        capture_output=True,
    )
    if cp.stdout is None:
        return None
    data = json.loads(cp.stdout.read())
    return OutputDefs(**data)
