from pathlib import Path

from lwm.helper.fs import read_toml, user_config_dir

SECRETS_DIR = "lde"
FILENAME = "secrets.toml"


def get_secrets_path(filepath: Path | None = None) -> Path | None:
    if filepath is not None and filepath.is_absolute():
        secrets_path = filepath
    else:
        secrets_path = user_config_dir(Path(SECRETS_DIR))

    return secrets_path


def load_secrets(secretspath: Path | None = None) -> dict:
    secrets_path = get_secrets_path(secretspath)

    if secrets_path is not None:
        secrets_file = secrets_path / FILENAME
    else:
        secrets_file = Path(__file__).parent.parent / FILENAME

    if secrets_file.exists():
        return read_toml(secrets_file)
    else:
        return {}
