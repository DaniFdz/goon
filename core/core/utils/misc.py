import yaml  # type: ignore


def yaml_loader(value):
    """
    Load a YAML string into a Python object.
    :param value: The YAML string to load.
    :return: The Python object.
    """
    if isinstance(value, str):
        return yaml.load(f"dummy: {value}", Loader=yaml.SafeLoader)["dummy"]

    return value
