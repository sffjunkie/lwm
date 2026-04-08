import json
from subprocess import Popen

from lwm.config.output.typedef import Outputs


def wlr_randr() -> Outputs | None:
    cp = Popen(  # type: ignore
        ["wlr-randr", "--json"],
        capture_output=True,
    )
    if cp.stdout is None:
        return None
    data = json.loads(cp.stdout.read())
    return Outputs(**data)
