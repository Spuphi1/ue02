import pytest
from single_element import find_single_element

def test_example_case():
    assert find_single_element([1, 2, 3, 4, 3, 1, 2]) == 4


def test_single_element_at_beginning():
    assert find_single_element([9, 1, 1, 2, 2]) == 9


def test_single_element_at_end():
    assert find_single_element([1, 1, 2, 2, 7]) == 7


def test_negative_numbers():
    assert find_single_element([-1, -1, -2, -2, -5]) == -5


def test_only_one_element():
    assert find_single_element([42]) == 42


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError):
        find_single_element([])


def test_even_length_list_raises_value_error():
    with pytest.raises(ValueError):
        find_single_element([1, 1, 2, 2])


def test_more_than_one_single_element_raises_value_error():
    with pytest.raises(ValueError):
        find_single_element([1, 2, 3, 3, 4])


def test_element_occurs_more_than_twice_raises_value_error():
    with pytest.raises(ValueError):
        find_single_element([1, 1, 1, 2, 2])


def test_non_integer_element_raises_type_error():
    with pytest.raises(TypeError):
        find_single_element([1, 1, "2"])