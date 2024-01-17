import pytest


@pytest.fixture
def base_dict():
    return {"a": 1, "b": {"c": 2, "d": {"e": 3}}}


@pytest.fixture
def update_with():
    return {"b": {"c": 4, "d": {"e": 5, "f": 6}}, "g": 7}
