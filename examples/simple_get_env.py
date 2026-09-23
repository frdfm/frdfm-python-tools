from frdfm_python_tools import get_env

print(get_env("TEST_VAR", env_file=".env", fallback="Value_fallback"))
print(get_env("TEST_VAR2", env_file=".env", fallback="Value_fallback"))