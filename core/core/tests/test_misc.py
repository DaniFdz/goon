import pytest

from core.core.utils.misc import yaml_loader


def test_yaml_loader_string():
    yaml_str = "value"
    result = yaml_loader(yaml_str)
    assert result == "value"


def test_yaml_loader_string_with_spaces():
    yaml_str = "value with spaces"
    result = yaml_loader(yaml_str)
    assert result == "value with spaces"


def test_yaml_loader_int():
    yaml_str = "1"
    result = yaml_loader(yaml_str)
    assert result == 1


def test_yaml_loader_float():
    yaml_str = "1.0"
    result = yaml_loader(yaml_str)
    assert result == 1.0


def test_yaml_loader_bool():
    yaml_str = "True"
    result = yaml_loader(yaml_str)
    assert result is True


def test_yaml_loader_not_str():
    with pytest.raises(TypeError, match="YAML file path must be a string"):
        yaml_loader(1)
