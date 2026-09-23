import os
from pathlib import Path


def get_env(value0, env_var_name: str, env_file: str = ".env", fallback_value: str = None) -> str | None:

    if value0:
        return value0

    if env_var_name:
        value = os.getenv(env_var_name)

        if value is not None:
            return value

        env_path = Path(env_file)

        if env_path.exists():
            for line in env_path.read_text().splitlines():
                line = line.strip()

                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)

                if key.strip() == env_var_name:
                    return value.strip().strip("\"'")

    return fallback_value