from core.core.utils.collections import deep_update


def test_deep_update(base_dict, update_with):
    result = deep_update(base_dict.copy(), update_with.copy())

    # Check the result after deep_update
    expected_result = {"a": 1, "b": {"c": 4, "d": {"e": 5, "f": 6}}, "g": 7}
    assert result == expected_result


def test_deep_update_empty_base(base_dict, update_with):

    # If the base dictionary is empty, the result should be the same as the update_with dictionary

    result = deep_update({}, update_with.copy())
    assert result == update_with


def test_deep_update_empty_update(base_dict):
    # If the update_with dictionary is empty, the result should be the same as the base dictionary
    result = deep_update(base_dict.copy(), {})
    assert result == base_dict


def test_deep_update_no_overlap():
    # If there is no overlap between base_dict and update_with, the result should be a combination of both
    base_dict = {"a": 1, "b": 2}
    update_with = {"c": 3, "d": 4}
    result = deep_update(base_dict.copy(), update_with.copy())
    expected_result = {"a": 1, "b": 2, "c": 3, "d": 4}
    assert result == expected_result
