import pytest


def test_foo():
    assert 1 == 1


if __name__ == "__main__":
    pytest.main(["-v", __file__])
