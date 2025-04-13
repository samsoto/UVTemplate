import pytest
from explorer.helpers.my_helper import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    assert add(-2, 3) == 1


if __name__ == "__main__":
    pytest.main(["-v", __file__])
