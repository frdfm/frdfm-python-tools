from frdfm_python_tools import get_env

print(get_env(None, "TEST_VAR", env_file=".env", fallback_value="Value_fallback"))
print(get_env(None, "TEST_VAR2", env_file=".env", fallback_value="Value_fallback"))
print(get_env(1, "TEST_VAR2", env_file=".env", fallback_value="Value_fallback"))