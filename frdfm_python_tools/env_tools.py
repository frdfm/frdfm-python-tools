import os
from pathlib import Path


def get_env(name: str, env_file: str = ".env", fallback: str = None) -> str | None:
    value = os.getenv(name)

    if value is not None:
        return value

    env_path = Path(env_file)

    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)

            if key.strip() == name:
                return value.strip().strip("\"'")

    return fallback