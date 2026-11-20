"""Robust statistics: median and median absolute deviation."""


def median(values):
    """Median of a non-empty sequence."""
    values = sorted(values)
    if not values:
        raise ValueError("median of an empty sequence")
    return values[len(values) // 2]


def mad(values):
    """Median absolute deviation from the median, a robust measure of spread."""
    m = median(values)
    return median(abs(v - m) for v in values)
