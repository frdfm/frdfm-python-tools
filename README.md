# frdfm-python-tools
Simple Python tools.

## Installation

You can install the package (```frdfm-python-tools```) via `pip`:

```bash
pip install git+https://github.com/frdfm/frdfm-python-tools.git
```

## Usage

```python
from frdfm_python_tools import get_env

print(get_env(None, "TEST_VAR", env_file=".env", fallback_value="Value_fallback"))
print(get_env(None, "TEST_VAR2", env_file=".env", fallback_value="Value_fallback"))
print(get_env(1, "TEST_VAR2", env_file=".env", fallback_value="Value_fallback"))
```
