import logging
import subprocess


def shellcmd_exists(command: str) -> bool:
    args = ["which", command]
    proc = subprocess.run(args)
    ok = proc.returncode == 0
    if not ok:
        logging.debug(f"Command `{command}' not found.")
    return ok


def shellcmd_output(args: list[str]) -> str:
    proc = subprocess.run(args, capture_output=True)
    return proc.stdout.decode("utf-8").strip("\n")
