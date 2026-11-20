import pytest

from playground import fit_line, mean, variance


def test_mean():
    assert mean([1, 2, 3]) == 2


def test_variance():
    assert variance([1, 2, 3, 4], ddof=1) == pytest.approx(5 / 3)


def test_fit_line():
    slope, intercept = fit_line([0, 1, 2], [1, 3, 5])
    assert slope == pytest.approx(2)
    assert intercept == pytest.approx(1)


def test_mean_of_empty_sequence():
    with pytest.raises(ValueError):
        mean([])


def test_variance_population():
    assert variance([1, 2, 3, 4]) == pytest.approx(1.25)


def test_variance_needs_more_values_than_ddof():
    with pytest.raises(ValueError):
        variance([1.0], ddof=1)


def test_fit_line_rejects_equal_x_values():
    # all x values equal: the slope is undefined
    with pytest.raises(ValueError):
        fit_line([1, 1], [2, 3, 4])


def test_fit_line_negative_slope():
    slope, intercept = fit_line([0, 1, 2, 3], [3.25, 2.75, 2.25, 1.75])
    assert slope == pytest.approx(-0.5)
    assert intercept == pytest.approx(3.25)
