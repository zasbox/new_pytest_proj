import pytest

from utils import arrs


@pytest.fixture
def arr():
    return [1, 2, 3]


def test_get(arr):
    assert arrs.get(arr, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(arr):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(arr, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(arr) == [1, 2, 3]
