import pytest

from playground import fit_line


def test_equal_weights_give_the_unweighted_fit():
    xs, ys = [0, 1, 2, 3], [1.0, 2.9, 5.2, 7.1]
    assert fit_line(xs, ys, weights=[2, 2, 2, 2]) == pytest.approx(fit_line(xs, ys))


def test_weights_must_match_the_points():
    with pytest.raises(ValueError):
        fit_line([0, 1, 2], [1, 2, 3], weights=[1, 1])


def test_negative_weights_are_rejected():
    with pytest.raises(ValueError):
        fit_line([0, 1, 2], [1, 2, 3], weights=[1, -1, 1])


def test_a_zero_weight_drops_the_point():
    # the outlier at x = 3 has weight 0: the fit is the line through the other three points
    slope, intercept = fit_line([0, 1, 2, 3], [1, 3, 5, 100], weights=[1, 1, 1, 0])
    assert slope == pytest.approx(2)
    assert intercept == pytest.approx(1)
