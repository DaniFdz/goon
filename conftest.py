import os

# Set on the earliest possible moment
os.environ["PYTEST_RUNNING"] = "true"

from core.core.tests.fixtures import *  # noqa: F401, F403, E402
from core.portfolio.tests.fixtures import *  # noqa: F401, F403, E402
