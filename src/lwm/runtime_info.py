import sys

from libqtile import __path__ as libqtile_path
from libqtile.log_utils import logger


def log_runtime_info() -> None:
    logger.debug(f"python prefix: {sys.prefix}")
    logger.debug(f"python version: {sys.version}")
    logger.debug(f"python platform: {sys.platform}")
    logger.debug(f"python path: {sys.path}")
    logger.debug(f"libqtile path: {libqtile_path}")
    logger.debug(f"__init__ file: {__file__}")
    logger.debug(f"__package__: {__package__}")

    lwm_env = shellcmd_output(["systemctl", "--user", "show-environment"])
    logger.debug(f"lwm env: {lwm_env}")
