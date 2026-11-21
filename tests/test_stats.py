import math

from playground.stats import mean, median, std, variance


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_and_even():
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5


def test_variance_of_constant_is_zero():
    assert variance([5, 5, 5]) == 0


def test_std_is_root_of_variance():
    xs = [1.0, 2.0, 4.0]
    assert math.isclose(std(xs), math.sqrt(variance(xs)))
