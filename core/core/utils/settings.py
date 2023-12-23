import os

from .misc import yaml_loader


def get_settings_from_environment(prefix):
    """Get settings from environment variables.

    :param prefix: The prefix to use for the environment variables.
    :return: The settings.
    """
    prefix_length = len(prefix)
    return {key[prefix_length:]: yaml_loader(val) for key, val in os.environ.items() if key.startswith(prefix)}
