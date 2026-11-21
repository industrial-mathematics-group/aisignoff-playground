"""Descriptive statistics for small samples."""

import math


def mean(xs):
    """The arithmetic mean of a sequence of numbers."""
    return sum(xs) / len(xs)


def variance(xs):
    """The sample variance (with Bessel's correction, dividing by n - 1)."""
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)


def std(xs):
    """The sample standard deviation."""
    return math.sqrt(variance(xs))


def median(xs):
    """The median: the middle value, or the mean of the two middle values."""
    s = sorted(xs)
    n = len(s)
    mid = n // 2
    if n % 2:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2
