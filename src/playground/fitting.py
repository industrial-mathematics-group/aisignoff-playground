"""Least-squares line fit (pretend an AI wrote most of this)."""

def _weighted_mean(values, weights):
    return sum(w * v for w, v in zip(weights, values)) / sum(weights)


def fit_line(xs, ys, weights=None):
    """Return slope and intercept of the least-squares line through (xs, ys).

    With ``weights``, each point counts with its weight (weighted least squares),
    for example ``1 / sigma**2`` for points with standard deviation ``sigma``.
    """
    xs, ys = list(xs), list(ys)
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("need at least two points, and as many x as y values")
    if weights is None:
        weights = [1.0] * len(xs)
    weights = list(weights)
    if len(weights) != len(xs):
        raise ValueError("need one weight per point")
    if any(w < 0 for w in weights) or sum(weights) == 0:
        raise ValueError("weights must be non-negative and not all zero")
    mx, my = _weighted_mean(xs, weights), _weighted_mean(ys, weights)
    sxx = sum(w * (x - mx) ** 2 for w, x in zip(weights, xs))
    if sxx == 0:
        raise ValueError("all x values are equal")
    sxy = sum(w * (x - mx) * (y - my) for w, x, y in zip(weights, xs, ys))
    slope = sxy / sxx
    return slope, my - slope * mx
