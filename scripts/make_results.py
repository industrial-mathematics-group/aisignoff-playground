#!/usr/bin/env python3
# AI-Generation: G1
# Human-Review: H2
# AI-Review: A1
# Assisted-by: Claude Opus 5.5 (Anthropic)
# AI-Reviewed-by: Claude Opus 5.5 (Anthropic), self-check by the generating session
# Reviewed-by: Pascal Jung
"""Writes results/fit.csv, or the file given as the first argument. This file declares itself with inline tags."""

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from playground import fit_line  # noqa: E402

DATA = {
    "a": ([0, 1, 2], [1, 3, 5]),
    "b": ([0, 1, 2, 3], [3.25, 2.75, 2.25, 1.75]),
    "c": ([0, 2, 4], [0, 3.5, 7]),
}

def write_results(path, data):
    """Write one row per dataset: its name, slope and intercept, rounded to 4 digits."""
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dataset", "slope", "intercept"])
        for name, (xs, ys) in data.items():
            row = fit_line(xs, ys)
            w.writerow([name, *(round(v, 4) for v in reversed(row))])


if __name__ == "__main__":
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / "results" / "fit.csv"
    write_results(out, DATA)
