import pytest

from playground.interp import interp

XS = [0.0, 1.0, 3.0]
YS = [0.0, 2.0, 0.0]


def test_between_knots():
    assert interp(0.5, XS, YS) == 1.0
    assert interp(2.0, XS, YS) == 1.0


def test_at_inner_knot():
    assert interp(1.0, XS, YS) == 2.0


def test_outside_returns_end_values():
    assert interp(-1.0, XS, YS) == 0.0
    assert interp(5.0, XS, YS) == 0.0


def test_needs_two_knots():
    with pytest.raises(ValueError):
        interp(0.0, [0.0], [1.0])


def test_at_last_knot():
    assert interp(3.0, XS, YS) == 0.0
