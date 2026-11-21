"""Piecewise linear interpolation on sorted knots."""

from bisect import bisect_right


def interp(x, xs, ys):
    """Interpolate linearly between the knots (xs, ys) at x.

    xs must be strictly increasing. Outside [xs[0], xs[-1]] the end values are returned.
    """
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("need at least two knots and as many values as knots")
    if x < xs[0]:
        return ys[0]
    if x > xs[-1]:
        return ys[-1]
    i = bisect_right(xs, x)
    x0, x1 = xs[i - 1], xs[i]
    y0, y1 = ys[i - 1], ys[i]
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)
