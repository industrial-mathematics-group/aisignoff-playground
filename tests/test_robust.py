import pytest

from playground.robust import mad, median


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_ignores_an_outlier():
    assert median([1, 2, 3, 4, 1000]) == 3


def test_median_of_empty_sequence():
    with pytest.raises(ValueError):
        median([])


def test_mad():
    assert mad([1, 2, 3, 4, 1000]) == 1
