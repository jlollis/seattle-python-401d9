from .reverse_array import reverse_array
import pytest


def test_reverse_array_module_exists():
    assert reverse_array


def test_list_gets_reversed():
    expected = [1, 2, 3, 4]
    actual = reverse_array([4, 3, 2, 1])
    assert expected == actual


def test_list_can_reverse_strings():
    expected = ['a', 'b', 'c']
    actual = reverse_array(['c', 'b','a'])
    assert expected == actual


def test_argument_must_be_valid_list():
    with pytest.raises(TypeError):
        reverse_array(1)
