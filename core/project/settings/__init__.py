import os.path
from pathlib import Path

import pymysql  # type: ignore
from split_settings.tools import include, optional

from core.core.utils.pytest import is_pytest_running

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing our own custom environment variables
ENVVAR_SETTINGS_PREFIX = "CORE_SETTINGS_"

LOCAL_SETTINGS_PATH = os.getenv(
    f"{ENVVAR_SETTINGS_PREFIX}LOCAL_SETTINGS_PATH",
    # Default value if LOCAL_SETTINGS_PATH is not set
    f"local/settings.{'unittests' if is_pytest_running() else 'dev'}.py"
)

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)

include(
    "base.py",
    "logging.py",
    "custom.py",
    optional(LOCAL_SETTINGS_PATH),
    "envvars.py",
)
