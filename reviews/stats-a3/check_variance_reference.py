"""Evidence of the A3 review of src/playground/stats.py (reviews/stats-a3.md).

Compares variance and std with Python's statistics module, the reference implementation of the
sample variance. Run from the repository root: python -m pytest reviews/stats-a3/check_variance_reference.py -q
(named check_*.py, so that the test suite of the content does not collect it)
It fails on the reviewed content: findings 1 and 2 of the report.
"""

import math
import random
import statistics
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from playground.stats import mean, std, variance  # noqa: E402

SAMPLES = [[1.0, 2.0, 4.0], [2.5, 2.5, 3.5, 7.0], [random.Random(1).gauss(0, 1) for _ in range(50)]]


def test_variance_matches_the_sample_variance():
    for xs in SAMPLES:
        assert math.isclose(variance(xs), statistics.variance(xs), rel_tol=1e-12), xs


def test_std_matches_the_sample_standard_deviation():
    for xs in SAMPLES:
        assert math.isclose(std(xs), statistics.stdev(xs), rel_tol=1e-12), xs


def test_mean_of_empty_sample_says_why():
    try:
        mean([])
    except ValueError:
        pass
    except ZeroDivisionError:
        raise AssertionError("mean([]) raises ZeroDivisionError instead of a ValueError")
